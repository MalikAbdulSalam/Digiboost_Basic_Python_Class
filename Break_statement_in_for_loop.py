#################################################### Break Statement ######################
# we want to get values of only first 5 indexes
thislist = ["apple", "banana", "cherry","apple_2", "banana_2", "cherry_1","apple_3", "banana_3", "cherry_2","apple_4", "banana_4", "cherry_4","apple_5", "banana_5", "cherry_5"]
print(thislist[0])
print(thislist[1])
print(thislist[2])
print(thislist[3])
print(thislist[4])


print("######################################################")

for x in thislist:
    print("Value of currect index is ", x)
    if x == "banana_2":
        print("Banana_2 found successfully")
        break
print("Our loop ended")
