import sys
import random
print('欢迎使用四则运算题目生成软件 1.0\n\n')
s = int(input('请输入生成题目数量：'))
##min =int(input('请输入题目数据下限：'))
##max =int(input('请输入题目数据上限：'))
min=1
max=100
print('\n')
i=0
with open('Exercises.txt', 'w') as E:
    with open('Answers.txt', 'w') as A:
        A.write('答案中的“·”表示“又”\n')
        while (i < s):
            i=i+1
            a=random.randint(min,max)
            b=random.randint(min,max)
            while ((int(a/b)*b != a)  and (int(b/a)*a != b)):
                a=random.randint(min,max)
                b=random.randint(min,max)
            c=random.randint(min,max)
            d=random.randint(min,max)
            m=random.randint(1,3)  ##控制运算符数量
            m=1
            k1=random.choice(['+', '-', '×', '÷']) ##运算符1
            k2=random.choice(['+', '-', '×', '÷']) ##运算符2
            k3=random.choice(['+', '-', '×', '÷']) ##运算符3
            if m==1:
                if k1=='+' or k1=='×':
                    print("%5s"%(i),') ',a,k1,b,'=')
                    E.write(str(i));E.write(')\t');E.write(str(a));E.write(k1);E.write(str(b));E.write('=\n');
                    if k1=='+':
                        J=a+b
                    if k1=='×':
                        J=a*b
                    print(J)
                    A.write(str(i));A.write(')\t');A.write(str(J));A.write('\n');
                if k1=='-' or k1=='÷':
                    if a<b:
                        if k1=='-':
                            print("%5s"%(i),') ',b,k1,a,'=')
                            E.write(str(i));E.write(')\t');E.write(str(b));E.write(k1);E.write(str(a));E.write('=\n');
                            J=b-a
                            print(J)
                            A.write(str(i));A.write(')\t');A.write(str(J));A.write('\n');
                        if k1=='÷':
                            print("%5s"%(i),') ',a,k1,b,'=')
                            E.write(str(i));E.write(')\t');E.write(str(a));E.write(k1);E.write(str(b));E.write('=\n');
                            J=str(a)+'/'+str(b)
                            print(J)
                            A.write(str(i));A.write(')\t');A.write(str(J));A.write('\n');
                    if a>=b: 
                        print("%5s"%(i),') ',a,k1,b,'=')
                        E.write(str(i));E.write(')\t');E.write(str(a));E.write(k1);E.write(str(b));E.write('=\n');
                        if k1=='-':
                            J=a-b
                        if k1=='÷':
                            J=int(a/b)
                        print(J)
                        A.write(str(i));A.write(')\t');A.write(str(J));A.write('\n');
            if m==2:
                print("%5s"%(i),') ',a,k1,b,k2,c,'=')
                E.write(str(i));E.write(')\t');E.write(str(a));E.write(k1);E.write(str(b));E.write(k2);E.write(str(c));E.write('=\n');
            if m==3:
                print("%5s"%(i),') ',a,k1,b,k2,c,k3,d,'=')
                E.write(str(i));E.write(')\t');E.write(str(a));E.write(k1);E.write(str(b));E.write(k2);E.write(str(c));E.write(k3);E.write(str(d));E.write('=\n');
