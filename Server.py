import ftplib
import os
import socket
import C_folder
import GUI
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

command_pro = True
yo = ''
status_flag = True
def Start_the_Server():
    try:
        if command_pro == True:
            authorizer = DummyAuthorizer()
            if not os.path.exists(r"C:\Brown"):
                print("making File...")
                os.makedirs(r"C:\Brown")

            authorizer.add_user('user', '12345', r"C:\Brown", perm='elradfmwMT')
            os.path.join(os.path.dirname(__file__))
            authorizer.add_anonymous(r"C:\Brown")




            handler = FTPHandler
            handler.authorizer = authorizer
            handler.banner = "pyftpdlib based ftpd ready."

            address = ('', 2121)
            server = FTPServer(address, handler)

            server.max_cons = 256
            server.max_cons_per_ip = 5
            if yo == 'y':

                print("d")

                server.serve_forever()

            else:
                server.close_all()


    except:
        print("something went wrong")










