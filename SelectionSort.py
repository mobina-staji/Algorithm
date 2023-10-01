#!/usr/bin/python3

#Selection sort program using python


n1=int(input('how many numbers are in your list?'))
num_list= []
for i in range (n1):
    min1=i
    number=int(input('enter the number:'))
    num_list.append(number)
    
len_list=len(num_list)
for j in range(len_list):
    min2=j
    for x in range (j+1 , len_list):
        if num_list[min2]>num_list[x]:
            min2=x
    num_list[j] , num_list[min2] = num_list[min2] , num_list[j]


print(num_list)



