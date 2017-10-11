class SpamManager(object):

    def __init__(self, client):
        self.client = client
        self.message_tracker = []