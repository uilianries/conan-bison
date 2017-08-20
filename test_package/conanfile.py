from conans import ConanFile
import os
from subprocess import check_call

class BisonTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    user = os.getenv("CONAN_USERNAME", "uilianries")
    channel = os.getenv("CONAN_CHANNEL", "testing")
    requires = "bison/3.0.4@%s/%s" % (user, channel)

    def test(self):
        check_call(["bison", "--version"])
        check_call(["bison", "-d", os.path.join(self.conanfile_directory, "mc_parser.yy")])
