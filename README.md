# GraphicAppPythonTemplate


## Purpose
No clue

## How to build (Windows)
### Using a setup file
- You need to install **cx_Freeze**. Open a powershell and copy/paste this : ```pip install cx_Freeze```
- You also need to install **idna** to manage internationnal domain name : ```pip install idna```
- Then go at the same level than **setup.py**, customize to you liking and use this in a terminal : ```python setup.py build```
- The executable will be in the **build/exe.win-amd64-xx** repertory named as your main python script file (for now)

### Using PyInstaler
- You need to install **PyInstaller**. Use this command to do so : ```pip install -U pyinstaller```
- Go at the same level of your main python file and use : ```pyinstaller -F your_program.py```
- The executable will be in the **dist/** repertory named as ```your_program```