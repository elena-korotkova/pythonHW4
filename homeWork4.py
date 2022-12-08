"""
1 Вычислить число π c заданной точностью d
*Пример:*

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
.
https://completerepair.ru/kak-vychislit-chislo-pi
.
.
2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
*Пример*

- при N=236     ->        [2, 2, 59]
.
.
3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*

- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
.
.
4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
*Пример:*

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
.
.
5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.
"""

def custom_pi(num):
    sum = 1
    for x in range (1,num+1):
        sum += 1 / ((2*x + 1) * (-3) ** x)
    return 12**0.5*sum

def get_pi(d):
    if 10**-10 <= d <= 10**(-1):
        from math import pi
        num = 1
        res = 0
        while abs(res - pi) > d:
            res=custom_pi(num)
            num+=1
        print(pi,res,num)
    else:
        print('__error__')

# **********************************

def simple(num):
    res = True
    for x in range(2,num):
        if num%x == 0:
            res = False
            break
    return res

def get_simple_list(num):

    return [x for x in range(2,num+1) if simple(x)]



def simple_row(n):
    num=n
    res=[]
    for x in get_simple_list(n):
        for t in get_simple_list(x):
            if num % t == 0:
                res.append(t)
                num//=t

    return res
# ************************************


def get_random_list(num):
    from random import randint
    return [randint(0,10) for x in range(num+1)]


def get_sorted_list(list1,list2):
    res=[]
    for x in list1:
        for y in list2:
            if x==y and x not in res:
                res.append(x)

    return res

def get_unic(num):
    result=[]
    lst=get_random_list(num)
    tmp=list(set(lst))
    print(lst)
    for x in get_sorted_list(lst,tmp):
        cnt=0
        for y in lst:
            if x == y:
                cnt+=1
        if cnt==1:
            result.append(x)

    return result
# ************

def get_urav(num,filename):
    from random import randint
    k=[t for t in range(num+1)]
    res=""
    for x in k[::-1]:
        tmp=randint(-10,10)
        if tmp:
            sep = '+ ' if tmp > 0 and x != k[-1] else ''
            res +=f"{sep}{tmp}{'x' if x!=0 else ''}{x} "
            # print(f"{tmp}{'x' if x!=0 else ''}{x}",end=' ')

    res+="= 0"

    with open(filename,'w') as file:
        file.write(res)

    return res

# ****************************************************************

def read_file(filename):
    res=''
    with open(filename,'r') as file:
        res=file.read()
    return res


def explode_str(str):
    tmp=str.split(' = ')
    res={}
    lst=tmp[0].split(' ')
    for x in lst:
        if x!='+':
            tmp_a = list(map(int,x.split('x')))
            if len(tmp_a)==1:
                tmp_a.append(0)
            res[tmp_a[1]]=tmp_a[0]
    return res

def sum_files(file1,file2):
    f1=read_file(file1)
    f2=read_file(file2)

    _f1=explode_str(f1)
    _f2=explode_str(f2)

    print(f1)
    print(f2)

    result={}

    for x in range(len(_f1)):
        result[x]=_f1.get(x,0)+_f2.get(x,0)

    _res=''
    keys=list(result.keys())

    for key in keys[::-1]:
        if result[key]!=0:
            sep = '+ ' if result[key] > 0 and key != keys[-1] else ''
            _res +=f"{sep}{result[key]}{'x' if key!=0 else ''}{key if key>0 else ''} "
    _res+='= 0'

    with open('sum_file','w') as file:
        file.write(_res)
    return _res

if __name__ == '__main__':
    # get_pi(0.0000000001)
    # print(simple_row(236))
    # print(get_unic(10))
    #
    # print(get_urav(4,'file1'))
    # print(get_urav(3,'file2'))

    print(sum_files('file1','file2'))