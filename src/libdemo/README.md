# demo library

A sample library project. It's purpose is to show how a C++ project could be structured and managed using cmake.

## Compilation

### Linux

    mkdir ./build
    cd build
    cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DDEMO_ADD_TESTS=ON -DCMAKE_INSTALL_PREFIX=./stage ..
    make -j`nproc`
    make install

### Windows

    md build
    cd build
    cmake -G"Visual Studio 16 2019" -Ax64 -Thost=x64 -DBUILD_SHARED_LIBS=ON -DDEMO_ADD_TESTS=ON -DCMAKE_INSTALL_PREFIX=./stage ..
    cmake --build . --config Release --target INSTALL

## Run the Unit Tests

### Linux

    cd ./build/tests
    ./demo_tests

### Windows

    cd build\tests\Release
    demo_tests.exe

