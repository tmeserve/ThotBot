import os, discord, json, shutil, mimetypes
from instagrapi import Client
from cogs.thot import Thot
mimetypes.init()


cl = Client()

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

def is_media_file(filename):
    mimestart = mimetypes.guess_type(filename)[0]

    if mimestart != None:
        mimestart = mimestart.split('/')[0]

        if mimestart in ['audio', 'video', 'image']:
            return True

    return False

def move_downloads():
    for entry in os.scandir('.'):
        if entry.is_file:
            if is_media_file(entry.path):
                shutil.move()

    # shutil.move()

if __name__ == '__main__':
    load_secrets()

    cl.login(user, password)

    # user_id = cl.user_id_from_username('sportzalien')
    # medias = cl.user_medias(user_id, 1)

    

    # print(medias)

    # thot = Thot(cl)
    # thot.grab_posts('sportzalien')

    move_downloads()