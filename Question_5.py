### 5. Write a Python program to swap two variables without temp variable?
##### Sol.

#taking input from user
var1=int(input("Enter first number : "))
var2=int(input("Enter second number : "))

print('Before swap:\nvar1 = {} and var2 = {}'.format(var1, var2))

#we are moving value of var1 and var2
external1=var1
external2=var2

#replace value of var1 and var2
var1=external2
var2=external1
print('\nAfter swap:\nvar1 = {} and var2 = {}'.format(var1, var2))


#############################################
#########ANSWER##########################
#            Enter first number : 4
#            Enter second number : 6
#            Before swap:
#            var1 = 4 and var2 = 6
#
#            After swap:
#            var1 = 6 and var2 = 4