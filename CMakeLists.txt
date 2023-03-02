cmake_minimum_required(VERSION 3.20)
project(CMakeSharedLib)


# build options
option(BUILD_SHARED_LIBS "Build using shared libraries" ON)


# CMakeSharedLib library
add_library(
  CMakeSharedLib
  src/main.cpp
)
target_include_directories(CMakeSharedLib PUBLIC include)
install(TARGETS CMakeSharedLib)
install(DIRECTORY include DESTINATION .)
