import socket
from colorama import init, Fore

# flags to color the messages
init()
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
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
            print(f'{GREEN}Port {port} is open and running {socket.getservbyport(port, protocol)}/{protocol} {RESET}')

    except socket.error:
        pass

# getting the target and the ports to scan
target = str(input('Enter the target IP or domain: '))
port_begin = int(input('Enter the first port to scan: '))
port_end = int(input('Enter the last port to scan: '))

print()
print(f'{YELLOW}Scanning {target} from port {port_begin} to {port_end}... {RESET}')
for port in range (port_begin, port_end+1):
    # check for tcp protocol
    check_port(target, port, 'tcp')
    # check for udp protocol
    check_port(target, port, 'udp')
