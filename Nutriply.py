import time


# class Success():
    # def __init__(self, food):
        # self.food = food





scrambled_eggs = ["eggs", "oil"]
scrambled_eggs_andtoast = ["eggs", "oil", "bread"]
fettucini_alfredo = ["alfredo sauce", "fettucini", "chicken"]
spaghetti_marinara = ["marinara sauce", "spaghetti"]
chicken_curry = ["curry sauce", "chicken", "rice"]
grilled_cheese = ["cheese", "bread"]
BLT = ["bread", "bacon", "lettuce", "tomato"]
bacon_n_eggs = ["bacon", "oil", "eggs"]
salad = ["lettuce", "tomato"]
cheeseburger = ["buns", "hamburger patties", "cheese", "tomato", "lettuce", "pickles"]

ingredient_list = ["eggs", "oil", "bread", "alfredo sauce", "fettucini", "chicken", "marinara sauce", "spaghetti", "curry sauce", "rice", "cheese", "bacon", "lettuce", "tomato", "buns", "hamburger patties", "pickles"]
recipe_list = ["scrambled eggs", "scrambled eggs and toast", "fettucini alfredo", "spaghetti with marinara", "chicken curry", "grilled cheese", "BLT", "eggs and bacon", "salad", "cheeseburger"]





def find_meal(y):
    result = all(elem in y for elem in scrambled_eggs)
    if result:
        print("Scrambled Eggs")
        success1 = True
    else:
        success1 = False
    result1 = all(elem in y for elem in scrambled_eggs_andtoast)
    if result1:
        print("Scrambled Eggs and Toast")
        success2 = True
    else:
        success2 = False
    result2 = all(elem in y for elem in fettucini_alfredo)
    if result2:
        print("Fettucini Alfredo")
        success3 = True
    else:
        success3 = False
    result3 = all(elem in y for elem in spaghetti_marinara)
    if result3:
        print("Spaghetti with marinara sauce")
        success4 = True
    else:
        success4 = False
    result4 = all(elem in y for elem in chicken_curry)
    if result4:
        print("Chicken Curry")
        success5 = True
    else:
        success5 = False
    result5 = all(elem in y for elem in grilled_cheese)
    if result5:
        print("grilled cheese")
        success6 = True
    else:
        success6 = False
    result6 = all(elem in y for elem in BLT)
    if result6:
        print("BLT")
        success7 = True
    else:
        success7 = False
    result7 = all(elem in y for elem in bacon_n_eggs)
    if result7:
        print("Eggs with bacon")
        success8 = True
    else:
        success8 = False
    result8 = all(elem in y for elem in salad)
    if result8:
        print("Salad")
        success9 = True
    else:
        success9 = False
    result9 = all(elem in y for elem in cheeseburger)
    if result9:
        print ("cheeseburger")
        success10 = True
    else:
        success10 = False
    if success1 == False and success2 == False and success3 == False and success4 == False and success5 == False and success6 == False and success7 == False and success8 == False and success9 == False and success10 == False:
        print(f"sorry {r}, nothing can be done with those ingredients! However...")
        print(" ")
        print(f"Only {set(scrambled_eggs).difference(y)} is needed to make scrambed eggs")
        print(" ")
        print(f"Only {set(fettucini_alfredo).difference(y)} is needed to make Fettucini Alfredo")
        print(" ")
        print(f"Only {set(spaghetti_marinara).difference(y)} is needed to make spaghetti with marinara")
        print(" ")
        print(f"Only {set(chicken_curry).difference(y)} is needed to make chicken curry")
        print(" ")
        print(f"Only {set(grilled_cheese).difference(y)} is needed to make grilled cheese")
        print(" ")
        print(f"Only {set(BLT).difference(y)} is needed to make a BLT")
        print(" ")   
        print(f"Only {set(bacon_n_eggs).difference(y)} is needed to make eggs with bacon")
        print(" ")
        print(f"Only {set(salad).difference(y)} is needed to make a salad")
        print(" ")
        print(f"Only {set(cheeseburger).difference(y)} is needed to make a cheeseburger") 

def greeting_message(r):
    active = True
    time.sleep(1)
    x = input(f"{r}, what ingredients do you have on hand? Print them separated by a comma (no spaces please!)")
    if x == "ingredient list":
        print(ingredient_list)
        greeting_message(r)
    elif x == "recipe list":
        print(recipe_list)
        greeting_message(r)
    else:
        y = x.split(',')
        find_meal(y)
        active = False

print("Welcome to Nutriply! Let's get you fed ASAP")
time.sleep(1)
r = str(input("what is your name?"))
greeting_message(r)








