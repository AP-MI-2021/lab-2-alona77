def is_prime(x):
    if x <= 1:
        print("nu este prim")
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
        print(prefix)
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
    print("1. Verificare daca un nr este superprim")
    print("2. Conversia unui numar din baza 10 in baza 2")
    print("3. Iesire din meniu")

    opt=int(input("Introduceti optiunea dorita"))
    while True:
        if opt == 1:
            n=int(input("introduceti nr pentru a verifica daca este superprim "))
            if is_prime(n): 
               print("Numarul", n, "este superprim")
            else :
                print("Numarul", n, "nu ete superprim")
        elif opt == 2:
            x =str(input("introduceti numarul: "))
            print(get_base_2(x))
        elif opt == 3:
            break

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


    
