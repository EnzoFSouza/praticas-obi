R = int(input()) #melhor resultado obtido
M = int(input()) #recorde mundial
L = int(input()) #recorde olímpico

if R < M:
    print("RM")

else:
    print("*")

if R < L:
    print("RO")

else:
    print("*")