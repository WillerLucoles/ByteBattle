from cx_Freeze import setup, Executable
import os


asset_folder = './asset/'

setup(
    name="Byte Battle",
    version="1.0",
    description="ByteBattle-Willer Lucoles",
    executables=[Executable("main.py", base="Win32GUI")],
    options={
        "build_exe": {
            "packages": ["pygame", "sqlite3"],
            "include_files": [asset_folder],
            "optimize": 2,
        }
    }
)
