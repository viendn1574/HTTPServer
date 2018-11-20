import time
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import NeuralNetwork


class StaticServer(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == '/hello':
            self.send_response(200)
            self.end_headers()

            self.wfile.write('hello1')

    def do_POST(self):
        # Doesn't do anything with posted data
        print "in post method"
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()
        print self.data_string
        data = json.loads(self.data_string)
        #self.wfile.write(data)s

        NeuralNetwork.add_model(data)
        #time.sleep(0.5)
        with open('./model.xml', 'rb') as file:
            self.wfile.write(file.read())
        return

    def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()




def run(server_class=HTTPServer, handler_class=StaticServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()


run()