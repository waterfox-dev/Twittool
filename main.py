import sys

from server.app import *
from server.module.flasktool.command import *
from server.module.logger.printer import Printer

try :
    if sys.argv[1] == '-np':
        create_page(sys.argv[2])
        Printer.log("Creator tool", f"Files for {sys.argv[2]} has been created !")
        exit()

    elif sys.argv[1] == '-r':
        if __name__ == '__main__':
            Printer.log("Server", "Running Server")
            app.run()

except IndexError :
    Printer.warn('Launcher', "No argumen given, one required")