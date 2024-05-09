from collections import Counter

numeros = [ 8, 6, 5,6,7,8,8,8,5,4,3,1,2,3,3,3,3,4,5,6,7,8,9,0,9,78,67,6,6,6,6,6,6,45,4,4,4,4,23,56,67,7,6,5,5,45,64,56,6,67,78,67,5,5]

#print(Counter()) # tmb co n sting, frases .split (separa palabras)ç

serie = Counter(numeros)

print(serie.most_common())