cmake_minimum_required(VERSION 3.14)
project(demo-tool CXX)

# set some common default compiler options
set(CMAKE_CXX_STANDARD 17)

# dependencies
find_package(Demo REQUIRED)

# explicitly list the source files instead of searching them
# https://stackoverflow.com/questions/1027247/is-it-better-to-specify-source-files-with-glob-or-each-file-individually-in-cmak
# https://cmake.org/cmake/help/v3.15/command/file.html?highlight=glob#filesystem
set(DEMOTOOL_SOURCES ${CMAKE_SOURCE_DIR}/src/main.cpp)

# add the new library, specifiy SHARED or STATIC is possible
# if not specified it will depend on whether BUILD_SHARED_LIBS is set to ON or OFF
add_executable(demo-tool ${DEMOTOOL_SOURCES})
target_link_libraries(demo-tool PUBLIC Demo::Demo)

# specify the install directory, always use a subdirectory for your header files(!)
install(TARGETS demo-tool DESTINATION bin/)

