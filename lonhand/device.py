import socket
import binascii

class EthernetRelay(object):

    def __init__(self, tcp_ip='192.168.1.43', tcp_port=8899, pwd="admin"):
        self._ip = tcp_ip
        self._port = tcp_port
        self._password = "61 64 6D 69 6E 0D 0A" # TBD
        self._state = False

    def is_on(self):
        self.control("55 AA 00 03 00 0A 00 0D")
        return self._state

    def toggle(self):
        self.control("55 AA 00 03 00 06 00 09")

    def turn_on(self):
        self.control("55 AA 00 03 00 02 01 06")

    def turn_off(self):
        self.control("55 AA 00 03 00 01 01 05")

    def control(self, cmd):
        BUFFER_SIZE = 2048
        #
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        #
        s.send(binascii.a2b_hex(self._password.replace(" ", "")))
        data = s.recv(BUFFER_SIZE)
        #
        s.send(binascii.a2b_hex(cmd.replace(" ", "")))
        data = s.recv(BUFFER_SIZE)
        #
        s.close
        #
        self._state = (data == "?") # TBD

