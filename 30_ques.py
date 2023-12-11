# 19. A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased. The program should read three integers: the number of students in each of the three 
# classes, a, b and c respectively.
# Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

import math

class_a = int(input("Enter Number of Students in class A : "))
class_b = int(input("Enter Number of Students in class B :"))
class_c = int(input("Enter Number of Students in class C :"))


a_desk = class_a//2
b_desk = class_b//2
c_desk = class_c//2
r_a_desk = a_desk % 2
r_b_desk = b_desk % 2
r_c_desk = c_desk % 2




# print(f"The lowest required Bench in Class A is { math.ceil(a_desk)}")
# print(f"The lowest required Bench in Class B is { math.ceil(b_desk)}")
# print(f"The lowest required Bench in Class C is { math.ceil(c_desk)}")


