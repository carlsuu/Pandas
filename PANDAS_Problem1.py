import pandas as pd
cars = pd.read_csv("cars.csv")
print ("List of cars and their descriptions:")
print(cars)
#first5
first = cars[0:5]
print("The first five cars are:")
print(first)
#last5
last = cars[27:32]
print("The last five cars are:")
print(last)