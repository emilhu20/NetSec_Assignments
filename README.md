### This is the implementation of throttling TCP connections 

The perform the proof-of-concept attack, the following is required: 
- Scapy library 
- Two computers connected to the same network. One shall act as the server and the other as the client. 

Please extract the contents of the zip file into your preferred folder. 

** Setting up the attack **
First check the IP addresses of the two computers and update the IP variables in the source codes accordingly. 
If there are no file present, then run the following command and ensure it is in the same folder

$ python fileGenerator.py 


** Performing the attack ** 
Start the server by running the following command

$ python3 server.py 

Then run the tool - The application will ask to enter either "delay" or "reset" to perform one of the attacks. 

$ python3 throttlingTCP.py

Finally, run the client

$ python3 client.py 

