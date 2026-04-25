import time



x=str(123456789 ** 100)
y=str(987654321 ** 100)

lx=len(x)
ly=len(y)

#単純計算アルゴリズム
x_array,y_array=[],[]
sum_elementary=0

for i in range(lx):
    x_array.append(int(x[lx-1-i]))
for j in range(ly):
    y_array.append(int(y[ly-1-j]))

#単純計算アルゴリズム(本体)
start=time.perf_counter()

for i in range(lx):
    for j in range(ly):
        sum_elementary+=10**(i+j)*x_array[i]*y_array[j]

finish=time.perf_counter()

passed_time= finish-start

#カラツバ法(本体)
def karatuba(a,b):

    check1=1
    check2=1
    if a<0:
        check1=-1
        a*=-1
    if b<0:
        check2=-1
        b*=-1
    a=str(a)
    b=str(b)
    la=len(a)
    lb=len(b)
    
    #ベースケース
    if max(la,lb)<10:

        return int(a)*int(b)*check1*check2

    else:

        a_karatuba_array,b_karatuba_array=[],[]

        #桁合わせ
        for i in range(la):
            a_karatuba_array.append(a[la-1-i])
        for j in range(lb):
            b_karatuba_array.append(b[lb-1-j])

        if la>lb:
            for i in range(la-lb):
                b_karatuba_array.append(0)
        elif lb>la:
            for i in range(lb-la):
                a_karatuba_array.append(0)

        common_length=max(la,lb)

        if common_length%2!=0:
            a_karatuba_array.append(0)
            b_karatuba_array.append(0)
            common_length+=1

        n=common_length
        half=n//2
        a_low,b_low=0,0
        a_high,b_high=0,0

        #二つの数をそれぞれ半分の大きさの数に分ける
        for i in range(half):
            a_low+=(10**i)*(int(a_karatuba_array[i]))
            b_low+=(10**i)*(int(b_karatuba_array[i]))
            a_high+=(10**i)*(int(a_karatuba_array[i+half]))
            b_high+=(10**i)*(int(b_karatuba_array[i+half]))

        #分割統治法
        z0=karatuba(a_low,b_low)
        z1=karatuba(a_high-a_low,b_high-b_low)
        z2=karatuba(a_high,b_high)
    
        sum_karatuba=((10**(2*half))*z2+(10**half)*(z0+z2-z1)+z0)*check1*check2

        return sum_karatuba


start=time.perf_counter()
#再帰呼び出し
sum_karatuba=karatuba(int(x),int(y))

finish=time.perf_counter()

passed_time2=finish-start

if sum_elementary==int(x)*int(y):
    print("単純計算:"+f' : {passed_time:.6f}'+"秒")
if sum_karatuba==int(x)*int(y):
    print("カラツバ法:"+f' : {passed_time2:.6f}'+"秒")