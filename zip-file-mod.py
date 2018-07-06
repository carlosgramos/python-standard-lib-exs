#Zipfile module
import zipfile
import os

#Find the version of os or os.path that will return the path including the current dir
#Note that __file__ is a constant representing the current file
print(os.getcwd())
print(os.path.abspath(__file__))
#dirname is the winner, now we can use it in the zip.ZipFile() method
print(os.path.dirname(__file__))


#Open and list
zip = zipfile.ZipFile(os.path.dirname(__file__) + '/Archive.zip', 'r')
print(zip.namelist())

#Metadata in the zip folder
for meta in zip.infolist():
    print(meta)

print(zip.getinfo('purchased.txt'))

#zipAccess to files in the zip folder
print(zip.read('wishlist.txt'))
with zip.open('wishlist.txt') as f:
    print(f.read())

#Extractiing files
zip.extract('purchased.txt')
zip.extractall()

#Closing the zip
zip.close()