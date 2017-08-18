from tempfile import mkdtemp
from os import path
from conans import ConanFile, AutoToolsBuildEnvironment, tools


class BisonConan(ConanFile):
    name = "bison"
    version = "3.0.4"
    settings = "os", "compiler", "build_type", "arch"
    description = "A general-purpose parser generator that converts an annotated context-free grammar into a deterministic LR or GLR"
    author = "Uilian Ries <uilianries@gmail.com>"
    url = "https://github.com/uilianries/conan-bison"
    license = "https://www.gnu.org/licenses/gpl-3.0.en.html"
    options = {"enable_yacc": [True, False]}
    default_options = "enable_yacc=True"
    exports = "LICENSE"
    install_dir = mkdtemp(prefix=name)
    release_name = "%s-%s" % (name, version)

    def source(self):
        tools.get("https://ftp.gnu.org/gnu/bison/bison-%s.tar.gz" % self.version)

    def _run(self, command):
        if self.settings.os == "Windows":
            tools.run_in_windows_bash(self, tools.unix_path(command))
        else:
            self.run(command)

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        with tools.environment_append(env_build.vars):
            configure_args = ['--prefix=%s' % self.install_dir]
            configure_args.append('--enable-yacc' if self.options.enable_yacc else '--disable-yacc')
            with tools.chdir(self.release_name):
                self._run("./configure %s" % ' '.join(configure_args))
                self._run("make all")
                self._run("make install")

    def package(self):
        self.copy(pattern="COPYING", dst=".", src=self.release_name)
        self.copy(pattern="*", dst="bin", src=path.join(self.install_dir, "bin"))
        self.copy(pattern="*", dst="lib", src=path.join(self.install_dir, "lib"))

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()
