def percent(votos, tot_votos):
  return votos*100/tot_votos

with open('dados_eleicao.txt') as arq:
  cand = []
  for linha in arq:
    linha = linha.strip('\n').split(',')
    cand.append(linha[2])
  cand.pop(0)

s = set(cand)

votos = []
for i in s:
  votos.append(cand.count(i))

lista = dict()
candidatos = list(s)
for i in range(len(s)):
  lista[candidatos[i]] = votos[i]

lista = sorted(lista.items(), key=lambda x: x[1], reverse=True)
lista = dict(lista)

with open('resultado.txt', 'w') as arq:
  arq.write(f"Resultados eleitorais\n{'-'*25}\nTotal de votos: {len(cand)}\n{'-'*25}\n")
  for i in lista.items():
    arq.write(f'{i[0]}: {percent(i[1], len(cand)):.1f}% ({i[1]})\n')
  arq.write(f"{'-'*25}\nVencedor: ")
  for x in lista.items():
    arq.write(x)
    break
  arq.write(f"\n{'-'*25}")

with open('resultado.txt') as arq:
  print(arq.read())