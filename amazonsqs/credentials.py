# -*- coding: utf-8 *-*
import os
import ConfigParser


class Credentials(object):

    def get_data(self):
        return self.access_key_id, self.secret_access_key, self.queue


class PlainCredentials(Credentials):

    def __init__(self, access_key_id, secret_access_key, queue):
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.queue = queue


class ConfigFileCredentials(Credentials):

    def __init__(self, config_file):
        config = ConfigParser.ConfigParser()
        config.read(os.path.join(os.getcwd(), config_file))
        self.access_key_id = config.get("amazonsqs", "access_key_id")
        self.secret_access_key = config.get("amazonsqs", "secret_access_key")
        self.queue = config.get("amazonsqs", "queue")
