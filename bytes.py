# a=b"akhila"
# print(a,type(a))
# print(list(a))
# print(tuple(a))
# print(set(a))

# y=b"akhila"
# for i in y:
#     print(i)

# print(ord('a'))
# print(chr(65))

# a=b"akhila"
# a[0]=65  # modifications cannot be done

# a=b'[4,5,6]'
# print(list(a))

# print(ord('['))
# print(ord(','))
# print(chr(91))
# print(chr(93))

v=bytearray(b"akhila")
# print(v,type(v))
# print(v[0])
v[0]=65
print(v)
v[3]=73
print(v)