import sys
from protocol import ProtocolTest

addr = sys.argv[1]
try:
    data = sys.argv[2]
except:
    data = None

if data:
    d = ProtocolTest(addr, 1234)
    d.send(data, dest=5678)
else:
    d = ProtocolTest(addr, 5678)
    d.listen()

print('===========')

while True:
    cmd = input('[rf shell]')
    cmds = cmd.split(' ')
    if cmds[0] == 'send':
        d.send(cmds[1], dest=cmds[2])
    
    if cmds[0] == 'echo':
        d.send('__')

    if cmds[0] == 'neighbors':
        pass