from sets import Set

S = "abbcbddbac"
T = Set(['a', 'd'])


best = len(S)
start = 0 
end = len(S) - 1

for i in xrange(0, len(S) - len(T) + 1):
  has = 0
  M = {}
  for c in T:
    M[c] = 0
  for j in xrange(i, len(S)):
    if S[j] in T:
      M[S[j]] += 1
      if M[S[j]] == 1:
	has += 1
	if has == len(T):
	  if j - i + 1 < best:
	    best = j - i + 1
	    start = i 
	    end = j
	  break
	
	
	
print best
print start
print end
