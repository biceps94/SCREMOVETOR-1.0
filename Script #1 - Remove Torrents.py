import os

dir_name = "G:/- Browser Downloads -"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".torrent"):
        os.remove(os.path.join(dir_name,item))

