n=103
print(" y^2 mod n=(x^3  + a*x + b)mod n\nEnter 'n':", n)

def polynomial(LHS,RHS,n):
    for i in range(0,n):
        LHS[0].append(i)
        RHS[0].append(i)
        LHS[1].append((i*i*i + a*i + b)%n)
        RHS[1].append((i*i)%n)


def points_generate(arr_x,arr_y,n):
    count=0
    for i in range(0,n):
        for j in range(0,n):
            if(LHS[1][i]==RHS[1][j]):
                count+=1
                arr_x.append(LHS[0][i])
                arr_y.append(RHS[0][j])
    return count

#main

LHS=[[]]
RHS=[[]]
LHS.append([])
RHS.append([])
a=1
print("Value of 'a':",a)
b=6
print("Value of 'b':",b)



polynomial(LHS,RHS,n)

arr_x=[]
arr_y=[]
#Generating base points
count=points_generate(arr_x,arr_y,n)
    
#Print Generated Points
print("Generated points are:")
for i in range(0,count):
    print(i+1," (",arr_x[i],",",arr_y[i],")\n")



#Calculation of Base Point
bx=arr_x[0]
by=arr_y[0]
print("Base Point taken is:\t(",bx,",",by,")\n")

d=29

print("The random number d1:", d)
if(d>=n):
    print("'d' should be less than 'n'.")
else:
    
    Qx=d*bx
    Qy=d*by
    print("Public key of sender is:\t(",Qx,",",Qy,")\n")

    #Encrytion
    k=30
    print("The random number d2:", k)
    if(k>=n):
        print("'k' should be less than 'n'")
    else:
        M=3107
        print("The message to be sent:\n", M)
        

        #Cipher text 1 generation
        C1x=k*bx
        C1y=k*by
        print("Value of Cipher text 1 i.e. C1:\t(",C1x,",",C1y,")\n")

        #Cipher text 2 generation
        C2x=k*Qx+M
        C2y=k*Qy+M
        print("Value of Cipher text 2 i.e. C2:\t(",C2x,",",C2y,")\n")

    #Decryption
        Mx=C2x-d*C1x
        My=C2y-d*C1y
        print("The message recieved by reciever is:\t",Mx)            
