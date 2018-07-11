import os
from conans import ConanFile, CMake, tools


class WinflexbisonConan(ConanFile):
    name = "winflexbison"
    version = "2.5.14"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Winflexbison here>"
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
        cmake.build()

    def package(self):
        output_path = os.path.join(self.build_folder, self.lib_name, "bin", str(self.settings.build_type))
        self.copy("*", dst="bin", src=output_path)
        if self.settings.build_type == "Debug":
            release_path = os.path.join(self.build_folder, self.lib_name, "bin", "Release")
            self.copy("*", excludes="*.exe", dst="bin", src=release_path)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

