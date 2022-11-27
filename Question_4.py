### 4. Write a Python program to solve quadratic equation?
##### Sol.

#=> This program computes roots of a quadratic equation when coefficients a, b and c are known.
#in this code , we use cmath that is complex math and it is advance version of math
import cmath

#This is quadratic equation
print("This is quadratic equation : ")
print("ax^2 + bx^1 + c = 0")

a=int(input("Enter coefficient of a : "))
b=int(input("Enter coefficient of b : "))
c=int(input("Enter constant value of c : "))

#The quadratic equation is :
print("The quadratic equation is :","{}*x^2 + {}*x + {} =0" .format(a,b,c))
#Formula to compute quadratic equation
# d=(-b*1) +/- (cmath.sqrt(b**2-4ac))/2a

dis=(b**2)-(4*a*c)
sqrt_dis=cmath.sqrt(dis)
print("value of total_dis is :=> ",sqrt_dis)

#There are two values came, one is positive and another is negative so solution1 and solution2 are 
solution1=((-b**2)+(sqrt_dis))/2*a
print("The positive factor is :=> ",solution1)

solution2=((-b**2)-(sqrt_dis))/2*a
print("The negative factor is :=>  ",solution2)

print("#####################################")
print('The solution are {} and {}'.format(solution1,solution2))
#########################################################
###################ANSWER###########################
#                This is quadratic equation :
#                ax^2 + bx^1 + c = 0
#                Enter coefficient of a : 12
#                Enter coefficient of b : 45
#                Enter constant value of c : 79
#                The quadratic equation is : 12*x^2 + 45*x + 79 =0
#                value of total_dis is :=>  42.035699113967404j
#                The positive factor is :=>  (-12150+252.2141946838044j)
#                The negative factor is :=>   (-12150-252.2141946838044j)
#                #####################################
#                The solution are (-12150+252.2141946838044j) and (-12150-252.2141946838044j)