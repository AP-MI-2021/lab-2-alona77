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

def main():
    print("1. Verificarea proprietatii daca un nr este palindrom.")
    print("2. Combinari de n luate cate k.")
    print("3. Iesire din meniu")

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

if __name__ == '__main__':
  main()

