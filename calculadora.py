def main():
    try:
        primeiro_numero = float(input("Digite o primeiro numero: "))
        segundo_numero = float(input("Digite o segundo numero: "))
    except ValueError:
        print("Entrada invalida. Digite apenas numeros reais.")
        return

    operacao = input("Escolha a operacao (+, -, *, /): ").strip()

    if operacao == "+":
        resultado = primeiro_numero + segundo_numero
    elif operacao == "-":
        resultado = primeiro_numero - segundo_numero
    elif operacao == "*":
        resultado = primeiro_numero * segundo_numero
    elif operacao == "/":
        if segundo_numero == 0:
            print("Nao e possivel dividir por zero.")
            return
        resultado = primeiro_numero / segundo_numero
    else:
        print("Operacao invalida.")
        return

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()