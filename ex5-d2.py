name = "Haceau"
age = 114514
height = 1919
height_cm = height * 2.54
weight = 810
weight_kg = weight * 0.45359
eyes = "brown"
teeth = "rainbow"
hair = "blue"

print(f"Let's talk about {name}.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
