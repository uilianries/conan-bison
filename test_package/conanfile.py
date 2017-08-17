from conans import ConanFile, tools
import os
from subprocess import check_call

class BisonTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    user = os.getenv("CONAN_USERNAME", "conan")
    channel = os.getenv("CONAN_CHANNEL", "stable")
    requires = "bison/3.0.4@%s/%s" % (user, channel)

    def imports(self):
        self.copy(pattern="*", dst="bin", src="bin")

    def test(self):
        with tools.chdir("bin"):
            assert(os.path.isfile("bison"))
            check_call(["./bison", "--version"])
