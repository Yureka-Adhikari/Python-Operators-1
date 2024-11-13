amount = int(input("Enter the amount you would like to withdraw: "))

notes_of_100= amount//100
notes_of_50= (amount%100)//50
notes_of_10= ((amount%100)%50)//10

print(f"Notes of 100: {notes_of_100}")
print(f"Notes of 50: {notes_of_50}")
print(f"Notes of 10: {notes_of_10}")