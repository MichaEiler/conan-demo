from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration

class DemoConan(ConanFile):
    name = "demo"
    version = "1.0"
    license = "MIT"
    url = "https://github.com/MichaEiler/conan-demo"
    settings = "os", "compiler", "arch", "build_type"

    # exports_sources = ["example_change.patch"]

    options = { "shared": [True, False] }
    default_options = { "shared": False }

    git_url = "git@github.com:MichaEiler/conan-demo.git"
    git_tag = "v1.0"
    src_path = "conan-demo/src/libdemo/"

    def configure(self):
        # check the selected settings
        if self.settings.os == "Arduino":
            raise ConanInvalidConfiguration("This library only compiles on platforms with full STL support.")

    def build_requirements(self):
        # this is where you can specify packages like the android-ndk, nasm and other build tools
        # self.requires("nasm/1.x.y")
        pass

    def requirements(self):
        # define dependencies here:
        #self.requires("boost/1.73.0@user/channel")
        #self.options["boost"].shared = self.option.shared
        pass

    def source(self):
        self.run(f"git clone {self.git_url}")
        self.run(f"cd {self.src_path} && git checkout {self.git_tag}")

        # in case of required changes to some source code or build files within the git repository
        # add the patch to exports_sources and apply it here
        # this will also work on windows, since we are using a python/conan patch tool implementation
        # https://docs.conan.io/en/latest/reference/tools.html#tools-patch
        # tools.patch(base_path=self.src_path, patch_file="example_change.patch")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = "ON" if self.options.shared else "OFF"
        cmake.definitions["DEMO_ADD_TESTS"] = "OFF"
        # many other options are set automatically by CMake class
        # for scenarios where cross compilation is important, those should have been already set in the conan profile
        cmake.configure(source_folder=self.src_path)
        cmake.build()

        # the default cmake options are set in a way that a good CMakeLists.txt file already puts the resulting files into
        # the correct folders within the conan package (e.g. package/lib/, package/include/, ...)
        cmake.install()
        

    def package(self):
        # most copy operations can be handled by cmake install, in case additional files need to be copied or the CMakeLists.txt
        # does not feature an install option, this can be done here
        if self.settings.os == "Windows" and self.settings.build_type == "Debug":
            self.copy("*.pdb", src="./Debug/", dst="lib/", keep_path=False)

    def package_info(self):
        # remember the cmake generated export header definitions in libdemo?
        # let's make sure that in case of a static library the correct defines are set when consuming this package
        if not self.options.shared:
            self.cpp_info.defines.append("DEMO_STATIC_DEFINE")

        self.cpp_info.libs.append(self.name)

        # define the name in the automatically generated find_package scripts
        self.cpp_info.names["cmake_find_package"] = "Demo"
        self.cpp_info.names["cmake_find_package_multi"] = "Demo"

        # linking system libraries in case necessary can be done here
        #if self.settings.os == "Linux":
        #    self.cpp_info.system_libs.append("pthread")


