# WAP to find the greatest of 3 numbers entered by the user.

ram_age = int(input("Enter Ram's number: "))
shyam_age = int(input("Enter Shyam's number: "))
rahul_age = int(input("Enter Rahul's number: "))

if(ram_age > shyam_age and ram_age > rahul_age):
        print(ram_age," is eldest")
elif(shyam_age > rahul_age):
    print(shyam_age," is eldest")
else:
    print(rahul_age,"is eldest")