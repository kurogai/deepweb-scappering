import string
from bs4 import BeautifulSoup
import random
import socks
import socket

class web_scappre:
    def create_connection(self, address, timeout=None, source_adress=None):
        sock = socks.socksocket()
        sock.connect(address)
        return sock

    def scan_link(self):
        link = 'http://'+''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(16)) + '.onion/'
        socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",9050)
        socket.socket = socks.socksocket
        socket.create_connection = self.create_connection

        import urllib.request

        try:
            with urllib.request.urlopen(link,timeout=10) as f:
                if f.status == 200:
                    soup = BeautifulSoup(f.read().decode(),'html.parser')
                    title = soup.find('title')
                    return {"status":f.status,"title":title.string,"link":link}
        except:
            return {"status":"Not found","title":"<nothing>","link":link}
