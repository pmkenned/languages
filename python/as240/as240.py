#!/usr/bin/env python

# TODO:
# * sta instruction doesn't work
# * currently has no parsing error messages
# * doesn't write file
# * regular expressions maybe done inefficiently

import sys
import re

# instructions which consume 1 word and require two register fields (Rs and Rd)
short2 = {
'add' :    0x0E00,
'and' :    0x1A00,
'cmr' :    0x4600,
'ldr' :    0x0800,
'mov' :    0x3A00,
'or'  :    0x1C00,
'str' :    0x0A00,
'sub' :    0x1000,
'xor' :    0x1E00,
}

# instructions which consume 1 word and require 1 register field (Rd)
short1 = {
'ashr' :    0x2600,
'decr' :    0x1600,
'incr' :    0x1400,
'ldsp' :    0x3C00,
'lshl' :    0x2000,
'lshr' :    0x2400,
'neg'  :    0x1200,
'not'  :    0x1800,
'pop'  :    0x3400,
'push' :    0x3200,
'rol'  :    0x2200,
'stsp' :    0x3E00,
}

# instructions which consume 1 word and require 0 register fields
short0 = {
'rtn'  :    0x3800,
'stop' :    0x3000,
}

# instructions which consume 2 words and require 1 register field
long1 = {
'cmi'  :    0x4400,
'lda'  :    0x0400,
'ldi'  :    0x0C00,
'ldsf' :    0x4000,
'sta'  :    0x0600,
'stsf' :    0x4200,
}

# instructions which consume 2 words and require 0 register field
long0 = {
'addsp' :    0x0f00,
'bra'   :    0x2800,
'brc'   :    0x4800,
'brn'   :    0x2C00,
'brv'   :    0x2E00,
'brz'   :    0x2A00,
'jsr'   :    0x3600,
}

def word_is_inst(s):
    if s in short2:
        return 'S2'
    if s in short1:
        return 'S1'
    if s in short0:
        return 'S0'
    if s in long1:
        return 'L1'
    if s in long0:
        return 'L0'
    return None

def write_to_mem(addr, data):
    if('addr' in memory):
        print 'error: overlapping org region at ' + addr
    else:
        memory[addr] = data

def fill_in_labels():
    for ref_addr in label_refs.keys():
        label = label_refs[ref_addr]
        if(label in labels):
            memory[ref_addr] = labels[label]
        else:
            print 'error: label ' + label + ' is undefined'

def store_labels(addr, line_data):

    # label definitions
    if('label_def' in line_data):
        label = line_data['label_def'];
        equ_def = ('pseudo' in line_data and line_data['pseudo'] == '.equ')
        target = ''
        if(equ_def):
            target = int(line_data['const'], 16)
        else:
            target = addr
        if(label in labels):
            print 'error: label ' + label + ' already defined'
        else:
            labels[label] = target

    # label references
    if('label_ref' in line_data):
        label = line_data['label_ref']
        label_refs[addr+1] = label

def common_parse_errors(token_str):
    return ''

def parse(tokens):
    line_data = {}
    token_str = get_token_str(tokens);

    # check for common errors
    error_str = common_parse_errors(token_str)
    if(error_str != ''):
        line_data['error'] = error_str
        return line_data
    
    s = re.compile('^d?(S2rr|S1r|S0)$')
    l = re.compile('^d?(L1r|L0)[cl]$')
    p = re.compile('^d?p[lc]$')

    l_or_s = re.compile('(L|S)')
    pseudo = re.compile('p')

    # check for a valid form
    valid = 0
    if( s.match(token_str) or l.match(token_str) or p.match(token_str) ):
        valid = 1
    # if not a valid form, return generic error message
    if(not valid):
        line_data['error'] = 'parse error'
        return line_data

    # we can assume a valid input line from this point forward

    for token in tokens:
        tok_type = token[0]
        tok_value = token[1]
        if(tok_type == 'l'):
            line_data['label_ref'] = tok_value
        elif(tok_type == 'd'):
            line_data['label_def'] = tok_value
        elif(tok_type == 'r'):
            if(not 'rd' in line_data):
                line_data['rd'] = tok_value
                line_data['rs'] = tok_value
            else:
                line_data['rs'] = tok_value
        elif(tok_type == 'c'):
            line_data['const'] = tok_value
        elif(l_or_s.match(tok_type)):
            line_data['inst'] = tok_value
        elif(pseudo.match(tok_type)):
            line_data['pseudo'] = tok_value

    if (not 'const' in line_data):
        line_data['const'] = '0'
    if (not 'rd' in line_data):
        line_data['rd'] = 0
    if (not 'rs' in line_data):
        line_data['rs'] = 0

    return line_data

def inst_to_hex(inst):
    inst_hex = ''
    if inst in short2:
        inst_hex = short2[inst]
    if inst in short1:
        inst_hex = short1[inst]
    if inst in short0:
        inst_hex = short0[inst]
    if inst in long1:
        inst_hex = long1[inst]
    if inst in long0:
        inst_hex = long0[inst]
    return inst_hex

def translate(line_data):
    translation = {}

    word0 = None
    word1 = None
    rd = None
    rs = None
    inst = None

    if('inst' in line_data):
        rd = line_data['rd']
        rs = line_data['rs']
        inst = line_data['inst']
        word0 = inst_to_hex(inst) | (int(rd) << 3) | int(rs)
        inst_type = word_is_inst(inst)
        if(inst_type == 'L0' or inst_type == 'L1'):
            word1 = int(line_data['const'],16)
    elif('pseudo' in line_data):
        if(line_data['pseudo'] == '.dw'):
            word0 = int(line_data['const'],16)

    if (word0 != None):
        translation['word0'] = word0
    if (word1 != None):
        translation['word1'] = word1

    return translation

def tokenize(line):
    words = line.split()
    first_word = 1

    d = re.compile('^([a-zA-Z_]\w*)')
    r = re.compile('^[rR]([0-7]),?$')
    l = re.compile('^[a-zA-Z_]\w*,?$')
    p = re.compile('^\.\w+$')
    c = re.compile('^\$([0-9A-Fa-f]{1,4}),?$')

    tokens = []

    for word in words:
        inst_type = word_is_inst(word)

        rm = r.match(word)
        cm = c.match(word)

        if(first_word and d.match(line)):
            tokens.append(('d',  word))
        elif(rm):
            tokens.append(('r', rm.group(1)))
        elif(inst_type):
            tokens.append((inst_type, word))
        elif(l.match(word)):
            tokens.append(('l', word))
        elif(p.match(word)):
            tokens.append(('p', word))
        elif(cm):
            tokens.append(('c', cm.group(1)))
        elif(word == ''):
            pass
        else:
            print 'error: unmatched token ' + word
        first_word = 0
    return tokens

def get_token_str(tokens):
    token_str = ''

    for token in tokens:
        typ = token[0]
        val = token[1]
        token_str += typ

    return token_str

def main():

    num_args = len(sys.argv)

    if(num_args < 2):
        print ('usage: {0} [OPTION]... FILE...'.format(sys.argv[0]))
        exit(1)

    input_filename = sys.argv[1]

    try:
        f = open(input_filename, 'r')
    except:
        print 'cannot open file ' + input_filename + ' for reading'
        exit(1)

    org = 0
    offset = 0

    num_errors = 0
    line_num = 0
    for line in f:
        line_num += 1

        line = re.sub('\;.*','',line)

        tokens = tokenize(line)
        line_data = parse(tokens)
        
        trans = translate(line_data)

        if('word0' in trans):
            write_to_mem(org + offset, trans['word0']) 
        if('word1' in trans):
            write_to_mem(org + offset + 1, trans['word1'])

        store_labels(org + offset, line_data)

        if('pseudo' in line_data and line_data['pseudo'] == '.org'):
            org = int(line_data['const'],16)
            offset = 0
        else:
            if('word0' in trans):
                offset += 1
            if('word1' in trans):
                offset += 1

    fill_in_labels()

    for key in memory.keys():
        value = memory[key]
        print '%04X' % key + ': ' + '%04X' % value

    f.close()

memory = {}
labels = {}
label_refs = {}

if __name__ == "__main__":
    main()
