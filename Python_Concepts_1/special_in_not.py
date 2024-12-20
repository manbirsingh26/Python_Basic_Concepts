# in and not usage
a = ["Manbir", "Harleen", "Ribnam", "Ranjodh", "Avneet"]
b = input("Enter your name to check if it is in the selection list: ")
if b in a:
    print("Yes", b, " you are selected")
if b not in a:
    print("Sorry!!", b, " Please try next time")


