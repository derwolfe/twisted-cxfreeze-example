import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["zope.interface"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "tw-cs",
        version = "0.1",
        description = "My twisted application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("echoserv.py", base=base)])
