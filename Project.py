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

