from instagrapi import Client



class Thot():

    client: Client

    def __init__(self, client):
        if type(client) == Client:
            self.client = client
        else:
            pass

    def grab_posts(self, user, amount=1):
        user_id = self.client.user_id_from_username(user)
        medias = self.client.user_medias(user_id, amount)

        for media in medias:
            self.client.video_download(media.pk)
            self.client.video_download_by_url(media.video_url)