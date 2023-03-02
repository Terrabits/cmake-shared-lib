from conan             import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class CMakeSharedLibConan(ConanFile):
    name         = "cmake_shared_lib"
    version      = "1.0.0"
    package_type = 'library'

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options  = {"shared": [True], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}



    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cmake_shared_lib"]
