import pandas as pd
cars = pd.read_csv("cars.csv")
print("List of cars and their description:")
print(cars)
#Odd columns
print(" ")
odd = cars.iloc[[0,1,2,3,4],[1,3,5,7,9]]
print("First five odd-numbered columns of cars:")
print(odd)
#Mazda
print(" ")
Mazda = cars.loc[cars['Model'] == 'Mazda RX4']
print("For model Mazda RX4:")
print(Mazda)
#Camaro
print(" ")
Camaro = cars.loc[cars['Model'] == 'Camaro Z28', ['Model','cyl']]
print("Number of cylinders of Camaro Z28:")
print(Camaro)
#Cylinders and Gear Type
print(" ")
CG = cars.loc[[1,28,18],['Model','cyl','gear']]
print("Number of cylinders and gear type of Mazda RX$4 Wag, Ford Pantera L, and Honda Civic:")
print(CG)