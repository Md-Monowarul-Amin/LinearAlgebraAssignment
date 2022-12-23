x=[2,3,5,7,8,9]

a=[3,8,25,38,62,95]
b=[4,9,20,48,60,98]
c=[5,7,23,49,62,83]

actual=[]
value_of_error = [0,0,0]

for i in x:
    actual.append(i*i)

for i in range(0,len(a)):
    value_of_error[0] += (actual[i]-a[i])*(actual[i]-a[i])

for i in range(0,len(b)):
    value_of_error[1] += (actual[i]-b[i])*(actual[i]-b[i])

for i in range(0,len(c)):
    value_of_error[2] += (actual[i]-c[i])*(actual[i]-c[i])

best = min(value_of_error)

if(best == value_of_error[0]):
    print("best curve is A")
elif(best == value_of_error[1]):
    print("best curve is B")
else:
    print("best curve is C")