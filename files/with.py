# with as context manager

with open("new/files/ajinkya.txt","r") as f:
    content = f.read()
    print(content)

# no need to write f.close()