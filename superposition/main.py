'''
Script: quCoin.py
Author: thuulk
Date: 2025
Description: Simulating a quantum coin with a qubit a Hadamard gate
'''


from superposition.QuantumCoin import QuantumCoin


if __name__ == "__main__":
    
    qCoin = QuantumCoin(1,1)
    nFlips = 1000
    counts = qCoin.flip_the_coin(nFlips)

    print(f"Lanzamientos totales: {nFlips}")
    print("Resultados crudos:", counts)

    c0 = counts.get('0', 0)
    c1 = counts.get('1', 0)

    p0 = c0 / nFlips
    p1 = c1 / nFlips

    print(f"Probabilidad aproximada de 0: {p0:.3f}")
    print(f"Probabilidad aproximada de 1: {p1:.3f}")