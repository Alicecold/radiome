#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json
import spotify
import secret
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


PORT_NUMBER = 8080

class handle(BaseHTTPRequestHandler):
    cred = credentials.Certificate(secret.FB_CREDENTIALS)
    app = firebase_admin.initialize_app(cred, {'databaseURL': secret.FB_DATABASE_URL})
    dbs = db.reference('weplay')
    user_dbs_ref = dbs.child('users')

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin', '*') #TODO: Do not allow random CORS
        self.end_headers()
        if self.path == '/' :
            spotify.login(spotify)
            self.user_dbs_ref.set({spotify.user: {
                'now': spotify.get_current_playing(spotify).encode('utf-8'),
                'broadcasting': True
            }})
            self.wfile.write(json.dumps({"path": "/" + spotify.user}))
        else:
            now = self.user_dbs_ref.child(self.path[1:]).get()
            self.wfile.write(json.dumps({"response": now}))
            print self.path
        return

try:
	server = HTTPServer(('', PORT_NUMBER), handle)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	server.serve_forever()

except KeyboardInterrupt:
	print 'shutting down the web server'
	server.socket.close()