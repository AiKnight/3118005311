import sys
import random
print('欢迎使用四则运算题目生成软件 1.0\n\n')
s = int(input('请输入生成题目数量：'))
min=1
max=100
print('\n')
i=0
with open('Exercises.txt', 'w') as E:
    E.write('小学四则运算题目\n\n')
    with open('Answers.txt', 'w') as A:
        A.write('小学四则运算答案\n\n')
        while (i < s):
            i=i+1
            a=b=c=100
            m=random.randint(1,2)  ##控制运算符数量
            ##m=1
            k1=random.choice(['+', '-', '×', '÷']) ##运算符1
            k2=random.choice(['+', '-', '×', '÷']) ##运算符2
            if m==1:
                while ((int(a/b)*b != a) or (a==b) ):
                    minx=random.randint(min,4*min)
                    a=random.randint(minx,max)
                    b=random.randint(minx,max)
                print("%5s"%(i),') ',a,k1,b,'=')
                E.write(str(i));E.write(')\t');E.write(str(a));E.write(k1);E.write(str(b));E.write('=\n');
                '''计算单运算符题目'''
                if k1=='+':
                    J=a+b
                if k1=='×':
                    J=a*b
                if k1=='-':
                    J=a-b
                if k1=='÷':
                    J=int(a/b)
                print(J)
                A.write(str(i));A.write(')\t');A.write(str(J));A.write('\n');


            if m==2:
                while ((int(a/b)*b != a) or (int(b/c)*c!=b) or int(int(a/b)/c)*c!=int(a/b) or (a==b==c)):
                        minx=random.randint(min,4*min)
                        a=random.randint(minx,max)
                        b=random.randint(minx,max)
                        c=random.randint(minx,max)
                print("%5s"%(i),') ',a,k1,b,k2,c,'=')
                E.write(str(i));E.write(')\t');E.write(str(a));E.write(k1);E.write(str(b));E.write(k2);E.write(str(c));E.write('=\n');
                '''计算双运算符题目'''
                if k1=='+':
                    if k2=='+':
                        J=a+b+c
                    if k2=='-':
                        J=a+b-c
                    if k2=='×':
                        J=a+b*c
                    if k2=='÷':
                        J=int(a-b/c)

                if k1=='-':
                    if k2=='+':
                        J=a-b+c
                    if k2=='-':
                        J=a-b-c
                    if k2=='×':
                        J=a-b*c
                    if k2=='÷':
                        J=int(a-b/c)

                if k1=='×':
                    if k2=='+':
                        J=a*b+c
                    if k2=='-':
                        J=a*b-c
                    if k2=='×':
                        J=a*b*c
                    if k2=='÷':
                        J=int(a*b/c)

                if k1=='÷':
                    if k2=='+':
                        J=int(a/b+c)
                    if k2=='-':
                        J=int(a/b-c)
                    if k2=='×':
                        J=int(a/b*c)
                    if k2=='÷':
                        J=int(a/b/c)
                print(J)
                A.write(str(i));A.write(')\t');A.write(str(J));A.write('\n');
    E.closed
    A.closed
