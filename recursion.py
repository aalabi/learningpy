# add up natural numbers up to n 

def recur_sum(n):
    """Function to get the summmation of natural numbers up to n"""
    if n <= 1 :
        return n
    else:
        return n + recur_sum(n-1)

def checkN(n):
    checkedN = False
    if n >= 1:
        checkedN = n
    return checkedN

print("This program sums up all natural number from 1 to the number supplied")
print("")

num = int(input("Enter a positive number "))

while not checkN(num):
    num = int(input("Enter a positive number "))
    
print("The sum is ", recur_sum(num))


