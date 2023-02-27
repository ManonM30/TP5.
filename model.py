# encoding : utf8
"""model, used to write in the file a.txt """
from Animal import Animal

class Model():
    """To save an individual in file and give it to the controller"""
    def __init__(self, filename):
        """method to init"""
        self.filename = filename
        self.file=open(self.filename, "r+")
        self.dico_animaux = {}

    def read_file(self):
        """method to read the file and create
        a dictionnary where the individual's names are the key"""
        for line in self.file:
            line = line.strip()
            tab = line.split(",")
            a = Animal(tab[0],tab[1],tab[2],tab[3],tab[4])
            self.dico_animaux[a.name] = a

    def save_good_format(self):
        """method to save the file without empty line.
         Empty line appears when we modify once individual.
         The modified individual is placed after the empty line in file.
         In this case, if you modify it again (twice or more),
         the modified individual's name not in list
         and in the controller.add_animal function,
         the choice is save_animal and not modify_animal.
         At the end, we have twice the same individual"""
        with open(self.filename, "r+") as good_file:
            text_file = good_file.read() #read the file
            text_file = text_file.strip() #to remove spaces at the beginning or at the end
            list_text_file = text_file.split("\n") #become a list,
            #an item= a line= individual (all attributes)
            length = int()
            # if the item is empty, remove it of the list
            for i in list_text_file:
                length = len(i)
                if length == 0:
                    position = list_text_file.index(i)
                    del list_text_file[position]
            # go back to being a text
            list_text_file = "\n".join(list_text_file)
            good_file.seek(0) #to change the position
            # of the File Handle at the beginning of the file
            good_file.write(list_text_file) #to write the obtained text in file
            good_file.truncate()
            good_file.close() # to save file without closing the app

    def save_animal(self, dict_animal):
        """method to save an individual in file.
        Is used in the case of a new individual is added !"""
        self.file = open(self.filename, "a+")
        self.read_file()
        self.file.write("\n"+dict_animal["species"]+","
                        +dict_animal["age"]+","+dict_animal["diet"]
                        +","+dict_animal["foot"]+","+dict_animal["name"])
        self.file.close()
        self.file = open(self.filename, "a+")
        self.save_good_format()
        self.file.seek(0)
        self.read_file() #to update dico_animaux used in get_name() function
     #that is used by controller.add_animal to obtain
     #the list of individual's names that are in file


    def modify_animal(self,dict_animal):
        """method to save an individual in file with its modifications"""
        #remove indivual's name to dictionnary which use to write in file
        self.delete_animal(dict_animal["name"])
        self.file = open(self.filename, "a+")
        self.read_file()
        self.file.write("\n"+dict_animal["species"] + ","
                        + dict_animal["age"] + "," + dict_animal["diet"]
                        + "," + dict_animal["foot"] + "," + dict_animal["name"])
        self.file.seek(0)
        self.save_good_format()
        self.read_file() #to update dico_animaux used in get_name() function
        self.file.close()

    def close(self):
        """method to close the file """
        self.file.close()

    def get_attributes(self)->[]:
        "method to retrieve attribute's label"
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

    def get_name(self):
        "method to retrieve and store the individual's names that are in file"
        list_name= []
        for key in self.dico_animaux: #the keys of dico_animaux is individual's names
            list_name.append(key)
        return list_name


    def delete_animal(self,delete_name):
        """method to delete an individual"""
        #to delete in dictionnary
        for key in self.dico_animaux:
            if key == delete_name:
                del self.dico_animaux[key]
                break
        #to delete in file
        self.file=open(self.filename,"r+")
        # to return a list containing each line in the file as a list item
        lines = self.file.readlines()
        self.file.truncate(0)
        self.file.seek(0)
        for line in lines: #for each item in list
            # each line become a list where each item is attribute's value
            line_content = line.strip().split(",")
            if line_content[-1]!=delete_name: #the last item is individual's name
                self.file.write(line) #only write the line without the deleted individu name
        self.file.close()

if __name__ == "__main__" :
    model = Model("a.txt")
    model.read_file()
    model.close()
    model.save_good_format()
