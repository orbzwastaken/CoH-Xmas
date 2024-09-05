# File Conversion
This is a .py program designed to convert audio files for an Uno, or other microcontroller, to use.
This program will find .mp3 files in a specific path and convert the audio into usable data for lights.

Made by: Me with assistance from CoPilot for troubleshooting.
> Last Updated on 9/3/2024 @ 5:23 PM (UDT-05:00) \
> Version 0.5


## Status
This program is: **Unfinished**
### What works?
The file indexing works.
  >The file indexing system or 'index.py' is a main part of the program. It looks at all the files located in your desired path, picks out a specific file type and puts them into a list. It then looks at that list of files, cleans up the string and then adds song into the master list. The master list is then made into a file called: 'songlist.txt'.

The program runs without an error?? maybe?

### What doesn't?
Converting the files does not currently work automatically. 
> I am in the process of connecting it to the main program and getting it to convert the mp3s.

Getting the ardino to pull data, also doesn't work.
> It is a serial connection I think so only numbers go through

Being robust when dealing with file names.
> It just isn't.

## This program requires the following libraries:
  ### Indexing:
    - os
    - glob

  ### Audio Conversion:
    - numpy
    - pydub
    - ffmpeg

## Necessary Edits and Notes
* For this program to work you need to set the variable '[path](https://replit.com/@OrBzWasTaken/FileConversion-mp3#index.py:6)' to the location of the folder holding all your .mp3 files.
* For best results with indexing, only name your .mp3 file the name of the song. The use of the delimiters: '**-**' and '**_**' are recommended instead of spaces in your file names. Other delimiters can be used instead of spaces but you will have to add whatever delimiter you use to the [list](https://replit.com/@OrBzWasTaken/FileConversion-mp3#index.py:14).

