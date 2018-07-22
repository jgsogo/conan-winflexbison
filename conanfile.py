import os
from conans import ConanFile, CMake, tools


class WinflexbisonConan(ConanFile):
    name = "winflexbison"
    version = "2.5.14"
    license = "Apache 2.0"
    url = "https://github.com/jgsogo/conan-winflexbison"
    description = "Conan package for winflexbison: a windows port the Flex (the fast lexical analyser) and Bison (GNU parser generator)."
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    lib_name = name + "-" + version

    def configure(self):
        if self.settings.os != "Windows" or self.settings.compiler != "Visual Studio":
            raise Exception("winflexbison is only supported for Visual Studio (Windows).")

    def source(self):
        tools.get("https://github.com/lexxmark/winflexbison/archive/v{version}.tar.gz".format(version=self.version))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.lib_name)
        if self.settings.compiler.version == "12":
            tools.replace_in_file(os.path.join(self.lib_name, 'flex', 'src', 'flexdef.h'), "#include <stdio.h>", "#include <stdio.h>\n#define snprintf _snprintf")
        cmake.build()

    def package(self):
        output_path = os.path.join(self.build_folder, self.lib_name, "bin", str(self.settings.build_type))
        self.copy("*", dst="bin", src=output_path)
        if self.settings.build_type == "Debug":
            release_path = os.path.join(self.build_folder, self.lib_name, "bin", "Release")
            self.copy("*", excludes="*.exe", dst="bin", src=release_path)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

