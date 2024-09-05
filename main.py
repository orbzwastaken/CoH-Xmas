#Main file for the program
#Libraries

#Scripts
from os import close, read
from index import *
from index import master_list as master_list, mp3_files as mp3_files

#----------------------------------------------------------
#Global variables
current_song = ""

#----------------------------------------------------------
# Functions


# Function to save processed data to a file
def save_data(filename, data, delimiter):
  with open(filename, 'w') as f:
    for entry in data:
      f.write(delimiter.join(map(str, entry)) + '\n')
    f.close()


#Run a file
def runfile(filename):
  with open(filename + ".py") as file:
    exec(file.read())
  print("Ran file: " + filename)
  file.close()


#----------------------------------------------------------
#Funcitons
def getCurrentSong(stepper):  #Gets the current song in the list
  temp = ""
  with open('songlist.txt', 'r') as mstr:  #Open file
    while True:
      line = mstr.readline(stepper)  #read a set line
      if not line:
        break
      else:  # if line is not empty
        temp = line.strip()  #removes whitespace
        temp.lower()  #makes sure it is lowercase
        if temp in mp3_files[stepper]:  #checks file list
          current_song = mp3_files[stepper]  #file equals current song

        else:
          print("temp value does not match mp3 list value")
          break


# Main function

runfile('index')  #Index all audio files in the directory
for stepper in range(len(master_list)):
  getCurrentSong(stepper)

runfile('convert')
