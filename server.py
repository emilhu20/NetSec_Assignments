"""
Implementation of server 
"""

import socket

#addresses, ports and buffer size
SERVER_ADDRESS = '127.0.0.1' #change the ip address here
SERVER_PORT = 12345

BUFFER_SIZE = 1024


#create socket and bind server to address and port 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))


#listen for client connections 
server_socket.listen()


#accept new connection
print('Waiting for a client connection...')
client_socket, client_address = server_socket.accept()
print('Connected to client at', client_address)


#open a file for writing the received data
with open('received_file.bin', 'wb') as file:
    while True:
        data = client_socket.recv(BUFFER_SIZE)
        file.write(data)

        if not data:
            break

#close sockets
client_socket.close()
server_socket.close()

print('File received')
