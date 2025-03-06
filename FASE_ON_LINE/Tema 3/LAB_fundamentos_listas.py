beatles=[]
beatles.append(' John Lennon ')
beatles.append(' Paul McCartney ')
beatles.append(' George Harrison ')
print(beatles)
for i in range(1):
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete Best")
print(beatles)
del(beatles[3:5])
print(beatles)
beatles.insert(0, "Ringo Star")
print(beatles)