from typing import AbstractSet


def run():
    input = 'no importa'
    input_sin_espacios = input.replace(' ', '')
    reverse = input_sin_espacios[::-1]
    
    if input_sin_espacios == reverse:
        esPalindromo = True
    else:
        esPalindromo = False
    
    if esPalindromo == True:
        print(input + " - es palindromo")
    else:
        print(input + " - no es palindromo")
    #print(esPalindromo)
    #funcion anonima (lambda)
    #palindrome = lambda string: string.replace(' ', '') == string[::-1].replace(' ', '') #Variable stores the function value
    #print(palindrome(input)) # returns True

if __name__ == '__main__':
    run()
