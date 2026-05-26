#Question5: Given two sets, determine if one is a subset of the other, if they are disjoint, or if they share some common elements. Use set operations to find the relationships between the two sets.  
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}
print("A is subset of B: ", setA.issubset(setB))
print("B is superset of A : ",setB.issuperset(setA))
print("A is disjoint from B: " , setA.isdisjoint(setB))