from turtle import home


students = ['carl', 'john', 'jim', 'jelloo']
foods = ['cream', 'bread', 'flour', 'pizza']

for food in foods[2:]:
    print("{food} is a good food".format(food=food))

home_town = {
    "city":"marion",
    "state":"Iowa",
    "population":1000
}

print(f"i was born in {home_town['city']}, {home_town['state']} - popultion of {home_town['population']}")


for key in home_town:
    print(f"{key} = {home_town[key]} ")

cohort = []

for x in range(0,3):
    print(x)
    cohort[x] = {
        "student": "carl",
        "fav_food": "pizza"
    }

print(cohort)