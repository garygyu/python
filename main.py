from classes.ingredients import ingredients
from classes.recipes import recipes
from classes.inventory import inventory

def main():

    i = Ingredient(title = "egg")

    r = Recipe(title = "Scrambled eggs", ingredients = [i],
               directions = ['Break egg', 'Beat egg', 'Stir egg'])

    r.print_recipe()

    if __name__ == "__main__":
        main()

print("Completed!!")
