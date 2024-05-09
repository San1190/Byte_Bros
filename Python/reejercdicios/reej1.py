#sets  ----- ste( 12323234143) | {}

mi_set = set(['a','b','c'])


print(type(mi_set))
print(mi_set)

m_set = {1,2,3,4,5,6,1,(1,2,3,5,6)} #elimina las repeticiones # solo admite tuplas, no otra cosa ya que no puweden variar

print(type(m_set))
print(m_set)
print(len(m_set))

print(2 in m_set)

if 2 in m_set:
    print("Potato")





s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)
s1.add(2)
print(s1)
s1.remove(3)
print(s1)
s1.discard(6)# descartar no eslo mismo q eliminar
print(s1)


s1.pop()
print(s1)

s1.clear()
print(s1)