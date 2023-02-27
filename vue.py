from tkinter import *
from tkinter import messagebox

class Application(Tk):
    """We create our window with all its components"""
    def __init__(self, controller):
        """method to inititate view"""
        Tk.__init__(self)
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.namelist = self.controller.get_model_name()
        self.creer_widgets()

    def creer_widgets(self):
        """method to inititate widgets"""
        self.label = Label(self, text="Individual information: ")
        self.label1 = Label(self, text="")
        self.label_search = Label(self, text="Recherche")
        self.bouton_display = Button(self, text="Afficher", command=self.display_something)
        self.bouton_quit = Button(self, text="Quitter", command=self.quit_window)
        self.bouton_add_animal = Button(self, text="Add/modify", command=self.add_animal)
        self.bouton_remove=Button(self,text="Remove", command=self.remove_animal)

        self.search = Entry(self)
        self.entries = {}
        self.entries_label = {}
        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)

        self.listbox=Listbox(self)
        counter_name= 0
        for name in self.namelist:
            counter_name += 1
            self.listbox.insert(counter_name, name)

        self.label.pack()
        self.label1.pack()
        self.label_search.pack()
        self.search.pack()
        self.bouton_display.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.bouton_quit.pack()
        self.bouton_add_animal.pack()
        self.bouton_remove.pack()
        self.listbox.pack()

    def quit_window(self):
        """method to quit our window"""
        self.controller.quit_window()

    def display_something(self):
        """method to give individual to the controller"""
        self.controller.display(self.search.get())

    def display_label(self, value):
        """"method to display given individual and all its atrributes"""
        self.label1['text'] = value

    def add_animal(self):
        """method to add new individual with attributes
        that the user has written in entries box. Update
        the file and list box. """
        dict_animal = {}
        for key in self.entries:
            dict_animal[key] = self.entries[key].get() #to syncrhonize the dictionnary with user input
            #(key = attributes and value= text entry)
            self.entries[key].delete(0, END) #to delete text in entries
        self.controller.add_animal(dict_animal) #to give the dictionnary to controller
        self.listbox.delete(0,END) #to delete entire list box
        self.listbox.insert(0,*self.controller.get_model_name())#to add the list of names of actual individuals to list box

    def remove_animal(self):
        """method to remove selected individual in file and update list box"""
        delete_name= self.listbox.get(ACTIVE) #To get the active item (selected individual in list box)
        self.controller.remove_model_animal(delete_name) #To give the name to remove to controller
        # to remove the selected indvidual to listbox
        for i in range (0,self.listbox.size()):  # for each item in list box (item=name of individual)
            # retrieve the deleteted name in list box and remove it
            if self.listbox.get(i)== delete_name:
                self.listbox.delete(i)
        messagebox.showinfo("Announcement","Individual has been removed")

    def view_window(self):
        """method to show our window"""
        self.title("Ma Première App :-)")
        self.mainloop()

    def message_add(self):
        """method to display a message when an individual is added"""
        messagebox.showinfo("Adding animal", message="The animal has been added.")

    def message_modified(self):
        """method to display a message when an individual is modified"""
        messagebox.showinfo("Animal Modification", message="The animal has been modified.")

if __name__ == "__main__":
    app = Application()
    app.view_window()
