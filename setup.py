from cx_Freeze import setup, Executable

setup(name="SpaceInvaders", 
	version="0.1", 
	description="Game",
	executables = [Executable("SpaceInvaders.py")])