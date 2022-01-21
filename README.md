# Project_2022

21/01/22

Have tried out pyTesseract, a python api to Tesseract, an Optical Caracter Recognition software.
https://en.wikipedia.org/wiki/Tesseract_(software)

Working on macOS i installed Tessaract with homebrew:

brew install tesseract

then installed support for all languagees, think there is 48 or so, including Norwegian:

brew install tesseract-lang


If you run Linux tesseract is available on apt
If you run Windows tesseract is available on vcpkg
or one could build from source:

https://github.com/tesseract-ocr/tesseract


Once installed, install python API pytesseract:

pip install pytesseract

And hopefuly you will be able to run receipt_reader.py

Have only tested with a REMA 1000 recipt i found online, seems to work ok at least.

-peter