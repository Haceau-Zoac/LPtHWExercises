numbers = []

def rang(numbers, end, step):
    i = 0
    while i < end:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step
        print("Numbers Now: ", numbers)
        print(f"At the bottom i is {i}")


rang(numbers, 6, 1)
print("The numbers: ")

for num in numbers:
    print(num)