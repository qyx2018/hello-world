from functools import partial as pto
from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
	'do not enter': CRIT,
	'railroad crossing': WARN,
	'55\nspeed limit': REGU,
	'wrong way': CRIT,
	'merging traffic': WARN,
	'one way': REGU,
}

critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

root = Tk()
root.title('Road Signs')
Button(root, text = 'QUIT', command = root.quit, bg = 'red', fg = 'white').pack()

MyButton = pto(Button, root)
CritButton = pto(MyButton, command = critCB, bg = 'white', fg = 'red')
WarnButton = pto(MyButton, command = warnCB, bg = 'goldenrod')
ReguButton = pto(MyButton, command = infoCB, bg = 'white')

for eachSign in SIGNS:
	signType = SIGNS[eachSign]
	cmd = '%sButton(text = %r%s).pack(fill = X, expand = True)' %(signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')
	eval(cmd)
	
root.mainloop()
