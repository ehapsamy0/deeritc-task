cmake_minimum_required(VERSION 3.10)
project(LoggerProject)

set(CMAKE_CXX_STANDARD 11)

# Create a logs directory for log files if it doesn't exist
execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory "${CMAKE_SOURCE_DIR}/logs")

# Add source files
add_executable(LoggerProject src/main.cpp src/Logger.cpp)
add_executable(LoggerTest src/LoggerTest.cpp src/Logger.cpp)
