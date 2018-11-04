import configparser
import os

class Config:
    def __init__(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        config = configparser.ConfigParser()
        config.read(__location__ + "/conf.ini")
        self.mysql_host = config['MYSQL']['host']
        self.mysql_user = config['MYSQL']['user']
        self.mysql_passwd = config['MYSQL']['passwd']
        self.mysql_db = config['MYSQL']['db']