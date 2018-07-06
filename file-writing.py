#Open a file
myFile = open('scores.txt', 'w')

#Show attributes and properties
print('Name: ' + myFile.name)
print('Mode: ' + myFile.mode)

#Write to file (note: file must be open first)
myFile.write("GRF : 100\nUYI : 99\nWER: 367")
myFile.close()

#Read the file
myFile = open('scores.txt', 'r')
print("Reading file ...\n" + myFile.read(10))
myFile.seek(0)
print("Seek pointer reset. Reading file again...\n" + myFile.read(10))
myFile.close()

#Iterate through file
myFile = open('scores.txt', 'r')
print('The first line is ' + myFile.readline())
myFile.seek(0)

#Ierate through each line and do something
for line in myFile:
    newHighScorer = line.replace('WER', 'PHL')
    
print('The new high scorer is: ' + newHighScorer)
    
myFile.close()