# LonHand client library

LonHand protocol implementation for USR-WP1 smart socket (one-channel relay) by USR IOT.

[Product link](https://www.usriot.com/download/LonHand/USR-WP1%20EN%20V1.3.1.pdf)

Usage:
```
from lonhand import device

# create switch
switch = WifiRelay('192.168.1.23')

# turn on
switch.turn_on()

# get state
state = switch.is_on()

# turn off
switch.turn_off()
```

Command:
```
55 AA - distinguishes a command, unlike for example the password which
        should be sent as is (with suffix 0D 0A)
00 03 - represents the length in bytes of the command (real) that follows,
        including the byte 00 (see below)
00    - fixed, reserved and not usable. However, it contributes to forming 
        the length in bytes of the command, for example in case of a device
        renaming command (which will contain the new name assigned): the
        length byte (and the checksum) will be recalculated also according
        to the length of the new name
02    - the actual command (ON)
01    - command parameter; in this case we are giving the ON command (02)
        and as a parameter the channel number to be switched on (01).
06    - checksum, and represents the sum (in HEX) of the parts: 
```        (0x00 + 0x03 + 0x00 + 0x02 + 0x01) = 0x06

Response:
```
AA 55 - marks the message as a response
00 04 - response length
00    - reserved
82 01 - is the confirmation response to the ON command
01    - channel/port that was affected
88    - checksum: (0x00 + 0x04 + 0x00 + 0x82 + 0x01 + 0x01) = 0x88
```

