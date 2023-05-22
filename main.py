import os
import shutil

def readDir():
    """
    Purpose:    
        Read the path dir of the main folder
    Return:
        :return: the string representation of the path dir to main folder
    """
    return input("\nEnter the path dir to main folder which contains subfolders to extract files from:\n")

def checkDir(path):
    """
    Purpose:    
        Check if the input path dir of the main folder is valid or not
    Precondition:
        :param path: the string representation of the path dir to main folder
    Return:
        :return True: if the path dir is valid
        :return False: otherwise
    """
    if os.path.isdir(path):
        return True
    else:
        return False

def scanSubfolder(mainFolderPath):
    """
    Purpose:
        Scan for all the subfolders in the main folder
    Return:
        :return: a list of paths to the subfolders
    """
    return [f.path for f in os.scandir(mainFolderPath) if f.is_dir()]

def makeDstFolder():
    """
    Purpose:
        Read the path of the destination folder and create the folder if it is not created
    Return:
        :return: the path to the destination folder
    """
    dstFolder = input("\nEnter the folder path for files to extract to:\n")
    if not os.path.exists(dstFolder):
        os.makedirs(dstFolder)
    return dstFolder

def extractFile(subfolders, dstFolder):
    """
    Purpose:
        Copy all files from subfolders and put into a single destination folder
    Postcondition:
        Open the destination folder contains all files
    """
    for folder in subfolders:
        for file in os.listdir(folder):
            source = os.path.join(folder, file)
            shutil.copy(source, dstFolder)
    os.startfile(dstFolder)


## MAIN ##

# Read the main folder and get the subfolders list
mainFolder = readDir()
while not checkDir(mainFolder):
    mainFolder = readDir()
subFolders = scanSubfolder(mainFolder)

# Read/create the extract destiantion folder
destinationFolder = makeDstFolder()

# Do file extraction, all files are copied not moved!
extractFile(subFolders, destinationFolder)

print("\nEXTRACTION COMPLETE!")