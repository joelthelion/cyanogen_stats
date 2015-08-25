#!/usr/bin/python3
import sys
from socketIO_client import SocketIO, BaseNamespace


class Namespace(BaseNamespace):

    """ Websocket connection handler. Handles input from the stats site. """

    def on_connect(self):
        print('[Connected]', file=sys.stderr)

    def csv_format(self, lst):
        return ",".join(str(x) for x in lst)

    def on_install(self, *args):
        payload = sorted(args[0].items())
        if not hasattr(self, "headers"):
            self.headers = [k for k, v in payload]
            print(self.csv_format(self.headers))
        print(self.csv_format([v for k, v in payload]))
    def on_disconnect(self):
        sys.exit(1)

socketIO = SocketIO('stats.cyanogenmod.com', 8080, Namespace)
socketIO.wait(seconds=1e6)
