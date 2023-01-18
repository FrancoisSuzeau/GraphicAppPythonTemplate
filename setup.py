from cx_Freeze import setup, Executable
base = None
# if your architecture is different then don't hesitate to change the relative path of your file when the main call is
executables = [Executable("src/main.py", base=base)]
# there is your personnal module you use/created in your project
packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
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

# the executable is in the 'build/exe.win-amd64-3.10' directory but named as the name of your main file (and not by the name you chose)
# -> it is not a feature but a bug or a missunderstanding. I'm still trying to correct this