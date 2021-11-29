def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return f"$ {numero} Fizz Buzz"
    elif numero % 5 == 0:
        return f"$ {numero} Buzz"
    elif numero % 3 == 0:
        return f"$ {numero} Fizz"
    else:
        return f"$ {numero}"

if __name__ == '__main__':
    sequence = '\n'.join(fizz_buzz(numero) for numero in range(1, 101))
    print(sequence)