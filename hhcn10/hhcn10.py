import socket
import time

class HHCN10Exception(Exception):
    pass

class HHCN10ValueError(HHCN10Exception):
    pass

class HHCN10:
    TCP_PORT = 5000

    def __init__(self, device_ip='192.168.0.105'):
        self.ip = device_ip

    def _send_msg_and_receive(self, msg: bytes):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.TCP_PORT))
            socket.timeout(1)
            s.sendall(msg)
            data = s.recv(1024)
            time.sleep(.5)

        return data


    def ping(self) -> bool:
        ''' Tries to ping the HHC-N10. Raises an exception
        if can't communicate with it'''

        rcv = self._send_msg_and_receive(b'name')
        return rcv == b'name="HHC-N1O"'

    def read_relay(self):
        ''' Returns True of False wether the relay is on or off'''
        rcv = self._send_msg_and_receive(b'read')
        return rcv == b'on1'

    def set_relay(self, relay_status: bool):
        ''' Sets the relay to the open (true) or closed (Off) position.'''
        if relay_status:
            msg = b'on1'
        else:
            msg = b'off1'

        self._send_msg_and_receive(msg)

    def toggle_relay_secs(self, seconds: int):
        ''' Sets the relay to be open during `seconds` seconds.
        WARNING: irrespective of the next set state, the relay
        will close at the end of the set seconds'''

        if not 0 <= seconds <= 99:
            raise HHCN10ValueError('Seconds must be a number between 1 and 99s')

        msg = f'on1:{seconds:02}'.encode()

        self._send_msg_and_receive(msg)


    def change_ip(self, new_ip: str, netmask: str, gateway: str):
        cmds = [
            f'AT+SET="{self.ip}"',
            f'AT+IP="{new_ip}"',
            f'AT+SUBNET="{netmask}"',
            f'AT+GATEWAY="{gateway}"',
            'AT+STATUS=0',
            'AT+SAVE=1'
        ]
        msg = ''.join(cmds).encode()


        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.bind(("", 65535))
            s.sendto(msg, ('<broadcast>', 65535))
