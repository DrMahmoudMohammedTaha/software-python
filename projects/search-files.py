from os import listdir
import os

def searchFiles(pathFolder):
    for filename in listdir(pathFolder):
        if filename.endswith(".html"):
            with open(pathFolder + "\\" + filename) as currentFile:
                text = currentFile.read()
                if ('img_avatar' in text):
                    print('found in: ' + filename[:-4] + '\n')

def deleteNotUsed(pathFolder , imageName):
    for filename in listdir(pathFolder):
        if filename.endswith(".html"):
            with open(pathFolder + "\\" + filename) as currentFile:
                text = currentFile.read()
                if ( imageName in text):
                    return
    
    os.remove("C:\\Users\\Dell\\Desktop\\w3-schools\\images\\" + imageName)
    print(imageName + " deleted")

path = "C:\\Users\\Dell\\Desktop\\w3-schools\\images"
for imgName in listdir(path):
    if imgName.endswith(".jpg"):
        deleteNotUsed("C:\\Users\\Dell\\Desktop\\w3-schools\\w3css" , imgName  )


