import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'@[\xa17\x00\xe3\x078\x8dY\xec\xaa\xe6\xecue'
    