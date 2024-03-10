# print even or odd program
def  oe(a):
    if a%2==0:
        return 'evennumber'
    else:
        return 'oddnumber'
    
#print random guessing random number
def random(guessing_nbr):
    n=0
    secret_nbr=79
    no_of_tries=3
    while(n<=no_of_tries):
        if guessing_nbr==secret_nbr:
            return "hurray! u have got it"
            
        
        elif guessing_nbr < secret_nbr:
            
            return 'u guessed lower nbr,try again'
            
        elif guessing_nbr > secret_nbr:
            return 'u guessed greater nbr,try again'
        guessing_nbr=int(input("enter u guess:"))
        n+=1
    
    return 'u reached max limit'

#print palindrome number
def palindrome(nbr):
    reversed=0
    while nbr>0:
        rem=nbr%10
        reversed=reversed*10+rem
        nbr=nbr//10
    if nbr==reversed:
       return  True
    else:
        return False


#print armstrong number
def armstrong(number):
     temp = number
     nums_digits=0
     while temp > 0:
        temp //= 10
        nums_digits+= 1
     temp=number
     sum_of_powers = 0
     while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** nums_digits
        temp //= 10
     return sum_of_powers == number




#print leap_year
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


#checking difficulty of a word
def consonants(word):
    word.lower()
    vowels=['a','e','i','o','u']
    c=0
    for i in word:
        for j in range(len(vowels)):
           if i!=vowels[j]:
                c+=1
    if c>5:
        return "difficult to sound"
    else:
        return "easy to sound"

#checking anagram or not
def anagram(a,b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)
















    