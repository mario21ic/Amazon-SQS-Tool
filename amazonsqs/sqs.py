# -*- coding: utf-8 -*-

from boto.sqs.connection import SQSConnection
from boto.sqs.message import Message
import os
import ConfigParser
import simplejson as json


class SQS(object):

    def __init__(self, config_file="config.ini"):
        config = ConfigParser.ConfigParser()
        config.read(os.path.join(os.getcwd(), config_file))

        aws_access_key_id = config.get("amazonsqs", "access_key_id")
        aws_secret_access_key = config.get("amazonsqs", "secret_access_key")
        aws_queue = config.get("amazonsqs", "queue")

        try:
            self.conn = SQSConnection(aws_access_key_id, aws_secret_access_key)
            self.set_queue(aws_queue)
        except:
            print 'Error connection'

    def get_all_queues(self):
        return self.conn.get_all_queues()

    def create_queue(self, queue, timeout):
        return self.conn.create_queue(queue, timeout)

    def set_queue(self, queue):
        self.queue = self.conn.get_queue(queue)
        return True

    def get_messages(self, limit=10):
        return self.queue.get_messages(limit)

    def count(self):
        #print "Count: %s" % self.queue.count()
        return self.queue.count()

    def write(self, data):
        m = Message()
        m.set_body(json.dumps(data))
        return self.queue.write(m)

    def delete(self, id):
        #print "Eliminando %s" % id
        self.cola.delete_message(id)

    def clear(self):
        return self.queue.clear()

    def delete_queue(self):
        return self.conn.delete_queue(self.queue)
