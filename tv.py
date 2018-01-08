##########################################################################
# Library of TV Related Functions
# Started November 2017
#
# Python 3.5
##########################################################################
import lib
import samsungctl
import config
import re


def television(args):
    
    command = args.get("command")

    command = parseCommand(command)   
    

    multiplier = 0
    if ("UP" in command) or ("DOWN" in command) or ("RIGHT" in command) or ("LEFT" in command):
        multString = re.search('(\d+)$', command)
        if (multString is not None):
            multString = multString.group(0)
            multiplier = int(multString)
            command = command.replace(multString,"")
            print (multiplier)
        

    command = decodeCommand(command)    

    if lib.is_number(command):
        for i in range(0, len(command)):            
            samsungctl.Remote(config.tvconfig).control("KEY_" + command[i])
            print ("KEY_" + command[i])
    else:
        if (multiplier > 0):
            for i in range(0, multiplier):           
                samsungctl.Remote(config.tvconfig).control(command)
                print (command)
        else:
            samsungctl.Remote(config.tvconfig).control(command)
            print (command)

    return "TV Control OK"

def decodeCommand(command):
      
    
    
    if "CHANNEL" in command:
        command = command.replace("CHANNEL","")
        command = decodeChannel(command)
    else:
        command = decodeButton(command)

    return command        

def decodeButton (command):      
    
    if command == "GUIDE":
        return "KEY_GUIDE"
    elif (command == "UP") or (command == "APP") or (command == "ARROWUP") or (command == "CURSORUP"):
        return "KEY_UP"
    elif (command == "DOWN") or (command == "ARROWDOWN") or (command == "CURSORDOWN"):
        return "KEY_DOWN"
    elif (command == "LEFT") or (command == "ARROWLEFT") or (command == "CURSORLEFT"):
        return "KEY_LEFT"
    elif (command == "RIGHT") or (command == "ARROWRIGHT") or (command == "CURSORRIGHT"):
        return "KEY_RIGHT"
    elif (command == "PAGEUP") or (command == "PAGEAPP"):
        return "KEY_CHUP"
    elif (command == "PAGEDOWN"):
        return "KEY_CHDOWN"    
    elif command == "LEFT":
        return "KEY_LEFT"
    elif command == "RIGHT":
        return "KEY_RIGHT"
    elif (command == "SELECT") or (command == "ENTER"):
        return "KEY_ENTER"
    elif (command == "RETURN") or (command == "BACK") or (command == "EXIT"):
        return "KEY_RETURN"
    elif command == "LIST":
        return "KEY_CH_LIST"
    elif command == "MENU":
        return "KEY_MENU"
    elif command == "INFO":
        return "KEY_INFO"
    elif command == "SOURCE":
        return "KEY_SOURCE"
    elif command == "VOLUMEUP":
        return "KEY_VOLUP"
    elif command == "VOLUMEDOWN":
        return "KEY_VOLDOWN"
    elif command == "VOLUMEDOWN":
        return "KEY_VOLDOWN"
    elif (command == "VOLUMEMUTE") or (command == "MUTE") :
        return "KEY_MUTE"
    elif (command == "HDMI") or (command == "CHROMECAST"):
        return "KEY_HDMI"
    elif command == "TOOLS":
        return "KEY_TOOLS"
    elif (command == "SUBTITLES") or (command == "SUBTITLE"):
        return "KEY_SUB_TITLE"
    elif (command == "TV") or (command == "TELLY"):
        return "KEY_DTV"
    elif (command == "WII") or (command == "WE") or (command == "WEE") or (command == "GAMES"):
        return "KEY_COMPONENT1"
    
    else:
        command = decodeChannel(command)
        return command
    


def decodeChannel(channel):

    channel = channel.upper()
    channel = channel.replace(" ", "")
    
    if (channel == "BBC1") or (channel == "BBCONE") or (channel == "ONE"):
        return "101"
    elif (channel == "BBC2") or (channel == "BBCTWO") or (channel == "TWO"):
        return "102"
    elif channel == "BBC4":
        return "106"
    elif channel == "ITV":
        return "003"
    elif channel=="ITV2":
        return "006"
    elif channel == "ITV3":
        return "010"
    elif channel == "ITV4":
        return "024"
    elif channel == "4":
        return "104"
    elif channel == "5":
        return "105"
    elif channel == "DAVE":
        return "012"
    elif channel == "FILM4":
        return "015"
    elif channel == "DRAMA":
        return "020"
    elif channel == "E4":
        return "028"
    elif channel == "BBC1SD":
        return "001"
    elif channel == "BBC2SD":
        return "002"
    elif (channel == "UP") or (channel == "OP") or (channel == "APP"):
        return "KEY_CHUP"
    elif channel == "DOWN":
        return "KEY_CHDOWN"
    elif (channel == "GUIDE") or (channel == "LIST"):
        return "KEY_GUIDE"
    elif channel == "INFO":
        return "KEY_INFO"
    
    
    else:
        return channel

    return channel


def decodeVolume(volume):
    volume=volume.upper()
    volume=volume.replace(" ","")

    if (volume == "UP") or (volume == "APP"):
        return "KEY_VOLUP"
    elif volume == "DOWN":
        return "KEY_VOLDOWN"
    elif (volume == "MUTE") or (volume == "UNMUTE") or (volume == "ONMUTE"):
        return "KEY_MUTE"
    else:
        return volume

    return volume

def parseCommand(command):
    command = command.upper()
    command = command.replace(" ","")
    print (command)

    command = command.replace("UPONE","UP1")
    command = command.replace("UPTO","UP2")
    command = command.replace("UPTHREE","UP3")
    command = command.replace("UPFOR","UP4")

    command = command.replace("DOWNONE","DOWN1")
    command = command.replace("DOWNTO","DOWN2")
    command = command.replace("DOWNTHREE","DOWN3")
    command = command.replace("DOWNFOR","DOWN4")
    return command
    
