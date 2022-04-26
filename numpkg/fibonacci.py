
n = int(input())

list = [0 for i in range(n+1)]

_curr = 0
_next = 1

list[0] = _curr
list[1] = _next

for i in range(2,n+1):
	_curr, _next = _next, _curr+_next
	list[i] = _next

print(list[:n+1])
print(list[n])
