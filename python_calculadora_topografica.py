from functools import partial
from tkinter import *
import math

# FUNÇÕES:

def Calcular_AreaDoPoligono():

    lista_de_coordenadas_x = []
    lista_de_coordenadas_y = []
    numero_de_pontos_poligono = int(input("Quantos pontos o polígono possui? "))
    while len(lista_de_coordenadas_x) < numero_de_pontos_poligono:
        proximo_ponto=len(lista_de_coordenadas_x) + 1
        x,y = input("Digite as coordenadas do ponto {}(Ex: 102.25, 47.81): ".format(proximo_ponto)).split(",")
        x = float(x)
        y = float(y)
        lista_de_coordenadas_x.append(x)
        lista_de_coordenadas_y.append(y)

    z = 0
    zz = 1
    area1 = []
    area2 = []
    while z < numero_de_pontos_poligono -1:
        expressao1 = lista_de_coordenadas_x[z] * lista_de_coordenadas_y[zz]
        expressao2 = lista_de_coordenadas_y[z] * lista_de_coordenadas_x[zz]
        area1.append(expressao1)
        area2.append(expressao2)
        if z < numero_de_pontos_poligono -1:
            z = z + 1
        else:
            z = z
        if zz < numero_de_pontos_poligono -1:
            zz = zz + 1
        else:
            zz = zz

    expressao1 = lista_de_coordenadas_x[-1] * lista_de_coordenadas_y[0]
    expressao2 = lista_de_coordenadas_y[-1] * lista_de_coordenadas_x[0]
    area1.append(expressao1)
    area2.append(expressao2)
    soma_area1 = sum(area1)
    soma_area2 = sum(area2)
    area = (soma_area1 - soma_area2)/2
    if area < 0:
        area = area * -1
    else:
        area = area

    print("S = ({:.3f} - {:.3f}))/2".format(soma_area1, soma_area2))
    print("A área do polígono é de {:.3f}m²".format(area))

def Calcular_Rumo(grau_Azimute, minuto_Azimute, segundo_Azimute):
    grau_Azimute=int(grau_Azimute)
    minuto_Azimute=int(minuto_Azimute)
    segundo_Azimute=int(segundo_Azimute)

    if grau_Azimute == 90 and minuto_Azimute == 0:
        resposta_rumo= (
            "Rumo = {}º {}′ {}” NE. Primeiro quadrante".format(
            grau_Azimute, minuto_Azimute, segundo_Azimute))
        return resposta_rumo

    elif grau_Azimute < 90:
        resposta_rumo= (
            "Rumo = {}º {}′ {}” NE. Primeiro quadrante.".format(
            grau_Azimute, minuto_Azimute, segundo_Azimute))
        return resposta_rumo

    elif grau_Azimute == 90 and minuto_Azimute >= 1:
        rumo=180 - grau_Azimute
        resposta_rumo = ("Rumo = {}º {}′ {}” SE. Segundo quadrante.".format(rumo, minuto_Azimute,
                                                                                               segundo_Azimute))
        return resposta_rumo

    elif grau_Azimute > 90 and grau_Azimute < 180:
        rumo=180 - grau_Azimute
        resposta_rumo= ("Rumo = {}º {}′ {}” SE. Segundo quadrante.".format(rumo, minuto_Azimute,
                                                                                               segundo_Azimute))
        return resposta_rumo

    elif grau_Azimute == 180 and minuto_Azimute == 0:
        rumo=180 - grau_Azimute
        resposta_rumo= ("Rumo = {}º {}′ {}” SE. Segundo quadrante.".format(rumo, minuto_Azimute,
                                                                                               segundo_Azimute))
        return resposta_rumo

    elif grau_Azimute == 180 and minuto_Azimute >= 1:
        rumo=grau_Azimute - 180
        resposta_rumo= ("Rumo = {}º {}′ {}” SW. Terceiro quadrante.".format(rumo, minuto_Azimute,
                                                                                                segundo_Azimute))
        return resposta_rumo

    elif grau_Azimute > 180 and grau_Azimute < 270:
        rumo=grau_Azimute - 180
        resposta_rumo= ("Rumo = {}º {}′ {}” SW. Terceiro quadrante.".format(rumo, minuto_Azimute,
                                                                                                segundo_Azimute))
        return resposta_rumo

    elif grau_Azimute == 270 and minuto_Azimute == 0:
        rumo=grau_Azimute - 180
        resposta_rumo= ("Rumo = {}º {}′ {}” SW. Terceiro quadrante.".format(rumo, minuto_Azimute,
                                                                                                segundo_Azimute))
        return resposta_rumo

    elif grau_Azimute == 270 and minuto_Azimute >= 1:
        rumo=360 - grau_Azimute
        resposta_rumo= ("Rumo = {}º {}′ {}” NW. Quarto quadrante.".format(rumo, minuto_Azimute,
                                                                                              segundo_Azimute))
        return resposta_rumo

    elif grau_Azimute > 270 and grau_Azimute <= 360:
        rumo=360 - grau_Azimute
        resposta_rumo= ("Rumo = {}º {}′ {}” NW. Quarto quadrante.".format(rumo, minuto_Azimute,
                                                                                              segundo_Azimute))
        return resposta_rumo
    pass

def Conversor_Azi4Rad(grau_xA, minuto_xA, segundo_xA):
    grau_xA=int(grau_xA)  ############## AZIMUTE A
    minuto_xA=int(minuto_xA)  ########## AZIMUTE A
    segundo_xA=int(segundo_xA)  ####### AZIMUTE A

    grau_xA_decimal=grau_xA  ##################################################### AZIMUTE A : CONVERTENDO GRAUS PARA DECIMAIS
    minuto_xA_decimal=minuto_xA / 60  ############################################ AZIMUTE A : CONVERTENDO GRAUS PARA DECIMAIS
    segundo_xA_decimal=segundo_xA / 3600  ######################################## AZIMUTE A : CONVERTENDO GRAUS PARA DECIMAIS
    valor_xA_decimal=grau_xA_decimal + minuto_xA_decimal + segundo_xA_decimal  ### VALOR AZIMUTE A DECIMAL

    valor_azimute_radianos=math.radians(valor_xA_decimal)  # CONVERTENDO O VALOR DO AZIMUTE DECIMAL PARA RADIANOS
    return valor_azimute_radianos

def Calculadora_Coordenada_X(distanciaAB, valor_azimute_radianos, coordenadaX_pontoA):
    coordenadaX_pontoA=float(coordenadaX_pontoA)
    senAzimute_pontoA=math.sin(valor_azimute_radianos)  ###### SENO AZIMUTE PONTO A
    coordX_pontoB=distanciaAB * senAzimute_pontoA + coordenadaX_pontoA  ###### COORDENADA X DO PONTO B
    return coordX_pontoB

def Calculadora_Coordenada_Y(distanciaAB, valor_azimute_radianos, coordenadaY_pontoA):
    coordenadaY_pontoA=float(coordenadaY_pontoA)
    cosAzimute_pontoA=math.cos(valor_azimute_radianos)  ###### COSSENO AZIMUTE PONTO A
    coordY_pontoB=distanciaAB * cosAzimute_pontoA + coordenadaY_pontoA  ###### COORDENADA Y DO PONTO B
    return coordY_pontoB

def Calculadora_Azimute_B(anguloExterno_grau, anguloExterno_minuto, anguloExterno_segundo, grau_azimuteA,
                          minuto_azimuteA, segundo_azimuteA):
    grau_azimuteA=int(grau_azimuteA)
    minuto_azimuteA=int(minuto_azimuteA)
    segundo_azimuteA=int(segundo_azimuteA)

    anguloExterno_grau=int(anguloExterno_grau)  ##########
    anguloExterno_minuto=int(anguloExterno_minuto)  ###### ÂNGULO CONVERTIDO
    anguloExterno_segundo=int(anguloExterno_segundo)  ####

    grau_beta=anguloExterno_grau - 180  ################## GRAU BETA - 180º
    azimuteB_grau=grau_azimuteA - grau_beta  #################### AZIMUTE B
    azimuteB_minuto=minuto_azimuteA - anguloExterno_minuto  #### AZIMUTE B
    azimuteB_segundo=segundo_azimuteA - anguloExterno_segundo  # AZIMUTE B

    if grau_beta < 0:
        grau_beta = grau_beta * -1
    else:
        grau_beta = grau_beta

    ############## AJUSTE DE GRAUS, MINUTOS E SEGUNDOS NA SUBTRAÇÃO
    if azimuteB_grau < 0:
        azimuteB_grau = azimuteB_grau + 360

    if azimuteB_segundo < 0:
        azimuteB_minuto=azimuteB_minuto - 1
        azimuteB_segundo=azimuteB_segundo + 60

    if azimuteB_minuto < 0:
        azimuteB_grau=azimuteB_grau - 1
        azimuteB_minuto=azimuteB_minuto + 60

    lista_azimute_B=[azimuteB_grau, azimuteB_minuto, azimuteB_segundo]
    print("\nAzB = AzA - Beta\nBeta = Ângulo Externo - 180º\nBeta = {}º {}′ {}”.\nAzB =  {}º {}′ {}” - {}º {}′ {}”.\nO azimute B é {}º {}′ {}”.".format(grau_beta, anguloExterno_minuto, anguloExterno_segundo,grau_azimuteA, minuto_azimuteA, segundo_azimuteA, grau_beta, anguloExterno_minuto, anguloExterno_segundo,lista_azimute_B[0], lista_azimute_B[1], lista_azimute_B[2]))
    respostaAzimuteB = ("AzB = AzA - Beta\nBeta = Ângulo Externo - 180º\nBeta = {}º {}′ {}”.\nAzB =  {}º {}′ {}” - {}º {}′ {}”.\nO azimute B é {}º {}′ {}”.".format(grau_beta, anguloExterno_minuto, anguloExterno_segundo,grau_azimuteA, minuto_azimuteA, segundo_azimuteA, grau_beta, anguloExterno_minuto, anguloExterno_segundo,lista_azimute_B[0], lista_azimute_B[1], lista_azimute_B[2]))

    return lista_azimute_B, respostaAzimuteB

def Calcular_Coordenadas_TKINTER():
    distanciaAB = entry_distancia.get()
    distanciaAB = float(distanciaAB)
    grau_xA, minuto_xA, segundo_xA = entry_azimuteA.get().split(",")
    coordX_pontoA, coordY_pontoA = entry_coordA.get().split(",")
    azimuteA_radiano = Conversor_Azi4Rad(grau_xA, minuto_xA, segundo_xA)
    coordenada_x_pontoB = Calculadora_Coordenada_X(distanciaAB, azimuteA_radiano, coordX_pontoA)
    coordenada_y_pontoB = Calculadora_Coordenada_Y(distanciaAB, azimuteA_radiano, coordY_pontoA)
    print("\nXb = Dab x Sen (AZa) + Coord. Xa")
    print("Xb = {} x Sen ({}° {}’ {}’’) + {} = {:.2f}m".format(distanciaAB, grau_xA, minuto_xA, segundo_xA, coordX_pontoA,
                                                          coordenada_x_pontoB))
    print("\nYb = Dab x Cos (AZa) + Coord. Ya")
    print("Yb = {} x Cos ({}° {}’ {}’’) + {} = {:.2f}m".format(distanciaAB, grau_xA, minuto_xA, segundo_xA, coordY_pontoA,
                                                               coordenada_y_pontoB))
    print("\nAs coordenadas de B são {:.2f}, {:.2f}.".format(coordenada_x_pontoB, coordenada_y_pontoB))
    lb_resultadoCoord["text"] = "Xb = Dab x Sen (AZa) + Coord. Xa\nXb = {} x Sen ({}° {}’ {}’’) + {} = {:.2f}m\n\nYb = Dab x Cos (AZa) + Coord. Ya\nYb = {} x Cos ({}° {}’ {}’’) + {} = {:.2f}m\n\nAs coordenadas de B são {:.2f}, {:.2f}.".format(distanciaAB, grau_xA, minuto_xA, segundo_xA, coordX_pontoA,
                                                          coordenada_x_pontoB,distanciaAB, grau_xA, minuto_xA, segundo_xA, coordY_pontoA,
                                                               coordenada_y_pontoB,coordenada_x_pontoB, coordenada_y_pontoB)

def Calcular_AziRumo_TKINTER():
    grau_xA, minuto_xA, segundo_xA= entry_azimuteA2.get().split(",")
    anguloExterno_grauB, anguloExterno_minutoB, anguloExterno_segundoB= entry_anguloex.get().split(",")
    lista_azimute_B, azimuteB=Calculadora_Azimute_B(anguloExterno_grauB, anguloExterno_minutoB, anguloExterno_segundoB, grau_xA,
                                          minuto_xA, segundo_xA)
    rumoB=Calcular_Rumo(lista_azimute_B[0], lista_azimute_B[1], lista_azimute_B[2])
    lb_resultadoAziRumo["text"] = "{}\n\n{}".format(rumoB, azimuteB)

def Fechar():
    exit()

janela = Tk()
janela.title("Calculadora Topográfica")
janela["background"] = "linen"
janela.geometry("800x680+280+10")

################################## TEXTOS, ENTRADAS E BOTÕES:

################################ calcular coordenadas do ponto B ##################################
lb_tituloCoord = Label(janela, text="Calculadora de Coordenada")
lb_tituloCoord.place(x=50, y=10)

### distancia
lb_distancia = Label(janela, text="Distância (Ex: 122.12)")
lb_distancia.place(x=10, y=40)

entry_distancia = Entry(janela, width=10)
entry_distancia.place(x=180, y=40)

### azimute A
lb_azimuteA = Label(janela, text="Azimute A (Ex:41,8,12)")
lb_azimuteA.place(x=10, y=70)

entry_azimuteA = Entry(janela, width=10)
entry_azimuteA.place(x=180, y=70)

### coordenadas A
lb_coordA = Label(janela, text="Coordenadas A (Ex:654,120)")
lb_coordA.place(x=10, y=100)

entry_coordA = Entry(janela, width=10)
entry_coordA.place(x=180, y=100)

### botao calcular coordenada
bt_calcularCoord = Button(janela, width=20, text="Calcular Coordenadas", command=Calcular_Coordenadas_TKINTER)
bt_calcularCoord.place(x=50, y=130)

######## CALCULANDO
lb_resultadoCoord = Label(janela, text="")
lb_resultadoCoord.place(x=5, y=170)

############ calculadora de azimute e rumo

lb_tituloAziRumo = Label(janela, text="Calculadora de Azimute e Rumo")
lb_tituloAziRumo.place(x=325, y=10)

lb_azimuteA2 = Label(janela, text="Azimute A (Ex:41,8,12)")
lb_azimuteA2.place(x=300, y=40)

entry_azimuteA2 = Entry(janela, width=10)
entry_azimuteA2.place(x=460, y=40)

lb_anguloex = Label(janela, text="Angulo Externo (Ex:41,8,12)")
lb_anguloex.place(x=300, y=70)

entry_anguloex = Entry(janela, width=10)
entry_anguloex.place(x=460, y=70)

### botao calcular azimute e rumo

bt_calcularAziRumo = Button(janela, width=20, text="Calcular Azimute e Rumo", command=Calcular_AziRumo_TKINTER)
bt_calcularAziRumo.place(x=340, y=130)

lb_resultadoAziRumo = Label(janela, text="")
lb_resultadoAziRumo.place(x=300, y=170)

############### calculadora de área do poligono
#preciso saber quantos pontos o poligono possui e as coordenadas

lb_tituloAreaPoligono = Label(janela, text="Calculadora de Área do Polígono")
lb_tituloAreaPoligono.place(x=585, y=10)

lb_numeroPontosPoligono = Label(janela, text="Nº pontos do poligono:")
lb_numeroPontosPoligono.place(x=575, y=40)

entry_numeroPontosPoligono = Entry(janela, width=10)
entry_numeroPontosPoligono.place(x=710, y=40)
def ListarCoordenadas_TKINTER():
    coordenadas = []
    x = entry_coordPol.get()
    coordenadas.append(x)
    print(coordenadas)

def AbrirPoligono_TKINTER():
    entries_poligono = []
    numero_pontosDoPoligono = int(entry_numeroPontosPoligono.get())
    while len(entries_poligono) < numero_pontosDoPoligono:
        proximo_ponto=len(entries_poligono) + 1
        y_label = 100 + (proximo_ponto*30)
        lb_coordPol = Label(janela, text="")
        lb_coordPol.place(x=570, y=y_label)
        entry_coordPol = Entry(janela, width=10)
        entry_coordPol.place(x=660, y=y_label)
        lb_coordPol["text"]= "Coord. Ponto {}".format(proximo_ponto)
        entries_poligono.append(1)
        if len(entries_poligono) == numero_pontosDoPoligono:
            y_bt = y_label + 30
            bt_calcularPoligono=Button(janela, width=20, text="Calcular", command=ListarCoordenadas_TKINTER)
            bt_calcularPoligono.place(x=600,y=y_bt)
        #x,y = input("Digite as coordenadas do ponto {}(Ex: 102.25, 47.81): ".format(proximo_ponto)).split(",")
        #x = float(x)
        #y = float(y)
        #lista_de_coordenadas_x.append(x)
        #lista_de_coordenadas_y.append(y)

#def addBox():
#    print("ADD")
#
#    ent = Entry(janela)
#    ent.pack()

bt_okPontosPoligono = Button(janela, width=20, text="Abrir Polígono", command=AbrirPoligono_TKINTER)
bt_okPontosPoligono.place(x=600, y=70)















lb_creditos = Label(janela, text="Desenvolvido por Eduardo Pinheiro.\nContato eduardopmr@hotmail.com.br")
lb_creditos.place(x=10,y=632)
botao_fechar = Button(janela, width=20, text="Sair", command=Fechar, bg="black", fg="white")
botao_fechar.place(x=630,y=635)

janela.mainloop()