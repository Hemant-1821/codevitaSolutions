N = int(input())
li = list(map(str,input().strip().split()))
pairs = []
for i in li:
  temp = list(i)
  lar = int(max(temp))*11
  sma = int(min(temp))*7
  #print(temp,lar,sma)
  sums = lar + sma
  #print(sums)
  pairs.append(int(str(sums)[-2]))
  #print(pairs)
di_even = {}
di_odd = {}
count = 0
i = 0
try:
  while i < N:
    if pairs[i] in di_even:
        di_even[pairs[i]] += 1
    else:
        di_even[pairs[i]] = 1
    if pairs[i+1] in di_odd:
        di_odd[pairs[i+1]] += 1
    else:
        di_odd[pairs[i+1]] = 1
    i += 2
except:
  pass
#print(di_even,di_odd)
for i in di_even:
  if di_even[i] == 2:
    count += 1
    if i in di_odd:
      if di_odd[i]>2:
          di_odd[i] = 2
  elif di_even[i] >= 3:
    count += 2
    if i in di_odd:
      di_odd[i] = 2
for i in di_odd:
  if di_odd[i] == 2:
    count += 1
  elif di_odd[i] >= 3:
    count += 2
print(count)