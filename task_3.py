import numpy as np, math
def Monte_Karlo(kk,n):
    k=0
    a = np.random.randint(0,2 ,n)
    b = np.random.randint(0,2 ,n)
    c = np.random.randint(0,2 ,n)
    d = np.random.randint(0,2 ,n)
    x = a + b + c + d

    for i in range(0,n):
        if x[i] == kk:
            k = k + 1
    print ("Вероятность по Монте-Карло:", k, n, k/n)

def Bernulli(n,k):
    C_n_k = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    P_n_k = C_n_k * 1/2**n
    print("Вероятность по Бернулли:", P_n_k)
    return P_n_k
print("Задание 1:")
Monte_Karlo(2,5000)
Bernulli(4,2)
print("Задание 2:")
Bernulli(5,3)