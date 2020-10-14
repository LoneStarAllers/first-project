def reverse(s):
    ns = ''
    for i in s:
        ns = i + ns
    return ns

s = 'parham'
print(reverse(s))

#################################

def vowels_counter(s):
    sound = "aAeEiIoOuU"
    count = 0
    for i in s:
        if i in sound:
            count += 1
    
    return "There is/are {} vowel chars in \n{}".format(count,s)

s = input("Input a string : ")
print(vowels_counter(s))

#################################

def Everyone(*args):
    List = []
    for i in args:
        List.append(i)
    
    return List

Persons = Everyone('Parham', 'Amin', 'Amir', 'Roohollah', 'Omid', 'nafiseh', 'Mohammadreza', 'Aryan')
for person in Persons:
    print("Hello " + person)

#################################

def histogram(items):
    for n in items:
        output = ''
        times = n
        while times > 0:
            output += '*'
            times -= 1
        print(output)
histogram([3,6,4,3,6,5])

#################################

def ages(**kwargs):
    return kwargs

Dic = ages(Nick=31, Chris=27, Alicia=32, Maddison=55, Travis=57)
for person, age in Dic.items():
    print("{} is {} years old".format(person, age))

#################################

def repeat(n,m):
    count = 0
    while n > 0:
        if n % 10 == m:
            count += 1
        n //= 10
    return count

n = int(input("Enter n : "))
m = int(input("Enter m : "))
print("{} has repeated {} times in {}".format(m,repeat(n,m),n))

#################################

def fact(n):
    f = 1
    # for i in range(1,n+1): if we want to go from 1 to n
    for i in range(n,1,-1):
        f *= i
    return f

print(fact(int(input("Enter a number : "))))

#################################

def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

n = int(input("Enter n : "))
print("Result is : ")
for i in range(1,n+1):
    print(fibo(i),end=' ')

#################################

def midlle_item(*args):

    return args[len(args) // 2]

print(midlle_item('red', 'green', 'blue', 'purpel', 'yellow'))

#################################

def degree_to_radian(degree):
    pi = 22/7
    radian = degree * (pi / 180)

    return "Radian equivalent to the degree {} is {}".format(degree,radian)

degree = float(input("Input a degree : "))
print(degree_to_radian(degree))
