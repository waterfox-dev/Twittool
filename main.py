from server.module.flasktool.command import *
from server.module.logger.printer import Printer
from server.app import *

import sys

try :
    if sys.argv[1] == '-np':
        create_page(sys.argv[2])
        Printer.log("Creator tool", f"Files for {sys.argv[2]} has been created !")
        exit()

    if sys.argv[1] == '-r':
        if __name__ == '__main__':
            Printer.log("Server", "Running Server")
            app.run()

except IndexError :
    Printer.ask("Question", "Are you sure about that")