import os, discord, json, shutil, mimetypes
from instagrapi import Client
from cogs.thot import Thot
mimetypes.init()


cl = Client()

# cl.set_proxy('20.47.108.204')

user = ''
password = ''


def scrape(user, amount=0):

    if amount == 0:
        string = 'instagram-scraper ' + user + ' -u ' + user + ' -p ' + password
    
    string = 'instagram-scraper ' + user + ' --maximum ' + amount + ' -u ' + user + ' -p ' + password

    os.system(string)

def load_secrets():
    global user, password
    f = open('secrets.json')

    file = json.load(f)

    user = file['username']
    password = file['password']

def load_proxies():
    global user, password
    f = open('Free_Proxy_List.json')

    file = json.load(f)

    for obj in file:
        try:
            cl.set_proxy(obj['ip'])
            cl.login(user, password)
        except:
            print('yikes')
            pass

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
                    
                    

if __name__ == '__main__':
    load_secrets()
    # load_proxies()

    # user_id = cl.user_id_from_username('sportzalien')
    # medias = cl.user_medias(user_id, 4)

    cl.login(user, password)
    

    # print(medias)

    thot = Thot(cl)
    thot.grab_posts('sportzalien', 4)
    thot.grab_hashtags('in_and_out', 4)
    thot.grab_collections('Pet Ads', 4)
    thot.grab_stories('dogekeeper', 4)

    # thot.grab_stories(input('user'), 4)

    move_downloads()