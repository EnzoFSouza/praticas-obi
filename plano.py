quota_original = int(input())
quota_atual = quota_original
n = int(input())
usos = list()
for i in range(n):
    usos.append(int(input()))

for i in range(len(usos)):
    sobra = quota_atual - usos[i]
    quota_atual = quota_original + sobra


print(quota_atual)