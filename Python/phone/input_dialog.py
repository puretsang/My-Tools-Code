from tkinter import *
import tkinter as tk
import sys
from tkinter import filedialog
from execute import execute_file

tk_root = tk.Tk()
e1 = Entry(tk_root, bd=1, bg='white', relief='solid')


def open_file():  # 是键的程序
    folder_root = tk.Tk()
    folder_root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=(('text files', 'txt'),))  # 获得选择好的文件
    e1.insert(0, file_path)
    execute_file(file_path)
    print('Filepath:', file_path)


def cancel():  # 否键的程序
    sys.exit()  # 因为否键没什么用，我们不管它，直接pass掉！


tk_root.title("号码魔方")  # 对话框标题
tk_root.geometry("800x400")
theLabel = Label(tk_root, text='     请把txt文件拖到输入框？', )
theLabel.pack()  # 对话框上面的说明文字


# E1.pack(anchor=CENTER)
e1.place(relx=0.5, rely=0.3, anchor=CENTER, width=400, height=120)

button1 = Button(text='选择文件', fg='white', command=open_file, bg='red')
button1.place(relx=0.5, rely=0.7, anchor=CENTER, width=180, height=50)

# button2 = Button(text='取消', command=cancel, bg='red', fg='white')
# button2.pack(ipadx=30, pady=10, side=LEFT)

tk_root.mainloop()
