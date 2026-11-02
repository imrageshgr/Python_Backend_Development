from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = "<h1>Hello! My first Python server.</h1>"
        self.wfile.write(message.encode("utf-8"))


server = HTTPServer(("127.0.0.1", 8000), MyServer)

print("Server is running on http://127.0.0.1:8000")

server.serve_forever()
