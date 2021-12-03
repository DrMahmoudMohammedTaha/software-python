import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)         # Sending an '200 OK' response

        self.send_header("Content-type", "text/html")
        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()

        # Extract query param
        name = 'World'
        query_components = parse_qs(urlparse(self.path).query)
        if 'name' in query_components:
            name = query_components["name"][0]

        html = f"<html><head></head><body><button>Authorization Request</button></body></html>"

        self.wfile.write(bytes(html, "utf8"))

        return


handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)
my_server.serve_forever()