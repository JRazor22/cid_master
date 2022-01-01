# cid_master

Only for use in educational purposes!!!

Github repository page: https://github.com/JRazor22/cid_master

# General 
You can use this script to change SD Card cid number!

This script work with Ubuntu 64-bit! To use this script you must have root privileges!

Not every SD Card has a changeable cid number! SD Cards that have changeable cid number are some of Samsung EVO cards!

In order to be able to read and change the SD Card cid number, you need an SD card adapter connected via an IDE bus to your host computer. This is not possible with an external SD Card reader connected via a USB port. Even not all notebooks with build-in SD Card readers can’t read SD Card cid number, because SD Card adapters are not connected via IDE bus. (more info at: https://www.getusb.info/how-to-read-cid-on-sd-card/)

To use this script you need Python3!! [Python3 Install instractions](https://docs.python-guide.org/starting/install3/linux/).
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

(sourse: https://www.cameramemoryspeed.com/sd-memory-card-faq/reading-sd-card-cid-serial-psn-internal-numbers/)


