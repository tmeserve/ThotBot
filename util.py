import os, discord, json, shutil, mimetypes
from instagrapi import Client
from cogs.thot import Thot
mimetypes.init()

def is_media_file(filename):
    mimestart = mimetypes.guess_type(filename)[0]

    if mimestart != None:
        mimestart = mimestart.split('/')[0]

        if mimestart in ['audio', 'video', 'image']:
            return [True, mimestart]

    return False

def move_downloads():
    for entry in os.scandir('.'):
        if entry.is_file:
            if is_media_file(entry.path):
                mimestart = mimetypes.guess_type(entry.path)[0]

                print(mimestart)

                if mimestart != None:
                    mimestart = mimestart.split('/')[0]

                    if mimestart == 'audio':
                        shutil.move('.\\download\\testing\\audio')
                        print('moved audio')
                    elif mimestart == 'video':
                        shutil.move('.\\download\\testing\\video')
                        print('moved video')
                    elif mimestart == 'image':
                        shutil.move('.\\download\\testing\\image')
                        print('moved image')
                    else:
                        print(mimestart)

def load_proxies(client, user, password):
    f = open('Free_Proxy_List.json')

    file = json.load(f)

    for obj in file:
        try:
            client.set_proxy(obj['ip'])
            client.login(user, password)
        except:
            print('yikes')
            pass
