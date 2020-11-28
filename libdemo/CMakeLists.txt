cmake_minimum_required(VERSION 3.14)
project(demo CXX)

# set some common default compiler options
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# explicitly list the source files instead of searching them
# https://stackoverflow.com/questions/1027247/is-it-better-to-specify-source-files-with-glob-or-each-file-individually-in-cmak
# https://cmake.org/cmake/help/v3.15/command/file.html?highlight=glob#filesystem
set(DEMO_SOURCES ${CMAKE_SOURCE_DIR}/src/demo.cpp)
set(DEMO_HEADERS ${CMAKE_SOURCE_DIR}/include/demo/demo.hpp)

# add the new library, specifiy SHARED or STATIC is possible
# if not specified it will depend on whether BUILD_SHARED_LIBS is set to ON or OFF
add_library(demo ${DEMO_SOURCES} ${DEMO_HEADERS})

target_include_directories(demo PUBLIC
    "${CMAKE_SOURCE_DIR}/include"
    "${CMAKE_BINARY_DIR}/exports")

# generate the exports header with all necessary macros
include(GenerateExportHeader)
generate_export_header(demo EXPORT_FILE_NAME "${CMAKE_BINARY_DIR}/exports/demo_export.hpp")

# specify the install directory, always use a subdirectory for your header files(!)
install(TARGETS demo DESTINATION lib/)
install(FILES ${DEMO_HEADERS} ${PROJECT_BINARY_DIR}/exports/demo_export.hpp DESTINATION include/demo/)

# include sub directory with unit tests if requested
if (DEMO_ADD_TESTS)
    add_subdirectory(tests)
endif()

