'''
1. Create 1st tuple with values -> (10, 20, 30), 2nd tuple with values -> (40,
50, 60):
a. Concatenate the two tuples and store it in “t_combine”
b. Repeat the elements of “t_combine” 3 times
c. Access the 3rd element from “t_combine”
d. Access the first three elements from “t_combine”
e. Access the last three elements from “t_combine
'''

tuple1 = tuple()
tuple2 = tuple()

tuple1 = (10, 20, 30)
tuple2 = (30, 40, 50)

t_combine = tuple1 + tuple2

print(t_combine[2])
print(t_combine[:3])
print(t_combine[len(t_combine)-3:])