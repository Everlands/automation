##########################################################################
# Library of Google Home Notification Functions
# Started November 2017
#
# Python 3.5
##########################################################################

from flask import Flask, request
from gtts import gTTS
from slugify import slugify
from pathlib import Path
from urllib.parse import urlparse
import pychromecast
import logging
import config
import flask_login
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


logging.info("Starting up chromecasts")
chromecasts = pychromecast.get_chromecasts()

try:
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == config.chromecast_name)
except:
    cast = False

##########################################################################
# Turn text string into speech (mp3) and call a function to play it
##########################################################################
def play_tts(text, lang='en', slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    filename = slugify(text+"-"+lang+"-"+str(slow)) + ".mp3"
    path = "/static/cache/"
    cache_filename = "." + path + filename
    tts_file = Path(cache_filename)
    if not tts_file.is_file():
        logging.info(tts)
        tts.save(cache_filename)

    urlparts = urlparse(request.url)
    mp3_url = "https://" +urlparts.netloc + path + filename 
    logging.info(mp3_url)
    play_mp3(mp3_url)

##########################################################################
# Play an mp3 file to the current cast device
##########################################################################
def play_mp3(mp3_url):

    try:
        cast.wait()
        mc = cast.media_controller
        mc.play_media(mp3_url, 'audio/mp3')
        return True
    except:
        return False


##########################################################################
# Say a phrase via Google Home
##########################################################################
def say(args):
    text = args.get("text")
    lang = args.get("lang")
    if not text:
        return False
    if not lang:
        lang = "en"
    play_tts(text, lang=lang)
    text = text.replace("Sarah","Sara")
    config.action_log.insert(0, {"user": flask_login.current_user.id, "action": text, "time": time.ctime()})

    return text

# or

def reply(text):
    play_tts(text,"en")
    return text



##########################################################################
# Play media file from a URL or path
##########################################################################
def play(filename):    
    urlparts = urlparse(request.url)
    mp3 = Path("./static/"+filename)
    if mp3.is_file():
        play_mp3("https://"+urlparts.netloc+"/static/"+filename)
        return filename
    else:
        return "False"
