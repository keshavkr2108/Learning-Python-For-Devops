name = "My name is Keshav Kumar"

# print(name.split(" "))
# print (name.upper()[3])
l = name.split()
# print(' '.join(l[:3]), l[3].upper(),l[4].upper())

print(' '.join(l[:3])," ".join([t.upper() for t in l[:2:-1]][::-1]))



""""
upper() -- to convert letter in uppercase

join -- apply on list



"""

print('**'.join(['1','2','3']))




