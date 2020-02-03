# game

This is an in-development game (think alpha or pre-alpha) where you start with very little on an astronimical body and the goal is to eventually terraform it.

# Installation

*Dependencies required to run:*

  - [pygame for py2.7 and pygame-sdl4 (32-bit)](http://www.pygame.org/wiki/GettingStarted) 
    - [Windows Direct Download](http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi)
	- [Mac Direct Download](http://pygame.org/ftp/pygame-1.9.1release-python.org-32bit-py2.7-macosx10.3.dmg)
	- [Linux and BSD installation information](http://www.pygame.org/download.shtml)
  - [python 2.7](https://www.python.org/downloads)
  
  

**Linux Installation via Python pip:**
"Game" runs on Python 2.7 and the Pygame package.
Since Linux distributions are often out of date, first make a local up to date version
of pip in your user files (this avoids conflicts with your official distribution copy).
Also never use sudo with pip as this throws errors and could change things your package
manager set up. Start with the console in the directory you want to download Game into.
```
pip install --user --upgrade pip
pip install --user pygame
git clone https://github.com/Master-Foo/game.git
cd game
```

**Run the game:**
```
python demo.py
```
