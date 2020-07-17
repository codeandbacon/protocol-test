import serial
import threading

class ProtocolTest():

    def __init__(self, addr, baudrate=115200):
        self.rf = serial.Serial(addr, baudrate)

    def layer2(self, data):
        return

    def layer1(self, data):
        """
        - remove total bytes
        - remove signal quality (if present)
        """
        print(data.decode('utf8'))
        return

    def send(self, data):
        # TODO: find a better way of sending, AT commands maybe?
        self.rf.write(bytes(f"send('{data}')\r", 'utf8'))

    def recv(self):
        print('waiting data...')
        while True:
            data = self.rf.readline()
            print('data received', data)
            self.layer1(data)
            # return

    def listen(self):
        print('listen serial port')
        th = threading.Thread(target=self.recv)
        th.start()
        return th