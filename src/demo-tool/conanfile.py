from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration

class DemoToolConan(ConanFile):
    name = "demo-tool"
    settings = "os", "compiler", "arch", "build_type"
    generators = [ "cmake_find_package", "cmake_find_package_multi" ]

    def build_requirements(self):
        # this is where you can specify packages like the android-ndk, nasm and other build tools
        # self.requires("nasm/1.x.y")
        pass

    def requirements(self):
        # define dependencies here:
        self.requires("demo/1.0@project/stable")
        self.options["demo"].shared = False

    def install(self):
        # in case some binary files from dependencies should be copied over
        # e.g. *.so, *.pdb files
        pass

