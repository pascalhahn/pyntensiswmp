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


class IntensisWMPDevice(object):
    MODES = ['AUTO', 'HEAT', 'DRY', 'FAN', 'COOL']
    FANMODES = ['AUTO', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Only support updown swings so far
    SWINGMODES = ['AUTO', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'SWING']

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._connection = IntensisWMPConnection(self._host, self._port)

    def set_temperature(self, degrees):
        self._connection.send_command('SET,1:SETPTEMP,{}'.format(
            temperature * 10
        ))

    def set_fan_mode(self, fanmode):
        self._connection.send_command('SET,1:FANSP,{}'.format(fan_mode))

    def set_operation_mode(self, operation_mode):
        self._connection.send_command('SET,1:MODE,{}'.format(operation_mode))

    def set_swing_mode(self, swing_mode):
        self._connection.send_command('SET,1:VANEUD,{}'.format(swing_mode))

    def turn_on(self):
        self._connection.send_command('SET,1:ONOFF,ON')

    def turn_off(self):
        self._connection.send_command('SET,1:ONOFF,OFF')

    def update_status(self):
        device_data = self._connection.send_command('GET,1:*')
        lines = device_data.split('\r\n')
        for line in lines:
            if line:
                logging.debug('Line parsing: {}'.format(line))
                field, value = line.strip().split(':')[1].split(',', 1)
                setattr(self, field, value)