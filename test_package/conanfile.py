import os

from conans import ConanFile, tools, RunEnvironment


class WinflexbisonTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def test(self):
        with tools.environment_append(RunEnvironment(self).vars):
            self.run("win_flex --version")
            self.run("win_flex %s" % os.path.join(self.source_folder, "calc.l"))

            self.run("win_bison --version")
            self.run("win_bison %s" % os.path.join(self.source_folder, "calc.y"))
