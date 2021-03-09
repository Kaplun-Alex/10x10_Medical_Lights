import tkinter.font
from tkinter import *
from tkinter import filedialog as fd

board = Tk()

myFont = tkinter.font.Font(family='Hervetica', size=12, weight='bold')  # присвоюєм за замовченням стиль
smallFont = tkinter.font.Font(family='Hervetica', weight='bold', size=12)
largeFont = tkinter.font.Font(family='Hervetica', weight='bold', size=24)  # мій шрифт для малих кнопок
board.title("Diode Board")  # назва вікна
board.geometry('1024x600+0+0')
backgroundcolor = "#000"
foregroundColor = "#006400"
board.configure(background=backgroundcolor)
#board.overrideredirect(1)

w = 5
b = 5
w_h = 18
h_t = 18
li_o = []


def exitBoard():
    board.destroy()

def load_file():
    try:
        global li_o
        file_name = fd.askopenfilename()
        with open(file_name, 'r') as filehandle:
            for line in filehandle:
                currentplace = line[:-1]
                li_o.append(currentplace)
        print(li_o)
    except FileNotFoundError:
        print('No file dude')


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
    try:
        kw = run_entry.get()
        print(keyparam)
        print(kw)
        clear_field()
        if li_o[0] == kw:
            bea1.config(bg='white')
        if li_o[1] == kw:
            bea2.config(bg='white')
        if li_o[2] == kw:
            bea3.config(bg='white')
        if li_o[3] == kw:
            bea4.config(bg='white')
        if li_o[4] == kw:
            bea5.config(bg='white')
        if li_o[5] == kw:
            bea6.config(bg='white')
        if li_o[6] == kw:
            bea7.config(bg='white')
        if li_o[7] == kw:
            bea8.config(bg='white')
        if li_o[8] == kw:
            bea9.config(bg='white')
        if li_o[9] == kw:
            bea10.config(bg='white')
        if li_o[10] == kw:
            bea11.config(bg='white')
        if li_o[11] == kw:
            bea12.config(bg='white')
        if li_o[12] == kw:
            beb1.config(bg='white')
        if li_o[13] == kw:
            beb2.config(bg='white')
        if li_o[14] == kw:
            beb3.config(bg='white')
        if li_o[15] == kw:
            beb4.config(bg='white')
        if li_o[16] == kw:
            beb5.config(bg='white')
        if li_o[17] == kw:
            beb6.config(bg='white')
        if li_o[18] == kw:
            beb7.config(bg='white')
        if li_o[19] == kw:
            beb8.config(bg='white')
        if li_o[20] == kw:
            beb9.config(bg='white')
        if li_o[21] == kw:
            beb10.config(bg='white')
        if li_o[22] == kw:
            beb11.config(bg='white')
        if li_o[23] == kw:
            beb12.config(bg='white')
        if li_o[24] == kw:
            bec1.config(bg='white')
        if li_o[25] == kw:
            bec2.config(bg='white')
        if li_o[26] == kw:
            bec3.config(bg='white')
        if li_o[27] == kw:
            bec4.config(bg='white')
        if li_o[28] == kw:
            bec5.config(bg='white')
        if li_o[29] == kw:
            bec6.config(bg='white')
        if li_o[30] == kw:
            bec7.config(bg='white')
        if li_o[31] == kw:
            bec8.config(bg='white')
        if li_o[32] == kw:
            bec9.config(bg='white')
        if li_o[33] == kw:
            bec10.config(bg='white')
        if li_o[34] == kw:
            bec11.config(bg='white')
        if li_o[35] == kw:
            bec12.config(bg='white')
        if li_o[36] == kw:
            bed1.config(bg='white')
        if li_o[37] == kw:
            bed2.config(bg='white')
        if li_o[38] == kw:
            bed3.config(bg='white')
        if li_o[39] == kw:
            bed4.config(bg='white')
        if li_o[40] == kw:
            bed5.config(bg='white')
        if li_o[41] == kw:
            bed6.config(bg='white')
        if li_o[42] == kw:
            bed7.config(bg='white')
        if li_o[43] == kw:
            bed8.config(bg='white')
        if li_o[44] == kw:
            bed9.config(bg='white')
        if li_o[45] == kw:
            bed10.config(bg='white')
        if li_o[46] == kw:
            bed11.config(bg='white')
        if li_o[47] == kw:
            bed12.config(bg='white')
        if li_o[48] == kw:
            bee1.config(bg='white')
        if li_o[49] == kw:
            bee2.config(bg='white')
        if li_o[50] == kw:
            bee3.config(bg='white')
        if li_o[51] == kw:
            bee4.config(bg='white')
        if li_o[52] == kw:
            bee5.config(bg='white')
        if li_o[53] == kw:
            bee6.config(bg='white')
        if li_o[54] == kw:
            bee7.config(bg='white')
        if li_o[55] == kw:
            bee8.config(bg='white')
        if li_o[56] == kw:
            bee9.config(bg='white')
        if li_o[57] == kw:
            bee10.config(bg='white')
        if li_o[58] == kw:
            bee11.config(bg='white')
        if li_o[59] == kw:
            bee12.config(bg='white')
        if li_o[60] == kw:
            bef1.config(bg='white')
        if li_o[61] == kw:
            bef2.config(bg='white')
        if li_o[62] == kw:
            bef3.config(bg='white')
        if li_o[63] == kw:
            bef4.config(bg='white')
        if li_o[64] == kw:
            bef5.config(bg='white')
        if li_o[65] == kw:
            bef6.config(bg='white')
        if li_o[66] == kw:
            bef7.config(bg='white')
        if li_o[67] == kw:
            bef8.config(bg='white')
        if li_o[68] == kw:
            bef9.config(bg='white')
        if li_o[69] == kw:
            bef10.config(bg='white')
        if li_o[70] == kw:
            bef11.config(bg='white')
        if li_o[71] == kw:
            bef12.config(bg='white')
        if li_o[72] == kw:
            beg1.config(bg='white')
        if li_o[73] == kw:
            beg2.config(bg='white')
        if li_o[74] == kw:
            beg3.config(bg='white')
        if li_o[75] == kw:
            beg4.config(bg='white')
        if li_o[76] == kw:
            beg5.config(bg='white')
        if li_o[77] == kw:
            beg6.config(bg='white')
        if li_o[78] == kw:
            beg7.config(bg='white')
        if li_o[79] == kw:
            beg8.config(bg='white')
        if li_o[80] == kw:
            beg9.config(bg='white')
        if li_o[81] == kw:
            beg10.config(bg='white')
        if li_o[82] == kw:
            beg11.config(bg='white')
        if li_o[83] == kw:
            beg12.config(bg='white')
        if li_o[84] == kw:
            beh1.config(bg='white')
        if li_o[85] == kw:
            beh2.config(bg='white')
        if li_o[86] == kw:
            beh3.config(bg='white')
        if li_o[87] == kw:
            beh4.config(bg='white')
        if li_o[88] == kw:
            beh5.config(bg='white')
        if li_o[89] == kw:
            beh6.config(bg='white')
        if li_o[90] == kw:
            beh7.config(bg='white')
        if li_o[91] == kw:
            beh8.config(bg='white')
        if li_o[92] == kw:
            beh9.config(bg='white')
        if li_o[93] == kw:
            beh10.config(bg='white')
        if li_o[94] == kw:
            beh11.config(bg='white')
        if li_o[95] == kw:
            beh12.config(bg='white')
        run_entry.delete(0, END)
    except IndexError:
        print('Load File')
        run_entry.delete(0, END)
        load_file()


exit_Board_button = Button(board, text="EXIT", font=myFont, command=exitBoard, height=1, width=8)
exit_Board_button.pack()
exit_Board_button.place(x=650, y=450)

load_Button = Button(board, text="LOAD", font=myFont, command=load_file, height=1, width=8)
load_Button.pack()
load_Button.place(x=650, y=350)

run_entry = Entry(board, font=largeFont, justify=CENTER, width=10)
run_entry.pack()
run_entry.place(x=650, y=10)

board.bind("<Return>", keyboard_walue)
board.bind("0x40000", keyboard_walue)

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

board.mainloop()
