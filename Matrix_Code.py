import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
st=[]
res = max(matrix, key = len)
for i in range(0,len(res)):
    for j in range(0,len(matrix)):
        x=matrix[j]
        st.append(x[i])
nst=''.join(st)
nst1=re.sub(r'\W', r' ',nst)
nst2=" ".join(nst1.split())
x = re.split("\w", nst)
print(x[0]==x[-1] and (nst2+x[0]) or (x[0]+nst2+x[-1]))