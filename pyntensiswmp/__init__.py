# Module that handles connection to intensis WMP device
import socket

class IntensisWMPConnection(object):
    TIMEOUT = 5
    TERMINATION = '\r\n'
    RECVBUF = 2048

    def __init__(self, host, port=3310):
        self._host = host
        self._port = port

    def send_command(self, command):
        # Always connect, execute command, wait for reply and exit
        # THIS SHOULD BE IMPROVED
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(IntensisWMPConnection.TIMEOUT)
        sock.connect((self._host, self._port))
        sock.sendall("{}{}".format(
            command, IntensisWMPConnection.TERMINATION).encode())
        reply = sock.recv(IntensisWMPConnection.RECVBUF)
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return reply.decode()
