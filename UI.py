from tkinter import *
from tkinter import filedialog


#File explorer window:
def browseFiles():
    filename = filedialog.askopenfilenames(initialdir = "/",
    title = "Select template",
    filetypes = ((".docx files", "*.docx*"),
                (".pdf files", "*.pdf*"),
                (".txt files", "*.txt*"),
                ("all files", "*.*")))
    
    label_file_explorer.configure(text = 'File opened: ' + filename)


#root window:
root = Tk()

#root window attributes:
root.title('Procedure Generator')
root.geometry("700x500")
root.config(background = "white")

label_file_explorer = Label(root,
                            text = 'Find template:',
                            width = 100,
                            height = 2,
                            fg = "blue")

button_explore = Button(root,
                        text = "Browse templates",
                        command = browseFiles)

button_exit = Button(root,
                     text = "Exit",
                     command = exit)


#Placing of widgets:
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1, row = 3)







root.mainloop()