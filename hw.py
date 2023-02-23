#### QUESTION 1 ####
#Given an array of positive integers nums, return a list of all of the negative integers.
Ex. 1
nums = [1, 3, 5, 7, 8]
Expected Output: [-1, -3, -5, -7, -8]

Ex. 2
nums = [100, 534, 32, 15, 77, 222, 788, 345, 75645, 22]
Expected Output: [-100, -534, -32, -15, -77, -222, -788, -345, -75645, -22]

### ANSWER ###
nums = [1, 3, 5, 7, 8]
def num_list(nums):
    negative_list = []
    for num in nums:
        negative = num-num-num
        negative_list.append(negative)
    return negative_list
        
        
num_list([1, 3, 5, 7, 8])
num_list([100, 534, 32, 15, 77, 222, 788, 345, 75645, 22])

#### QUESTION 2 ####
#Given a string, return a list of all of the digits in the string.
#Ex. 2
#sentence = "My phone number is (555) 555-4321"
#Expected Output: ['5', '5', '5', '5', '5', '5', '4', '3', '2', '1']

### ANSWER ###


#### QUESTION 3 ####
# Given a string digits, return a string of the digits + 1

# Ex. 1
# digits = '123'
# Expected Output: '124'

# Ex. 2
# digits = '99'
# Expected Output: '100'

### ANSWER ###
x = '123'
ex = int(x)
ex += 1

print(ex)
answer = str(ex)


print(answer)
print(type(answer))

x = '99'
ex = int(x)
ex += 1

print(ex)
answer = str(ex)


print(answer)
print(type(answer))