from cx_Freeze import setup, Executable
import os

# if your architecture is different then don't hesitate to change the relative path of your file when the main call is
executables = [
        Executable(
            script="main.py", 
            base="Win32GUI",
            targetName="GraphicAppPythonTemplate.exe",
            # copyDependentFiles = True,
            # compress=True,
            # appendScriptToExe = True,
            # appendScriptToLibrary = True,
            icon = None # if you want to use an icon file, specify the file name here
        )
]

packages = ["idna", "os", "packages"]
includefiles = [os.path.join('packages', 'application.py'), os.path.join('packages', 'functions.py')] #include path of your personnal module if they are not located in the same directory of your main script
binaries = []
excludes = []
options = {
    'build_exe': {    
        'excludes':excludes,
        'packages':packages,
        'include_files':includefiles,
        'bin_includes':binaries,
        "include_msvcr": True
    },
}
# all the external module (such as matplot lib etc is copy directly in the lib directory and then transformed in a dynamic library file)

# change the name field with name of your application
setup(
    name = "GraphicAppPythonTemplate",
    options = options,
    version = "1.0",
    description = 'Un template d\'application graphique et transformer en executable',
    executables = executables
)

# the executable is in the 'build/exe.win-amd64-xx' directory but named as the name of your main file