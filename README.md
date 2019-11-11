# What is this?  
  
This is a small script used to get rid of overrides (files that already exist in Kreedz Climbing) that may get into your hammer_resources folder when extracting some other games.  
  
# Raptor's VBSP can ignore overrides so what's the point?  
  
True, you can use -ignoreoverrides when compiling to skip any file that comes with the game, but what's the point of having useless copies of the files cluttering your disk?  
  
# How do I use this?  
  
First, make sure you have python installed. Then, just run this script from command line as such:  
  
## python cleanup.py [path1] [path2]  
  
where:  
  
path1 is the path to the folder containing stock_*.txt files. These come with the game and are located in your |steam_dir|\steamapps\KreedzClimbing\bin  
path2 is the path to the folder where you extracted files from another Source Engine game. For example, if you extracted the files straight into your hammer_resources directory, the path would be |steam_dir|\steamapps\KreedzClimbing\kz\hammer_resources  
  
You can also use the script without arguments. Doing so, you will be prompted to confirm whether that's what you actually wanted to do. If you answer positively, the script will assume that both stock_*.txt files and the unpacked game files are in the directory from which you are running the script. A negative answer to the prompt will allow you to enter the correct paths.
