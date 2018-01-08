import time

action_log=[{"user":"system","action": "Server started", "time": time.ctime()}]

tvconfig = {
    "name": "samsungctl",
    "description": "PC",
    "id": "",
    "host": "192.168.0.X",
    "port": 55000,
    "method": "legacy",
    "timeout": 0,
}

chromecast_name = "Google Home" 

url = "https://myserveraddress.net"

rfdevices = [ 
{"id": "1","description": "Dining Room Light", "voice": "|DININGROOMLIGHT|DININGROOM|","onCode": 11111111, "offCode": 1111112, "protocol": 1, "pulselength": 350},
{"id": "2","description": "Kitchen Light", "voice": "|KITCHENLIGHT|COOKINGLIGHT|",  "onCode": 1111113, "offCode": 11111114, "protocol": 1, "pulselength": 350},
{"id": "3","description": "Bedside Light", "voice": "|BEDSIDELIGHT|BEDROOM|", "onCode": 1111115, "offCode": 1111116, "protocol": 1, "pulselength": 350},
{"id": "4","description": "Spare",    "voice": "|SPARE|SPARELIGHT|", "onCode": 1111117, "offCode": 1111118, "protocol": 1, "pulselength": 350}
]

notifications = [
    {"id": "1", "notification": "I'm on my way"},
    {"id": "2", "notification": "I've just left"},
    {"id": "3", "notification": "I'm going to be late"},
    {"id": "4", "notification": "I'm at the shops"},
    {"id": "5", "notification": "I'm at the pub"},
    {"id": "6", "notification": "Put the kettle on"
    ]

users = {
        'user1@server.net': {'password': 'password', 'name': 'user1', 'phonetic': 'user one'},
        'user2@server.net':{'password': 'letmein', 'name': 'user2', 'phonetic': 'user two'}
         }


api_key = "INSERTABIGSTRANGEWORDHERE"

