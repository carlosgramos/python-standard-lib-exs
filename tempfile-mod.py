#Import the tempfile module
import tempfile

#Create a temporary file
tempFile = tempfile.TemporaryFile()

#Write to the file -> b turns it into a byte literal
tempFile.write(b"Save this special number for me: 34780")
tempFile.seek(0)

#Read from the temp file
print(tempFile.read())

#Close the file
tempFile.close()

