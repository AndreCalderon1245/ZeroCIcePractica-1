import sys
import Ice # type: ignore
Ice.loadSlice('Printer.ice')
import Example # type: ignore

class Client(Ice.Application):
    def run(self, argv):
        if len(argv) < 2:
            print("Usage: {} <proxy>".format(argv[0]))
            return 1

        proxy = self.communicator().stringToProxy("printer1:tcp -h localhost -p 10000")
        printer = Example.PrinterPrx.checkedCast(proxy)

        if not printer:
            raise RuntimeError('Proxy Invalido')
        
        printer.write('Hola Mundo!')

        return 0

if __name__ == '__main__':
    sys.exit(Client().main(sys.argv))