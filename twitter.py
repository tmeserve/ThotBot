'''
@miguelmalvarez is the author of the twitter image downloading
'''

import tweepy, os, json, wget
from tweepy import OAuthHandler


class Twitter:

    def __init__(self,):
        pass

    def parse(self, cls, api, raw):
        status = cls.first_parse(api, raw)
        setattr(status, 'json', json.dumps(raw))
        return status

    def init_tweepy(self,):
        # Status() is the data model for a tweet
        tweepy.models.Status.first_parse = tweepy.models.Status.parse
        tweepy.models.Status.parse = self.parse
        # User() is the data model for a user profile
        tweepy.models.User.first_parse = tweepy.models.User.parse
        tweepy.models.User.parse = self.parse


    def authorise_twitter_api(self, config):
        auth = OAuthHandler(config['DEFAULT']['consumer_key'], config['DEFAULT']['consumer_secret'])
        auth.set_access_token(config['DEFAULT']['access_token'], config['DEFAULT']['access_secret'])
        return auth


    # It returns [] if the tweet doesn't have any media
    def tweet_media_urls(self, tweet_status):
        # At least one image
        if 'media' in tweet_status.entities:
            # Grabbing all pictures
            media = tweet_status.extended_entities['media']
            return [f"{item['media_url']}?format=jpg&name=large" for item in media]
        else:
            return []

    def download_images(self, status, num_tweets, output_folder):
        downloaded = 0

        for tweet_status in status:
            if downloaded >= num_tweets:
                break

            for count, media_url in enumerate(self.tweet_media_urls(tweet_status)):
                # Only download if there is not a picture with the same name in the folder already
                created = tweet_status.created_at.strftime('%d-%m-%y at %H.%M.%S')
                file_name = "{}_({}).jpg".format(created, count + 1)
                if not os.path.exists(os.path.join(output_folder, file_name)):
                    print(media_url)
                    print(output_folder + '/' + file_name)
                    # TODO: Figure out how to include ':orig' at the end in a way that works with wget to get the
                    # full size resolution
                    wget.download(media_url, out=output_folder + '/' + file_name)
                    downloaded += 1


    def download_images_by_user(self, api, username, retweets, replies, num_tweets, output_folder):
        status = tweepy.Cursor(api.user_timeline, screen_name=username, include_rts=retweets, exclude_replies=replies,
                            tweet_mode='extended').items()
        self.download_images(status, num_tweets, output_folder)


    def download_images_by_tag(self, api, tag, retweets, replies, num_tweets, output_folder):
        status = tweepy.Cursor(api.search, '#' + tag, include_rts=retweets, exclude_replies=replies,
                            tweet_mode='extended').items()
        self.download_images(status, num_tweets, output_folder)