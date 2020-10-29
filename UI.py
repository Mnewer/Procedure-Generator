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
    
    label_file_explorer.configure(text = str("File opened: " + filename))

#splash screen:
splash_root = Tk()
splash_root.geometry("500x600")
splash_root_label = Label(splash_root, text = "Procedure Generator", font = "Helvetica",)
splash_root_label.pack(pady = 90)
splash_root.overrideredirect(True)
logo = PhotoImage(file = "logo.png")
logoimage = Label(image = logo)
logoimage.pack()

#root window:
def main_window():
    splash_root.destroy()
    root = Tk()
    root.title('Procedure Generator')
    root.geometry("500x600")

    label_file_explorer = Label(root,
                                text = 'Find template:',
                                width = 100,
                                height = 4,
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



#Splash screen timer:
splash_root.after(3000, main_window)




mainloop()