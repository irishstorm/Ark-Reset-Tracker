#   Create a Server Reset Tracker
#   Todo
#   Make a List of servers, saved to file
#   Generate list of reset servers
#   Save the Generated List to a txt file
import os
import datetime
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ark Reset Tracker")
root.geometry("600x400")


with open('resetLog.txt', 'a') as f:
    print("Creating file")
with open('resetList.txt', 'a') as f:
    print("Creating file")


def GenerateReset():
    temp = ""
    date = datetime.datetime.now()
    dateformatted = " - " + str(date.day) + " " + \
        str(date.strftime("%B")) + " " + str(date.year)

    serverList = GetServerList()
    serverList = serverList.split(',')
    apps = [x for x in serverList if x.strip()]

    for i in range(0, len(serverList)):
        if i == (len(serverList) - 1):
            temp += serverList[i]
        else:
            temp += serverList[i] + ","

    print(temp + dateformatted)

    with open('resetLog.txt', 'a') as f:
        f.write(temp + dateformatted + '\n')

    #   Copy the reset list to clipboard
    root.clipboard_clear()
    root.clipboard_append(temp + dateformatted)
    # now it stays on the clipboard after the window is closed
    root.update()

    resetLog.insert(END, temp + dateformatted + "\n")
    consoleLog.insert(
        END, "The reset list has been generated.\nCopied to clipboard!.\n")


def donothing():
    consoleLog.insert(
        END, "Todo:\nFix save button not saving\n")


def GetServerList():
    if os.path.isfile('ResetList.txt'):
        with open('ResetList.txt', 'r') as f:
            temp = f.read()
    return temp


def openNewServerWindow():
    newServerWindow = Toplevel(root)
    newServerWindow.title("Edit Server List")
    newServerWindow.geometry("400x200")

    servers = Text(newServerWindow, height=10)
    servers.pack()
    servers.insert(END, GetServerList())

    print("OpenNewServerWindow :: " + servers.get("1.0", "end-1c"))

    save = Button(newServerWindow, text="Save", padx=40,
                  pady=10, command=lambda: saveServerList(servers.get("1.0", "end-1c"), newServerWindow))
    save.pack(side=BOTTOM)


def saveServerList(text, window):
    with open('resetList.txt', 'w') as f:
        f.write(text)
        print("saveServerList :: Saving reset list : " + text)
        consoleLog.insert(END, "Server listings changed.\n")

    mylist.delete(0, 'end')
    ServerListings()
    window.destroy()


#####   Menu's   #####
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Edit Server List", command=openNewServerWindow)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=helpmenu)
helpmenu.add_command(label="ToDo", command=donothing)

root.config(menu=menubar)


m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

#   Server List
mylist = Listbox(root)


def ServerListings():
    tempApps = GetServerList()
    tempApps = tempApps.split(',')
    apps = [x for x in tempApps if x.strip()]

    for i in range(0, len(apps)):
        mylist.insert(i, apps[i])


mylist.pack(side=TOP)
m1.add(mylist)
m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

ServerListings()


#   Reset List
resetLog = Text(root, height=15)
resetLog.pack(side=BOTTOM, fill=BOTH)
if os.path.isfile('resetLog.txt'):
    with open('resetLog.txt', 'r') as f:
        tempLog = f.read()
        resetLog.insert(END, tempLog)
m2.add(resetLog)


#   Generate Reset Button
btn = Button(root, text="Generate", padx=40,
             pady=10, command=GenerateReset)
btn.pack(side=BOTTOM)

#   Console Log
consoleLog = Text(root, height=10)
consoleLog.pack(side=BOTTOM, fill=BOTH)


root.mainloop()
