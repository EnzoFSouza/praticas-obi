R = int(input())
F = int(input())
C = int(input())

if F > 3 * R or C < 95:
    print("diminuir")

elif F < 2 * R and C > 97:
    print("aumentar")

else:
    print("manter")