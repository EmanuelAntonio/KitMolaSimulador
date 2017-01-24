from cx_Freeze import setup, Executable
setup(
    name = "KitMola",
    version = "0.2",
    options = {"build_exe": {
        'packages': ["os","sys","ctypes","wx","OpenGL","math"],
        'include_msvcr': True,
    }},
    executables = [Executable("KitMola.py",base="Win32GUI",icon="icon.ico")]
)
#'include_files': ['boneca.jpg'],
