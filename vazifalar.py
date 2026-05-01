import os
os.system("cls")

# 1.m
# def nol(list):
#     list2 = []
#     list3 = []
#     for i in list:
#         if i ==0:
#             list2.append(i)
#         if i !=0:
#             list3.append(i)
#     print(list3+list2)
# print(nol(list([3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1])))


# 2.m
# def func(list1):
#     list2 = []
#     for i in list1: 
#         if list1.count(i)<=2 and i not in list2:
#             list2.append(i)
#     return list2
# list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# a = func(list1)
# print(a)



# 3.m
# def qosh(list1,list2):
#     list3 = []
#     min_len = min(len(list1),len(list2))
#     for i in range(min_len):
#         list3.append(list1[i])
#         list3.append(list2[i])
#     if len(list1) > len(list2):
#         for i in range(min_len,len(list1)):
#             list3.append(list1[i])
#     else:
#         for i in range(min_len,len(list2)):
#             list3.append(list2[i])
#     return list3
# list1 = [1,2,3,4]
# list2 = [1,2,3,4,5]
# print(qosh(list1,list2))


# 4.m
# def birlashtir(a,b):
#     new = []
#     for i in a:
#         if i in b and i not in new:
#             new.append(i)
#     return new
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(birlashtir(a,b))


# 5.m
# def qosh(a):
#     list1 = []
#     list2 = []
#     for i in range(a):
#         s = int(input(f"{i+1} - sonni kriting: "))
#         list1.append(s)
#     print(list1)
#     for i in list1:
#         if list1.count(i) >= 2 and i not in list2:
#             list2.append(i)
#     return list2

# a = int(input("Listga qancha ma'lumot kritasz: "))
# natija = qosh(a)
# print(natija)


# 6.m
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = list(map(lambda n: n*n , list1))
# print(list2)


# 7.m
# def sana(matn):
#     dict1 = {}
#     for i in matn:
#        dict1[i] = matn.count(i)
#     return dict1
# matn = 'w3resource'
# print(sana(matn)) 






