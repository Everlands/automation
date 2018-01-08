# Home Automation

Basic home automation project for Raspberry Pi and Google Home

- Controls Samsung TV via IFTTT Webhook

  if (voice command) then (http://url:port/telly/?command= {{the command text}})

- Sends Google Home Notification Messages via IFTTT Webhook

  if (event) then (http://url:port/say/?text={{the message}} )

- Controls 433MHZ Remote devices via IFTTT Webhook

  if (voice command) then (http://url:port/rfcontrol/?command= {{the command text}})
  
  
# Voice Commands - TV

Examples:

"BBC1"
"channel bbc 1"
"channel dave"
"channel 02"
"channel up 2"
"volume up"
"volume down 5"
"guide"
"cursor up"
"cursor up 3"
"mute"
"info"
"back"
"exit"

# ToDo

- 433Mhz RF coder / decoder
- Dashboard for web /  mobile control of devices instead of IFTTT


