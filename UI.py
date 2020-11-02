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

#Project or serial number input:
project_serial_var = ()

def input_serial_project_number():
    project_serial = numeber.get()
    print("Serial or project number is: " + project_serial)
    project_serial_var.set("")    

#splash screen:
splash_root = Tk()
splash_root.geometry("500x600+500+100")
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
    root.geometry("500x600+500+100")

    label_file_explorer = Label(root,
                          text = 'Find template:',
                          width = 100,
                          height = 4,
                          fg = "black")

    btn_explore = Button(root,
                  text = "Browse templates",
                  command = browseFiles)

    btn_exit = Button(root,
               text = "Exit",
               command = exit)
    
    project_srnr_label = Label(root,
                         text = 'Input project/serial number:')
    project_serial_entry = Entry(root,
                           textvariable = project_serial_var)
    enter_btn = Button(root,
                       text = 'Enter',
                       command = project_serial_entry)


#Placing of widgets::
    label_file_explorer.pack()
    
    btn_explore.pack()
    btn_exit.pack()
    project_srnr_label.pack()
    project_serial_entry.pack()
    enter_btn.pack()

#Splash screen timer:
splash_root.after(1000, main_window)




mainloop()