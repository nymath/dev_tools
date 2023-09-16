include Makefile.function

CXX = g++
CFLAGS = -Wall -std=c++17
DEBUG_FLAGS = -g -O0
RELEASE_FLAGS = -O3

# make DEBUG=1 或 make RELEASE=1
ifdef DEBUG
    CFLAGS += $(DEBUG_FLAGS)
endif
ifdef RELEASE
    CFLAGS += $(RELEASE_FLAGS)
endif

INCLUDE_FLAGS = -I./include
LINKING_FLAGS = -lm -lboost_program_options

SRCS = $(wildcard src/*.cpp)
OBJS = $(patsubst src/%.cpp, build/%.o, $(SRCS))
DEPENDENCIES = $(patsubst src/%.cpp, build/%.d, $(SRCS)) build/main.d

TARGET = main

all: $(TARGET)

$(TARGET): $(OBJS) build/main.o
	$(CXX) $(CFLAGS) $^ $(LINKING_FLAGS) -o $@

build/main.o: main.cpp
	$(call compile_rule)

build/%.o: ./src/%.cpp
	$(call compile_rule)

clean:
	rm -rf build $(TARGET)

.PHONY: clean


# automatic dependencies
-include $(DEPENDENCIES)

build/main.d: main.cpp
	$(call dependency_rule)

build/%.d: ./src/%.cpp
	$(call dependency_rule)


