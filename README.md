## AL META Damage Screen Analyzer
### About
This program analyzes a screenshotted image of the damage screen in Azur Lane specifically for META battles. Because of the nature of the game's damage counting system, the total damage displayed in-game is almost always different from the individual shipgirls' total damage totaled manually, if not always. This program's purpose is to automate that, by using Python for optical character recognition (OCR) and a batch file for the routine of checking a new file, and passing it to the Python script through the command line if there is one. The output displays: 1) total damage displayed in-game, 2) total damage from adding all shipgirls' total damage and, 3) the difference between the two aforementioned outputs.

The suitable users for this program would be: 1) Azur Lane players that are, 2) PC players, 3) use emulators for playing the game and, 4) often plays META battles and wants to calculate the total damage of each ship.

Main libraries used:
* [OpenCV](https://pypi.org/project/opencv-python) - image processing
* [Python Tesseract](https://github.com/madmaze/pytesseract) - Python wrapper for Google's Tesseract
### Prerequisites
* [Python](https://www.python.org/downloads) - programming language in order to use OCR tools
* [Pip](https://pip.pypa.io/en/stable/installation) - package management system
* [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) - optical character recognition engine
### Setup
Install the necessary package
```
pip install pytesseract
```
### Usage
Change the path variables `sc_path` (emulator screenshots folder path) and `fl_path`(`main.py` path) in `main.bat` to its respective paths, and `pytesseract.pytesseract.tesseract_cmd` in `main.py` for the tesseract path.

Run the batch file in the background whenever you want to analyze a damage screen soon. Check the name of the screenshots folder of your emulator to make sure it has no spaces. After that you only need to take the screenshot itself in order for the program to analyze it.

You can also run the Python file manually to analyze existing images. This is the syntax for the command:
```
python -u python_file_path -img image_file_path
```
An example:
```
python -u "C:\Users\User\Documents\folder\main.py" -img C:\Users\User\Downloads\folder\example.png
```
#### Notes
The most important thing to note is that this program isn't perfect. I had a small amount of images to test on, to which most of it look similar to each other, particularly I'm talking about the ships who are MVP on those images. The calculated total for the shipgirls' damage and the extracted total damage in-game from the image could be either higher or lower than usual, and varying from obvious to subtle as it depends on the digits affected. The total damage displayed in the game is much more susceptible to inaccurate readings, compared to the individual damages, as its background is highly affected by the MVP shipgirl's art.