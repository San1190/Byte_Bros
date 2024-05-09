def infinite_sevens():
  while True:
    yield 7
        
for i in infinite_sevens():
  print(i)
