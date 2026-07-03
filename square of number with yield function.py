
def squares():
  x = range(1, 4) # 1 to 4
  for n in x:
      yield n**2
   
for y in squares():
	print(y)   	# prints 1 4 9 16
