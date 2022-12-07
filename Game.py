from Barco import Barco
from Button import Button
from InputBox import InputBox
from Cuadro import Cuadro
import pygame
import random

#Variables globales necesarias en el codigo
background = pygame.image.load('Imagenes/Fondo.jpg')
letras = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10}

def menu():
    #Se genera la ventana y se carga el fondo
    pygame.init()
    menu = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Batalla Naval: Menu")
    menu.blit(background, (0,0))
    
    #Instancias de botón
    PlayB = Button("Jugar")
    PlayB.setCords(465,400), PlayB.setrangeEnd(62,35)
    ExitB = Button("Salir")
    ExitB.setCords(520,730), ExitB.setrangeEnd(50,35)


    Running = True
    while Running:
        pos = pygame.mouse.get_pos()                          #Obtiene la posición del mouse
        
        PlayB.draw(menu, pos)
        ExitB.draw(menu, pos)   #Verifica el color del boton y lo dibuja

        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ExitB.pressed(pos):  #Verifica si se preciona el boton
                    Running = False
                    exit()
                if PlayB.pressed(pos):
                    Running = False
                    configurar()
        pygame.display.update()
    pygame.quit()

def configurar():
    #se crea la vetana
    pygame.init()
    configurarW = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Batalla Naval: Configurar")
    configurarW.blit(background, (0,0))

    #Se crea la matriz jugador vacía y se carga la de la computadora
    MatJugador = [[0,0,0,0,0,0,0,0,0,0], 
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0]]
    MatComputadora = cargarLista()

    #Instancia de barco necesaria para dibujarla
    BarcoM = Barco(416, 240, 1, 5)
    tipo = 1
    cuadros = 5
    barcos = []

    #Instancias de botón
    VeriB = Button("Verificar")
    VeriB.setCords(456,500), VeriB.setrangeEnd(88,35)
    IniB = Button("Iniciar")
    IniB.setCords(800,800), IniB.setrangeEnd(65,35)
    ExitB = Button("Salir")
    ExitB.setCords(520,730), ExitB.setrangeEnd(50,35)

    #Instancias de inputBox
    InputX = InputBox(464, 340, 30, 30, "")
    InputY = InputBox(508, 340, 30, 30, "")
    InputZ = InputBox(485, 420, 30, 30, "")

    #Labels necesarias
    arialfont = pygame.font.SysFont('arial', 40)
    CordsLabel = arialfont.render("X   Y" , 0, (0,0,0))
    ZCordLabel = arialfont.render("Z" , 0, (0,0,0))

    Running = True
    while Running:
        pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
        
            InputX.handle_event(event)      #Captura los eventos y actualiza el inputBox
            InputX.update()
            InputY.handle_event(event)
            InputY.update()
            InputZ.handle_event(event)
            InputZ.update()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ExitB.pressed(pos):          #Verifica si el boton fue precionado
                    Running = False 
                    exit()
                if IniB.pressed(pos):
                    Running = False
                    juego(barcos, MatJugador, MatComputadora)
                if VeriB.pressed(pos):
                    if InputZ.get_text() == "H":                #Verifica si es horizontal
                        if int(InputX.get_text()) > 0 and int(InputX.get_text()) + cuadros <= 11:       #Verifica que no se salga del rango
                            if InputY.get_text() in letras: #Verifica que la letra esté dentro del rango
                                barcos.append(Barco((int(InputX.get_text())-1)*30+50, (letras[InputY.get_text()]-1)*30+50, tipo, cuadros)) #Crea el barco en las coordenadas
                                aux = 0
                                for i in range(cuadros):
                                    MatJugador[letras[InputY.get_text()]-1][int(InputX.get_text())-1+aux] = 1 #Recorre la matriz agregando unos
                                    aux += 1
                                tipo += 1
                                cuadros -= 1
                                if tipo <= 5:       #Verifica si es el ultimo barco o cambia al siguiente para colocar
                                    BarcoM.set_Image(tipo, cuadros)
                    if InputZ.get_text() == "V":                #Verifica si es vertical
                        if int(InputX.get_text()) > 0 and int(InputX.get_text()) < 10:  #Verifica si es horizontal
                            if InputY.get_text() in letras and letras[InputY.get_text()] + cuadros <= 11:
                                barcos.append(Barco((int(InputX.get_text())-1)*30+50, (letras[InputY.get_text()]-1)*30+50, str(tipo)+"R", cuadros)) #Crea el barco en las coordenadas
                                aux = 0
                                for i in range(cuadros):
                                    MatJugador[letras[InputY.get_text()]-1+aux][int(InputX.get_text())-1] = 1
                                    aux += 1
                                tipo += 1
                                cuadros -= 1
                                if tipo <= 5: #Verifica si es el ultimo barco o cambia al siguiente para colocar
                                    BarcoM.set_Image(tipo, cuadros)
        
        #Logica para dibujar todo lo necesario
        configurarW.blit(background, (0,0))
        configurarW.blit(CordsLabel, (468, 300))
        configurarW.blit(ZCordLabel, (490, 380))
        if tipo <= 5:
            VeriB.draw(configurarW, pos)
        else:
            VeriB.setCords(800, 800)
            IniB.setCords(456,500)
            IniB.draw(configurarW, pos)
        ExitB.draw(configurarW, pos)
        InputY.draw(configurarW)
        InputX.draw(configurarW)
        InputZ.draw(configurarW)
        BarcoM.draw(configurarW)
        for barc  in barcos:        #Recorre los barcos para dibujarlos siempre
            barc.draw(configurarW)

        pygame.display.update()
    pygame.quit()

def juego(Barcos, MatJugador, MatComputadora):
    #Se crea la ventana
    pygame.init()
    juegoW = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Batalla Naval: Juego")
    juegoW.blit(background, (0,0))

    #Variables necesarias
    cuadros = []
    DisparoJugador = []
    DisparoComputadora = []
    scoreCompu = 0
    scoreJugador = 0

    #Instancias de boton
    DispB = Button("Disparar")
    DispB.setCords(456,410), DispB.setrangeEnd(88,35)
    ExitB = Button("Salir")
    ExitB.setCords(520,730), ExitB.setrangeEnd(50,35)

    #Instancias de inputbox
    InputX = InputBox(464, 340, 30, 30, "")
    InputY = InputBox(508, 340, 30, 30, "")

    #Label y fuente necesaria
    arialfont = pygame.font.SysFont('arial', 40)
    CordsLabel = arialfont.render("X   Y" , 0, (0,0,0))

    #Toma random el jugador a iniciar
    juega = random.randint(0, 1)
    if juega == 1:
        verifica = 16
    else:
        verifica = 15

    Running = True
    while Running:
        pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
        
            InputX.handle_event(event)
            InputX.update()
            InputY.handle_event(event)
            InputY.update()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ExitB.pressed(pos):
                    Running = False
                    exit()
                if DispB.pressed(pos) and juega == 0:
                    if int(InputX.get_text()) > 0 and int(InputX.get_text()) <= 10:     #Detecta que no se salga de rango
                        if InputY.get_text() in letras:
                            if (int(InputX.get_text()), letras[InputY.get_text()]) not in DisparoJugador: #Verifica que no haya disparado a esa casilla antes
                                if MatComputadora[letras[InputY.get_text()]-1][int(InputX.get_text())-1] == 1:  #Verifica si hay barco o está vacío
                                    cuadros.append(Cuadro((int(InputX.get_text())-1)*30+50, (letras[InputY.get_text()]-1)*30+450, "c")) #Dibuja el cuadro con correcto
                                    scoreJugador += 1
                                else:
                                    cuadros.append(Cuadro((int(InputX.get_text())-1)*30+50, (letras[InputY.get_text()]-1)*30+450, "x")) #Dibuja el cuadro con incorrecto
                                juega = 1
                                DisparoJugador.append((int(InputX.get_text()), letras[InputY.get_text()])) #Agrega el disparo a la lista
        
        #Verifica si alguien gano y verifica quien inicio, para saber si deja que el otro juegue
        if scoreCompu == 15 or scoreJugador == 15:
            if verifica == 16:
                verifica -= 1
            else:
                verificar(scoreCompu, scoreJugador)

        #verifica si el tiro es de la computadora
        if juega == 1:
            while True:         #Siepre sucede hasta que no se encuentre el tiro registrado
                posx = random.randint(0, 9)
                posy = random.randint(0, 9)
                if (posx, posy) not in DisparoComputadora:  #Verifica si el tiro no está
                    DisparoComputadora.append((posx, posy)) #Agrega el disparo a la lista
                    break
            if MatJugador[posy][posx] == 1:
                cuadros.append(Cuadro(posx*30+50, posy*30+50, "c")) #Verifica si hay barco para dibujar correcto
                scoreCompu += 1
            else:
                cuadros.append(Cuadro(posx*30+50, posy*30+50, "x")) #Dibuja el cuadro con incorrecto
            juega = 0


        juegoW.blit(background, (0,0))
        juegoW.blit(CordsLabel, (468, 300))
        ExitB.draw(juegoW, pos)
        DispB.draw(juegoW, pos)
        InputY.draw(juegoW)
        InputX.draw(juegoW)
        for barc  in Barcos:    #Recorre los barcos para dibujarlos
            barc.draw(juegoW)
        for cudr in cuadros:    #Recorre los cuadros para siempre dibujarlos
            cudr.draw(juegoW)

        pygame.display.update()
    pygame.quit()

def verificar(scoreComputadora, scoreJugador):
    #Crea la ventana
    pygame.init()
    backgroundF = pygame.image.load('Imagenes/FondoFinal.jpg')
    verificarW = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Batalla Naval: Final")
    verificarW.blit(backgroundF, (0,0))
    
    #Buttons
    ExitB = Button("Menu")
    ExitB.setCords(520,730), ExitB.setrangeEnd(50,35)

    arialfont = pygame.font.SysFont('Arial Black', 40)

    #Crea el texto según lo que pasó con los scores
    if scoreComputadora == scoreJugador:
        text = arialfont.render("EMPATE" , 0, (0,0,0))
        verificarW.blit(text, (110, 370))
    elif scoreComputadora >= scoreJugador:
        text = arialfont.render("PERDISTE" , 0, (0,0,0))
        verificarW.blit(text, (90, 370))
    else:
        text = arialfont.render("GANASTE" , 0, (0,0,0))
        verificarW.blit(text, (90, 370))
    
    Running = True
    while Running:
        pos = pygame.mouse.get_pos()

        ExitB.draw(verificarW, pos)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ExitB.pressed(pos):
                    Running = False
                    menu()
        pygame.display.update()
    pygame.quit()

def cargarLista():
    data = open ('Tableros/' + str(random.randint(1, 5)) + '.txt','r')  #Abre un archivo random de la matriz de la compu
    mensaje = data.read()
    guardarColum = False
    guardarFila = False
    matriz = []
    templist = []
    for i in mensaje:       #Recorre el texto y realiza logica necesaria para crear la matriz
        if i == "[" and not guardarColum:   
            guardarColum = True
        elif guardarColum and i == "[":
            guardarFila = True
        elif guardarFila and i == "1":
            templist.append(1)
        elif guardarFila and i == "0":
            templist.append(0)
        elif guardarFila and i == "]":
            matriz.append(templist)
            templist = []
            guardarFila = False        
    data.close()
    return matriz

if __name__ == "__main__":
   menu()