import tkinter.font
from tkinter import *
from tkinter import filedialog as fd

win = Tk()
board = Tk()

myFont = tkint er.font.Font(family='Hervetica', size=12, weight='bold')  # присвоюєм за замовченням стиль
smallFont = tkinter.font.Font(family='Hervetica', weight='bold', size=32)
largeFont = tkinter.font.Font(family='Hervetica', weight='bold', size=40)  # мій шрифт для малих кнопок
win.title("DNA Switcher")
board.title("Diode Board")  # назва вікна
win.geometry('490x400+515+180')
board.geometry('1024x600+0+0')
backgroundcolor = "#000"
foregroundColor = "#006400"
board.configure(background=backgroundcolor)
win.overrideredirect(1)
board.overrideredirect(1)
win.resizable(False, False)
board.resizable(False, False)

w = 3
b = 3
w_h = 18
h_t = 18

def exitConfigurator():
    win.destroy()
    board.destroy()
def deleteWalue():
    for e in ea1, ea2, ea3, ea4, ea5, ea6, ea7, ea8, ea9, ea10, ea11, ea12, \
             eb1, eb2, eb3, eb4, eb5, eb6, eb7, eb8, eb9, eb10, eb11, eb12, \
             ec1, ec2, ec3, ec4, ec5, ec6, ec7, ec8, ec9, ec10, ec11, ec12, \
             ed1, ed2, ed3, ed4, ed5, ed6, ed7, ed8, ed9, ed10, ed11, ed12, \
             ee1, ee2, ee3, ee4, ee5, ee6, ee7, ee8, ee9, ee10, ee11, ee12, \
             ef1, ef2, ef3, ef4, ef5, ef6, ef7, ef8, ef9, ef10, ef11, ef12, \
             eg1, eg2, eg3, eg4, eg5, eg6, eg7, eg8, eg9, eg10, eg11, eg12, \
             eh1, eh2, eh3, eh4, eh5, eh6, eh7, eh8, eh9, eh10, eh11, eh12:
        e.delete(0, END)

def browse_file():
    li_o = []
    file_name = fd.askopenfilename()
    with open(file_name, 'r') as filehandle:
        for line in filehandle:
            currentplace = line[:-1]
            li_o.append(currentplace)
    print(li_o)
    deleteWalue()
    ea1.insert(0, li_o[0])
    ea2.insert(0, li_o[1])
    ea3.insert(0, li_o[2])
    ea4.insert(0, li_o[3])
    ea5.insert(0, li_o[4])
    ea6.insert(0, li_o[5])
    ea7.insert(0, li_o[6])
    ea8.insert(0, li_o[7])
    ea9.insert(0, li_o[8])
    ea10.insert(0, li_o[9])
    ea11.insert(0, li_o[10])
    ea12.insert(0, li_o[11])
    eb1.insert(0, li_o[12])
    eb2.insert(0, li_o[13])
    eb3.insert(0, li_o[14])
    eb4.insert(0, li_o[15])
    eb5.insert(0, li_o[16])
    eb6.insert(0, li_o[17])
    eb7.insert(0, li_o[18])
    eb8.insert(0, li_o[19])
    eb9.insert(0, li_o[20])
    eb10.insert(0, li_o[21])
    eb11.insert(0, li_o[22])
    eb12.insert(0, li_o[23])
    ec1.insert(0, li_o[24])
    ec2.insert(0, li_o[25])
    ec3.insert(0, li_o[26])
    ec4.insert(0, li_o[27])
    ec5.insert(0, li_o[28])
    ec6.insert(0, li_o[29])
    ec7.insert(0, li_o[30])
    ec8.insert(0, li_o[31])
    ec9.insert(0, li_o[32])
    ec10.insert(0, li_o[33])
    ec11.insert(0, li_o[34])
    ec12.insert(0, li_o[35])
    ed1.insert(0, li_o[36])
    ed2.insert(0, li_o[37])
    ed3.insert(0, li_o[38])
    ed4.insert(0, li_o[39])
    ed5.insert(0, li_o[40])
    ed6.insert(0, li_o[41])
    ed7.insert(0, li_o[42])
    ed8.insert(0, li_o[43])
    ed9.insert(0, li_o[44])
    ed10.insert(0, li_o[45])
    ed11.insert(0, li_o[46])
    ed12.insert(0, li_o[47])
    ee1.insert(0, li_o[48])
    ee2.insert(0, li_o[49])
    ee3.insert(0, li_o[50])
    ee4.insert(0, li_o[51])
    ee5.insert(0, li_o[52])
    ee6.insert(0, li_o[53])
    ee7.insert(0, li_o[54])
    ee8.insert(0, li_o[55])
    ee9.insert(0, li_o[56])
    ee10.insert(0, li_o[57])
    ee11.insert(0, li_o[58])
    ee12.insert(0, li_o[59])
    ef1.insert(0, li_o[60])
    ef2.insert(0, li_o[61])
    ef3.insert(0, li_o[62])
    ef4.insert(0, li_o[63])
    ef5.insert(0, li_o[64])
    ef6.insert(0, li_o[65])
    ef7.insert(0, li_o[66])
    ef8.insert(0, li_o[67])
    ef9.insert(0, li_o[68])
    ef10.insert(0, li_o[69])
    ef11.insert(0, li_o[70])
    ef12.insert(0, li_o[71])
    eg1.insert(0, li_o[72])
    eg2.insert(0, li_o[73])
    eg3.insert(0, li_o[74])
    eg4.insert(0, li_o[75])
    eg5.insert(0, li_o[76])
    eg6.insert(0, li_o[77])
    eg7.insert(0, li_o[78])
    eg8.insert(0, li_o[79])
    eg9.insert(0, li_o[80])
    eg10.insert(0, li_o[81])
    eg11.insert(0, li_o[82])
    eg12.insert(0, li_o[83])
    eh1.insert(0, li_o[84])
    eh2.insert(0, li_o[85])
    eh3.insert(0, li_o[86])
    eh4.insert(0, li_o[87])
    eh5.insert(0, li_o[88])
    eh6.insert(0, li_o[89])
    eh7.insert(0, li_o[90])
    eh8.insert(0, li_o[91])
    eh9.insert(0, li_o[92])
    eh10.insert(0, li_o[93])
    eh11.insert(0, li_o[94])
    eh12.insert(0, li_o[95])

def save_as_button():
    file_name = fd.asksaveasfilename()  # filetypes=(("TXT files", "*.txt"), ("All files", "*.*"))
    li_s = [ea1.get(), ea2.get(), ea3.get(), ea4.get(), ea5.get(), ea6.get(), ea7.get(), ea8.get(), ea9.get(),
            ea10.get(), ea11.get(), ea12.get(), eb1.get(), eb2.get(), eb3.get(), eb4.get(), eb5.get(), eb6.get(),
            eb7.get(),
            eb8.get(), eb9.get(), eb10.get(), eb11.get(), eb12.get(), ec1.get(), ec2.get(), ec3.get(), ec4.get(),
            ec5.get(),
            ec6.get(), ec7.get(), ec8.get(), ec9.get(), ec10.get(), ec11.get(), ec12.get(), ed1.get(), ed2.get(),
            ed3.get(), ed4.get(), ed5.get(),
            ed6.get(), ed7.get(), ed8.get(), ed9.get(), ed10.get(), ed11.get(), ed12.get(), ee1.get(), ee2.get(),
            ee3.get(), ee4.get(), ee5.get(),
            ee6.get(), ee7.get(), ee8.get(), ee9.get(), ee10.get(), ee11.get(), ee12.get(), ef1.get(), ef2.get(),
            ef3.get(), ef4.get(), ef5.get(),
            ef6.get(), ef7.get(), ef8.get(), ef9.get(), ef10.get(), ef11.get(), ef12.get(), eg1.get(), eg2.get(),
            eg3.get(), eg4.get(), eg5.get(),
            eg6.get(), eg7.get(), eg8.get(), eg9.get(), eg10.get(), eg11.get(), eg12.get(), eh1.get(), eh2.get(),
            eh3.get(), eh4.get(), eh5.get(),
            eh6.get(), eh7.get(), eh8.get(), eh9.get(), eh10.get(), eh11.get(), eh12.get()]
    with open(file_name, 'w') as filehandle:
        for listitem in li_s:
            filehandle.write('%s\n' % listitem)

def clear_button():
    deleteWalue()
    for e in ea1, ea2, ea3, ea4, ea5, ea6, ea7, ea8, ea9, ea10, ea11, ea12,\
             eb1, eb2, eb3, eb4, eb5, eb6, eb7, eb8, eb9, eb10, eb11, eb12,\
             ec1, ec2, ec3, ec4, ec5, ec6, ec7, ec8, ec9, ec10, ec11, ec12,\
             ed1, ed2, ed3, ed4, ed5, ed6, ed7, ed8, ed9, ed10, ed11, ed12,\
             ee1, ee2, ee3, ee4, ee5, ee6, ee7, ee8, ee9, ee10, ee11, ee12,\
             ef1, ef2, ef3, ef4, ef5, ef6, ef7, ef8, ef9, ef10, ef11, ef12,\
             eg1, eg2, eg3, eg4, eg5, eg6, eg7, eg8, eg9, eg10, eg11, eg12,\
             eh1, eh2, eh3, eh4, eh5, eh6, eh7, eh8, eh9, eh10, eh11, eh12:
        e.insert(0, 0)

def clear_field():
    for c in bea1, bea2, bea3, bea4, bea5, bea6, bea7, bea8, bea9, bea10, bea11, bea12, \
             beb1, beb2, beb3, beb4, beb5, beb6, beb7, beb8, beb9, beb10, beb11, beb12, \
             bec1, bec2, bec3, bec4, bec5, bec6, bec7, bec8, bec9, bec10, bec11, bec12, \
             bed1, bed2, bed3, bed4, bed5, bed6, bed7, bed8, bed9, bed10, bed11, bed12, \
             bee1, bee2, bee3, bee4, bee5, bee6, bee7, bee8, bee9, bee10, bee11, bee12, \
             bef1, bef2, bef3, bef4, bef5, bef6, bef7, bef8, bef9, bef10, bef11, bef12, \
             beg1, beg2, beg3, beg4, beg5, beg6, beg7, beg8, beg9, beg10, beg11, beg12, \
             beh1, beh2, beh3, beh4, beh5, beh6, beh7, beh8, beh9, beh10, beh11, beh12:
        c.config(bg='black')

def keyboard_walue(keyparam):
    kw = run_entry.get()
    print(keyparam)
    print(kw)
    clear_field()
    if ea1.get() == kw:
        bea1.config(bg='white')
    if ea2.get() == kw:
        bea2.config(bg='white')
    if ea3.get() == kw:
        bea3.config(bg='white')
    if ea4.get() == kw:
        bea4.config(bg='white')
    if ea5.get() == kw:
        bea5.config(bg='white')
    if ea6.get() == kw:
        bea6.config(bg='white')
    if ea7.get() == kw:
        bea7.config(bg='white')
    if ea8.get() == kw:
        bea8.config(bg='white')
    if ea9.get() == kw:
        bea9.config(bg='white')
    if ea10.get() == kw:
        bea10.config(bg='white')
    if ea11.get() == kw:
        bea11.config(bg='white')
    if ea12.get() == kw:
        bea12.config(bg='white')
    if eb1.get() == kw:
        beb1.config(bg='white')
    if eb2.get() == kw:
        beb2.config(bg='white')
    if eb3.get() == kw:
        beb3.config(bg='white')
    if eb4.get() == kw:
        beb4.config(bg='white')
    if eb5.get() == kw:
        beb5.config(bg='white')
    if eb6.get() == kw:
        beb6.config(bg='white')
    if eb7.get() == kw:
        beb7.config(bg='white')
    if eb8.get() == kw:
        beb8.config(bg='white')
    if eb9.get() == kw:
        beb9.config(bg='white')
    if eb10.get() == kw:
        beb10.config(bg='white')
    if eb11.get() == kw:
        beb11.config(bg='white')
    if eb12.get() == kw:
        beb12.config(bg='white')
    if ec1.get() == kw:
        bec1.config(bg='white')
    if ec2.get() == kw:
        bec2.config(bg='white')
    if ec3.get() == kw:
        bec3.config(bg='white')
    if ec4.get() == kw:
        bec4.config(bg='white')
    if ec5.get() == kw:
        bec5.config(bg='white')
    if ec6.get() == kw:
        bec6.config(bg='white')
    if ec7.get() == kw:
        bec7.config(bg='white')
    if ec8.get() == kw:
        bec8.config(bg='white')
    if ec9.get() == kw:
        bec9.config(bg='white')
    if ec10.get() == kw:
        bec10.config(bg='white')
    if ec11.get() == kw:
        bec11.config(bg='white')
    if ec12.get() == kw:
        bec12.config(bg='white')
    if ed1.get() == kw:
        bed1.config(bg='white')
    if ed2.get() == kw:
        bed2.config(bg='white')
    if ed3.get() == kw:
        bed3.config(bg='white')
    if ed4.get() == kw:
        bed4.config(bg='white')
    if ed5.get() == kw:
        bed5.config(bg='white')
    if ed6.get() == kw:
        bed6.config(bg='white')
    if ed7.get() == kw:
        bed7.config(bg='white')
    if ed8.get() == kw:
        bed8.config(bg='white')
    if ed9.get() == kw:
        bed9.config(bg='white')
    if ed10.get() == kw:
        bed10.config(bg='white')
    if ed11.get() == kw:
        bed11.config(bg='white')
    if ed12.get() == kw:
        bed12.config(bg='white')
    if ee1.get() == kw:
        bee1.config(bg='white')
    if ee2.get() == kw:
        bee2.config(bg='white')
    if ee3.get() == kw:
        bee3.config(bg='white')
    if ee4.get() == kw:
        bee4.config(bg='white')
    if ee5.get() == kw:
        bee5.config(bg='white')
    if ee6.get() == kw:
        bee6.config(bg='white')
    if ee7.get() == kw:
        bee7.config(bg='white')
    if ee8.get() == kw:
        bee8.config(bg='white')
    if ee9.get() == kw:
        bee9.config(bg='white')
    if ee10.get() == kw:
        bee10.config(bg='white')
    if ee11.get() == kw:
        bee11.config(bg='white')
    if ee12.get() == kw:
        bee12.config(bg='white')
    if ef1.get() == kw:
        bef1.config(bg='white')
    if ef2.get() == kw:
        bef2.config(bg='white')
    if ef3.get() == kw:
        bef3.config(bg='white')
    if ef4.get() == kw:
        bef4.config(bg='white')
    if ef5.get() == kw:
        bef5.config(bg='white')
    if ef6.get() == kw:
        bef6.config(bg='white')
    if ef7.get() == kw:
        bef7.config(bg='white')
    if ef8.get() == kw:
        bef8.config(bg='white')
    if ef9.get() == kw:
        bef9.config(bg='white')
    if ef10.get() == kw:
        bef10.config(bg='white')
    if ef11.get() == kw:
        bef11.config(bg='white')
    if ef12.get() == kw:
        bef12.config(bg='white')
    if eg1.get() == kw:
        beg1.config(bg='white')
    if eg2.get() == kw:
        beg2.config(bg='white')
    if eg3.get() == kw:
        beg3.config(bg='white')
    if eg4.get() == kw:
        beg4.config(bg='white')
    if eg5.get() == kw:
        beg5.config(bg='white')
    if eg6.get() == kw:
        beg6.config(bg='white')
    if eg7.get() == kw:
        beg7.config(bg='white')
    if eg8.get() == kw:
        beg8.config(bg='white')
    if eg9.get() == kw:
        beg9.config(bg='white')
    if eg10.get() == kw:
        beg10.config(bg='white')
    if eg11.get() == kw:
        beg11.config(bg='white')
    if eg12.get() == kw:
        beg12.config(bg='white')
    if eh1.get() == kw:
        beh1.config(bg='white')
    if eh2.get() == kw:
        beh2.config(bg='white')
    if eh3.get() == kw:
        beh3.config(bg='white')
    if eh4.get() == kw:
        beh4.config(bg='white')
    if eh5.get() == kw:
        beh5.config(bg='white')
    if eh6.get() == kw:
        beh6.config(bg='white')
    if eh7.get() == kw:
        beh7.config(bg='white')
    if eh8.get() == kw:
        beh8.config(bg='white')
    if eh9.get() == kw:
        beh9.config(bg='white')
    if eh10.get() == kw:
        beh10.config(bg='white')
    if eh11.get() == kw:
        beh11.config(bg='white')
    if eh12.get() == kw:
        beh12.config(bg='white')
    run_entry.delete(0, END)

exit_Conf_button = Button(win, text="EXIT", font=myFont, command=exitConfigurator, height=1, width=8)
exit_Conf_button.pack()
exit_Conf_button.place(x=380, y=350)

save_as_Button = Button(win, text="SAVE AS", font=myFont, command=save_as_button, height=1, width=8)
save_as_Button.pack()
save_as_Button.place(x=210, y=350)

browse_Button = Button(win, text="BROWSE", font=myFont, command=browse_file, height=1, width=8)
browse_Button.pack()
browse_Button.place(x=10, y=350)

clear_Button = Button(win, text="CLEAR", font=myFont, command=clear_button, height=1, width=8)
clear_Button.pack()
clear_Button.place(x=110, y=350)

run_entry = Entry(win, font=myFont, justify=CENTER, width=9)
run_entry.pack()
run_entry.place(x=10, y=280)

board.bind("<Return>", keyboard_walue)
win.bind("<Return>", keyboard_walue)

ea1 = Entry(win, font=myFont, justify=CENTER, width=w)
ea2 = Entry(win, font=myFont, justify=CENTER, width=w)
ea3 = Entry(win, font=myFont, justify=CENTER, width=w)
ea4 = Entry(win, font=myFont, justify=CENTER, width=w)
ea5 = Entry(win, font=myFont, justify=CENTER, width=w)
ea6 = Entry(win, font=myFont, justify=CENTER, width=w)
ea7 = Entry(win, font=myFont, justify=CENTER, width=w)
ea8 = Entry(win, font=myFont, justify=CENTER, width=w)
ea9 = Entry(win, font=myFont, justify=CENTER, width=w)
ea10 = Entry(win, font=myFont, justify=CENTER, width=w)
ea11 = Entry(win, font=myFont, justify=CENTER, width=w)
ea12 = Entry(win, font=myFont, justify=CENTER, width=w)
ea1, ea2, ea3, ea4, ea5, ea6, ea7, ea8, ea9, ea10, ea11, ea12.pack()
ea1.place(x=10, y=5)
ea2.place(x=50, y=5)
ea3.place(x=90, y=5)
ea4.place(x=130, y=5)
ea5.place(x=170, y=5)
ea6.place(x=210, y=5)
ea7.place(x=250, y=5)
ea8.place(x=290, y=5)
ea9.place(x=330, y=5)
ea10.place(x=370, y=5)
ea11.place(x=410, y=5)
ea12.place(x=450, y=5)

eb1 = Entry(win, font=myFont, justify=CENTER, width=w)
eb2 = Entry(win, font=myFont, justify=CENTER, width=w)
eb3 = Entry(win, font=myFont, justify=CENTER, width=w)
eb4 = Entry(win, font=myFont, justify=CENTER, width=w)
eb5 = Entry(win, font=myFont, justify=CENTER, width=w)
eb6 = Entry(win, font=myFont, justify=CENTER, width=w)
eb7 = Entry(win, font=myFont, justify=CENTER, width=w)
eb8 = Entry(win, font=myFont, justify=CENTER, width=w)
eb9 = Entry(win, font=myFont, justify=CENTER, width=w)
eb10 = Entry(win, font=myFont, justify=CENTER, width=w)
eb11 = Entry(win, font=myFont, justify=CENTER, width=w)
eb12 = Entry(win, font=myFont, justify=CENTER, width=w)
eb1, eb2, eb3, eb4, eb5, eb6, eb7, eb8, eb9, eb10, eb11, eb12.pack()
eb1.place(x=10, y=35)
eb2.place(x=50, y=35)
eb3.place(x=90, y=35)
eb4.place(x=130, y=35)
eb5.place(x=170, y=35)
eb6.place(x=210, y=35)
eb7.place(x=250, y=35)
eb8.place(x=290, y=35)
eb9.place(x=330, y=35)
eb10.place(x=370, y=35)
eb11.place(x=410, y=35)
eb12.place(x=450, y=35)

ec1 = Entry(win, font=myFont, justify=CENTER, width=w)
ec2 = Entry(win, font=myFont, justify=CENTER, width=w)
ec3 = Entry(win, font=myFont, justify=CENTER, width=w)
ec4 = Entry(win, font=myFont, justify=CENTER, width=w)
ec5 = Entry(win, font=myFont, justify=CENTER, width=w)
ec6 = Entry(win, font=myFont, justify=CENTER, width=w)
ec7 = Entry(win, font=myFont, justify=CENTER, width=w)
ec8 = Entry(win, font=myFont, justify=CENTER, width=w)
ec9 = Entry(win, font=myFont, justify=CENTER, width=w)
ec10 = Entry(win, font=myFont, justify=CENTER, width=w)
ec11 = Entry(win, font=myFont, justify=CENTER, width=w)
ec12 = Entry(win, font=myFont, justify=CENTER, width=w)
ec1, ec2, ec3, ec4, ec5, ec6, ec7, ec8, ec9, ec10, ec11, ec12.pack()
ec1.place(x=10, y=65)
ec2.place(x=50, y=65)
ec3.place(x=90, y=65)
ec4.place(x=130, y=65)
ec5.place(x=170, y=65)
ec6.place(x=210, y=65)
ec7.place(x=250, y=65)
ec8.place(x=290, y=65)
ec9.place(x=330, y=65)
ec10.place(x=370, y=65)
ec11.place(x=410, y=65)
ec12.place(x=450, y=65)

ed1 = Entry(win, font=myFont, justify=CENTER, width=w)
ed2 = Entry(win, font=myFont, justify=CENTER, width=w)
ed3 = Entry(win, font=myFont, justify=CENTER, width=w)
ed4 = Entry(win, font=myFont, justify=CENTER, width=w)
ed5 = Entry(win, font=myFont, justify=CENTER, width=w)
ed6 = Entry(win, font=myFont, justify=CENTER, width=w)
ed7 = Entry(win, font=myFont, justify=CENTER, width=w)
ed8 = Entry(win, font=myFont, justify=CENTER, width=w)
ed9 = Entry(win, font=myFont, justify=CENTER, width=w)
ed10 = Entry(win, font=myFont, justify=CENTER, width=w)
ed11 = Entry(win, font=myFont, justify=CENTER, width=w)
ed12 = Entry(win, font=myFont, justify=CENTER, width=w)
ed1, ed2, ed3, ed4, ed5, ed6, ed7, ed8, ed9, ed10, ed11, ed12.pack()
ed1.place(x=10, y=95)
ed2.place(x=50, y=95)
ed3.place(x=90, y=95)
ed4.place(x=130, y=95)
ed5.place(x=170, y=95)
ed6.place(x=210, y=95)
ed7.place(x=250, y=95)
ed8.place(x=290, y=95)
ed9.place(x=330, y=95)
ed10.place(x=370, y=95)
ed11.place(x=410, y=95)
ed12.place(x=450, y=95)

ee1 = Entry(win, font=myFont, justify=CENTER, width=w)
ee2 = Entry(win, font=myFont, justify=CENTER, width=w)
ee3 = Entry(win, font=myFont, justify=CENTER, width=w)
ee4 = Entry(win, font=myFont, justify=CENTER, width=w)
ee5 = Entry(win, font=myFont, justify=CENTER, width=w)
ee6 = Entry(win, font=myFont, justify=CENTER, width=w)
ee7 = Entry(win, font=myFont, justify=CENTER, width=w)
ee8 = Entry(win, font=myFont, justify=CENTER, width=w)
ee9 = Entry(win, font=myFont, justify=CENTER, width=w)
ee10 = Entry(win, font=myFont, justify=CENTER, width=w)
ee11 = Entry(win, font=myFont, justify=CENTER, width=w)
ee12 = Entry(win, font=myFont, justify=CENTER, width=w)
ee1, ee2, ee3, ee4, ee5, ee6, ee7, ee8, ee9, ee10, ee11, ee12.pack()
ee1.place(x=10, y=125)
ee2.place(x=50, y=125)
ee3.place(x=90, y=125)
ee4.place(x=130, y=125)
ee5.place(x=170, y=125)
ee6.place(x=210, y=125)
ee7.place(x=250, y=125)
ee8.place(x=290, y=125)
ee9.place(x=330, y=125)
ee10.place(x=370, y=125)
ee11.place(x=410, y=125)
ee12.place(x=450, y=125)

ef1 = Entry(win, font=myFont, justify=CENTER, width=w)
ef2 = Entry(win, font=myFont, justify=CENTER, width=w)
ef3 = Entry(win, font=myFont, justify=CENTER, width=w)
ef4 = Entry(win, font=myFont, justify=CENTER, width=w)
ef5 = Entry(win, font=myFont, justify=CENTER, width=w)
ef6 = Entry(win, font=myFont, justify=CENTER, width=w)
ef7 = Entry(win, font=myFont, justify=CENTER, width=w)
ef8 = Entry(win, font=myFont, justify=CENTER, width=w)
ef9 = Entry(win, font=myFont, justify=CENTER, width=w)
ef10 = Entry(win, font=myFont, justify=CENTER, width=w)
ef11 = Entry(win, font=myFont, justify=CENTER, width=w)
ef12 = Entry(win, font=myFont, justify=CENTER, width=w)
ef1, ef2, ef3, ef4, ef5, ef6, ef7, ef8, ef9, ef10, ef11, ef12.pack()
ef1.place(x=10, y=155)
ef2.place(x=50, y=155)
ef3.place(x=90, y=155)
ef4.place(x=130, y=155)
ef5.place(x=170, y=155)
ef6.place(x=210, y=155)
ef7.place(x=250, y=155)
ef8.place(x=290, y=155)
ef9.place(x=330, y=155)
ef10.place(x=370, y=155)
ef11.place(x=410, y=155)
ef12.place(x=450, y=155)

eg1 = Entry(win, font=myFont, justify=CENTER, width=w)
eg2 = Entry(win, font=myFont, justify=CENTER, width=w)
eg3 = Entry(win, font=myFont, justify=CENTER, width=w)
eg4 = Entry(win, font=myFont, justify=CENTER, width=w)
eg5 = Entry(win, font=myFont, justify=CENTER, width=w)
eg6 = Entry(win, font=myFont, justify=CENTER, width=w)
eg7 = Entry(win, font=myFont, justify=CENTER, width=w)
eg8 = Entry(win, font=myFont, justify=CENTER, width=w)
eg9 = Entry(win, font=myFont, justify=CENTER, width=w)
eg10 = Entry(win, font=myFont, justify=CENTER, width=w)
eg11 = Entry(win, font=myFont, justify=CENTER, width=w)
eg12 = Entry(win, font=myFont, justify=CENTER, width=w)
eg1, eg2, eg3, eg4, eg5, eg6, eg7, eg8, eg9, eg10, eg11, eg12.pack()
eg1.place(x=10, y=185)
eg2.place(x=50, y=185)
eg3.place(x=90, y=185)
eg4.place(x=130, y=185)
eg5.place(x=170, y=185)
eg6.place(x=210, y=185)
eg7.place(x=250, y=185)
eg8.place(x=290, y=185)
eg9.place(x=330, y=185)
eg10.place(x=370, y=185)
eg11.place(x=410, y=185)
eg12.place(x=450, y=185)

eh1 = Entry(win, font=myFont, justify=CENTER, width=w)
eh2 = Entry(win, font=myFont, justify=CENTER, width=w)
eh3 = Entry(win, font=myFont, justify=CENTER, width=w)
eh4 = Entry(win, font=myFont, justify=CENTER, width=w)
eh5 = Entry(win, font=myFont, justify=CENTER, width=w)
eh6 = Entry(win, font=myFont, justify=CENTER, width=w)
eh7 = Entry(win, font=myFont, justify=CENTER, width=w)
eh8 = Entry(win, font=myFont, justify=CENTER, width=w)
eh9 = Entry(win, font=myFont, justify=CENTER, width=w)
eh10 = Entry(win, font=myFont, justify=CENTER, width=w)
eh11 = Entry(win, font=myFont, justify=CENTER, width=w)
eh12 = Entry(win, font=myFont, justify=CENTER, width=w)
eh1, eh2, eh3, eh4, eh5, eh6, eh7, eh8, eh9, eh10, eh11, eh12.pack()
eh1.place(x=10, y=215)
eh2.place(x=50, y=215)
eh3.place(x=90, y=215)
eh4.place(x=130, y=215)
eh5.place(x=170, y=215)
eh6.place(x=210, y=215)
eh7.place(x=250, y=215)
eh8.place(x=290, y=215)
eh9.place(x=330, y=215)
eh10.place(x=370, y=215)
eh11.place(x=410, y=215)
eh12.place(x=450, y=215)

clear_button()

bea1 = Frame(board, bg='black', width=w_h, height=h_t)
bea2 = Frame(board, bg='black', width=w_h, height=h_t)
bea3 = Frame(board, bg='black', width=w_h, height=h_t)
bea4 = Frame(board, bg='black', width=w_h, height=h_t)
bea5 = Frame(board, bg='black', width=w_h, height=h_t)
bea6 = Frame(board, bg='black', width=w_h, height=h_t)
bea7 = Frame(board, bg='black', width=w_h, height=h_t)
bea8 = Frame(board, bg='black', width=w_h, height=h_t)
bea9 = Frame(board, bg='black', width=w_h, height=h_t)
bea10 = Frame(board, bg='black', width=w_h, height=h_t)
bea11 = Frame(board, bg='black', width=w_h, height=h_t)
bea12 = Frame(board, bg='black', width=w_h, height=h_t)
bea1, bea2, bea3, bea4, bea5, bea6, bea7, bea8, bea9, bea10, bea11, bea12.pack()
bea1.place(x=10, y=10)
bea2.place(x=42, y=10)
bea3.place(x=74, y=10)
bea4.place(x=106, y=10)
bea5.place(x=138, y=10)
bea6.place(x=170, y=10)
bea7.place(x=202, y=10)
bea8.place(x=234, y=10)
bea9.place(x=266, y=10)
bea10.place(x=298, y=10)
bea11.place(x=330, y=10)
bea12.place(x=362, y=10)

beb1 = Frame(board, bg='black', width=w_h, height=h_t)
beb2 = Frame(board, bg='black', width=w_h, height=h_t)
beb3 = Frame(board, bg='black', width=w_h, height=h_t)
beb4 = Frame(board, bg='black', width=w_h, height=h_t)
beb5 = Frame(board, bg='black', width=w_h, height=h_t)
beb6 = Frame(board, bg='black', width=w_h, height=h_t)
beb7 = Frame(board, bg='black', width=w_h, height=h_t)
beb8 = Frame(board, bg='black', width=w_h, height=h_t)
beb9 = Frame(board, bg='black', width=w_h, height=h_t)
beb10 = Frame(board, bg='black', width=w_h, height=h_t)
beb11 = Frame(board, bg='black', width=w_h, height=h_t)
beb12 = Frame(board, bg='black', width=w_h, height=h_t)
beb1, beb2, beb3, beb4, beb5, beb6, beb7, beb8, beb9, beb10, beb11, beb12.pack()
beb1.place(x=10, y=42)
beb2.place(x=42, y=42)
beb3.place(x=74, y=42)
beb4.place(x=106, y=42)
beb5.place(x=138, y=42)
beb6.place(x=170, y=42)
beb7.place(x=202, y=42)
beb8.place(x=234, y=42)
beb9.place(x=266, y=42)
beb10.place(x=298, y=42)
beb11.place(x=330, y=42)
beb12.place(x=362, y=42)

bec1 = Frame(board, bg='black', width=w_h, height=h_t)
bec2 = Frame(board, bg='black', width=w_h, height=h_t)
bec3 = Frame(board, bg='black', width=w_h, height=h_t)
bec4 = Frame(board, bg='black', width=w_h, height=h_t)
bec5 = Frame(board, bg='black', width=w_h, height=h_t)
bec6 = Frame(board, bg='black', width=w_h, height=h_t)
bec7 = Frame(board, bg='black', width=w_h, height=h_t)
bec8 = Frame(board, bg='black', width=w_h, height=h_t)
bec9 = Frame(board, bg='black', width=w_h, height=h_t)
bec10 = Frame(board, bg='black', width=w_h, height=h_t)
bec11 = Frame(board, bg='black', width=w_h, height=h_t)
bec12 = Frame(board, bg='black', width=w_h, height=h_t)
bec1, bec2, bec3, bec4, bec5, bec6, bec7, bec8, bec9, bec10, bec11, bec12.pack()
bec1.place(x=10, y=74)
bec2.place(x=42, y=74)
bec3.place(x=74, y=74)
bec4.place(x=106, y=74)
bec5.place(x=138, y=74)
bec6.place(x=170, y=74)
bec7.place(x=202, y=74)
bec8.place(x=234, y=74)
bec9.place(x=266, y=74)
bec10.place(x=298, y=74)
bec11.place(x=330, y=74)
bec12.place(x=362, y=74)

bed1 = Frame(board, bg='black', width=w_h, height=h_t)
bed2 = Frame(board, bg='black', width=w_h, height=h_t)
bed3 = Frame(board, bg='black', width=w_h, height=h_t)
bed4 = Frame(board, bg='black', width=w_h, height=h_t)
bed5 = Frame(board, bg='black', width=w_h, height=h_t)
bed6 = Frame(board, bg='black', width=w_h, height=h_t)
bed7 = Frame(board, bg='black', width=w_h, height=h_t)
bed8 = Frame(board, bg='black', width=w_h, height=h_t)
bed9 = Frame(board, bg='black', width=w_h, height=h_t)
bed10 = Frame(board, bg='black', width=w_h, height=h_t)
bed11 = Frame(board, bg='black', width=w_h, height=h_t)
bed12 = Frame(board, bg='black', width=w_h, height=h_t)
bed1, bed2, bed3, bed4, bed5, bed6, bed7, bed8, bed9, bed10, bed11, bed12.pack()
bed1.place(x=10, y=106)
bed2.place(x=42, y=106)
bed3.place(x=74, y=106)
bed4.place(x=106, y=106)
bed5.place(x=138, y=106)
bed6.place(x=170, y=106)
bed7.place(x=202, y=106)
bed8.place(x=234, y=106)
bed9.place(x=266, y=106)
bed10.place(x=298, y=106)
bed11.place(x=330, y=106)
bed12.place(x=362, y=106)

bee1 = Frame(board, bg='black', width=w_h, height=h_t)
bee2 = Frame(board, bg='black', width=w_h, height=h_t)
bee3 = Frame(board, bg='black', width=w_h, height=h_t)
bee4 = Frame(board, bg='black', width=w_h, height=h_t)
bee5 = Frame(board, bg='black', width=w_h, height=h_t)
bee6 = Frame(board, bg='black', width=w_h, height=h_t)
bee7 = Frame(board, bg='black', width=w_h, height=h_t)
bee8 = Frame(board, bg='black', width=w_h, height=h_t)
bee9 = Frame(board, bg='black', width=w_h, height=h_t)
bee10 = Frame(board, bg='black', width=w_h, height=h_t)
bee11 = Frame(board, bg='black', width=w_h, height=h_t)
bee12 = Frame(board, bg='black', width=w_h, height=h_t)
bee1, bee2, bee3, bee4, bea5, bee6, bee7, bee8, bee9, bee10, bee11, bee12.pack()
bee1.place(x=10, y=138)
bee2.place(x=42, y=138)
bee3.place(x=74, y=138)
bee4.place(x=106, y=138)
bee5.place(x=138, y=138)
bee6.place(x=170, y=138)
bee7.place(x=202, y=138)
bee8.place(x=234, y=138)
bee9.place(x=266, y=138)
bee10.place(x=298, y=138)
bee11.place(x=330, y=138)
bee12.place(x=362, y=138)

bef1 = Frame(board, bg='black', width=w_h, height=h_t)
bef2 = Frame(board, bg='black', width=w_h, height=h_t)
bef3 = Frame(board, bg='black', width=w_h, height=h_t)
bef4 = Frame(board, bg='black', width=w_h, height=h_t)
bef5 = Frame(board, bg='black', width=w_h, height=h_t)
bef6 = Frame(board, bg='black', width=w_h, height=h_t)
bef7 = Frame(board, bg='black', width=w_h, height=h_t)
bef8 = Frame(board, bg='black', width=w_h, height=h_t)
bef9 = Frame(board, bg='black', width=w_h, height=h_t)
bef10 = Frame(board, bg='black', width=w_h, height=h_t)
bef11 = Frame(board, bg='black', width=w_h, height=h_t)
bef12 = Frame(board, bg='black', width=w_h, height=h_t)
bef1, bef2, bef3, bef4, bef5, bef6, bef7, bef8, bef9, bef10, bef11, bef12.pack()
bef1.place(x=10, y=170)
bef2.place(x=42, y=170)
bef3.place(x=74, y=170)
bef4.place(x=106, y=170)
bef5.place(x=138, y=170)
bef6.place(x=170, y=170)
bef7.place(x=202, y=170)
bef8.place(x=234, y=170)
bef9.place(x=266, y=170)
bef10.place(x=298, y=170)
bef11.place(x=330, y=170)
bef12.place(x=362, y=170)

beg1 = Frame(board, bg='black', width=w_h, height=h_t)
beg2 = Frame(board, bg='black', width=w_h, height=h_t)
beg3 = Frame(board, bg='black', width=w_h, height=h_t)
beg4 = Frame(board, bg='black', width=w_h, height=h_t)
beg5 = Frame(board, bg='black', width=w_h, height=h_t)
beg6 = Frame(board, bg='black', width=w_h, height=h_t)
beg7 = Frame(board, bg='black', width=w_h, height=h_t)
beg8 = Frame(board, bg='black', width=w_h, height=h_t)
beg9 = Frame(board, bg='black', width=w_h, height=h_t)
beg10 = Frame(board, bg='black', width=w_h, height=h_t)
beg11 = Frame(board, bg='black', width=w_h, height=h_t)
beg12 = Frame(board, bg='black', width=w_h, height=h_t)
beg1, beg2, beg3, beg4, beg5, beg6, beg7, beg8, beg9, beg10, beg11, beg12.pack()
beg1.place(x=10, y=202)
beg2.place(x=42, y=202)
beg3.place(x=74, y=202)
beg4.place(x=106, y=202)
beg5.place(x=138, y=202)
beg6.place(x=170, y=202)
beg7.place(x=202, y=202)
beg8.place(x=234, y=202)
beg9.place(x=266, y=202)
beg10.place(x=298, y=202)
beg11.place(x=330, y=202)
beg12.place(x=362, y=202)

beh1 = Frame(board, bg='black', width=w_h, height=h_t)
beh2 = Frame(board, bg='black', width=w_h, height=h_t)
beh3 = Frame(board, bg='black', width=w_h, height=h_t)
beh4 = Frame(board, bg='black', width=w_h, height=h_t)
beh5 = Frame(board, bg='black', width=w_h, height=h_t)
beh6 = Frame(board, bg='black', width=w_h, height=h_t)
beh7 = Frame(board, bg='black', width=w_h, height=h_t)
beh8 = Frame(board, bg='black', width=w_h, height=h_t)
beh9 = Frame(board, bg='black', width=w_h, height=h_t)
beh10 = Frame(board, bg='black', width=w_h, height=h_t)
beh11 = Frame(board, bg='black', width=w_h, height=h_t)
beh12 = Frame(board, bg='black', width=w_h, height=h_t)
beh1, beh2, beh3, beh4, beh5, beh6, beh7, beh8, beh9, beh10, beh11, beh12.pack()
beh1.place(x=10, y=234)
beh2.place(x=42, y=234)
beh3.place(x=74, y=234)
beh4.place(x=106, y=234)
beh5.place(x=138, y=234)
beh6.place(x=170, y=234)
beh7.place(x=202, y=234)
beh8.place(x=234, y=234)
beh9.place(x=266, y=234)
beh10.place(x=298, y=234)
beh11.place(x=330, y=234)
beh12.place(x=362, y=234)

win.mainloop()
board.mainloop()
