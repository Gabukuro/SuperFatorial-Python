## Super Fatorial

O super fatorial de um número N é definida pelo produto dos N primeiros fatoriais de N. Assim, o super fatorial de 4 é sf(4) = 1! * 2! * 3! * 4! = 288.

Comparação de tempo de execução por abordagem:

| Número   |Normal |Dinâmica |
|----------|-------|---------|
| 4        | 0.033 | 0.016   |
| 10       | 0.049 | 0.074   |
| 20       | 0.100 | 0.237   |
| 25       | 0.169 | 0.406   |
| 30       | 0.227 | 0.595   |
| 35       | 0.243 | 0.741   |
| 40       | 0.304 | 1.011   |

## Análise de Complexidade 

### Abordagem Normal

A complexiddade para este algoritmo é conhecida como quadrática, denominada por O(n^2). Vamos dar uma olhada na função: 

```python
def superFatorial(n):
  fact = 1

  if n == 0:
    return 0

  for i in range (1, n + 1): 
    for x in range(1, i + 1):
      fact *= x

  return fact
```

Neste trecho de código podemos observar a existência de um loop dentro de outro loop, ambos iteram todos os itens do valor de entrada da função.

### Abordagem Dinâmica

Como a abordagem dinâmica conta com a implementação de uma função recursiva, a sua complexidade é equivalente ao número de chamadas da função recursiva. Desta forma O(n+m), já que neste caso m recebeu o valor de n, ficando O(2n).

```python 
def multiplyNumbersDin(n, m):
  if m == 1:
    return 1
  elif n == 1:
    return n*multiplyNumbersDin(m - 1, m - 1)
  else: 
    return n*multiplyNumbersDin(n -1, m)

def superFatorialDin(n):
  return multiplyNumbersDin(n, n)
``` 