# python-hhc-n10

## What is this lib ?
This library is made to communicate with HHC-N10 devices. They are relays that can be toggled via ethernet (TCP/IP).

## How to install the lib ?
You can get it from [pypi](https://pypi.org/project/python-hhc-n10/) like so:
```
pip3 install python-hhc-n10
```

## How to use the lib
```python3
from hhcn10 import hhcn10

h = hhcn10.HHCN10()

h.set_relay(True)
print('The relay is: ' + str(h.read_relay()))

time.sleep(1)

h.set_relay(False)
print('And now the relay is: ' + h.read_relay())
```

Please note that the implementation of their TCP stack is finnicky and only accepts 5 parallel connections. If you try to open too many sockets at once the relay will hang for some time.

## Default params
The relay default's IP is `192.168.0.105/24`. If your computer is not in this same subnet, you'll need to add a static route + a static IP in the same subnet as this relay. You can then change the device's IP using the `change_ip(addr, netmask, gw)` method.
