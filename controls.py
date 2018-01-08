import RPi.GPIO as GPIO
import logging
from rpi_rf import RFDevice
import config
import notify
import time
import flask_login

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(22, GPIO.OUT)

rfdevice = RFDevice(27)
rfdevice.enable_tx()

def rfcontrol(args):
    logging.info(args)
    command = args.get("command")
    id = args.get("id")

    command = command.upper()
    command = command.replace(" ","")
    command = command.replace("'","")
    command = command.replace("PLEASE","")

    if(id):
        id = id.upper()
        id = id.replace(" ","")
        iId = int(id)
        try:
            device = next(d for d in config.rfdevices if d["id"] == id)
        except:
            device = False;
        action = command
    else:
        if  command[:2] == "ON":
            action = "ON"
            command = command[2:]
        elif command[:3] == "OFF":
            action = "OFF"
            command = command[3:]
        elif command[-2:] == "ON":
            action = "ON"
            command = command[:-2]
        elif command[-3:] == "OFF":
            action = "OFF"
            command = command [:-3]
        try:
            if command[:3] == "THE":
                command = command[3:]
            device = next(d for d in config.rfdevices if ("|"+command+"|" in d["voice"]))
        except:
            device = False;

    if(device):
        logging.info ("CONFIG " + device["description"])
        config.action_log.insert(0, {"user":  flask_login.current_user.id, "action": "Turned " + device["description"] + " " + action,  "time": time.ctime() })
        res = send(action, device)
    else:
        res = "Unknown Device"
        notify.reply("I'm sorry, I don't recognise that device")

    return "Power control OK: " + res

def send(action, device):

    rfdevice = RFDevice (27)
    rfdevice.enable_tx()
    if action == "ON":
        code = device["onCode"]
    elif action == "OFF":
        code = device["offCode"]
    else:
        code = 0
    protocol = device["protocol"]
    pulselength =  device["pulselength"]
    rfdevice.tx_code(code, protocol, pulselength)
    rfdevice.tx_code(code, protocol, pulselength)
    rfdevice.tx_code(code, protocol, pulselength)
    logging.info(str(code) +
             " [protocol: " + str(1) +
             ", pulselength: " + str(350) + "]")
    rfdevice.cleanup()
    return device["description"] + " Turned " + action
