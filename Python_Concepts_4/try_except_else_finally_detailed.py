"""
# We can define as many exceptions as we want
try:
    print(x)
except NameError:
    print(f"Name not defined")
except:
    print(f"An error occurred")
# Here if we don't use except then NameError will be raised, so instead of that we just put a message

"""
# Simple Example

try:
    a = float(input("Enter first number:-"))
    b = float(input("Enter second number:-"))
    c = float(input("Enter third number:-"))

except Exception as e:
    print(f"OOPS!!! Error:{e}")

else:
    avg = float((a+b+c)/3)
    #avg_1 = round(avg, 3)
    #print(f"Average of entered three numbers is:{avg_1}")
    print(f"Average of entered three numbers is:{avg:.3f}") #This is another way to display intended no of decimals only

finally:
    print(f"Thank you! Have a nice day")









