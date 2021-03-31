import string
from bs4 import BeautifulSoup
import random
import socks
import socket
import requests
from termcolor import colored
from file_create import createFile
import json


session = requests.session()
ONION_DOMAIN      = '.onion'
HTTP_PROTOCOL     = 'http://'
SITE              = ''
PROXY_ADRESS      = '127.0.0.1:9050'
session.proxies = {
                    'http':  'socks5h://' + PROXY_ADRESS,
                    'https': 'socks5h://' + PROXY_ADRESS
                   }



class web_scappre:
    def create_connection(self, address, timeout=None, source_adress=None):
        sock = socks.socksocket()
        sock.connect(address)
        return sock


    def scan_link(self):
        try:
            random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

            link = HTTP_PROTOCOL + random_string + ONION_DOMAIN
            #link = 'http://toponiibv4eo4pctlszgavni5ajzg7uvkd7e2xslkjmtcfqesjlsqpid.onion'

            socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, PROXY_ADRESS)
            socket.socket = socks.socksocket
            socket.create_connection = self.create_connection
            response = session.get(link)

            if(session.get(link).status_code == 200):
                result = { "code": 200, "link": link }
                return result

        except requests.ConnectionError as errorConnection:
            result = { "code": 404, "link": link }
            return result
            
    def getScrapped(currentThread,file):

        web_scappreed = web_scappre()
        #print("THREAD -> ",currentThread)
        response = web_scappreed.scan_link()

        if response["code"] == 200:
            print("[*] - "+colored((response["link"]+" [FOUND]"),"green"))
            createFile(file,response["link"])
            return response
        else:
            print("[!] - "+colored((response["link"]+" [INVALID]"),"red"))
        
        return -1
