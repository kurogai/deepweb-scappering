import threading
import json
from termcolor import colored
from scrappe import web_scappre

def t(n,p,f):
    w = web_scappre()
    r = w.scan_link()
    
    if r['status'] == 200:
        print(colored(("[-] [  ",r['status']," ] - [",r['link'],"] - [",r['title'],"] - [",p,"%]"),"green"))

        with open(f,"a") as _file:
            #a = str("[",r['link'],"] - [",r['title'],"]\n")
            a = json.dumps(r)
            _file.write(a)
            _file.close()
    else:
        print("[-] [  ",r['status']," ] - [",r['link'],"] - [",r['title'],"] - [",p,"%]")

    return r

def main():

    size = int(input("DeepWebFindLink (enter max depth size) -> "))
    t_size = int(input("DeepWebFindLink (enter thread size) -> "))
    file = str(input("DeepWebFindLink (output name) -> "))

    print("[ DeepWeb Find Link -> Scappre the deepweb to find links")
    print("[+] Made by: Kurogai")
    print("[Github] -> https://github.com/kurogai")
    print("\n\n")
    print("[ n ] [ Status ] - [              link              ] - [ Title ]")
    
    # calculate percent of 10% each time
    perc = str((size / 100) * 10)
    
    try:
        for s in range(size):
            count = str((s / size) * 10)
            count = count[:10]
            
            for t_l in range(t_size):
                thread = threading.Thread(target=t,args=(s,count,file,))
                thread.start()
            

    except KeyboardInterrupt:
        print("[Paused] Continue? (s/n) :",end="")
        x = str(input())

        if x == "s":
            pass
        else:
            print("[+] Saved output to current folder, exiting")
            exit()


if __name__ == '__main__':
    main()