from vue import Application
from model import Model

class Controller() :
    """To interact between vue.py and model.py"""
    def __init__(self):
        """method to init"""
        self.model = Model("a.txt")
        self.model.read_file()
        self.view = Application(self)
        self.view.view_window()

    def display(self, value):
        """method to display an individual on the window"""
        self.view.display_label(self.model.dico_animaux[value])

    def add_animal(self, dict_animal):
        """method to add or modify an individual"""
        existing_animals= self.model.get_name() #to retrieve and store
        # the individual's names that are in file
        # to verifiy if the name that the user
        # has written in the entry box is already in file
        if dict_animal["name"] not in existing_animals:
            self.model.save_animal(dict_animal)
            self.view.message_add()
        if dict_animal["name"] in existing_animals:
            self.model.modify_animal(dict_animal)
            self.view.message_modified()

    def get_model_entries(self):
        """method to return the list of attributes"""
        return self.model.get_attributes()

    def get_model_name(self):
        """method to return the list of individual's names that are in file"""
        return self.model.get_name()

    def remove_model_animal(self,delete_name):
        """method to give to model.py the name of individual to delete"""
        self.model.delete_animal(delete_name)

    def quit_window(self):
        """method to quit the window"""
        print("close app")
        self.model.close()
        self.view.destroy()

if __name__ == "__main__" :
    C = Controller()


