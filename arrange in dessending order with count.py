l1 = [100,200,300,400,100,200,50,300,500,500,600,100]
uni_val = set(l1)
uni_list = list(uni_val)
print(l1)
uni_list.sort(reverse=True)
print(uni_list)
for i in uni_list:
    y= l1.count(i)
    print(f"{i}--> {y} ")