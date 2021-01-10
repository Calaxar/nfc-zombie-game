# NFC Zombie Game
A game played at my youth group, revamped to use nfc tags and a Raspberry pi

The game can be played as follows:
There's a zombie outbreak, the leaders have become zombies. A cure has been discovered, but it's locked away on a leaders computer!
NFC figurines are hidden around the play area; finding these keys and solving the computers riddles are crucial to take the zombies down. The kids have to find all the figures, answer the computers puzzle for each of them, and then discover and act out the printed cure, to cure the zombies and win the game. 
If a kids gets tagged by a zombie, they are "dead" and lie down where they are until another kid tags them to revive them. (You could instead opt to have one or two medics)

Materials required to run game:
* Raspberry Pi (and standard required periphals)
* [RC522 RFID Module](https://components101.com/wireless/rc522-rfid-module)
* Jumper cables
* NFC figures (Skylanders, Amiibo, etc.) Note: Regular RFID tags can also be used

The wiring between the pi and the RFID module should be set up like this:

RC522 pin name | Physical RPi pin | RPi pin name
--- | --- | --- 
SDA | 24 | GPIO8, CE0 
SCK | 23 | GPIO11, CE0 
MOSI | 19 | GPIO10, CE0 
MISO | 21 | GPIO9, CE0 
IRQ | 18 | GPIO24 
GND | 20 | Ground 
RST | 22 | GPIO25
3.3V | 17 | 3V3 

The [pi-rc522](https://github.com/ondryaso/pi-rc522) library will need to be installed to run the script

The Rasbperry pi must have SPI enabled to use the RFID module
