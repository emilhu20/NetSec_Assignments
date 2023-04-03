
import os

#size of file
size = 1000* 1024 * 1024

#file content -> just random data
data = os.urandom(size)

#write to binary file 
with open('file.bin', 'wb') as file:
    file.write(data)
    
print('File has been generated')