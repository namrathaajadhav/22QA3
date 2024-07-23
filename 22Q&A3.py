#Python program to insert an element at end of an Array.
numbers = [1,3,5]
numbers.insert(10,50.0)
print(numbers)


#Python program to insert element at a given location in Array.

numbers = [1,3,5]
numbers.insert(1,2)
numbers.insert(1,4)
print(numbers)



#Write a python program  to check the sizes of given two list are same.

list1 =["green"], ["red"], ["blue"]
list2 = ["green"], ["red"], ["blue"]
list3 = list1[:]
result1 = "are_list_identical"(list1,list2)
result2 = "are_list_identical"(list1,list3)


#Python program to create a list. (all posible ways)


numbers = [1,2,3,4]
new_list = numbers * 8
print(new_list)

a = [1,2,3,4]
b = [5,6,7]
c = [8,9,10]
combination = [*a, *b,*c]
print(combination)


#Python program to access a given element from the nested list ? 
list1 = ['a', 'b','c','d',['apple','blue'],['300','500','800']]
print(list1[4][1][2])
print(list1[-1])

firstlist = [[1,2]], [[3,4]], [[5,6]]
print(firstlist[1][0])


#Write a python program to find largest and smallest  number in an list.
list - [1,2,3,4,5]
large = 0 
small = list[0]
for i in list:
    if i > large:
        large = i     
    elif i <small:
        samll = 1
        print("large:{}, samll: {}".format(large,samll))


#Write a python program  to find  sum of list elements ?
llist = [1,2,3,4,5,65,55,70]
sum = 0
for i in list:
    sum = sum+i
    print("sum of list is:",sum)

#Python program to find heighest frequency elemnt in list.

numbers = [1,2,3,3,4,3,4,1]
frequancy_element = max(set(numbers), key = numbers.count)
print(frequancy_element)

#Python program to reverse an list in two ways ?

list = [1,2,3,4,5,65,55,70]
list.reverse()
print(list)

value = list[::-1]
print(value)
