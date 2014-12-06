from sets import Set

S = "abbcbbdca"
T = Set(['a', 'c', 'd'])


best = len(S)
start = 0 
end = len(S) - 1

chain = []

gathered = Set()
counter = {}

for c in T:
  counter[c] = 0

for i in xrange(0, len(S)):
  if S[i] in T:
    chain.append(i)
    counter[S[i]] += 1
    if len(chain) > 1 and S[chain[0]] == S[i]:
      counter[S[chain[0]]] -= 1
      del chain[0]
      
    if S[i] not in gathered:
      gathered.add(S[i])
    
  if len(gathered) == len(T):
    if chain[-1] - chain[0] + 1 < best:
      best = chain[-1] - chain[0] + 1
      start = chain[0]
      end = chain[-1]
      
      counter[S[chain[0]]] -= 1
      if counter[S[chain[0]]] == 0:
	gathered.remove(S[chain[0]])      
      del chain[0]
      while counter[S[chain[0]]] > 1:
	counter[S[chain[0]]] -= 1
	del chain[0]
	
  
  
print best
print start
print end