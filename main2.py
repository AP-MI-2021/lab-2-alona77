def is_palindrome(n):
    """"
    5. Determină dacă un număr dat este palindrom.
    -Funcția principală: `is_palindrome(n) -> bool`
    -Funcția de test: `test_is_palindrome()`
    """
    c = n 
    p = 0
    while n >= 1:
         p = p * 10 + n % 10
         n = n // 10
    if c == p :
        return True
    else:
        return False

def get_n_choose_k(n,k):
    """
    10. Calculează combinări de `n` luate câte `k` (`n` și `k` date).
    - Funcția principală: `get_n_choose_k(n: int, k: int) -> int`
    - Funcția de test: `test_get_n_choose_k()`
    """
    na = 1
    fk = 1
    ni = 1    
    for i in range(1,n+1):
        na = na * i
    for i in range (1, k+1):
        fk = fk * i
    for i in range(1, n-k+1):
        ni = ni * i
    c= na // (ni * fk)
    return c

def is_prime(x):
    if x <= 1:
        False
    else:
        for i in range(2,x-1):
            if x % i == 0:
                return False
    return True

    
def is_superprime(n):
    """
    6.Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. De exemplu, 233 este superprim, deoarece 2, 23 și 233 sunt toate prime, dar 237 nu este superprim, deoarece 237 nu este prim.
    Funcția principală: is_superprime(n) -> bool
    Funcția de test: test_is_superprime()
    """
    copy=n
    c=0
    while n >= 1:
        c=c+1
        n=n//10
    puterea= 10**(c-1)
    for i in range (1,c+1):
        prefix = copy // puterea
        puterea = puterea // 10
        if is_prime(prefix)!=True:
            return False
    return True


def get_base_2(x):
    """ 
    Transformă un număr dat din baza 10 în baza 2. Numărul se dă în baza 10.
    Funcția principală: get_base_2(n: str) -> str
    Funcția de test: test_get_base_2()
    """
    n=int(x)
    putere = 1
    rez = 0
    while n > 0:
        cif = n % 2
        rez = rez + cif * putere
        putere = putere * 10
        n = n // 2
    return str(rez)


def main():
    print("1. Verificarea proprietatii daca un nr este palindrom.")
    print("2. Combinari de n luate cate k.")
    print("3. Verificare daca un nr este superprim")
    print("4. Conversia unui numar din baza 10 in baza 2")
    print("5. Iesire din meniu")

    while True:
        opt = int (input("Introduceti optiunea dorita"))
        if opt == 1:
            x = int(input("Introduceti numarul: "))
            if is_palindrome(x):
                print(x, 'Numarul  este palindrom \n')
            else :
                print(x, "Numarul nu este palindrom \n")

        elif opt == 2:
            n = int(input("n = "))
            k = int(input("k = "))
            if k <= n:
                print("Combinari de", n, "luate cate", k, "este", get_n_choose_k(n,k))
            else :
                print("Numerele introduse nu respecta ordinea")

        elif opt == 3:
            n=int(input("introduceti nr pentru a verifica daca este superprim "))
            if is_prime(n): 
               print("Numarul", n, "este superprim")
            else :
                print("Numarul", n, "nu ete superprim")

        elif opt == 4:
             x =str(input("introduceti numarul: "))
             print(get_base_2(x))
        else:
            break

def test_is_palindrom():
    assert is_palindrome(1234321) == True
    assert is_palindrome(45) == False
    assert is_palindrome(678) == False
    assert is_palindrome(454) == True
    assert is_palindrome(1) == True
    assert is_palindrome(6) == True

def test_get_n_choose_k():
    assert get_n_choose_k(12, 6) == 924
    assert get_n_choose_k(5, 3) == 10
    assert get_n_choose_k(10, 8) == 45
    assert get_n_choose_k(3,4) == 0
    assert get_n_choose_k(8, 10) == 0

def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(237) == False
    assert is_superprime(22) == False
    assert is_superprime(29) == True


def test_get_base_2():
    assert get_base_2(75) == 1001011
    assert get_base_2(12) == 1100 
    assert get_base_2(2) == 10

if __name__ == '__main__':
  main()

