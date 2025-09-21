import pandas as pd
from figuras import rectangulo, triangulo, circulo

df = pd.read_csv("figuras.csv")
print("El archivo ha sido leído\n")

for index, row in df.iterrows():
    figura = row["FIGURA"]
    m1 = row["MEDIDA1"]
    m2 = row["MEDIDA2"]

    if figura == "r":
        a, p = rectangulo(m1, m2)
    elif figura == "t":
        a, p = triangulo(m1, m2)
    elif figura == "c":
        a, p = circulo(m1)
    else:
        print(f"Figura desconocida en fila {index}")
        continue

    print(f"Fila {index}: FIGURA={figura} → Área={a}, Perímetro={p}")

