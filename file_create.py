
def createFile(name, content):
    fileCreate = open(name, "w")
    fileCreate.close()

    fileCreate = open(name, "a")
    fileCreate.write(content + "\n")
    fileCreate.close()

