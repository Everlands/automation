##########################################################################
# Everlands Home Automation Project
#
# Take input from URL / IFTTT 
# Reroute to
#   1] Google Home for Voice Notifications
#   2] Samsung Remote Control for TV Functions
#   3] RF Transceiver for Home Automation [Lights, Sockets etc]
#
# Started November 2017
#
# Python 3.5
##########################################################################

#from flask import Flask, request , abort , redirect , Response ,url_for, render_template
import flask
import socket
import logging
import os
import config
import tv
import lib
import controls
import notify
import flask_login
from cameralib import VideoCamera
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_=os.system("clear")

app = flask.Flask(__name__)

app.secret_key = 'UBIQUITOUSDONKEYBALLS' 
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/play/<filename>')
def play(filename):
    return notify.play(filename, flask.request)

@app.route('/say/')
@flask_login.login_required
def say():
    return notify.say(flask.request.args)

@app.route('/telly/')
@flask_login.login_required
def telly():
    return tv.television(flask.request.args)

@app.route('/rfcontrol/')
@flask_login.login_required
def rfcontrol():
    return controls.rfcontrol(flask.request.args)

@app.route('/')
def home():
    return flask.render_template('home.html', thisuser = flask_login.current_user )

@app.route('/power/')
@flask_login.login_required
def power():
    return flask.render_template('power.html', devices = config.rfdevices, thisuser = flask_login.current_user)

@app.route('/status/')
@flask_login.login_required
def status():
    return flask.render_template('status.html', thisuser = flask_login.current_user, log = config.action_log[:100] )

@app.route('/tvremote/')
@flask_login.login_required
def tvremote():
    return flask.render_template('tvremote.html', thisuser = flask_login.current_user) 

@app.route('/notify/')
@flask_login.login_required
def notifications():
    username = flask_login.current_user.id.split("@")[0].capitalize()
    if username == "Sara":
        username = "Sarah"
    return flask.render_template('notify.html', notifications = config.notifications, username = username, thisuser = flask_login.current_user) 

@app.route('/camera/')
@flask_login.login_required
def camera():
    config.action_log.insert(0, {"user": flask_login.current_user.id, "action": "Viewed camera", "time": time.ctime()})
    return flask.render_template('camera.html', thisuser = flask_login.current_user)

@app.route('/video_feed/')
@flask_login.login_required
def video_feed():
    return flask.Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        loBad=""
        if 'loBad' in flask.request.args:
            loBad = flask.request.args['loBad']

        return flask.render_template('login.html', thisuser = flask_login.current_user, message = loBad)

    email = flask.request.form['email'].lower()
    if flask.request.form['password'] == config.users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        config.action_log.insert(0, {"user": flask_login.current_user.id, "action": "Logged in", "time": time.ctime()})
        return flask.redirect(config.url + '/')

    return flask.redirect(config.url + '/login/?loBad=1')


@app.route('/logout/')
def logout():
    flask_login.logout_user()
    return flask.redirect(config.url + '/login/')

@login_manager.unauthorized_handler
def unauthorized_handler():
    #return 'Unauthorized'
    return flask.redirect(config.url + '/login/')

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in config.users:
        return

    user = User()
    user.id = email    
    return user


@login_manager.request_loader
def request_loader(request):

    user = User()
    api_key = request.args.get('api_key')
    if api_key:
        if api_key==config.api_key:
            userid = request.args.get("user")
            if userid:
                user.id = userid
            else:
                user.id = "System"            
        else:
            return
    else:
        email = request.form.get('email')
        if email not in config.users:
            return

        user.id = email
                

        # DO NOT ever store passwords in plaintext and always compare password
        # hashes using constant-time comparison!        
        user.is_authenticated = request.form['password'] == config.users[email]['password']

    return user



def gen(cameralib):
    while True:
        frame = cameralib.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


if __name__ == '__main__':
        app.run(debug=False, threaded=True,  port=5000, host='0.0.0.0')
