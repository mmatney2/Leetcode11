


def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


n = [2,7,11,15, 20]
t=9
print(twosum(n, t))

def twosum(nums, target):
    dict = {}
    # print(values)
    for i, x in enumerate(nums):
       #v, k              nums = iterable
        if target - x in dict:
            return [dict[target-x], i]
            
        else:
            dict[x] = i #how we write the value from the dict[key] = value
            #dict[key]  = value
            print(dict)
t=35
a = [2,7,11,15, 20]

print(twosum(a, t))

for index in range(len(values)):
    value = values[index]
    print(index, value)

index = 0
for value in values:
   print(index, value)
   index += 1

def myName(name):
    values = {}
    for i, x in enumerate(name):
        if x in values:
            return [values[x], i]
        else:
            values[x] = i
        print(values)
print(myName('marquita'))

def myName2(name):
    values={}
    for i, x in enumerate(name):
        if x not in values:
            values[x] = [i]
            print(values)
            # return values
        else:
            values[x].append(i)
            return values
    

print(myName2('marquita'))

def interviewQ(name):
    dict = {}
    for i, letter in enumerate(name):
        if letter not in dict:
            dict[letter] = [i]
            #dict[key] = [value]
            # print(dict)
        else:
            dict[letter].append(i)
            #dict[key] append (value)
            return dict
print(interviewQ('marquita'))