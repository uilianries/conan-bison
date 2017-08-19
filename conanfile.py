from tempfile import mkdtemp
from os import path, symlink
from conans import ConanFile, AutoToolsBuildEnvironment, tools


class BisonConan(ConanFile):
    name = "bison"
    version = "3.0.4"
    settings = "os", "compiler", "build_type", "arch"
    description = "A general-purpose parser generator that converts an annotated context-free grammar into a deterministic LR or GLR"
    author = "Uilian Ries <uilianries@gmail.com>"
    url = "https://github.com/uilianries/conan-bison"
    license = "https://www.gnu.org/licenses/gpl-3.0.en.html"
    exports = "LICENSE"
    install_dir = mkdtemp(prefix=name)
    release_name = "%s-%s" % (name, version)

    def source(self):
        tools.get("https://ftp.gnu.org/gnu/bison/bison-%s.tar.gz" % self.version)

    def configure(self):
        if self.settings.os == "Windows":
            raise Exception("Bison is not supported on Windows.")

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        configure_args = ['--prefix=%s' % self.install_dir]
        with tools.chdir(self.release_name):
            env_build.configure(args=configure_args)
            env_build.make(args=["all"])
            env_build.make(args=["install"])

    def package(self):
        self.copy(pattern="COPYING", dst=".", src=self.release_name)
        self.copy(pattern="bison", dst="bin", src=path.join(self.install_dir, "bin"))
        self.copy(pattern="*", dst="lib", src=path.join(self.install_dir, "lib"))

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()
        self.env_info.path.append(path.join(self.package_folder, "bin"))
