# import collections

#userList = [{1:["testUser1","user@email.com","userpassword"]},{1:["testUser2","user@email.com","userpassword"]}]

# businessList=[{1:[1,'new business','new location','new category','describing the business']},{2:[1,'new business','new location','new category','describing the business']}]


# new =[]
# for x in userList:
#     for u in x.values():
#         new.append(u[0])
#         if 'testUser1' not in new:
#             print('not in')
#         else:
#             print('in')

# print(new)
# oldlist=[]
# newlist=[]
# for bus in businessList:
#     for key, value in bus.items():
#         if key == 2:
#             oldlist.append([x for x in  value])
#             for index, value in enumerate():
#                 if index == 0:
#                     value[0] = 21
#                 if index == 1:
#                     value[1] = 'louis'
#                 if index == 2:
#                     value[2] = 'louis'
#                 for k in businessList:
#                     for key, val in k.items():
#                         if key == 2:
#                             newlist.append([x for x in  value])

                    

# if oldlist[0] == newlist[0]:
#     print('yes')

# print(businessList)

# x= [{1:['cheq','musanje', 'michael']},{2:['louis','mike', 'stevo']}]

# x[1] = ['mike','louis']
##############################################
# oldlist=[]
# newlist=[]
# for xt in x:
#     for key, val in xt.items():
#         if key == 2:
#             oldlist.append([x for x in val])
#             xt[key]=['xxxxxxxxxx']
#             newlist.append([x for x in xt[key]])
#             if oldlist[0] == newlist[0] and oldlist[1] == newlist[1]:
#                 print('they are similar')
#             else:
#                 print('not the same')

# print(x)
#############################################

# ls=[]
# leng = len(ls)
# ls.append('louis')

# if len(ls) > leng:
#     print('appended')

# businessList=[{1:[1,'new business','new location','new category','describing the business']},{2:[100,'new business','new location','new category','describing the business']}]

# foundrows=[]
# for x in businessList:
#     for val in x.values():
#         if val[0] == 1:
#             foundrows.append(x)

# print(foundrows)

##################################################

reviewList = [{1:[1, 1, 1,'louis', 'this is the review that we are looking for']},{2:[1, 1, 1, 'michael', 'this is the test review , its not real']}]

busid = 1

foundreviews = []
for x in reviewList:
    for y in x.values():
        if y[2] == 1:
            foundreviews.append(y)

print(foundreviews)