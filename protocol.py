import serial
import threading

class ProtocolTest():

    def __init__(self, dev_addr, rf_address=1, baudrate=115200):
        self.rf = serial.Serial(dev_addr, baudrate)
        self.address = rf_address
        self.neighbors = []

    def layer3(self, data):
        """
        - actual payload
        """
        print('[transport layer] ', data)
        return

    def layer2(self, data):
        """
        - check packet type
        """
        pkt_type = data[:2].decode()
        source_addr = data[2:6]
        dest_addr = data[6:10]
        print('[network layer] ', 'packet type ', pkt_type, ' from ', source_addr, ' for ', dest_addr)
        if pkt_type == '00':
            self.send('hello from', pkt_type='01')
            return

        if pkt_type == '01':
            print('new neighbour', source_addr)
            # self.send('hello from', pkt_type='01')
            return


        self.layer3(data[10:])

    def layer1(self, data):
        """
        - remove total bytes
        - remove signal quality (if present)
        """
        data_len = data[0]
        print('[link layer] ', data_len, ' bytes')
        self.layer2(data[1:data_len + 1])

    def send(self, data, dest='0000', pkt_type='00'):
        # TODO: find a better way of sending, AT commands maybe?
        # self.rf.write(bytes(f"t\r", 'utf8'))
        print('sending', data, dest, pkt_type)
        source_addr = self.address
        payload = f'{pkt_type}{source_addr}{dest}{data}'
        self.rf.write(bytes(f"send('{payload}')\r", 'utf8'))

    def recv(self):
        print('waiting data...')
        while True:
            data = self.rf.readline()
            if data[:3].decode() == 'RCV':
                self.layer1(data[3:])
            # self.send('received')
            # return

    def listen(self):
        print('listen serial port')
        th = threading.Thread(target=self.recv)
        th.start()
        return th