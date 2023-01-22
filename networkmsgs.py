import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,scrolledtext,END
from socket import *
import json,time
info='''
haozi
'''
class App(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("通讯小工具")
        self.root.resizable(False, False)
        self.layout()
        # self.root.protocol("WM_DELETE_WINDOW", self._stop)
        self.root.mainloop()
    def _stop(self):
        exit(0)
    def layout(self):
        tabContainer = ttk.Notebook(self.root)
        tabContainer.pack()

        HomeTab = ttk.Frame(tabContainer)
        tabContainer.add(HomeTab, text='主界面')
        self._layHomeTab(HomeTab)

        ipTab = ttk.Frame(tabContainer)
        tabContainer.add(ipTab, text='查询IP')
        self._layIpTab(ipTab)

        # HelpTab = ttk.Frame(tabContainer)
        # tabContainer.add(HelpTab, text='帮助')
        # self._layHelpTab(HelpTab)
    def _layIpTab(self, tab):
        transferBtn = ttk.Button(tab, text='查询', command=self._scachip)
        transferBtn.grid(row=7, column=0, padx=0, pady=20)

        self._ipout=tk.Text(tab)
        self._ipout.grid(row=0, column=1, padx=3, pady=10, columnspan=2,rowspan=2)
    def _scachip(self):
        self._ipout.delete(1.0,"end")
        addrs = getaddrinfo(gethostname(),None)
        for item in addrs:
            if item[0]==AF_INET:
                self._ipout.insert('insert',item[4][0]+"\n")
    def _layHomeTab(self,tab):
        self.msgst=tk.scrolledtext.ScrolledText(tab,height=33, wrap=tk.WORD)
        self.msgst.grid(row=0, column=0, padx=0, pady=0, columnspan=3,rowspan=5)
        # self.msgst=tk.Text(tab,height=33)
        # self.msgst.grid(row=0, column=0, padx=0, pady=0, columnspan=3,rowspan=5)
        
        # self.inputs=tk.Text(tab,width=40)
        self.inputs = tk.scrolledtext.ScrolledText(tab, width=40, wrap=tk.WORD)
        self.inputs.grid(row=0, column=4, padx=3,
                         pady=10, columnspan=4, rowspan=2)

        temp = ttk.Button(tab, text='清空', command=self._clear)
        temp.grid(row=2, column=4, padx=0, pady=0)

        temp = ttk.Button(tab, text='发送', command=self._gomsg)
        temp.grid(row=2, column=5, padx=0, pady=0)

        self._PORT = tk.StringVar()
        self._PORT.set("8000")
        ttk.Label(tab, text='端口:') \
            .grid(row=2, column=6, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self._PORT, justify='left', width=10) \
            .grid(row=2, column=7, padx=5, pady=10, columnspan=1)

        self._IP = tk.StringVar()
        self._IP.set("127.0.0.1")
        ttk.Label(tab, text='目标IP:') \
            .grid(row=3, column=4, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self._IP, justify='left', width=10) \
            .grid(row=3, column=5, padx=5, pady=10, columnspan=1)

        self._IPme = tk.StringVar()
        self._IPme.set("127.0.0.1")
        ttk.Label(tab, text='本地IP:') \
            .grid(row=3, column=6, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self._IPme, justify='left', width=10) \
            .grid(row=3, column=7, padx=5, pady=10, columnspan=1)

        temp = ttk.Button(tab, text='停止', command=self._stopserver)
        temp.grid(row=4, column=4, padx=0, pady=0, columnspan=2)

        temp = ttk.Button(tab, text='运行', command=self._runserver)
        temp.grid(row=4, column=6, padx=0, pady=0, columnspan=2)
    def _layHelpTab(self,tab):
        ttk.Label(tab,text=info).grid(row=0,column=0)
    def _clear(self):
        self.inputs.delete(1.0,"end")
    def _gomsg(self):
        try:
            tcp_client_socket = socket(AF_INET, SOCK_STREAM)
            tcp_client_socket.connect((self._IP.get(), int(self._PORT.get())))
            send_data = self.inputs.get(1.0,"end")
            tcp_client_socket.send(self._msgsEncode(send_data).encode("gbk"))
            # recvData = tcp_client_socket.recv(1024)
            tcp_client_socket.close()
            self._clear()
        except Exception as e:
            messagebox.showerror("ERROR",e)
    def _runserver(self):
        self.serverthread=threading.Thread(target=self._server)
        self.serverthreadstop=False
        self.serverthread.start()
    def _stopserver(self):
        # self.serverthread.stop()
        self.serverthreadstop=True
    def _server(self):
        while True:
            tcp_server_socket = socket(AF_INET, SOCK_STREAM)
            tcp_server_socket.bind((self._IPme.get(), int(self._PORT.get())))
            tcp_server_socket.listen(128)
            # tcp_server_socket.setblocking(False)
            client_socket, clientAddr = tcp_server_socket.accept()
            recv_data = client_socket.recv(10000)
            # self.msgst.insert('insert',"["+clientAddr[0]+"]():\n"+recv_data.decode("gbk")+"\n")
            self.msgst.insert('insert',self._msgsDecode(recv_data.decode("gbk"),clientAddr))
            self.msgst.see(END)
            client_socket.send("OK200".encode('gbk'))
            client_socket.close()
            if self.serverthreadstop:
                break
    def _msgsDecode(self,recv_data,clientAddr):
        temp=json.loads(recv_data)
        return "["+clientAddr[0]+"]("+temp["time"]+"):\n"+temp["data"]+"\n"
    def _msgsEncode(self,data):
        temp=json.dumps({
            "time":self._gettime(),
            "data":data
        })
        return temp
    def _gettime(self):
        t=time.localtime(time.time())
        return str(t.tm_year)+"/"+str(t.tm_mon)+"/"+str(t.tm_mday)+" "+str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec)
def runapp():
    app=App()
if __name__ == '__main__':
    app = App()
