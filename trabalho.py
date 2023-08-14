import socket
from colorama import init, Fore

# flags to color the messages
init()
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

# function to check if a port is open
def check_port(host, port, protocol):
    # check the protocol used and then creates the proper socket
    if (protocol == 'tcp'):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
        sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sc.settimeout(0.1)
    try:
        if (not sc.connect_ex((host, port))):
            print(f'{GREEN}Port {port} is open and running {socket.getservbyport(port, protocol)}/tcp {RESET}')

    except socket.error:
        pass

for port in range (0, 450):
    # check for tcp protocol
    check_port('104.21.52.8', port, 'tcp')
    # check for udp protocol
    check_port('104.21.52.8', port, 'udp')
