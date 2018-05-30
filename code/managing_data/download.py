url = "https://www.dropbox.com/sh/ryl8efwispnjw21/AACt2dLasqSDsCf-kcQwoWyfa?dl=1"
import urllib.request
import os

def downloadDeepFashionZip():
    currentPath = os.getcwd()
    file_name = currentPath+"/../../DeepFashion.zip"
    print('Downloading DeepFashion')
    urllib.request.urlretrieve(url, file_name)  
    print("Download Finished")

downloadDeepFashionZip()