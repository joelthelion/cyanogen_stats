#!/usr/bin/python3
from socketIO_client import SocketIO, BaseNamespace

class Namespace(BaseNamespace):

    def on_connect(self):
        print('[Connected]')
    def on_install_response(self, *args):
        print(args)

#socketIO = SocketIO('stats.cyanogenmod.com', 8080, Namespace, wait_for_connection=True,
socketIO = SocketIO('stats.cyanogenmod.com', 8080, Namespace)
socketIO.wait(seconds=100)
