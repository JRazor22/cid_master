# cid_master

Only use in educational purposes!!!

# General 
You can use this script to change SD Card cid number!

This script work with Ubuntu 64-bit! To use this script you must have root privileges!

Not every SD Card has a changeable cid number! SD Cards that have changeable cid number are some of Samsung EVO cards!

To use this script you need Python3!! [Install instractions](https://docs.python-guide.org/starting/install3/linux/).
# Install:
```
git clone https://github.com/JRazor22/cid_master.git
cd cid_master
```
# Usage:
```
python3 cid_master.py
```
# What is cid?

Information about an SD card is encoded in its internal card registries. One of these is the Card Identification (CID) Register, a 16 byte code that contains information that uniquely identifies the SD card, including the card serial number (PSN), manufacturer ID number (MID) and manufacture date (MDT). The CID register is set when the card is manufactured and cannot be changed after it is set. (According to SD card specification the information is only to be written once, however if a card does not conform to the specification this information could be changed!)



