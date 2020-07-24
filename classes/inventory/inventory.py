class Inventory(object):

    def __init__(self, items={}):
        self.items = items

    def add(self, item):
        if self.items.haskey(item):
            self.items[item] += 1
        else:
            self.items[item] = 1

    def remove(self, item):
        if self.items.haskey(item):
            if items[item] < 1:
                print ("Can not go negative, sorry")
            else:
                self.items[item] -= 1
        else:
            print ("No such an item in the inventory, sorry")

    def check(self, item):
        if self.items.haskey(item):
            return True
        else:
            return False

    def print_inventory(self):
        for item in self.items.keys():
            print (item + " - " + self.items[item])
