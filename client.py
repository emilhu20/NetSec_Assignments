"""
Implementation of client 
"""

import socket


#addresses, ports and buffer size
SERVER_ADDRESS = '192.168.0.167'    #change ip address here
SERVER_PORT = 12345

CLIENT_ADDRESS = '192.168.0.196'        #change ip address here
CLIENT_PORT = 12346

BUFFER_SIZE = 1024


#find file to send to server and open it 
with open('file.bin', 'rb') as file:
    file_data = file.read()
    file_size = len(file_data)


#create TCP socket and connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind((CLIENT_ADDRESS, CLIENT_PORT))

client_socket.connect((SERVER_ADDRESS, SERVER_PORT))


#send data - data gets divided into buffer size pieces 
bytes_sent = 0

while bytes_sent < file_size:
    data = file_data[bytes_sent:bytes_sent + BUFFER_SIZE]
    client_socket.send(data)
    bytes_sent += len(data)


#close the client socket
client_socket.close()
print('File sent')
