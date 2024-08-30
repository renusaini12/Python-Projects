from tkinter import*
root = Tk()
root.title('Menubar')
root.geometry("600x600")


Textarea = Text(root,font='arial 15')
Textarea.pack(expand = True,fill=BOTH)


menubar=Menu(root)

filemenu=Menu(menubar,tearoff=0)

filemenu.add_command(label='new')
filemenu.add_command(label='open')
filemenu.add_separator()
filemenu.add_command(label='save')
menubar.add_cascade(label='file',menu=filemenu)

editmenu=Menu(menubar,tearoff=0)

editmenu.add_command(label='Undo')
editmenu.add_command(label='Redo')
editmenu.add_separator()
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_separator()
editmenu.add_command(label='Paste')
menubar.add_cascade(label='Edit',menu=editmenu)

searchmenu=Menu(menubar,tearoff=0)

searchmenu.add_command(label='Find text')
searchmenu.add_command(label='Find next')
searchmenu.add_separator()
searchmenu.add_command(label='Find previous')
searchmenu.add_command(label='Replace text')
searchmenu.add_separator()
searchmenu.add_command(label='Go to line')
menubar.add_cascade(label='search',menu=searchmenu)

sourcemenu=Menu(menubar,tearoff=0)

sourcemenu.add_command(label='show blank spaces')
sourcemenu.add_command(label='scroll past the end')
sourcemenu.add_separator()
sourcemenu.add_command(label='show indent guides')
sourcemenu.add_command(label='show code folding')
sourcemenu.add_separator()
sourcemenu.add_command(label='show code style warnings')
menubar.add_cascade(label='Source',menu=sourcemenu)

runmenu=Menu(menubar,tearoff=0)

runmenu.add_command(label='Run')
runmenu.add_separator()
runmenu.add_command(label='Run cell')
runmenu.add_separator()
runmenu.add_command(label='Run cell and advance')
runmenu.add_separator()
runmenu.add_command(label='Re-Run last cell')
menubar.add_cascade(label='Run',menu=runmenu)

debugmenu=Menu(menubar,tearoff=0)

debugmenu.add_command(label='Debug cell')
debugmenu.add_separator()
debugmenu.add_command(label='Step')
debugmenu.add_command(label='Step into')
debugmenu.add_separator()
debugmenu.add_command(label='Step Return')
debugmenu.add_separator()
debugmenu.add_command(label='Continue')
debugmenu.add_command(label='Stop')
menubar.add_cascade(label='Debug',menu=debugmenu)

consolesmenu=Menu(menubar,tearoff=0)

consolesmenu.add_command(label='New console')
consolesmenu.add_separator()
consolesmenu.add_command(label='New special console')
consolesmenu.add_separator()
consolesmenu.add_command(label='Restart kernel')
consolesmenu.add_separator()
consolesmenu.add_command(label='Remove all variables')
menubar.add_cascade(label='Consoles',menu=consolesmenu)

projectsmenu=Menu(menubar,tearoff=0)

projectsmenu.add_command(label='New project')
projectsmenu.add_separator()
projectsmenu.add_command(label='Open project')
projectsmenu.add_command(label='Close project')
projectsmenu.add_command(label='Delete project')
projectsmenu.add_separator()
projectsmenu.add_command(label='Recent project')
menubar.add_cascade(label='Projects',menu=projectsmenu)

toolsmenu=Menu(menubar,tearoff=0)

toolsmenu.add_command(label='Perferances')
toolsmenu.add_command(label='PYTHONPATH manager')
toolsmenu.add_command(label='current user environment variabels')
toolsmenu.add_separator()
toolsmenu.add_command(label='Reset spyder to factory defaults')
menubar.add_cascade(label='Tools',menu=toolsmenu)

viewmenu=Menu(menubar,tearoff=0)

viewmenu.add_command(label='Panes')
viewmenu.add_command(label='Lock panes and toolbars')
viewmenu.add_separator()
viewmenu.add_command(label='Toolbars')
viewmenu.add_command(label='Hide toolbars')
viewmenu.add_command(label='Window layouts')
viewmenu.add_separator()
viewmenu.add_command(label='Use previous layout')
viewmenu.add_command(label='Use next layout')
menubar.add_cascade(label='View',menu=viewmenu)

helpmenu=Menu(menubar,tearoff=0)

helpmenu.add_command(label='Spyder documentations')
helpmenu.add_command(label='Spyder tutorial')
helpmenu.add_separator()
helpmenu.add_command(label='Shortcuts summary')
helpmenu.add_command(label='Interactive tours')
helpmenu.add_separator()
helpmenu.add_command(label='Troubleshooting')
menubar.add_cascade(label='Help',menu=helpmenu)


root.config(menu=menubar)

scroll =Scrollbar(Textarea)
scroll.pack(side =RIGHT,fill=Y)
scroll.config(command=Textarea.yview)
Textarea.config(yscrollcommand=scroll.set)

root.mainloop()