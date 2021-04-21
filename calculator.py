print("This progress is to calculate the BMI of an individual\n")
name = raw_input("Enter your name: ")
weight = input("Enter your weight in pounds: ")
height1 = input("Enter your height in feet: ")
height2 = input("Enter your height in inches: ")
height = float(height1 * 12.0 + height2)
weight = weight * 0.45
height = height * 0.025
print(height)
print(weight)

bmi = weight / (height ** height)
print(height)
print(weight)
print(bmi)

if bmi < 18.5:
    print(name + ' is underweight')

if 18.5 <= bmi <= 24.9:
    print(name + ' is normal weight')

if 25 <= bmi <= 29.9:
    print(name + ' is overweight')

if bmi > 30:
    print(name + 'is obese')
