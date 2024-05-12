# Server.py
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import Ice
Ice.loadSlice('Printer.ice')
import Example

class ConsolePrinter(Example.Printer):
    def write(self, message, current=None):
        print(message)

class Server(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = ConsolePrinter()

        properties = broker.getProperties()
        properties.setProperty("PrinterAdapter.Endpoints", "tcp -h localhost -p 10000")

        adapter = broker.createObjectAdapter("PrinterAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("printer1"))

        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0

if __name__ == '__main__':
    server = Server()
    sys.exit(server.main(sys.argv))