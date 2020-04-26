import os
import shutil
import zipfile

filepath = "../temp/zipFile"
path = os.listdir("../temp/")

if not "zipFile" in  path:
    os.mkdir(filepath)
    print ("path test created")
else:
    print ("Path already exist")
    fileclaimpath = "../temp/zipFile"
    pathclaim = os.listdir("../temp")
    print pathclaim
    if "SERCON201556.zip" in pathclaim:
        with zipfile.ZipFile("../temp/SERCON201556.zip", 'r') as zip_ref:
            zip_ref.extractall(fileclaimpath)
        print "File unzipped Successfully...!"
    else:
        print "claim File does Not exist"       
