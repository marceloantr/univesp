## conversor.py
# Converte um número de base decimal para qualquer outra base (entre 0 e 36),
# utilizando letras como dígitos acima de 9.
# A partir de um número decimal fornecido pelo usuário, e pela base indicada, 
# converte o número a partir do método de sucessivas divisões com resto.

# Pergunta -- input() -- o número a ser convertido e a base, convertendo o valor informado em 
# número inteiro  -- int().
# Utiliza try/except para exceção de número digitado de maneira errada (impossível de ser convertido em inteiro).
try:
    num = int(input("Número a ser convertido em base decimal: "))
    base = int(input("Base para a qual converter: "))
except:
    print("Números fornecidos em formato incorreto.")
    exit()

# Cria duas listas em branco: uma para os dígitos do resto, e outra para os 
# algarismos na base solicitada.
resto_digitos = []
algarismos = []

# Só roda o programa se a base estiver entre 1 e 36
if base >= 1:
    if base <= 36:

        # Se a base for menor que 10, utiliza apenas os algarismos indo-arábicos
        if base <= 10:
            algarismos.extend(range(0,base))
        
        # Se a base for maior que 10, utiliza letras em ordem alfabética para os dígitos.
        else:
            algarismos.extend(range(0,9))

            # Roda um loop acrescentando letras para cada valor acima de 9, até o limite do total da base.
            # Como só é possível recorrer a 26 letras, o programa está limitado a no máximo base 36.
            for i in range(10,base):
                algarismos.append(chr(i - 10 + ord('a'))) # A função chr() retorna o caractere correspondente ao valor inteiro,
                                                          # que por sua vez é definido com o valor ordinal do caractere 'a', 
                                                          # somado a posição após 10 de cada algarismo a ser criado.
                                                          # Na maioria das codificações, a letra a corresponde ao valor ordinal 97,
                                                          # de modo que 98 será a letra b, e assim por diante.

        # Outra limitação é realizar a operação apenas com números maiores que 0, por enquanto. Faz o teste.
        if num > 0:
            # Realiza a primeira divisão inteira, e também computa o resto.
            # 'quociente' receberá o resultado da divisão sem resto, que será usado 
            # nas divisões posteriores.
            quociente = num // base
            resto = num % base
            
            # Já acrescenta à lista de dígitos o primeiro resto.
            # Esta lista acrescenta um número decimal, indicando a posição na lista do 
            # algarismo que será chamado na impressão, posteriormente.
            resto_digitos.append(resto)

            # Continua a rodar o programa enquanto o quociente da divisão inteira for diferente de 0.
            while quociente != 0:
                resto = quociente % base
                quociente = quociente // base
                resto_digitos.append(resto)
                
            # Imprime o número convertido.
            print("Número convertido: ",end='')
            # Utiliza a função .pop() para ir retornando os últimos dígitos acrescentados, que serão escritos da esquerda
            # para a direita.
            while len(resto_digitos) > 0:
                digito = resto_digitos.pop()
                # Imprime o algarismo correspondente ao valor na base solicitada. As listas em Python são indexadas 
                # a partir de 0, portanto o valor do primeiro algarismo estará na posição 0. Assim, 
                # é preciso subtrair 1 do valor, a fim de encontrar a posição do algarismo.
                print(algarismos[digito-1],end='')
            print("")
        
        # Tratamento simples de erros, como números negativos e bases fora do padrão.
        else:
            print("No momento, este programa só realiza conversão de números positivos.")
    else:
        print("A base precisa ser menor ou igual a 36!")
else:
    print("A base precisa ser maior que 0!")