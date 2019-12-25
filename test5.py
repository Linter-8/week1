#回到原点
countx = 0
county = 0
answer="no"

while(answer=="no"):
    mingling=input("you choose:")
    if(mingling=="U"):
        county+=1
    if(mingling=="D"):
        county-=1
    if(mingling=="L"):
        countx-=1
    if(mingling=="R"):
        countx+=1
    else:
        print("please input rihgt mingling")
    answer=input("do you want to finish? (yes or no):")
if((countx==0)and(county==0)):
    print("True")
else:
    print("False")
   
