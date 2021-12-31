import os, discord, json, shutil, mimetypes
from instagrapi import Client
from cogs.thot import Thot
mimetypes.init()

class Instagram:

    client : Client

    def __init__(self, user, password):
        if type(user) == str and type(password) == str:
            self.client.login(user, password)    

    def load_proxies(self, user, password):
        f = open('Free_Proxy_List.json')

        file = json.load(f)

        for obj in file:
            try:
                self.client.set_proxy(obj['ip'])
                self.client.login(user, password)
            except:
                print('yikes')
                pass