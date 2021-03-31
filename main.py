import threading
from termcolor import colored
from scrappe import web_scappre
from file_create import createFile
from banner import banner
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("size",help="Informe o total de links a serem encontrados!", type=int)
parser.add_argument("threads",help="Informe o total de threads", type=int)
parser.add_argument("filename",help="Informe o nome e local do arquivo a ser criado", type=str)
args = parser.parse_args()


def main():

    size = args.size
    total_threads = args.threads
    file = args.filename

    banner()

    threads = list()
    for index in range(1,total_threads):
        currentThread = threading.Thread(target=web_scappre.getScrapped,args=(index,file))
        threads.append(currentThread)
        
        currentThread.start()



if __name__ == '__main__':
    main()