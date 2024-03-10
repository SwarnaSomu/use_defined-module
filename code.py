import program
# print even or odd program
a=int(input())
print(program.oe(a))
print()

#print random guessing random number
guessing_nbr=int(input())
print(program.random(a))
print()

#print palindrome number
nbr=int(input())
print(program.palindrome(nbr))
print()

#print armstrong number
number=int(input())
print(program.armstrong(number))
print()

#print leap_year
year=int(input())
print(program.leap_year(year))
print()

#checking difficulty of a word
word=input()
print(program.consonants(word))
print()

#checking anagram or not
b=input()
a=input()
print(program.anagram(a,b))
print()

#printing pattern
n=int(input())
program.pattern(n)
