# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ehabsami/Desktop/booknest/logger_task

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ehabsami/Desktop/booknest/logger_task/build

# Include any dependencies generated for this target.
include CMakeFiles/LoggerTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/LoggerTest.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/LoggerTest.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/LoggerTest.dir/flags.make

CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.o: CMakeFiles/LoggerTest.dir/flags.make
CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.o: ../src/LoggerTest.cpp
CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.o: CMakeFiles/LoggerTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ehabsami/Desktop/booknest/logger_task/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.o -MF CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.o.d -o CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.o -c /home/ehabsami/Desktop/booknest/logger_task/src/LoggerTest.cpp

CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ehabsami/Desktop/booknest/logger_task/src/LoggerTest.cpp > CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.i

CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ehabsami/Desktop/booknest/logger_task/src/LoggerTest.cpp -o CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.s

CMakeFiles/LoggerTest.dir/src/Logger.cpp.o: CMakeFiles/LoggerTest.dir/flags.make
CMakeFiles/LoggerTest.dir/src/Logger.cpp.o: ../src/Logger.cpp
CMakeFiles/LoggerTest.dir/src/Logger.cpp.o: CMakeFiles/LoggerTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ehabsami/Desktop/booknest/logger_task/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/LoggerTest.dir/src/Logger.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/LoggerTest.dir/src/Logger.cpp.o -MF CMakeFiles/LoggerTest.dir/src/Logger.cpp.o.d -o CMakeFiles/LoggerTest.dir/src/Logger.cpp.o -c /home/ehabsami/Desktop/booknest/logger_task/src/Logger.cpp

CMakeFiles/LoggerTest.dir/src/Logger.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/LoggerTest.dir/src/Logger.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ehabsami/Desktop/booknest/logger_task/src/Logger.cpp > CMakeFiles/LoggerTest.dir/src/Logger.cpp.i

CMakeFiles/LoggerTest.dir/src/Logger.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/LoggerTest.dir/src/Logger.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ehabsami/Desktop/booknest/logger_task/src/Logger.cpp -o CMakeFiles/LoggerTest.dir/src/Logger.cpp.s

# Object files for target LoggerTest
LoggerTest_OBJECTS = \
"CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.o" \
"CMakeFiles/LoggerTest.dir/src/Logger.cpp.o"

# External object files for target LoggerTest
LoggerTest_EXTERNAL_OBJECTS =

LoggerTest: CMakeFiles/LoggerTest.dir/src/LoggerTest.cpp.o
LoggerTest: CMakeFiles/LoggerTest.dir/src/Logger.cpp.o
LoggerTest: CMakeFiles/LoggerTest.dir/build.make
LoggerTest: CMakeFiles/LoggerTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ehabsami/Desktop/booknest/logger_task/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable LoggerTest"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/LoggerTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/LoggerTest.dir/build: LoggerTest
.PHONY : CMakeFiles/LoggerTest.dir/build

CMakeFiles/LoggerTest.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/LoggerTest.dir/cmake_clean.cmake
.PHONY : CMakeFiles/LoggerTest.dir/clean

CMakeFiles/LoggerTest.dir/depend:
	cd /home/ehabsami/Desktop/booknest/logger_task/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ehabsami/Desktop/booknest/logger_task /home/ehabsami/Desktop/booknest/logger_task /home/ehabsami/Desktop/booknest/logger_task/build /home/ehabsami/Desktop/booknest/logger_task/build /home/ehabsami/Desktop/booknest/logger_task/build/CMakeFiles/LoggerTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/LoggerTest.dir/depend

