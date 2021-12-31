num = int(input("Enter a positive number to test: "))

while num < 1:
    num = int(input("Enter a positive number to test: "))
    
start = 2
step = 1
stop = num
stop += step

for i in range (start, stop, step):
    if num % i != 0:
        print("{} is NOT a divisor of {} ... continuing" .format(i, num))
    elif num % i == 0 and i != num:
        print("{} is a divisor of {} ... stopping" .format(i, num))     
        print("{} is not a prime number." .format(num))
        break
    elif i == num:
        print("{} is a prime number." .format(num))
