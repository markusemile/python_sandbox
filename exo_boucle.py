# We will display the names of 10 users with a loop.
a = range(10)
for i in a:
    print(f"user {i}")

print("\n")

# Show a word upside down
w = "bonjour"
w = reversed(w)
for i in w:
    print(i[::-1], end='')

print("\n")
# Fix the error in the loop
mot = "Python"
for i in range(len(mot)):
    print(i, end='')

print("\n")
# Show the multiplication table for a number
nb = 0
while nb <= 0:
    nb = int(input("Enter a whole number: "))
    if nb <= 0:
        print("Please enter a whole number!")

print(f"Multiplication table of {nb}")
for i in range(1, 11):
    print(f"{i}*{nb}={i*nb}")

print("\n")
evens = []
# evens = [str(i) for i in range(1,103,2)]
for i in range(102):
    if i % 2 == 0:
        evens.append(str(i))
joined_evens = '-'.join(evens)
print(f"Here are the first 100 even numbers\n{joined_evens}")