if (NOT DEFINED ENV{ANDROID_NDK_HOME})
    message (FATAL_ERROR "ANDROID_NDK_HOME environment variable not set!")
endif()

# Set android platform settings
set(ANDROID_ABI "arm64-v8a")
set(ANDROID_NATIVE_API_LEVEL 28)
set(ANDROID_STL "c++_shared")
set(ANDROID_TOOLCHAIN clang)

# Include actual android.toolchain.cmake
include($ENV{ANDROID_NDK_HOME}/build/cmake/android.toolchain.cmake)

# Remove debug symbols from release build
# https://github.com/android/ndk/issues/243
if ("${CMAKE_BUILD_TYPE}" STREQUAL "Release")
    string(REPLACE "-g" "" CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS})
    string(REPLACE "-g" "" CMAKE_CXX_FLAGS_RELEASE ${CMAKE_CXX_FLAGS_RELEASE})
    string(REPLACE "-g" "" CMAKE_C_FLAGS ${CMAKE_C_FLAGS})
    string(REPLACE "-g" "" CMAKE_C_FLAGS_RELEASE ${CMAKE_C_FLAGS_RELEASE})
endif()

