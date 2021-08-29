#dict or json in python
dist={
    'a':1,
    'b':[1,2,34,3]
}
lend=len(dist)
sums=sum(dist['b'])
print(dist,lend,'\n')
print("%.6f" %sums)