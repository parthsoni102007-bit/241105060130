print("Population Growth Tracker")
population = int(input("Enter initial population: "))
rate = int(input("Enter growth rate: "))
years = int(input("Enter years: "))
i = 1
while i <= years:
increase = population * rate / 100
population = population + increase
if population > 1000000:
print("Overpopulated")
else:
print("Normal population")
i = i + 1
print("Final population:", population
if population < 0:
print("Invalid data")
else:
print("Data valid")
