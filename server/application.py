'''Super server'''
import http.server
import socketserver

PORT = 8000

class TestMe():
    '''For test demo'''
    def take_five(self):
        '''5'''
        return 5
    
    def port(self):
        '''port'''
        return PORT
if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
