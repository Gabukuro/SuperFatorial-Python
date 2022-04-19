from datetime import datetime

def superFatorial(n):
  fact = 1

  if n == 0:
    return 0

  for i in range (1, n + 1): 
    for x in range(1, i + 1):
      fact *= x

  return fact

def multiplyNumbersDin(n, m):
  if m == 1:
    return 1
  elif n == 1:
    return n*multiplyNumbersDin(m - 1, m - 1)
  else: 
    return n*multiplyNumbersDin(n -1, m)

def superFatorialDin(n):
  return multiplyNumbersDin(n, n)

n = int(input('Digite um número: ').strip())

before = datetime.now()
fact = superFatorial(n)
after = datetime.now()

print("\nFatorial => ", fact)
print("\nTempo de execução em milissegundos (normal): ", ((after - before).total_seconds() * 1000))

before = datetime.now()
fact = superFatorialDin(n)
after = datetime.now()

print("\nFatorial => ", fact)
print("\nTempo de execução em milissegundos (dinâmica): ", ((after - before).total_seconds() * 1000))

