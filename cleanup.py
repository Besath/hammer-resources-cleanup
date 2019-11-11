import sys
import os

#stocks_dir - where the lists of stock files are (|steam_dir|\steamapps\KreedzClimbing\bin by default)
#resources_dir - where materials, models, etc. folders are located

if len(sys.argv) == 1:
    print(
        "\nWhen run without arguments, the script assumes that both the stock_*.txt files\n"
        "and folders with resources (materials, models, particles, sound) are in the same\n"
        "directory as the script\n")
    choice = input("Are you sure you want to continue in the current directory? (Y/N) ")
    if (choice.lower() == 'y'):
        stocks_dir = os.curdir
        resources_dir = os.curdir
    else:
	    stocks_dir = input("Enter path to the folder with stock_*.txt files (|steam_dir|\\steamapps\\KreedzClimbing\\bin by default): ")
	    resources_dir = input("Enter path to directory with extracted game files: ")
elif len(sys.argv) == 3:
    stocks_dir = sys.argv[1]
    resources_dir = sys.argv[2]
else:
    print(
        "\nUsage: python cleanup.py [path1] [path2]\n\n"
        "path1 - path to directory with stock_*.txt files (|steam_dir|\\steamapps\\KreedzClimbing\\bin by default)\n"
        "path2 - path to directory with extracted game files (e.g. |steam_dir|\\steamapps\\KreedzClimbing\\kz\\hammer_resources)\n")
    sys.exit()

def delete_files(file_name):
    list_file = open(os.path.join(stocks_dir, file_name), "r")
    stocks_list = list_file.read().splitlines()
    list_file.close()
    for f in stocks_list:
        try:
            os.remove(os.path.join(resources_dir, f))
            print("Deleted file " + os.path.join(resources_dir, f))
        except FileNotFoundError:
            print("File not found: " + os.path.join(resources_dir, f))
            continue

files_list = [
    "stock_ani.txt", "stock_mdl.txt", "stock_mp3.txt", "stock_pcf.txt",
    "stock_phy.txt", "stock_raw.txt", "stock_vmt.txt", "stock_vtf.txt",
    "stock_vtx.txt", "stock_vvd.txt", "stock_wav.txt"
]

for i in range(len(files_list)):
    delete_files(files_list[i])
