cars = 100  #total number of cars
space_in_a_car = 4.0      #4 persons can sit
drivers = 30  #total number of available drivers
passengers = 90   #Number of passengers
cars_not_driven = cars - drivers  #Subtracting available drivers from total number of cras gives the number of cars which are not driven
cars_driven = drivers # Cars which are driven by drivers
carpool_capacity = cars_driven * space_in_a_car #Total number of  available space to sit in a car
average_passengers_per_car = passengers / cars_driven #Number of passengers to sit in a car excluded drivers
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
"in each car.")