import os
from conans import ConanFile, CMake
from conans.tools import download, unzip, os_info, SystemPackageTool

class CatalystConan(ConanFile):
    name = "catalyst"
    version = "5.4.1"
    license = "<Put the package license here>"
    url = "https://github.com/bilke/conan-catalyst"
    description = "ParaView in-situ libraries"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports = ["FindCatalyst.cmake"]

    source_dir_name = "Catalyst-v%s-Base-Enable-Python-Essentials-Extras-Rendering-Base" % version
    install_dir = "_install"

    def source(self):
        zip_name = "%s.tar.gz" % self.source_dir_name
        download("https://www.paraview.org/paraview-downloads/download.php?submit=Download&version=v5.4&type=binary&os=Sources&downloadFile=%s" % zip_name , zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def system_requirements(self):
        pack_name = None
        if os_info.linux_distro == "ubuntu":
            pack_name = "openmpi" # libopenmpi-dev
        elif os_info.is_macos:
            pack_name = "open-mpi"
        if pack_name:
            installer = SystemPackageTool()
            installer.install(pack_name)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = self.install_dir
        cmake.definitions["PARAVIEW_INSTALL_DEVELOPMENT_FILES"] = "ON"
        if os_info.is_macos:
            cmake.definitions["PARAVIEW_DO_UNIX_STYLE_INSTALLS"] = "ON"
        if self.options.shared == False:
            cmake.definitions["BUILD_SHARED_LIBS"] = "OFF"
        if self.settings.build_type == "Debug" and self.settings.compiler == "Visual Studio":
            cmake.definitions["CMAKE_DEBUG_POSTFIX"] = "_d"
        source_path = "%s/%s" % (self.conanfile_directory, self.source_dir_name)
        self.run('%s/cmake.sh "%s" %s' % (source_path, source_path, cmake.command_line))
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*", dst=".", src=self.install_dir)
        self.copy("FindCatalyst.cmake", dst=".", src=self.conanfile_directory)

    #def package_info(self):
    #    self.cpp_info.libs = ["hello"]
