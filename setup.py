from cx_Freeze import setup, Executable

setup(
    name = "tetris_exefile",
    version = "0.1",
    description = "Game",
    executables = [Executable("tetris_code.py")])
