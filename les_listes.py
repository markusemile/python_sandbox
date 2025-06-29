a = ["Gregory"]
a.extend(["Alex", "Emile", "Attila", "Bruno", "Patrick", "Bruno", "Fabrice"])

print(f"The list :\n{a}\n")

# from 0 and we take 2 elements
print("from 0 and we take 2 elements : print(arr[0:2])")
print(a[0:2])

# from 0 till end by step 2 (odds)
print("\nfrom 0 till end by step 2 (odds) : print(a[::2]))")
print(a[::2])

# from element 1 till end, by step 2 (evens)
print("\nfrom element 1 till end, by step 2 (evens : print(a[1::2]))")
print(a[1::2])

# revers list
print("\nReverse list : print(a[::-1])")
print(a[::-1])

# all elements except first and last
print("\nall elements except first and last : print(a[1:-1])")
print(a[1:-1])

# return element index
print("\nReturn element index: a.index('Patrick')")
print(a.index("Patrick"))

# return number of occurrences
print("\nreturn number of occurrences: a.count('Bruno')")
print(a.count("Bruno"))

b = a
# sort directly the array
# a.sort()

# sort and put into a variable
print("\nsort and put into a variable : c = sorted(b)")
c = sorted(b)
print(c)

print(f"\nReverse the sorted list : elem.reverse()")
# reverse the sorted list
a.reverse()
print(a)

# pop

print("\nBefore pop")
deleted_elem = c.pop(0)
print(c)

print("\nAfter pop remove element 0: elem.pop(0) or the last deleted_elem = elem.pop(-1)")
print(c)

print("\nthe element was deleted by pop is : print(deleted_elem)")
print(deleted_elem)

print("\nremove all elems : c.clear() ")
c.clear()
print(c)

print("\nJoin a array of string : ' '.join(c)")
print('["This", "is", "a", "string", "of", "characters", "."]')
c = ["This", "is", "a", "string", "of", "characters", "."]
print(" ".join(c))


print("\nSplit a sentence  : elem.split(', ')")
d = "This, is, a, string, of, characters."
print(d)
e = d.split(",")
print(e)

print("\nCheck if elem in the array")
print(a)
print("Check if Patrick into the array : (\"Patrick\" in a)")
print("Patrick" in a)
print("Check if Trump into the array : (\"Trump\" in a)")
print("Trump" in a)

print("\nNested Array")
ff = ["python", ["java", "Angular", ["c++"]], ["ruby"]]
print(ff)
print("Print first element : l = ff[0] ")
print(ff[0])
print("Print the two first letter of the first element: l = ff[0][0:2] ")
print(ff[0][0:2])
print("Tack the last elem of the second element : l = ff[1][-1] ")
print(ff[1][-1])
print("Tack the two first letters of last elem of the second element : l = ff[1][-1][0][0:2] ")
print(ff[1][-1][0][0:2])
