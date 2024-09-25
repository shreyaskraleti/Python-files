# # 1. Given a list of strings representing the days of the week, write a 
# function that returns a sublist containing only the weekdays (Monday 
# to Friday).
list1 = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
def weekdays():
    for i in range(7):
        if list1[i[0]] != "s":
            return list1.append(i)
        else:
        print("these days are weekend")
res = weekdays(list1)
print(res)''