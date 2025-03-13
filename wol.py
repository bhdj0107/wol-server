from socket import *
import struct
import sys
import traceback
macAddr = sys.argv[1]
broadcast = sys.argv[2]

try:
    sep = macAddr[2]
    macAddr = macAddr.replace(sep,'')
        
    data = b'FFFFFFFFFFFF' + (macAddr * 16).encode()
    send_data = b''
    
    for i in range(0, len(data), 2):
        send_data += struct.pack('B', int(data[i: i + 2], 16))
    
    broadcast_sock = socket(AF_INET, SOCK_DGRAM)
    broadcast_sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    broadcast_sock.sendto(send_data, (broadcast, 9))
    broadcast_sock.close()
    print("OK")
except Exception as e:
    print("error")
