# Find the average age of the patients.     DONE
# Where are the majority of indivduals from.     DONE
# Costs of smokers vs. non-smokers.     DONE
# Average age of people with at least one child.  DONE   
# Average charges (cost).     DONE
# Average BMI.     DONE

import csv
#age[0],sex[1],bmi[2],children[3],smoker[4],region[5],charges[6]
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []
with open("insurance.csv") as insurance:     # Getting all the data separated.
    entries = csv.DictReader(insurance)
    for entry in entries:
        age.append(entry["age"])
        sex.append(entry["sex"])
        bmi.append(entry["bmi"])
        children.append(entry["children"])
        smoker.append(entry["smoker"])
        region.append(entry["region"])
        charges.append(entry["charges"])

def get_average(data_list):     # Gets the average for the input list.
    data_total = 0
    for data in data_list:
        data_total += float(data)
    return data_total / len(data_list)

def all_averages(age, bmi, children, charges):     # This will print out all of the numerical averages.
    print("The average age is: " + str(get_average(age)))
    print("The average BMI is: " + str(get_average(bmi)))
    print("The average number of children is: " + str(get_average(children)))
    print("The average charges are: $" + str(get_average(charges)))

all_averages(age, bmi, children, charges)     # This will be live.

smoker_and_charges = list(zip(smoker, charges))

# for i in range(len(smoker_and_charges)):     # This is how to iterate through the list!
#     total_charges = 0
#     total_charges += float(smoker_and_charges[i][1])
# print(str(total_charges))

def smoker_vs_non(smoker_and_charges):
    smoker = 0
    smoker_charge = 0
    non = 0
    non_charge = 0
    for smokes in smoker_and_charges:
        if "yes" in smokes:
            smoker += 1
            smoker_charge += float(smokes[1])
        else:
            non += 1
            non_charge += float(smokes[1])
    average_smoker_cost = smoker_charge / smoker
    average_non_smoker_cost = non_charge / non
    print("The total number of smokers is: " + str(smoker))
    print("The total number of non-smokers is : " + str(non))
    print("The total charges for smokers is: $" + str(smoker_charge))
    print("The total charges for non-smokers is: $" + str(non_charge))
    print("This means that the average charges for a smoker is ${}, while the average charges for a non-smoker is ${}.".format(average_smoker_cost, average_non_smoker_cost))

smoker_vs_non(smoker_and_charges)     # This will be live.

# areas = []     # This tells me what the different regions are.
# for reg in region:
#     if reg in areas:
#         continue
#     else:
#         areas.append(reg)
# print(areas)

def majority_region(region):     # Needs a cleaner way to determine which area has the most people, and what happens in a tie.
    southwest = 0
    southeast = 0
    northwest = 0
    northeast = 0
    for reg in region:
        if reg == "southwest":
            southwest += 1
        elif reg == "southeast":
            southeast += 1
        elif reg == "northwest":
            northwest += 1
        else:
            northeast += 1
    if southwest > southeast and southwest > northwest and southwest > northeast:
        print("Most people reside in the southwest.")
    elif southeast > southwest and southeast > northwest and southeast > northeast:
        print("Most people reside in the southeast.")
    elif northwest > southwest and northwest > southeast and northwest > northeast:
        print("Most people reside in the northwest.")
    elif northeast > southwest and northeast > southeast and northeast > northwest:
        print("Most people reside in the northeast.")
    else:
        print("People are spread out pretty evenly among a few regions.")

majority_region(region)     # This will be live.

children_and_age = list(zip(children, age))

def average_age_with_children(children_and_age):     # This calculates the average age of folks with kids.
    total_age = 0
    number_with_kids = 0
    for kids in children_and_age:
        if int(kids[0]) > 0:
            number_with_kids += 1
            total_age += float(kids[1])
    avg_age_with_kids = total_age / number_with_kids
    print("The average age for an individual with at least one child is: " + str(avg_age_with_kids))

average_age_with_children(children_and_age)     # This will be live.