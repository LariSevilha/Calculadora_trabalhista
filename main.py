#funções para calcular
def calcfe():
     while not (sal := input(f"Salário bruto: ")).isdigit() or (sal := int(sal)) < 0 or sal > 1000000:
          print('Valor inválido, por favor digite apenas números')
     while not (meses := input(f"Meses trabalhados:  ")).isdigit() or (meses := int(meses)) < 0 or meses > 1000000:
         print('Valor inválido, por favor digite apenas números')
     tot = (sal * meses/12) + sal /3
     print("O valor da suas férias é: ","%.2f" % tot) #esse operador matemático vai imprimir 2 números da casa decimais após a virgula.

def calcfg():
    while not (sala := input(f"Salário bruto: ")).isdigit() or (sala := int(sala)) < 0 or sala > 1000000:
        print('Valor inválido, por favor digite apenas números')
    tot_fgts = (8 / 100 ) * sala 
    print("Seu depósito mensal é: ","%.2f" % tot_fgts)

def seg():
    while not (ult := input(f"Qual o valor do seu ultimo salario? ")).isdigit() or (ult := int(ult)) < 0 or ult > 1000000:
        print('Valor inválido, por favor digite apenas números')
    while not (penul := input(f"Qual o valor do seu penultimo salario? ")).isdigit() or (penul := int(penul)) < 0 or penul > 1000000:
         print('Valor inválido, por favor digite apenas números')
    while not (ant := input(f"Qual o valor do seu antipenultimo salario? ")).isdigit() or (ant := int(ant)) < 0 or ant > 1000000:
         print('Valor inválido, por favor digite apenas números')
    while not (meses := input(f"Quantos meses voce trabalhou até a dispensa? ")).isdigit() or (meses := int(meses)) < 0 or meses >  10000:
         print('Valor inválido, por favor digite apenas números')         
    if meses < 9:
        print("Voce não tem direito ao seguro desemprego.")
    else:
        media = ult + penul + ant / 3
        if media > 1.858:
            media * 0,80
        elif media <= 1.859 >=  3.097:
            media * 0,5 +1.350
        elif media < 3.097:
            media = 2.106
        print("O seu seguro é de: ","%.2f" % media) 
 #função principal
def main():
 #menu
  while True:
    print("\n\n ============= Calculadora trabalhista ============= \n\n 1- Calcular Férias \n\n 2- Calcular FGTS \n\n 3- Calcular seguro desemprego \n\n 4- Sair ")
    print("--------- Escolha uma opção: -------- \n\n")
    resp = int(input("Digite: "))

    if resp == 1:
     print("============= Calculo de férias ============= ")
     calcfe()
    elif resp == 2:
      print("============= Calcular Fgts ============= ")
      calcfg()
    elif resp == 3:
        print("============= Seguro desemprego ============= ")
        seg()
    elif resp == 4:
        break
    else:
        print("Opção inválida")
        main()
main()
