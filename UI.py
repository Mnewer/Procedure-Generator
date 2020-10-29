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
logo = PhotoImage(file = "logo.png")
logoimage = Label(image = logo)
logoimage.place(x = 175, y = 150, width = 400, height = 249)

label_file_explorer = Label(root,
                            text = 'Find template:',
                            width = 100,
                            height = 2,
                            fg = "blue")

btn_explore = Button(root,
                        text = "Browse templates",
                        command = browseFiles)

btn_exit = Button(root,
                     text = "Exit",
                     command = exit)


#Placing of widgets:
label_file_explorer.grid(column = 1, row = 1)

btn_explore.grid(column = 1, row = 2)

btn_exit.grid(column = 1, row = 3)







root.mainloop()