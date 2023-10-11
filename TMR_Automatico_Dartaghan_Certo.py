import math

def Athos (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
    notaDoAluno_foco = notaDoAluno*0.5
    presençaDoAluno_defoque = presençaDoAluno_Tratada*0.25
    rendimentoFinal_defoque = rendimentoFinal_Tratado*0.25
    notaDeComportamento_foco = notaDeComportamento*0.5
    somaFinalAthos = notaDoAluno_foco + presençaDoAluno_defoque + rendimentoFinal_defoque + notaDeComportamento_foco

    if (somaFinalAthos >= 10.5):
        votoAthos = 1
    else:
        votoAthos = 0

    listaAthos= [votoAthos,somaFinalAthos]

    return(listaAthos)

def Aramis (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
    notaDoAluno_foco = notaDoAluno*0.5
    presençaDoAluno_defoque = presençaDoAluno_Tratada*0.25
    rendimentoFinal_foco = rendimentoFinal_Tratado*0.5
    notaDeComportamento_desfoque = notaDeComportamento*0.25
    somaFinalAramis = notaDoAluno_foco + presençaDoAluno_defoque + rendimentoFinal_foco + notaDeComportamento_desfoque
    
    if (somaFinalAramis >= 10.5):
        votoAramis = 1
    else:
        votoAramis = 0
    
    listaAramis= [votoAramis,somaFinalAramis]

    return(listaAramis)

def Porthos (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
    notaDoAluno_defoque = notaDoAluno*0.25
    presençaDoAluno_foco = presençaDoAluno_Tratada*0.5
    rendimentoFinal_foco = rendimentoFinal_Tratado*0.5
    notaDeComportamento_desfoque = notaDeComportamento*0.25
    somaFinalPorthos = notaDoAluno_defoque + presençaDoAluno_foco + rendimentoFinal_foco + notaDeComportamento_desfoque

    if (somaFinalPorthos >= 10.5):
        votoPorthos = 1
    else:
        votoPorthos = 0

    listaPorthos= [votoPorthos,somaFinalPorthos]
    
    return(listaPorthos)

def Dartaghan (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento):
    def Dartaghan1 (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento):
            def Athos (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
                notaDoAluno_foco = notaDoAluno*0.5
                presençaDoAluno_defoque = presençaDoAluno_Tratada*0.25
                rendimentoFinal_defoque = rendimentoFinal_Tratado*0.25
                notaDeComportamento_foco = notaDeComportamento*0.5
                somaFinalAthos = notaDoAluno_foco + presençaDoAluno_defoque + rendimentoFinal_defoque + notaDeComportamento_foco

                if (somaFinalAthos >= 10.5):
                    votoAthos = 1
                else:
                    votoAthos = 0

                listaAthos= [votoAthos,somaFinalAthos]

                return(listaAthos)

            def Aramis (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
                notaDoAluno_foco = notaDoAluno*0.5
                presençaDoAluno_defoque = presençaDoAluno_Tratada*0.25
                rendimentoFinal_foco = rendimentoFinal_Tratado*0.5
                notaDeComportamento_desfoque = notaDeComportamento*0.25
                somaFinalAramis = notaDoAluno_foco + presençaDoAluno_defoque + rendimentoFinal_foco + notaDeComportamento_desfoque
                
                if (somaFinalAramis >= 10.5):
                    votoAramis = 1
                else:
                    votoAramis = 0
                
                listaAramis= [votoAramis,somaFinalAramis]

                return(listaAramis)

            def Porthos (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
                notaDoAluno_defoque = notaDoAluno*0.25
                presençaDoAluno_foco = presençaDoAluno_Tratada*0.5
                rendimentoFinal_foco = rendimentoFinal_Tratado*0.5
                notaDeComportamento_desfoque = notaDeComportamento*0.25
                somaFinalPorthos = notaDoAluno_defoque + presençaDoAluno_foco + rendimentoFinal_foco + notaDeComportamento_desfoque

                if (somaFinalPorthos >= 10.5):
                    votoPorthos = 1
                else:
                    votoPorthos = 0

                listaPorthos= [votoPorthos,somaFinalPorthos]
                
                return(listaPorthos)
            

            varPorthos = Porthos(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)
            varAthos = Athos(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)
            varAramis = Aramis(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)

            votoPorthos = varPorthos[0]
            votoAthos = varAthos [0]
            votoAramis = varAramis [0]

            julgamentoFinal_PrimeiraMaquina = votoAramis+votoPorthos+votoAthos

            return(julgamentoFinal_PrimeiraMaquina)

    def Dartaghan2 (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento):
            def Athos (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
                notaDoAluno_foco = notaDoAluno*0.5
                presençaDoAluno_defoque = presençaDoAluno_Tratada*0.25
                rendimentoFinal_defoque = rendimentoFinal_Tratado*0.25
                notaDeComportamento_foco = notaDeComportamento*0.5
                somaFinalAthos = notaDoAluno_foco + presençaDoAluno_defoque + rendimentoFinal_defoque + notaDeComportamento_foco

                if (somaFinalAthos >= 10.5):
                    votoAthos = 1
                else:
                    votoAthos = 0

                listaAthos= [votoAthos,somaFinalAthos]

                return(listaAthos)

            def Aramis (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
                notaDoAluno_foco = notaDoAluno*0.5
                presençaDoAluno_defoque = presençaDoAluno_Tratada*0.25
                rendimentoFinal_foco = rendimentoFinal_Tratado*0.5
                notaDeComportamento_desfoque = notaDeComportamento*0.25
                somaFinalAramis = notaDoAluno_foco + presençaDoAluno_defoque + rendimentoFinal_foco + notaDeComportamento_desfoque
                
                if (somaFinalAramis >= 10.5):
                    votoAramis = 1
                else:
                    votoAramis = 0
                
                listaAramis= [votoAramis,somaFinalAramis]

                return(listaAramis)

            def Porthos (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
                notaDoAluno_defoque = notaDoAluno*0.25
                presençaDoAluno_foco = presençaDoAluno_Tratada*0.5
                rendimentoFinal_foco = rendimentoFinal_Tratado*0.5
                notaDeComportamento_desfoque = notaDeComportamento*0.25
                somaFinalPorthos = notaDoAluno_defoque + presençaDoAluno_foco + rendimentoFinal_foco + notaDeComportamento_desfoque

                if (somaFinalPorthos >= 10.5):
                    votoPorthos = 1
                else:
                    votoPorthos = 0

                listaPorthos= [votoPorthos,somaFinalPorthos]
                
                return(listaPorthos)
            

            varPorthos = Porthos(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)
            varAthos = Athos(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)
            varAramis = Aramis(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)

            votoPorthos = varPorthos[0]
            votoAthos = varAthos [0]
            votoAramis = varAramis [0]

            julgamentoFinal_SegundaMaquina = votoAramis+votoPorthos+votoAthos

            return(julgamentoFinal_SegundaMaquina)

    def Dartaghan3 (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento):
            def Athos (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
                notaDoAluno_foco = notaDoAluno*0.5
                presençaDoAluno_defoque = presençaDoAluno_Tratada*0.25
                rendimentoFinal_defoque = rendimentoFinal_Tratado*0.25
                notaDeComportamento_foco = notaDeComportamento*0.5
                somaFinalAthos = notaDoAluno_foco + presençaDoAluno_defoque + rendimentoFinal_defoque + notaDeComportamento_foco

                if (somaFinalAthos >= 10.5):
                    votoAthos = 1
                else:
                    votoAthos = 0

                listaAthos= [votoAthos,somaFinalAthos]

                return(listaAthos)

            def Aramis (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
                notaDoAluno_foco = notaDoAluno*0.5
                presençaDoAluno_defoque = presençaDoAluno_Tratada*0.25
                rendimentoFinal_foco = rendimentoFinal_Tratado*0.5
                notaDeComportamento_desfoque = notaDeComportamento*0.25
                somaFinalAramis = notaDoAluno_foco + presençaDoAluno_defoque + rendimentoFinal_foco + notaDeComportamento_desfoque
                
                if (somaFinalAramis >= 10.5):
                    votoAramis = 1
                else:
                    votoAramis = 0
                
                listaAramis= [votoAramis,somaFinalAramis]

                return(listaAramis)

            def Porthos (notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento,):
                notaDoAluno_defoque = notaDoAluno*0.25
                presençaDoAluno_foco = presençaDoAluno_Tratada*0.5
                rendimentoFinal_foco = rendimentoFinal_Tratado*0.5
                notaDeComportamento_desfoque = notaDeComportamento*0.25
                somaFinalPorthos = notaDoAluno_defoque + presençaDoAluno_foco + rendimentoFinal_foco + notaDeComportamento_desfoque

                if (somaFinalPorthos >= 10.5):
                    votoPorthos = 1
                else:
                    votoPorthos = 0

                listaPorthos= [votoPorthos,somaFinalPorthos]
                
                return(listaPorthos)
            

            varPorthos = Porthos(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)
            varAthos = Athos(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)
            varAramis = Aramis(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)

            votoPorthos = varPorthos[0]
            votoAthos = varAthos [0]
            votoAramis = varAramis [0]

            julgamentoFinal_TerceiraMaquina = votoAramis+votoPorthos+votoAthos

            return(julgamentoFinal_TerceiraMaquina)

    votoDartaghan = Dartaghan1(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)+ Dartaghan2(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)+ Dartaghan3(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)
        
    if (votoDartaghan == 9):
        return(print("Dartaghan não encontrou nenhum conflito de resutaltado"))

    else:
        diferençaDartaghan1 = abs((Dartaghan1(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento) - Dartaghan2(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)))
        MediaDartaghan1 = (Dartaghan1(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento) + Dartaghan2(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento))/2
        erroDartaghan1 = diferençaDartaghan1/MediaDartaghan1
        porcentualErroDartaghan1 = erroDartaghan1*100

        diferençaDartaghan2 = abs((Dartaghan2(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento) - Dartaghan3(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)))
        MediaDartaghan2 = (Dartaghan2(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento) + Dartaghan3(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento))/2
        erroDartaghan2 = diferençaDartaghan2/MediaDartaghan2
        porcentualErroDartaghan2 = erroDartaghan2*100

        diferençaDartaghan3 = abs((Dartaghan1(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento) - Dartaghan3(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)))
        MediaDartaghan3 = (Dartaghan1(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento) + Dartaghan3(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento))/2
        erroDartaghan3 = diferençaDartaghan3/MediaDartaghan3
        porcentualErroDartaghan3 = erroDartaghan3*100


        return(print(f"Dartaghan encontrou divergências matemáticas, no caso a incongruência é:\nDo Primeiro sistema com o segundo{erroDartaghan1} ou {porcentualErroDartaghan1}%\nDo Primeiro sistema com o terceiro{erroDartaghan3} ou {porcentualErroDartaghan3}%\nDo Segundo sistema com o Terceiro{erroDartaghan2} ou {porcentualErroDartaghan2}%"))

notaDoAluno = float(input("Qual a nota do aluno? "))
presençaDoAluno = float(input("Qual a presença, apenas o valor da porcentagem, do aluno? "))
rendimento_AtividadesPedidas = float(input("Quantas atividades você, professor, pediu? "))
rendimento_AtividadesFeitas = float(input("Quantas atividades o aluno fez? "))
notaDeComportamento = float(input("Qual a nota de comportamento do aluno? "))

#Tratamento de dados especiais

presençaDoAluno_Tratada = presençaDoAluno/10
rendimentoFinal = (rendimento_AtividadesFeitas*100)/rendimento_AtividadesPedidas

rendimentoFinal_Tratado = rendimentoFinal/10

varPorthos = Porthos(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)
varAthos = Athos(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)
varAramis = Aramis(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)

votoPorthos = varPorthos[0]
votoAthos = varAthos [0]
votoAramis = varAramis [0]

valorPorthos = varPorthos[1]
valorAthos = varAthos [1]
valorAramis = varAramis [1]

julgamentoFinal = votoAramis+votoPorthos+votoAthos


dar = Dartaghan(notaDoAluno,presençaDoAluno_Tratada,rendimentoFinal_Tratado,notaDeComportamento)


if (julgamentoFinal > 2):
    print (f"O aluno foi aprovado pelo TMR, com totalidade, com as notas de cada função sendo \n Athos:{round(valorAthos,2)} \n Aramis:{round(valorAramis,2)} \n Porthos:{round(valorPorthos,2)}")
    print(dar)

elif (julgamentoFinal == 2):
    if (votoAramis == 0):
        discrepante = "Aramis"
    
    elif (votoAthos == 0):
        discrepante = "Athos"

    elif (votoPorthos == 0):
        discrepante = "Porthos"
    
    print (f"O aluno foi aprovado pelo TMR, sem a totalidade, pois o {discrepante} discordou, com as notas de cada função sendo \n Athos:{round(valorAthos,2)} \n Aramis:{round(valorAramis,2)} \n Porthos:{round(valorPorthos,2)}")
    print(dar)
elif (julgamentoFinal < 2):
    if (julgamentoFinal == 1):
        if (votoAramis == 1):
            discrepante = "Aramis"
    
        elif (votoAthos == 1):
            discrepante = "Athos"

        elif (votoPorthos == 1):
            discrepante = "Porthos"
        
        print (f"O aluno foi reprovado pelo TMR, sem a totalidade, pois o {discrepante} discordou, com as notas de cada função sendo \n Athos:{round(valorAthos,2)} \n Aramis:{round(valorAramis,2)} \n Porthos:{round(valorPorthos,2)}")
        print(dar)
    elif (julgamentoFinal==0):
         print (f"O aluno foi reprovado pelo TMR, com totalidade, com as notas de cada função sendo \n Athos:{round(valorAthos,2)} \n Aramis:{round(valorAramis,2)} \n Porthos:{round(valorPorthos,2)}")
         print(dar)




