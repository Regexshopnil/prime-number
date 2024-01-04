# Python program that generates prime numbers within a specified range.

min_value = int(input ("Please enter the min value: "))  
max_value = int(input ("Please enter the max value: "))  
  
print("Prime Numbers in the given range: ")  
for num in range (min_value, max_value + 1):  
    if num > 1:  
        for i in range (2, num):  
            if(num % i) == 0:  
                break  
        else:  
            print(num) 
