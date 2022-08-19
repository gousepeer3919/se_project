iProgram to check if number is palindrome using a recursive function
num=int(input("Enter number\n"))
def rev(n,temp):
    if n==0:
        return temp
    else:
        temp=(temp*10)+(n%10)
        return rev(int(n/10),temp)
print(rev(num,0))
if(num==rev(num,0)):
    print("Palindrome")
else:
    print("Not palindrome")

