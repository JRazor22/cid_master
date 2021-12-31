#Change Cid on sd card
import time
import os
import subprocess
from subprocess import Popen, PIPE
#Banner
print("""
                                                                                                 
 .d8888b. 8888888 8888888b.        888b     d888        d8888  .d8888b. 88888888888 8888888888 8888888b.  
d88P  Y88b  888   888  "Y88b       8888b   d8888       d88888 d88P  Y88b    888     888        888   Y88b 
888    888  888   888    888       88888b.d88888      d88P888 Y88b.         888     888        888    888 
888         888   888    888       888Y88888P888     d88P 888  "Y888b.      888     8888888    888   d88P 
888         888   888    888       888 Y888P 888    d88P  888     "Y88b.    888     888        8888888P"  
888    888  888   888    888       888  Y8P  888   d88P   888       "888    888     888        888 T88b   
Y88b  d88P  888   888  .d88P       888   "   888  d8888888888 Y88b  d88P    888     888        888  T88b  
 "Y8888P" 8888888 8888888P"        888       888 d88P     888  "Y8888P"     888     8888888888 888   T88b 
                                                                                                                                                
                                                                                                        
Please select one of the listed options:                                                                                                                                                                                                
    1. Clone SD Card CID
    2. Enter Manually SD Card CID
    3. Read SD Card CID

""")

class Timeout(Exception):
    """ioctl: Connection timed out"""
    pass
class Invalid_argument(Exception):
    """ioctl: Invalid argument"""
    pass
class Lock(Exception):
    """Read-only file system"""
    pass
class Length(Exception):
    """CID should be 32 chars long! Two chars are one hex byte"""
    pass


print("Option: ",end="")
option = input()
if (option != "1") and (option != "2") and (option != "3"):
    print("\nERROR: No option or Wrong option selected, Please run script again and choose one of the listed options: 1, 2 or 3!!!\n")
#option 1
if option == "1":
    print("\nPlease enter your orginal sd card, wait for 10 seconds and press ENTER! ")
    enter = input()
    if enter == "":
        find = os.popen('sudo find /sys -name cid -print').read()
        if find != "":
            orginal_cid = os.popen('cat %s'%find).read()
        else:
            print("ERROR: No SD Card, please insert SD Card and run script again! \n")
            exit()
        print("Orginal SD Card CID number is:",orginal_cid)
        print("Please remove orginal SD Card and press ENTER!")
        enter1 = input()
        if enter1 == "":
            print("Please enter your SD Card with changeable CID, wait for 10 seconds and press ENTER!")
            enter2 = input()
            if enter2 == "":
                find = os.popen('sudo find /sys -name cid -print').read()
                if find != "":
                    new_cid = os.popen('cat %s' % find).read()
                    print("Current SD Card CID is:",new_cid)
                else:
                    print("ERROR: No SD Card, please insert SD Card and run script again! \n")
                    exit()
                try:
                    print("Writing new CID...")
                    process = subprocess.Popen('sudo ./mmc prog_cid /dev/mmcblk0 %s'%orginal_cid, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    time.sleep(10)
                    output = process.communicate()[0].decode("ascii")
                    #print(output)
                    if output == "ioctl: Invalid argument\nWriting new CID.\n":
                        raise Invalid_argument
                    if output == "ioctl: Connection timed out\nFailed to enter vendor mode. Genuine Samsung Evo Plus?\n":
                        raise Timeout
                    if output == "open: Read-only file system\n":
                        raise Lock
                except Timeout:
                    print("\nERROR: Please insert SD Card with changeable CID and try again!\n")
                    exit()
                except Invalid_argument:
                    print("\nERROR: Please insert SD Card with changeable CID and try again!\n")
                    exit()
                except Lock:
                    print("\nSD Card state is Read-only, please remove SD Card Lock and try again!\n")
                    exit()
                print("\nEject the SD Card, wait for 10 seconds and insert it again and press ENTER!")
                enter3 = input()
                if enter3 == "":
                    find = os.popen('sudo find /sys -name cid -print').read()
                if find != "":
                    control_cid = os.popen('cat %s' % find).read()
                    if control_cid == orginal_cid:
                        print("Congratulation, SD Card CID is successfully cloned!!!\n")
                    else:
                        print("ERROR: Something went wrong, please make sure that your SD Card is with changeable and try again!")
                else:
                    print("No SD Card, please insert SD Card and run script again! \n")
                    exit()
            else:
                print("\nPlease just press ENTER!!!\n")
                exit()
        else:
            print("\nPlease just press ENTER!!!\n")
            exit()
    else:
        print("\nPlease just press ENTER!!!\n")
        exit()
#option 2
if option == "2":
    print("\nPlease enter your SD Card with changeable CID, wait for 10 seconds and press ENTER:")
    enter3 = input()
    if enter3 == "":
        print("Please enter your new CID number (CID Format: 1b534d303030303010d9b914e500f201)")
        print("\nNew CID: ",end="")
        manual_cid = input().replace(" ", "")
        print("\nEntered following CID:",manual_cid)
        print("\nPress y to continue or n to cancel and hit ENTER: ",end="")
        enter2 = input()
        if (enter2!="N") and (enter2!="n") and (enter2!="Y") and (enter2!="y"):
            print("\nERROR: No option selected!\n")
            exit()
        if (enter2 == "n") or (enter2 == "N"):
            exit()
        if (enter2 == "y") or (enter2 == "Y"):
            find = os.popen('sudo find /sys -name cid -print').read()
            if find != "":
                new_cid = os.popen('cat %s' % find).read()
                print("\nCurrent SD Card CID is:", new_cid)
            else:
                print("ERROR: No SD Card, please insert SD Card and run script again! \n")
                exit()
            try:
                print("Writing new CID...")
                process = subprocess.Popen('sudo ./mmc prog_cid /dev/mmcblk0 %s' %manual_cid, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                time.sleep(10)
                output = process.communicate()[0].decode("ascii")
               # print(output)
                if output == "ioctl: Invalid argument\nWriting new CID.\n":
                    raise Invalid_argument
                if output == "ioctl: Connection timed out\nFailed to enter vendor mode. Genuine Samsung Evo Plus?\n":
                    raise Timeout
                if output == "open: Read-only file system\n":
                    raise Lock
                if output == "CID should be 32 chars long! Two chars are one hex byte\n: Success\n":
                    raise Length
            except Timeout:
                print("\nERROR: Please insert SD Card with changeable CID and try again!\n")
                exit()
            except Invalid_argument:
                print("\nERROR: Please insert SD Card with changeable CID and try again!\n")
                exit()
            except Lock:
                print("SD Card state is Read-only, please remove SD Card Lock and try again!\n")
                exit()
            except Length:
                print("\nERROR: CID should be 32 chars long! Two chars are one hex byte!\n")
                exit()
            print("\nEject the SD Card, wait for 10 seconds and insert it again and press ENTER!")
            enter3 = input()
            if enter3 == "":
                find = os.popen('sudo find /sys -name cid -print').read()
            if find != "":
                control_cid = os.popen('cat %s' % find).read()
                if control_cid == manual_cid:
                    print("Congratulation, SD Card CID is successfully changed!!!\n")
                else:
                    print("ERROR: Something went wrong, please make sure that your SD Card is with changeable and try again!")
            else:
                print("No SD Card, please insert SD Card and run script again! \n")
                exit()
    else:
        print("\nPlease just press ENTER!!!\n")
        exit()

if option == "3":
    find = os.popen('sudo find /sys -name cid -print').read()
    if find != "":
        orginal_cid = os.popen('cat %s' % find).read()
        print("\nSD Card CID number is:",orginal_cid)
    else:
        print("\nERROR: No SD Card, please enter SD Card and run script again! \n")
        exit()

