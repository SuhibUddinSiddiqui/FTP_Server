import socket
import Server
from tkinter import filedialog
from tkinter import *
import threading


ip =socket.gethostbyname(socket.gethostname())
YO_INPUT = ""
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        Frame.status_flag = True

    def init_window(self):
        self.master.title("FTP Server")
        self.pack(fill=BOTH, expand=1)

        my_label = Label(self,text="FTP Link :",font = "Helvetica 12 bold italic")
        my_label.place(x=10,y=40)

        Frame.my_label1 = Label(self, text=ip)
        Frame.my_label41 = Label(self, text="! ! ! Your Sever is Started... ! ! !", fg="red", font="Helvetica 16 bold italic")

        my_label2 = Label(self, text="Port  :",font="Helvetica 12 bold italic")
        my_label2.place(x=10, y=80)

        Frame.my_label3 = Label(self, text="2121")


        Connect_Button = Button(self, text=" Connect ",height=5,width=20,bg='light blue', command= self.TH_chalo)
        Connect_Button.place(x=30, y=189)

        Connect_Button = Button(self, text=" Disconnect ", height=5, width=20, bg='light blue' , command=self.client_exit)
        Connect_Button.place(x=200, y=189)








    def TH_chalo(self):
        if Frame.status_flag == True:
            Frame.my_label1.configure(text=ip)
            Frame.my_label1.place(x=100, y=40)
            Frame.my_label3.configure(text="2121")
            Frame.my_label3.place(x=100, y=80)
            Frame.my_label41.configure(text="! ! ! Your Sever is Started... ! ! !")
            Frame.my_label41.place(x=40, y=120)

            Server.yo = 'y'
            t1 = threading.Thread(target=Server.Start_the_Server)
            t1.start()
            Frame.status_flag = False
            #print(Frame.status_flag)
            # Server.command_pro = False

    def client_exit(self):
        if Frame.status_flag == False:
            Server.yo = 'n'
            Frame.my_label1.configure(text="Empty")
            Frame.my_label1.place(x=100, y=40)
            Frame.my_label3.configure(text="Empty")
            Frame.my_label3.place(x=100, y=80)
            Frame.my_label41.configure(text="Disconnect")
            Server.Start_the_Server()
            Frame.status_flag = True
            #print(Frame.status_flag)
            #print(Server.yo)


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()