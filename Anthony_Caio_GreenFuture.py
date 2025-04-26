"""
author: Anthony Antczak and Caio Gentil Corado
date: 12/16/2024
CPT: Green Future
"""
from InquirerPy import prompt
import statistics

# MAX SEARCH
def max_search(haystack: list) -> int:
	"""Returns where the highest number of a list is
	>>> max_search([1,3,6,0])
	2
	>>> max_search([6,1,2,3,6])
	0
	"""
	max_index = 0
	for i in range(len(haystack)):
		if haystack[i] > haystack[max_index]:
			max_index = i
	return max_index

# SELECTION SORT
def selection_sort(lst: list) -> list:
	"""Sorts a list in ascending order
	>>> selection_sort([5,3,0])	
	[0,3,5]
	>>> selection_sort([0,3,5])
	[0,3,5]
	"""
	for i in range(len(lst)):
		min_index = i
		for j in range(i, len(lst)):
			if lst[j] < lst[min_index]:
				min_index = j
		lst[i], lst[min_index] = lst[min_index], lst[i]

# function to do prompts without 3 lines of code
def promptinput(message,choices):
    """Creates a prompt of choices"""
    user_input = [
        {
            "type": "list",
            "message": message,
            "choices": choices
        }
    ]
    return prompt(user_input)[0]

# function to input quiz questions
def get_input(prompt, limit):
    """An input that will refuse if any number is higher then the limit"""
    user_input = int(input(prompt))
    while not user_input < limit:
        user_input = int(input("Use a number from *0* to *10*: "))
    return user_input

# function to save data
def data_output(variable, name):
    """Saves a file"""
    variable = str(variable)
    with open("CPT\\data\\"+name, mode="a") as f_out:
        f_out.writelines(variable)
        f_out.write("\n")

def data_input_numbers(name, choice):
    """Input the data with the average and the mode"""
    with open("CPT\\data\\"+name, mode = "r") as f_in:
        user_input = f_in.read().splitlines()
        for i in range(len(user_input)):
             user_input[i] = int(user_input[i])
    selection_sort(user_input)
    avg = sum(user_input)/len(user_input)
    mode = statistics.mode(user_input)
    print(f"The average of {choice} is {avg} and the mode is {mode}.")


def data_input_string(name, choice):
    """input the data with the mode"""
    with open("CPT\\data\\"+name, mode = "r") as f_in:
        user_input = f_in.read().splitlines()
        mode = statistics.mode(user_input)
    print(f"The mode of {choice} is {mode}.")

# function to say that the user is doing good
def u_good(name, variable):
    """prints if the user is doing good"""
    if variable <=5:
        print(f"{name}: {variable} is very good, keep it like this or lower to minimize your carbon footprint"+"\n")
def main():
    #input / output
    #ask the user if company or person
    comp = promptinput("Company or Person?", ["Company", "Person"])
    print(comp)
    if comp == "Person":
        yes_no = str(input("Do you want to do the quiz?(y/n) "))
        while yes_no.lower().startswith("y"):
            name = str(input("What's your name? "))
            #quiz here
            print("==========================================================="+"\n"+"|Answer the following qustions based on a scale of 0 to 10|"+"\n"+"===========================================================")
            animal_based_products = get_input("How often do you use animal-based products? ",11)
            processed_food = get_input("How much of the food that you eat is not unprocessed, unpackaged or locally grown? ", 11)
            energy_consumption = get_input("How energy unefficient is your home? ",11)
            renewable_energy_usage = get_input("What percentage of your home's electricity doesn't come from renewable sources?(1 = 10% and 10 = 100%) ", 11)
            trash_generation = get_input("Compared to your neighbors, how much trash do you generate? ", 11)
            print("=============================================================================="+"\n"+"|Answer the following questions by chosing the option that most represent you|"+"\n"+"==============================================================================")
            # I GOT THIS IDEA FROM "Thierri - aulasdev" on tiktok
            housetype = promptinput("Which housing type best describes your home",["Freestanding, no running water", "Freestanding, running water", "Multi-storey apartment", "Duplex, row house or building with 2-4 housing units", "Luxury condominium"])
            mat = promptinput("What material is your house constructed with?",["Straw/Bamboo", "Wood", "Brick/Concrete", "Adobe", "Steel/Other"])
            elec = promptinput("Do you have electricity in your home?",["Yes", "No"])
            housesize = promptinput("What is the size of your home?",["Tiny(5m2/50sq ft)","Small(29m2/308sq ft)", "Medium(100m2/1081sq ft)", "Large(378m2/4071sq ft)", "Huge(+474m2/5102sq ft)"])
            print("=========================================="+"\n"+"|Answer the question with precise numbers|"+"\n"+"==========================================")
            people = int(input("How many people live in your household? "))

            # Saving Data
            # processing / output
            data_output(name, "name.txt")
            data_output(animal_based_products, "animal.txt")
            data_output(processed_food, "food.txt")
            data_output(energy_consumption, "energy.txt")
            data_output(renewable_energy_usage, "renew.txt")
            data_output(trash_generation, "trash.txt")
            data_output(housetype, "housetype.txt")
            data_output(mat, "mat.txt")
            data_output(elec, "elec.txt")
            data_output(housesize, "housesize.txt")
            data_output(people, "people.txt")

            # Giving tips on how to improve carbon emission

            u_good("Animal Based Products",animal_based_products)
            if animal_based_products > 5:
                print(f"Animal based products: {animal_based_products} try to lower this number, animal based products account for 57% of emissions"+"\n")
            u_good("Processed Foods",processed_food)
            if processed_food > 5:
                print(f"processed foods: {processed_food} try to lower this number, food processing accounts for a third of (GHG) greenhouse gasses"+"\n")
            u_good("Energy Consumption",energy_consumption)
            if energy_consumption > 5:
                print(f"energy consumption: {energy_consumption} try to lower this number, using a lot of electricity can create a lot of CO2 emissions"+"\n")
            u_good("Renewable Energy Usage",renewable_energy_usage)
            if renewable_energy_usage > 5:
                print(f"renewable energy usage: {renewable_energy_usage} try to lower this number, the production and consumption of renewable energy causes CO2 emissions"+"\n")
            u_good("Trash Generation", trash_generation)
            if trash_generation > 5:
                print(f"trash generation: {trash_generation} try to lower this number, trash accounts for 10%-15% of (GHG) greenhouse gasses and kills clean drinking water or marine animals"+"\n")
            #quiz again?
            
            yes_no = str(input("Do you want to do the quiz again? "))
        
    # processing / output
    if comp == "Company":
        # Company Questions
        compname = str(input("What is your company name? "))
        what = promptinput("What data are you looking for?",["Food", "Electricity", "Housing"])
        # Processing data(avg, max, min, median, and everything)
        if what == "Food": 
            data_input_numbers("food.txt", "animal-based products")
            data_input_numbers("trash.txt", "trash generation")
        if what == "Electricity":
            data_input_numbers("renew.txt", "renewable energy")
            data_input_numbers("energy.txt", "energy efficiency")
            data_input_string("elec.txt", "energy in home")
        if what == "Housing":
            data_input_numbers("people.txt", "people in a household")
            data_input_string("housesize.txt", "house size")
            data_input_string("mat.txt", "materials")
            data_input_string("housetype.txt", "house type")
            with open("CPT\\data\\"+"people.txt", mode ="r") as family_in:
                family = family_in.read().splitlines()
                for i in range(len(family)):
                    family[i] = int(family[i])
                maximus = family[max_search(family)]
            print(f"The household with the highest amout of people is {maximus}")


if __name__ == "__main__":
    main()


# if not cmp[0] == p and not cmp[0] == c