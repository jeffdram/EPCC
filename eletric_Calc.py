lei = int(input("Escolha a lei que deseja utilizar: \n1 - 1ª lei de Ohm (V = R*I_)\n"
                "2 - 2ª lei de Ohm (P = R*I)\n3 - 3ª A resistência"
                " equivalente em um circuito em série ou paralelo\n0. Sair\n"))  # Menu para a escolha de que lei se deseja usar
while not (lei == 0):  # Estrutura de escolha de lei
    if lei == 1:  # Calculo da primeira lei
        choose = int(input(
            "O que deseja descobrir?\n1 - voltagem\n2 - corrente\n3 - resistência\n"))  # Estrutura de escolha do que se deseja calcular
        if choose == 1:  # Calculo da voltagem
            corr = input("Insira a corrente (Utilize ',' no número): ")  # Inserir a corrente
            corrCalc = float(corr.replace(",", "."))  # Converte a vírgula em ponto

            r = input("Insira a resistência (Utilize ',' no número): ")  # Inserir a resistência
            rCalc = float(r.replace(",", "."))  # Converte a vírgula em ponto

            volt = float(corrCalc * rCalc)  # Calculo do valor da voltagem
            voltAnswer = str(volt)  # Converte a resposta em texto
            voltAnswer = voltAnswer.replace(".", ",")  # Converte o ponto em virgula
            print(f'A voltagem é {voltAnswer} V')  # Saída da informação do valor da voltagem
        elif choose == 2:  # Calculo da corrente
            volt = input("Insira a voltagem: ")  # Inserir o valor da voltagem
            voltCalc = float(volt.replace(",", "."))  # Converte a vírgula em ponto

            r = input("Insira a resistência: ")  # Inserir o valor da resistência
            rCalc = float(r.replace(",", "."))  # Converte a vírgula em ponto

            corr = float(voltCalc / rCalc)  # Calculo do valor da corrente
            corrAnswer = str(corr)  # Converte a resposta em texto
            corrAnswer = corrAnswer.replace(".", ",")  # Converte o ponto em virgula
            print(f'A corrente é {corrAnswer} A')  # Saída do valor da corrente
        elif choose == 3:  # Calculo da resistência
            volt = input("Insira a voltagem: ")  # Inserir o valor da voltagem
            voltCalc = float(volt.replace(",", "."))  # Converte a vírgula em ponto

            corr = input("Insira a corrente (Utilize ',' no número): ")  # Inserir a corrente
            corrCalc = float(corr.replace(",", "."))  # Converte a vírgula em ponto

            r = float(voltCalc / corrCalc)  # Calculo do valor da resistência
            rAnswer = str(r)  # Converte a resposta em texto
            rAnswer = rAnswer.replace(".", ",")  # Converte o ponto em virgula
            print(f'A resistência é {rAnswer} ohm')  # Saída do valor da resistência
        else:  # Caso o usuário digite uma opção não aceita
            print("Escolha não aceita!")  # Saída de mensagem de erro
    elif lei == 2:  # Calculo da segunda lei
        volt = input("Insira a voltagem: ")  # Inserir o valor da voltagem
        voltCalc = float(volt.replace(",", "."))  # Converte a vírgula em ponto

        corr = input("Insira a corrente (Utilize ',' no número): ")  # Inserir a corrente
        corrCalc = float(corr.replace(",", "."))  # Converte a vírgula em ponto

        p = float(voltCalc * corrCalc)  # Calculo do valor da potência
        pAnswer = str(p)  # Converte a resposta em texto
        pAnswer = pAnswer.replace(".", ",")  # Converte o ponto em virgula
        print(f'A potência é {pAnswer} W')  # Saída do valor da potência
    elif lei == 3:  # Calculo da 3ª lei
        system = int(input("1 - Circuito em série\n2 - Circuito em paralelo\n"))  # Escolha do tipo de circuito
        if system == 1:  # CIrcuiro em série
            amount = int(
                input("Insira a quantidade  de resistencias: "))  # Escolha da quantidade de resistencias do circuito
            rSum = float(0.0)
            rTotal = []  # Guardar todas as resistencias

            for x in range(amount):  # Pedir a resistencia x vezes (Como dito pelo usuario anteriormente)
                r = input("Insira o valor da resistencia: ")  # Pedir o valor da resistencia
                rNum = float(r.replace(",", "."))  # Troca de , por .
                rTotal.append(rNum)  # Junta o valor da resistencia a lista de valores do circuito

            for x in range(len(rTotal)):  # Leitura da lista e calculo da resistencia resultante
                rSum += rTotal[x]  # Soma dos valores da resistencia

            rSum_Answer = str(rSum)  # Converter números em texto
            rSum_Answer = rSum_Answer.replace(".", ",")  # Converter os pontos para virgulas
            print(
                f'O valor da resistência equivalente do circuito é {rSum_Answer} ohm')  # Saída do valor da resistência equivalente
        elif system == 2:
            amount = int(
                input("Insira a quantidade  de resistencias: "))  # Escolha da quantidade de resistencias do circuito
            rSum = float(0.0)
            rTotal = []  # Guardar todas as resistencias

            for x in range(amount):  # Pedir a resistencia x vezes (Como dito pelo usuario anteriormente)
                r = input("Insira o valor da resistencia: ")  # Pedir o valor da resistencia
                rNum = float(r.replace(",", "."))  # Troca de , por .
                rTotal.append(rNum)  # Junta o valor da resistencia a lista de valores do circuito

            for x in range(len(rTotal)):  # Leitura da lista e calculo da resistencia resultante
                rSum += (1 / rTotal[x])  # Soma dos valores da resistencia
            rSum = rSum ** -1  # Terminar o calculo da soma

            rSum_Answer = str(rSum)  # Converter números em texto
            rSum_Answer = rSum_Answer.replace(".", ",")  # Converter os pontos para virgulas
            print(
                f'O valor da resistência equivalente do circuito é {rSum_Answer} ohm')  # Saída do valor da resistência equivalente
        else:
            print("Opção inválida!")
    else:  # Caso o usuário digite uma opção não aceita
        print("Opção não aceita!\n")  # Mensagem de erro

    lei = int(input("\nEscolha a lei que deseja utilizar: \n1 - 1ª lei de Ohm (V = R*I_)\n"
                    "2 - 2ª lei de Ohm (P = R*I)\n3 - 3ª A resistência"
                    " equivalente em um circuito em série ou paralelo\n0. Sair\n"))  # Menu para a escolha de que lei se deseja usar
print("\n\n\n\nE N C E R R A N D O . . . . ")  # Mensagem de encerramento
