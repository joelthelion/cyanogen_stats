#!/usr/bin/python3
import sys
from socketIO_client import SocketIO, BaseNamespace

class Namespace(BaseNamespace):
    def on_connect(self):
        print('[Connected]',file=sys.stderr)
    def csv_format(self,lst):
        return ",".join(str(x) for x in lst)
    def on_install(self, *args):
        payload = args[0]
        if not hasattr(self,"headers"):
            self.headers=payload.keys()
            print(self.csv_format(self.headers))
        print(self.csv_format(payload.values()))

socketIO = SocketIO('stats.cyanogenmod.com', 8080, Namespace)
socketIO.wait(seconds=100)
