elev = ['B'+str(9-i) for i in range(9)] + [str(i+1)+'F' for i in range(9)]
s,t=map(str,input().split())
print(abs(elev.index(s)-elev.index(t)))
