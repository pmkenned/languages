# directories

# source file diretory
SRC_DIR = src
# top-level output directory (for .o and .d files)
OBJ_DIR = bin

############
SRCS = \
	main.cpp

TARGET = c4e1
############

.PHONY: all clean

all: target

clean:
	rm -rf $(OBJ_DIR) $(TARGET)

#########
# USAGE #
#########
# the makefile assumes the following variables are defined:
# OBJ_DIR: the top object level directory
# SRCS: the source files
# TARGET: the target (executable) name

ifeq ($(TARGET),)
ERRORMSG = "No target specified"
else ifeq ($(OBJ_DIR),)
ERRORMSG = "No object directory specified"
else ifeq ($(SRCS),)
ERRORMSG = "No sources specified"
endif

CURR_DIR = $(shell pwd)   # the current directory

# global compiler flags
CXX = g++
CXXFLAGS += -Wall -ansi -pedantic -I"$(CURR_DIR)/include" -I"$(CURR_DIR)/$(SRC_DIR)" # NOTE: 'include' doesn't exist
LDFLAGS = -L"$(CURR_DIR)/lib" # NOTE: 'lib' doesn't exist

# list of all object files
OBJS = $(SRCS:.cpp=.o)
# list of all dep files
DEPS = $(OBJS:.o=.d)
# full list of paths to all objs
OBJS_FULL = $(addprefix $(OBJ_DIR)/,$(OBJS))
# full list of paths to all deps
DEPS_FULL = $(addprefix $(OBJ_DIR)/,$(DEPS))

# sanity check for '.cpp' suffix
TMP_SRCS_NOT_CPP = $(filter-out %.cpp,$(SRCS))
ifneq (,$(TMP_SRCS_NOT_CPP))
ERRORMSG = "Feeling nervous about '$(TMP_SRCS_NOT_CPP)'; I only know how to build .cpp files"
endif

# targets

.PHONY: target

ifneq ($(ERRORMSG),)
target:
	$(error $(ERRORMSG))
else
target: $(OBJ_DIR)/$(TARGET).exe
	cp $< $(TARGET)

# dependency generation from g++
$(OBJ_DIR)/%.d: $(SRC_DIR)/%.cpp
	mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -MM -MP -MT $(@:.d=.o) -o $@ $<

# compilation step
# don't need to mkdir for object files since d files already exist
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

ifneq ($(MAKECMDGOALS),clean)
-include $(DEPS_FULL)
endif

# link step
$(OBJ_DIR)/$(TARGET).exe: $(OBJS_FULL)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)
endif
