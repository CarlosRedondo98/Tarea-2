#Carlos Redondo Hurtado
#carlos.redondo@javeriana.edu.co


import numpy as np
import cv2
import random
import math
import os


class imageShape:

    # Constructor
    def __init__(self, ancho, alto):
        self.ancho = ancho  # ancho
        self.alto = alto    # alto

    # Método
    def generateShape (self):
        size = (self.alto, self.ancho, 3)       # tamaño de la imagen
        self.fondo = np.zeros(size, np.uint8)   # fondo negro
        self.num = random.randint(0, 3)        # número aleatorio entre 0 y 3
        #self.num=3
        self.imagenDisponible = False           # booleano para saber si hay una imagen disponible
        self.tipoFigura = "NULL"                # string para saber que tipo de figura se crea

        # Triangulo
        if self.num == 0:
            lado = min(self.ancho, self.alto)/2       # longitud de los lados
            altura = math.sqrt(lado**2+(lado/2)**2)   # altura del triangulo

            #Esquina izquierda
            puntox1 = int(float(self.ancho/2 - lado/2))
            puntoy1 = int(float(self.alto/2 + altura/2))
            punto1 = (puntox1,puntoy1)

            #Esquina derecha
            puntox2 = int(float(self.ancho/2 + lado/2))
            puntoy2 = int(float(self.alto/2 + altura/2))
            punto2 = (puntox2, puntoy2)

            #Esquina superior
            puntox3 = int(float(self.ancho/2 ))
            puntoy3 = int(float(self.alto/2 - altura/2))
            punto3 = (puntox3, puntoy3)

            cordenadas = np.array([punto1, punto2, punto3])                                    # array de coordenadas
            self.imagenFig = cv2.drawContours(self.fondo, [cordenadas], 0, (246, 176, 0), -1)  # crea la figura
            cv2.imwrite("Triangle.png", self.imagenFig)                                        # guarda la imagen
            self.imagenDisponible = True                                                       # hay una imagen disponible
            self.tipoFigura = 'Triangle'                                                       # el tipo es un triangulo

        # Cuadrado
        elif self.num == 1:
            lado = int(float(min(self.ancho, self.alto)/2))                        # longitud de los lados
            centro = (int(float(self.ancho / 2)), int(float(self.alto / 2)))       # centro de la imagen

            #Esquina inferior izquierda
            puntox1 = int(float(self.ancho/2-lado/2))
            puntoy1 = int(float(self.alto/2+lado/2))
            punto1 = (puntox1, puntoy1)

            #Esquina superior izquierda
            puntox2 = puntox1
            puntoy2 = int(float(self.alto/2 - lado/2))
            punto2 = (puntox2, puntoy2)

            # Esquina inferior derecha
            puntox3 = int(float(self.ancho/2 + lado/2))
            puntoy3 = int(float(self.alto/2 + lado/2))
            punto3 = (puntox3, puntoy3)

            # Esquina superior derecha
            puntox4 = puntox3
            puntoy4 = int(float(self.alto/2 - lado/2))
            punto4 = (puntox4, puntoy4)

            cordenadas = np.array([punto1, punto2, punto4, punto3])                            # array de coordenadas
            self.imagenFig = cv2.drawContours(self.fondo, [cordenadas], 0, (246, 176, 0), -1)  # crea la figura
            aux = cv2.getRotationMatrix2D(centro, 45, 1)                                       # rota 45 grados la figura creada
            self.imagenFig = cv2.warpAffine(self.imagenFig, aux, (self.ancho, self.alto))
            cv2.imwrite("Square.png", self.imagenFig)                                          # guarda la imagen
            self.imagenDisponible = True                                                       # hay una imagen disponible
            self.tipoFigura = 'Square'                                                         # el tipo es un cuadrado


        # Rectangulo
        elif self.num == 2:
            ladoHorizontal = int(float(self.ancho/2))     # Magnitud del ancho
            ladoVertical = int(float(self.alto/2))        # Magnitud del alto

            # Esquina inferior izquierda
            puntox1 = int(float(self.ancho/2 - ladoHorizontal/2))
            puntoy1 = int(float(self.alto/2 + ladoVertical/2))
            punto1 = (puntox1, puntoy1)

            # Esquina superior izquierda
            puntox2 = puntox1
            puntoy2 = int(float(self.alto/2 - ladoVertical/2))
            punto2 = (puntox2, puntoy2)

            # Esquina inferior derecha
            puntox3 = int(float(self.ancho/2 + ladoHorizontal/2))
            puntoy3 = int(float(self.alto/2 + ladoVertical/2))
            punto3 = (puntox3, puntoy3)

            # Esquina superior derecha
            puntox4 = puntox3
            puntoy4 = int(float(self.alto/2 - ladoVertical/2))
            punto4 = (puntox4, puntoy4)

            cordenadas = np.array([punto1, punto2, punto4, punto3])                             # array de coordenadas
            self.imagenFig = cv2.drawContours(self.fondo, [cordenadas], 0, (246, 176, 0), -1)   # crea la figura
            cv2.imwrite("Rectangle.png", self.imagenFig)                                        # guarda la imagen
            self.imagenDisponible = True                                                        # hay una imagen disponible
            self.tipoFigura = 'Rectangle'                                                       # el tipo es un cuadrado

        # Circulo
        else:
            radio = int(float(min(self.ancho, self.alto)/4))
            centro = (int(float(self.ancho / 2)), int(float(self.alto / 2)))                 # centro de la imagen
            self.imagenFig = cv2.circle(self.fondo, centro, radio, (246, 176, 0), -1)        # crea el circulo
            cv2.imwrite("Circle.png", self.imagenFig)                                        # guarda la imagen
            self.imagenDisponible = True                                                     # hay una imagen disponible
            self.tipoFigura = 'Circle'                                                       # el tipo es un circulo

    # Método showShape
    def showShape(self):
        if self.imagenDisponible == True:                       # pregunta si hay imagen disponible
            cv2.imshow("Imagen Disponible: ", self.imagenFig)   # muestra la imagen existente
            cv2.waitKey(5000)                                   # delay de 5s
            cv2.destroyAllWindows()                             # elimina las ventanas creadas
        else:
            cv2.imshow(self.fondo)                              # muestra la imagen en negro
            cv2.waitKey(5000)                                   # delay de 5s
            cv2.destroyAllWindows()                             # elimina las ventanas creadas

    # Método getShape
    def getShape(self):
        return self.imagenFig, self.tipoFigura       # retorna la imagen con la figura y el tipo de fiura tratada

    # Método whatShape
    def whatShape(self, imagenIngresada):
        self.imagenFig = imagenIngresada
        im_gray = cv2.cvtColor(self.imagenFig, cv2.COLOR_BGR2GRAY)                                   # de BGR a escala de grises
        ret, thresh = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)              # umbralizacion
        contornos, jerarquía = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # encuentra los contornos

        for c in contornos:
            epsilon = 0.01*cv2.arcLength(c, True)                    # cálcula perimetro de contorno
            approx = cv2.approxPolyDP(c, epsilon, True)              # aprximación de la curva
            x, y, w, h = cv2.boundingRect(approx)                    # rectángulo delimitador

            if len(approx) == 3:                                     # condición para el triangulo
                print('La figura corresponde a un Triangulo')        # mostrar en pantalla la figura correspondiente
                tipoFiguraResultante = 'Triangle'                    # asignación del string del tipo de figura
            elif len(approx) >= 5:                                   # Condicion para clasificar Circulo
                print('La figura corresponde a un Circulo')          # mostrar en pantalla la figura correspondiente
                tipoFiguraResultante = 'Circle'                      # asignación del string del tipo de figura
            elif len(approx) == 4:                                   # condición para el cuadrado y rectángulo
                if (w/h)  == 1:                                      # condición para el cuadrado
                    print('La figura corresponde a un Cuadrado')     # mostrar en pantalla la figura correspondiente
                    tipoFiguraResultante = 'Square'                  # asignación del string del tipo de figura
                else:                                                # condición para el rectángulo
                    print('La figura corresponde a un Rectangulo')   # mostrar en pantalla la figura correspondiente
                    tipoFiguraResultante = 'Rectangle'               # asignación del string del tipo de figura
            else:                                                    # otro caso
                print('La figura no es un triangulo, cuadrado, rectagulo o circulo ')
                tipoFiguraResultante = 'NULL'                        # asignación del string del tipo de figura

        return (tipoFiguraResultante)
