# 06)Faça um programa que gere as tabuadas do 1 até o 10.

for i in range(1, 11):
    print(f"Tabuada do {i}:")
    
    # Loop para gerar os resultados da tabuada
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    
    print()