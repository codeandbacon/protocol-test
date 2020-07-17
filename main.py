import sys
from protocol import ProtocolTest

addr = sys.argv[1]
data = sys.argv[2]


d = ProtocolTest(addr)

# d.send(data)
d.listen()