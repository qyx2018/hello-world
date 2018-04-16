import tkinter

root = tkinter.Tk()

hello = tkinter.Label(root, text = 'Hello World!')
hello.pack()

quit = tkinter.Button(root, text = 'QUIT', command = root.quit, bg = 'red', fg = 'white')
quit.pack(fill = tkinter.X, expand = 1)

tkinter.mainloop()
