size = int(input("Enter the size of list: "))
mylist = []
for i in range(size):
    mylist.append(int(input("Enter the element in list: ")))

print(f"\nYour list is {mylist}")

reverse1 = mylist[:]
inbuilt = reverse1.reverse()
print(f"\nThe first reverse of {mylist} is {reverse1}")
reverse2 = mylist[::-1]
print(f"The second reverse of {mylist} is {reverse2}")
reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3)-i-1] = reverse3[len(reverse3)-i-1], reverse3[i]


print(f"The third reverse of {mylist} is {reverse3}\n")

if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give the same results!")
else:
    print("Your program is wrong.")