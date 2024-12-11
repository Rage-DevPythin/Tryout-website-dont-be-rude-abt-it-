from http.server import BaseHTTPRequestHandler, HTTPServer

# Making something starting with (class)
class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Define response for the root url
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"It is a tryout website made by an app dev")

            # Define response for the /about url
        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"This is my websites about page. (NO HTML IS ALLOWED BEYOND THIS POINT)")

            # Define response for the /data URL {JSON}
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'{"message": "Hello JSON", "status": "succses"}')
            # Handle unknown paths
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Error 404 Not Found: The requested url was not found on this server.")

def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
