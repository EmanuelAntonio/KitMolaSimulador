from cx_Freeze import setup, Executable
setup(
    name = "KitMola",
    version = "0.1.4",
    options = {"build_exe": {
        'packages': ["os","sys","wx","OpenGL","PIL"],
        'include_msvcr': True,
        'include_files': ['cam.ico','config.ico','obj.ico','tool.ico'],
    }},
    executables = [Executable("KitMola.py",base="Win32GUI",icon="icon.ico")]
    )



#'include_files': ['boneca.jpg'],
