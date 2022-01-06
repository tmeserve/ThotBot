import instagram, twitter, util
from instagrapi import Client
cl = Client()

if __name__ == '__main__':
    user, password = util.load_secrets()