import ctypes
import tkinter as tk
from tkinter import ttk
info='''
此程序是对于报价信息文本的编写进行的帮助，以便得到更高的效率
左侧是文本输入框用于输入信息，有七项分别是起运港，目的港，价格，船东，直达/中转，时间，有效期
为了用户便捷输入，有些输入框会有默认值
右侧是输出框，用于输出，此输出框可进行编辑，以便更方便的体验
下侧是按钮，基本按钮有生成，转大写，复制，而后面的两个按钮则为基本按钮组成的操作
这就结束了对报价小工具的基本描述
'''
class App(object):
    def __init__(self):
        self.dll = ctypes.cdll.LoadLibrary('I:\\exe\\python\\GUI\\报价辅助\\copy.dll')
        '''
        copy.dll
        DLLEXPORT void setClip(char*)
        '''
        self.root = tk.Tk()
        self.root.title("报价小工具")
        self.root.resizable(False, False)
        self.layout()
        self.root.mainloop()
    def layout(self):
        tabContainer = ttk.Notebook(self.root)
        tabContainer.pack()

        ipTab = ttk.Frame(tabContainer)
        tabContainer.add(ipTab, text='生成')
        self._layIpTab(ipTab)

        timeTab = ttk.Frame(tabContainer)
        tabContainer.add(timeTab, text='帮助')
        self._layTimeTab(timeTab)
    def _layIpTab(self, tab):
        self.POL = tk.StringVar()
        self.POL.set("Qingdao")
        ttk.Label(tab, text='POL(起运港):') \
            .grid(row=0, column=0, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self.POL, justify='left', width=25) \
            .grid(row=0, column=1, padx=5, pady=10, columnspan=3)
        
        self.POD = tk.StringVar()
        self.POD.set("")
        ttk.Label(tab, text='POD(目的港):') \
            .grid(row=1, column=0, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self.POD, justify='left', width=25) \
            .grid(row=1, column=1, padx=5, pady=10, columnspan=3)
        
        self.OCEAN_FREIGHT = tk.StringVar()
        self.OCEAN_FREIGHT.set("USD")
        ttk.Label(tab, text='OCEAN FREIGHT(价格):') \
            .grid(row=2, column=0, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self.OCEAN_FREIGHT, justify='left', width=25) \
            .grid(row=2, column=1, padx=5, pady=10, columnspan=3)
        
        self.CARRIER = tk.StringVar()
        self.CARRIER.set("")
        ttk.Label(tab, text='CARRIER(船东):') \
            .grid(row=3, column=0, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self.CARRIER, justify='left', width=25) \
            .grid(row=3, column=1, padx=5, pady=10, columnspan=3)
        
        self.SERVICE = tk.StringVar()
        self.SERVICE.set("")
        ttk.Label(tab, text='SERVICE(直达/中转):') \
            .grid(row=4, column=0, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self.SERVICE, justify='left', width=25) \
            .grid(row=4, column=1, padx=5, pady=10, columnspan=3)
        
        self.T_T = tk.StringVar()
        self.T_T.set("about 99 days")
        ttk.Label(tab, text='T/T(航程):') \
            .grid(row=5, column=0, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self.T_T, justify='left', width=25) \
            .grid(row=5, column=1, padx=5, pady=10, columnspan=3)
        
        self.VALID = tk.StringVar()
        self.VALID.set("")
        ttk.Label(tab, text='VALID(有效期):') \
            .grid(row=6, column=0, padx=5, pady=10)
        ttk.Entry(tab, textvariable=self.VALID, justify='left', width=25) \
            .grid(row=6, column=1, padx=5, pady=10, columnspan=3)

        ttk.Label(tab, text='输出:') \
            .grid(row=0, column=4, padx=5, pady=10)
        self.t=tk.Text(tab,width=25)
        self.t.grid(row=0, column=5, padx=5, pady=10, columnspan=3,rowspan=7)

        transferBtn = ttk.Button(tab, text='生成', command=self._transferIp)
        transferBtn.grid(row=7, column=0, padx=0, pady=20)
        
        transferBtn = ttk.Button(tab, text='转大写', command=self._upper)
        transferBtn.grid(row=7, column=1, padx=0, pady=20)

        transferBtn = ttk.Button(tab, text='复制', command=self._copy)
        transferBtn.grid(row=7, column=2, padx=0, pady=20)
        
        transferBtn = ttk.Button(tab, text='生成并复制', command=self._transferIpAndCopy)
        transferBtn.grid(row=7, column=3, padx=0, pady=20)

        transferBtn = ttk.Button(tab, text='生成并转大写并复制', command=self._transferIpAndUpperAndCopy)
        transferBtn.grid(row=7, column=4, padx=0, pady=20)
    def _transferIpAndUpperAndCopy(self):
        self._transferIp()
        self._upper()
        self._copy()
    def _upper(self):
        temp=self.t.get(1.0,"end")
        self.t.delete(1.0,"end")
        self.t.insert('insert',temp.upper())
    def _transferIpAndCopy(self):
        self._transferIp()
        self._copy()
    def _copy(self):
        #copy_s(self.t.get(1.0, "end"))
        self.dll.setClip(ctypes.c_char_p(bytes(self.t.get(1.0,"end"),'utf-8')))
    def _transferIp(self):
        self.t.delete(1.0,"end")
        temp="POL:"+self.POL.get()+"\n"
        temp=temp+"POD:"+self.POD.get()+"\n"
        temp=temp+"OCEAN FREIGHT:"+self.OCEAN_FREIGHT.get()+"\n"
        temp=temp+"CARRIER:"+self.CARRIER.get()+"\n"
        temp=temp+"SERVICE:"+self.SERVICE.get()+"\n"
        temp=temp+"T/T:"+self.T_T.get()+"\n"
        temp=temp+"VALID:"+self.VALID.get()
        self.t.insert('insert',temp)
    def _layTimeTab(self, tab):
        ttk.Label(tab,text=info)\
            .grid(row=0,column=0,)
if __name__ == '__main__':
    app = App()
