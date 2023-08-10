# list=["a","b","c"]
# sec_lst= [0]*5
# combined = list+sec_lst
# print(combined)
# abc= list(range(20))
# print(abc)
# char=list("Hello ankush")
# print(char)


# set=list(range(20))
# print(set[::2])

# list=["a","b","c","d","e"]
# first,second,third,*other = list
# print(first,second,other)
# for letter in enumerate(list):
#     print(letter)

# list.append("f")
# list.insert(0,"_")
# list.pop(2)
# list.remove("b")
# del list[0:3]
# list.clear()
# print(list)
# print(list.index("b"))
# print(list.count("c"))
# letters=[23,45,34,12,56]
# # letters.sort(reverse=True)
# print(sorted(letters))
# print(letters)


# items=[
#     ("product1",9),
#     ("product2",12),
#     ("product3",10),
# ]
# # lst=[]
# # items.sort(key=lambda item:item[1])
# # print(items)
# # for item in items:
# #     lst.append(item[1])
# # print(lst)
# lst=list(map(lambda item:item[1] ,items))
# print(lst)

prices=[
    ("product1", 10),
    ("product2", 14),
    ("product3", 8),
]
filtered = list(filter(lambda price: price[1] >= 10, prices))
print(filtered)



# array
# from array import array
# number = array("i",[1,2,3,])
# number.append(4)
# print(number)

# set
# number=[1,2,3,1]
# first= set(number)
# second={1,2,3,4,5,6}
# print(first|second)

# dic

# point=dict(x=1,y=2)
# point["z"]=3
# print(point["y"])
# # print(point)
# print(point.get("a",5))
# del point["x"]
# print(point)
# for i in point.items():
#     print(i)
#


# unpacking operator
# point= range(5)
#
# print(*point)

# list=[1,7,3,4,5]
# max=list[0]
# for lst in list:
#     if lst>max:
#         max=lst
# print(max)