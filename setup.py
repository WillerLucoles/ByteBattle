from cx_Freeze import setup, Executable
import os


assets_folder = './assets'

setup(
    name="Byte Battle",
    version="1.0",
    description="ByteBattle-Willer Lucoles",
    executables=[Executable("main.py", base="Win32GUI")],
    options={
        "build_exe": {
            "packages": ["pygame", "sqlite3"],
            "include_files": [assets_folder],
            "optimize": 2,
        }
    }
)
