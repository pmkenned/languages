	xor	R0, R0
l0	stop
	not	R5
	pop	R7
l1	ldsf	R1, $79D9
	ldr	R6, R1
	rtn
	jsr	$659E
l2	add	R2, R6
l3	.equ	$1FC1
	push	R3
	or	R7, R1
	.org	$0011
	mov	R4, R0
	cmi	R0, $696F
	lshl	R3
	rtn
	brz	l15
	ashr	R4
	stop
	str	R1, R0
	mov	R5, R5
	rtn
	rtn
	addsp	$78C8
	rtn
	cmr	R4, R5
	sub	R6, R0
	mov	R3, R4
	brz	$5171
	mov	R5, R2
	brz	$3D91
	ldsp	R4
	ldsp	R4
	lshr	R2
	or	R3, R4
	stop
	cmi	R4, l10
	brz	$4A32
	bra	l2
	sta	$604B,	R2
	stop
	and	R5, R3
l4	.equ	$3024
	lshr	R5
	stop
	stop
	not	R0
	neg	R1
	ldi	R0, $7AD4
	ldsf	R1, $19A0
	lshl	R2
	.org	$004a
	lshr	R3
	sta	$5550,	R7
	rtn
	rtn
	ldi	R4, $77F3
	rtn
	lshr	R0
	and	R0, R1
	sub	R2, R0
	stop
l5	addsp	$767D
	.org	$0062
	ldsf	R4, l14
	stop
	or	R2, R2
	addsp	$0D66
	brz	l4
	rtn
	stsf	R2, $305F
l6	push	R5
	push	R1
	rtn
	rtn
	and	R2, R1
	stop
	bra	$0F26
	lshr	R0
	sta	$19D7,	R1
	xor	R3, R3
l7	stsf	R7, $47E2
	ldr	R6, R7
	ldi	R0, l8
	lshr	R7
	.org	$0087
l8	rtn
	brz	l14
	jsr	l4
	stop
	ldr	R6, R5
	cmr	R3, R0
l9	stop
l10	stop
	lda	R1, $03DE
l11	and	R5, R6
	neg	R0
	stop
l12	brn	l11
	push	R3
	ldi	R4, $744D
	mov	R5, R7
	ldsp	R1
	stsp	R5
	or	R6, R7
	rtn
	.org	$00a3
	stsp	R6
	and	R5, R0
	neg	R1
	jsr	$0F2B
	addsp	$338F
	rtn
l13	brn	$51B5
	rtn
	pop	R7
	sub	R2, R5
	rtn
	rtn
	cmr	R5, R4
	decr	R3
	stop
	stop
	stop
	rtn
	ldsf	R2, $7FD3
	sta	$1704,	R5
	addsp	$4290
	rtn
	rol	R7
	.dw	l14
	addsp	l12
	sta	l17, R7
	sta	l7, R2
	stop
l14	str	R4, R1
	rtn
	addsp	l2
	rtn
l15	lshl	R4
	rol	R3
	ldsp	R7
	.org	$00db
	lshl	R0
	rtn
	push	R0
	rtn
	sta	l6, R5
	decr	R7
	jsr	$2251
	ldi	R1, l17
	decr	R1
	push	R7
	lda	R1, $2480
	sub	R0, R6
	and	R5, R6
l16	bra	l3
l17	.equ	$0728
	or	R3, R6
	stop
	brc	$049A
	brc	$64B8
	cmi	R2, l10
	cmr	R0, R4
	sub	R5, R1
	and	R7, R3
	lshl	R5
	ldi	R2, $1578
	addsp	l17
	decr	R0
	stsf	R6, l18
	brv	$42A2
	brz	l0
	stop
	stsf	R5, l4
	brn	$49E4
	add	R4, R7
	rtn
	ldi	R2, $7043
	stop
l18	rtn
	lshl	R5
	stop
	addsp	l2
	rtn
	stop
	or	R3, R1
	.org	$011a
	lda	R3, $5EF5
	bra	$1B85
l19	and	R6, R7
	mov	R4, R6
	ldsf	R7, $72DD
	stsf	R7, l7
	ldsf	R5, $7243
	brc	$1E9D
	bra	$4C21
	rtn
	lshr	R2
