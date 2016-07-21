#import tkFont
from tkinter import Tk, ttk, PhotoImage, Label, Menu, Frame, font
#from pyglet.window import key

class mainFrameGui():

    def __init__(self, win, tabObject):
        self.__win = win
        #self.__win
        self.__tabObject = tabObject

    def loadMenu(self):
        self.menubar = Menu(self.__tabObject)
        self.toolsmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Tools", menu=self.toolsmenu)
        self.toolsmenu.add_command(label="Set Time Record")
        self.toolsmenu.add_command(label="Optic Power Cal")
        self.toolsmenu.add_command(label="COM Config")
        self.aboutmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help",  menu=self.aboutmenu)
        self.aboutmenu.add_command(label="About")
        self.__win.config(menu=self.menubar)

    def loadLogo(self):
        frameImg = Frame(self.__win)
        frameImg.pack(anchor='nw')#(row = 0, column = 0)
        #file = 'C:/Projects/Python testout/Universal Tuning/images/greenLedGB.gif'
        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        photo = PhotoImage(file = 'images/logo.png')
        label = Label(frameImg, image=photo)
        label.image = photo
        label.grid(row=0, column=0)

        # set space between 2 label
        lblEmpty = Label(frameImg, text="       ")
        lblEmpty.grid(row=0, column=1)

        #Create a Combobox for slot select
        lblGen = Label(frameImg, font="Arial 15 bold", text='Slot#:')
        lblGen.grid(row=0, column=2)
        cmbSlot = ttk.Combobox(frameImg, width=5, font="Arial 15 bold", state='readonly')
        cmbSlot['value'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
        cmbSlot.current(0)
        cmbSlot.grid(row=0, column=3)

        # set other space between the components
        lblEmpty = Label(frameImg, text="       ")
        lblEmpty.grid(row=0, column=4)

        #Create Card Type Combobox
        lblGen = Label(frameImg, font="Arial 15 bold", text='Board Type:')
        lblGen.grid(row=0, column=5)
        cmbBrdType = ttk.Combobox(frameImg, width=15, font="Arial 15 bold", state='normal')
        cmbBrdType['value'] = ('DWDM Tx', 'Hs Rx');
        cmbBrdType.current(0)
        cmbBrdType.grid(row=0, column=6)

        #img.grid(row = 1, column = 1, sticky = 'w')

    def makeGroups(self, tabControl):
        grpMonitor = ttk.LabelFrame(tabControl, text=' Dynamic Name Based on Board Type')
        grpMonitor.grid(column=0, row=0, padx=50, pady=100)
        ttk.Label(grpMonitor, text="Channel 1:").grid(column=0, row=0)
        #tabControl.grid(row=1, column=0, pady=200, padx=300)

    def makeTab(self):
        # rename tab name take me 5 minutes
        #self.__tabObject = ttk.Notebook(self.__win) # Create Tab Control
        #self.__tabObject.grid(row=100, column=0)

        self.__tabObject.pack(fill='x')#grid(row=1, column=0) # Pack to make visible
        tabMon = Frame(self.__tabObject)  # create Control tab
        self.__tabObject.add(tabMon, text='Monitor') # Add the tab
        self.makeGroups(tabMon)
        tabCrt = Frame(self.__tabObject)  # create Control tab
        self.__tabObject.add(tabCrt, text='Control') # Add the tab
        self.makeGroups(tabCrt)
        tabBrdInfo = ttk.Frame(self.__tabObject)  # create Control tab
        self.__tabObject.add(tabBrdInfo, text='Board Info') # Add the tab
        tabAlarm = ttk.Frame(self.__tabObject)  # create Control tab
        self.__tabObject.add(tabAlarm, text='Alarms') # Add the tab
        tabConf = ttk.Frame(self.__tabObject)  # create Control tab
        self.__tabObject.add(tabConf, text='Config') # Add the tab
        tabRSU = ttk.Frame(self.__tabObject)  # create Control tab
        self.__tabObject.add(tabRSU, text='RSU Config') # Add the tab
        #tabMon.grid(row=1, column=0, pady=200, padx=300)   # need to assign the number slowly until finding a right side

    def makeBottomButton(self):
        #helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
        frameButton = Frame(self.__win)
        frameButton.pack(side='bottom')
        btnSave = ttk.Button(frameButton, text="Save")
        btnSave.grid(row=0, column=0)
        btnRecord = ttk.Button(frameButton, text="Record")
        btnRecord.grid(row=0, column=1)
        btnClose = ttk.Button(frameButton, text="Close")
        btnClose.grid(row=0, column=2)

if __name__ == '__main__':
    win = Tk()  # Create instance
    win.title("Tuning GUI")  # Add a title
    tabObject = ttk.Notebook(win)
    dGui = mainFrameGui(win, tabObject)
    dGui.loadMenu()
    dGui.loadLogo()
    dGui.makeTab()
    dGui.makeBottomButton()
    win.mainloop()
