# str="my name is python"
# res=""
# for chr in str:
#     if chr!=" ":
#         res=chr+res
# rev=""
# count=0
# for chr in str:
#     if chr!="":
#        rev=rev+res[count]
#        count+=1
#     else:
#         rev=rev+''
# print(rev)
# n=4
# i=1
# while i<=n:
#     print('* '*n)
    # i+=1
# 
# n=7
# i=1
# while i<=n:
#     print('* '*n*2)
#     i+=1
## n=7
# i=1
# while i<=n:
#     print('* '*i)
#     i+=1
# n=10
# i=1
# while i<=n:
#    print('* '*i)
# n=4
# for i in range(1,n+1):
#    if i==1 or i==n:
#       print('* '*n)
#    else:
#        print('* '+"  " *(n-2)+'* ')
#     n=4
# for i in range(1,n+1):
#   if i==1 or i==n:
#       print('* '*n*2)
#   else:
#       print('* '+"  " *(n+2)+'*')
# 
# n=7 
# m=3
# for i in range(m,n+1):
#     print(i)
          
# n=5
# for i in range(n,-1,-1):
#     print(i)
# n=10
# m=6
# for i in range(n,m-1,-1):
#     print(i)
# n=4
# m=2
# sum=1
# for i in range(m,n+1):
#     sum=sum*i
# print(sum)
# n=6
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+i
# print(c)
# n=6
# for i in range(1,n+1):
#     if n%i==0:
#        print(i)
# n=10
# m=3
# for num in range(m,n+1):
#     if num%2!=0:
#        print(num)
# for i in range(1,100):
#     f=0
#     for j in range(1,i+1):
#         if i%j==0:
#            f=f+1
#     if f==2:
#         print(j)
# c=0
# for i in range(1,100):
#     f=0
#     for j in range(1,i+1):
#         if i%j==0:
#            f=f+1
#     if f==2:
#         c=c+1
# print(c)
# n=153
# temp=n
# s=0
# while n<0:
#     r=r%10
#     s=s+r**3
#     n//=10
# if temp==s:
#     print('temp')
# n=1
# m=100
# for i in range(n,m+1):w
#     if i%2!=0:
#         continue  
#     else:
#         print(i)
# n=5
# f=0
# for i in range(1,n):
#     if n%i==0:
#         f=f+1
# if f==1:
#     print('prime')
# else:
#     print('not')
# for n in range(1,500):
#     l=len(str(n))
#     temp=n
#     sum=0
#     while n>0:
#         r=n%10
#         res=r**l
#         sum=sum+res
#         n//=10
#     if temp==sum:
#         print(temp)
# remove space from fiven text
# str='he llo wor ld'
# for chr in str:
#     if chr!=" ":
#      print(chr,end='')
# Reverse a string
# str='hello'
# rev=''
# for chr in str:
#     rev=chr+rev
# print(rev)
# remove spaces and reverse the string
# str='he llo world'
# rev=''
# for chr in str:
#     if chr!=" ":
#         rev=chr+rev
# print(rev)
# snake to camel case
# string='my_variable_name'
# n=string.split("_")
# res=''
# res+=n[0]
# for chr in range(1,3):
#    res=res+n[chr].capitalize()
# print(res)
# snake to pascal
# string='my_variablr_name'
# n=string.split('_')
# res=''
# for chr in n:
#     res=res+chr.capitalize()
# print(res)
# reverse a string
# s='hello'
# rev=''
# for chr in s:
#   rev=chr+rev
# print(rev)
# palidrome check
# s='madam'
# rev=''
# for chr in s:
#     rev=chr+rev
# if rev==s:
#    print('palindrome')
# else:
#    print('not')
# count of digits
# n=123
# sum=0
# for i in range(1,3):
#     n=n%10
#     sum=sum+n
# print(sum) 
# product of digits
# n=123
# pro=1
# for digit in str(n):
#     pro=pro*int(digit)
#     n//=10
# print(pro)
# s='apple'
# c1=0
# c2=0
# vowels='aeiou'
# for chr in s:
#     if chr in vowels:
#         c1=c1+1
#     else:
#        c2=c2+1
# print(c1)
# print(c2)
# n=9
# f=0
# for i in range (1,n):
#     if n%i==0:
#         f=f+i
# if f==n:
#     print('perfect')
# else:
#     print('not')
# # n = int(input("Enter a number: "))
# original_n = n
# sum_of_factorials = 0

# while n > 0:
#     digit = n % 10
#     factorial = 1
#     for i in range(1, digit + 1):
#         factorial *= i
#     sum_of_factorials += factorial
#     n //= 10

# if sum_of_factorials == original_n:
#     print(f"{original_n} is a Strong Number.")
# else:
#     print(f"{original_n} is not a Strong Number.")
# n = 5
# a, b = 0, 1

# print("Fibonacci Series:")
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
# prime numbers
# m=10
# n=30
# for i in range(m,n+1):
#     f=0
#     for j in range(1,i+1):
#         if i%j==0:
#             f=f+1
#     if f==2:
#      print(i)
# n=143
# sum=0
# temp=n
# while n>0:
#     r=n%10
#     r=r**3
#     sum=sum+r
#     n//=10
# if temp==sum:
#     print('armstrong')
# else:
    # print('not')
# for n in range(1,500):
#     sum=0
#     temp=n
#     l=len(str(n))
#     while n>0:
#         r=n%10
#         res=r**l
#         sum=sum+res
#         n//=10
#     if temp==sum:
#       print(temp)
# first prime number
# n=10
# m=26
# lastprime=-1
# for i in range(10,25):
#     f=0
#     for j in range(1,i+1):
#         if i%j==0:
#             f=f+1
#     if f==2:
#        lastprime=i
# print(lastprime)
# str='krishna'
# vowels='aeiou'
# rev=''
# lastletter=-1
# for chr in str:
#     if chr in vowels:
#         rev=rev+chr
#         print(rev)
#         break
# str='krishna'
# vowels='aeiou'
# lastletter=None
# for chr in reversed(str):
#      if chr in vowels:
#         lastletter=chr
#         break
# if lastletter:
#     print(chr)
# for i in range(1,11):
#     if i%2==0:
#         continue
#     print(i)
