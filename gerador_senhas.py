import random
import string


def gerar_senha_numerica(tamanho):
    numeros = string.digits
    senha = "".join(random.choice(numeros) for _ in range(tamanho))
    return senha


def gerar_senha_completa(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def pedir_tamanho():
    while True:
        entrada = input("Quantos caracteres você quer na senha? ")

        if entrada.isdigit() and int(entrada) >= 4:
            return int(entrada)

        print("Por favor, digite um número inteiro de pelo menos 4.")


def mostrar_menu():
    print("\n=== Gerador de Senhas ===")
    print("1 - Senha numérica  (ex: 482910)")
    print("2 - Senha completa  (ex: aB3#kL!9)")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()
    return opcao


def main():
    print("Bem-vindo ao gerador de senhas!")

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            tamanho = pedir_tamanho()
            senha = gerar_senha_numerica(tamanho)
            print(f"\nSua senha numérica: {senha}")

        elif opcao == "2":
            tamanho = pedir_tamanho()
            senha = gerar_senha_completa(tamanho)
            print(f"\nSua senha completa: {senha}")

        elif opcao == "0":
            print("\nAté mais!")
            break

        else:
            print("\nOpção inválida. Digite 1, 2 ou 0.")


if __name__ == "__main__":
    main()
