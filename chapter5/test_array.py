# print (','.join(map(str,['women','me'])))
from chapter5.arraybag import ArrayBag

a = ArrayBag()
# print(type(ArrayBag(a)))
a.add('zhang')
b = ArrayBag()
b.add('min')
c = b + a
print(c)