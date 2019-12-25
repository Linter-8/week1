# 猜数字
import random
count = 0
x=0
y=0
guess=[]
answer=[]
for i in range(3):
    x=random.randint(1,3)
    y=random.randint(1,3)
    guess.append(x)
    answer.append(y)
for i in range(3):
    if (guess[i] == answer[i]):
        count=count+1
print(count)
