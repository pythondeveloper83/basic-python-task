# create a function to sum 2 value , return the result
x = int(input('inter the x value : '))
y = int(input('inter the y value : '))


def summation(x, y):
    result = x + y
    return result

z =summation (x, y)
print(z)

# 	write a function that multiplies any count of numbers

def multiplication (x,y):
    mul=x*y
    return mul

f=multiplication(x,y)
print(f)

# example to show the map function
# map function deploy the function one by one on the required list
def add_one (number):
    return number +1
nums = map (add_one, [1, 2, 3 ,4, 5])
print(list(nums))   # convert the map into a list, for readability

# example to show the zip function
# zip function used with dictionary to assign first is the key and second is the value
g=list(zip([1, 2, 3], 'abc'))
print(g)

# example to show the filter function
values = filter(None,[1, 2, 'ABC', 0, None, '', 4])
print(list(values))

# example to show the range function
s=dict(zip("abc", range(5)))
print(s)

h=list(range(1, 5, 2))  # range ( start , stop , take 2 step between start and stop )
print(h)

n=list (range(0,8))
print(n)

