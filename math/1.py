def find_ord(a, p):
    i = 1
    while (a ** i) % p != 1:
        i += 1
    return i

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def prime_factors(n):
    factors = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return gcd(a, b) == 1
def are_coprime(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return 1 if gcd(a, b) == 1 else -1

def ord(a, p):
    for i in range(1, p):
        for j in a:
            flag = 1
            k = i ** j % p
            print(f"${i}^{{{j}}} = {k}mod {p}$ \\quad")
            if k == 1:
                flag = 0
                break
        if flag == 1 and are_coprime(i,p)==1 :
            return i
    return -1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def reduced_residue_system(m):
    return [i for i in range(1, m) if gcd(i, m) == 1]



p=int(input("请输入一个素数p："))
a = euler_totient(p)
print(f"欧拉函数值为：{a}，")
prime_factors_list = prime_factors(a)
unique_prime_factors_list = list(set(prime_factors_list))
print(f"{a} 的素因数分解为：{unique_prime_factors_list}，")
ord_list = [a // i for i in unique_prime_factors_list]
print(f"欧拉函数除以g值为：{ord_list}，")
result=ord(ord_list, p)
if(result==-1):
    print("不存在原根")
    exit(0)
print(f"{result}是原根，")
len_ord=euler_totient(a)
print(f"模{p}的原根个数为{len_ord}，")
print(f"模欧拉函数：{a}的简化剩余系为：")
xi=reduced_residue_system(a)
print(xi)
for i in xi:
    gen=(result**i)%p
    print(f"${result}^{{{i}}}={gen}mod {p} $\\quad")