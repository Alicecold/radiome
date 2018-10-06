#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import spotify

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        spotify.login(spotify)
        self.wfile.write(spotify.get_current_playing(spotify))
        return

try:
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	server.serve_forever()

except KeyboardInterrupt:
	print 'shutting down the web server'
	server.socket.close()