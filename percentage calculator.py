print("Enter the marks you have obtained in the following subjects:")

maths=int(input("The marks obtained in mathematics: "))
science=int(input("The marks obtained in science: "))
eng=int(input("The marks obtained in english: "))
health=int(input("The marks obtained in Health: "))

sum = maths + science + eng + health

total_percentage= (sum/400)*100

print(f"Total percentage: {total_percentage}")