# Audio file indexing
#Libraries
import os
import glob

#Scripts
from main import save_data

#----------------------------------------------------------
#Global variables
master_list = []
path = "Audio Files/"  #Change this to your file path
filetype = ".mp3"  #Change this to your file type
delim_list = [',', '-', '_']

#----------------------------------------------------------
# Main function

#get all '.mp3' files in the directory
mp3_files = glob.glob(path + '*' + filetype)

#cleans up file names and adds it to the master list
for i in range(len(mp3_files)):
  temp = []
  temp = mp3_files.copy() #copies the list to a temp list
  temp[i] = temp[i].replace(path, "")  #clears the path
  master_list.append(temp[i].replace(filetype, ""))  #adds the song name to the master list

  for j in range(len(delim_list)): # Fixes the text
    if delim_list[j] in str(master_list[i]):
      #replaces other delimiters with spaces
      master_list[i] = master_list[i].replace(delim_list[j], " ")
  
  master_list[i] = master_list[i].title()  #capitalizes the song name
  
  
  
save_data('songlist.txt', master_list, '')