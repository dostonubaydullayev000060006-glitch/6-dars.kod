import os
os.system("cls")

# 1.m
# def func1(a):
#     list1 = []
#     for i in a:
#         if i>0:
#             list1.append(i)
#     return list1

# list1 = func1([1, -1, 2, 9, -3, -11, 20, 5, -8, 4])
# print(list1)

# 2.m
# def func2(dict1):
#     for i,j in dict1.items():
#         dict1[i] = j.upper()
#     return dict1

# dict1 = {
#     "Ism": "Ali",
# 	"Familya": "Kamolov",
# 	"Manzil": "Angren shahri"
# }
# b = func2(dict1)
# print(b)


# 3.m
# def func3(list1,list2):
#     dict1 = {}
#     for i in range(4):
#         dict1[list1[i]]=list2[i]
#     return dict1
    
# list1=["Jon", "Jeyms", "Piter", "Tony"]
# list2=["Vik", "Bond", "Parker", "Stark"]
# s = func3(list1,list2)
# print(s)


# 4.m
# def juft_yigindi(tpl):
#     if not tpl: 
#         return 0
    
#     if tpl[0] % 2 == 0:
#         return tpl[0] + juft_yigindi(tpl[1:])
#     else:
#         return juft_yigindi(tpl[1:])

# t = (2, 3, 5, 6, 3, 7, 8, 4)
# print(juft_yigindi(t))


