elements={'Carbon':['C',4,1],'Oxygen':['O',-2,2],'Chlorine':['Cl',-1,1],'Hydrogen':['H',1,2]}

ele1=input("Enter name of element 1")
ele2=input("Enter name of element 2")
l1=elements[ele1]
l2=elements[ele2]

if(ele1==ele2):
    if(ele1=='Carbon' or ele1=='Chlorine'):
        print("REaction not possible")
    else:
        print(l1[0],' + ',l2[0],' -> ',l2[0],'2')
        if(l2[1]<0):
            print("REaction not possible")
else:
    if(l1[1]<0 and l2[1]<0):
        print("Covalent compound")
    elif(l1[1]>0 and l2[1]>0):
        print('C + 2H2 -> CH4')
    else:
        if(l1[1]>l2[1]):
            if(abs(l1[1])>abs(l2[1])):
                val=abs(l1[1])//abs(l2[1])
                count=val//l2[2]
                print(l1[0],' + ',count,l2[0],l2[2],' -> ',l1[0],l2[0],count*l2[2])
            else:
                val=l2[1]//l1[1]
                print(abs(val),l1[0],l1[2],' + ',l2[0],l2[2],' -> ',l1[0],l1[2],l2[0],l2[2]//l1[2])
