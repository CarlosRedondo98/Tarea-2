#Carlos Redondo Hurtado
#carlos.redondo@javeriana.edu.co


# Importar la clase imageShape
from imageShape import *

# Main
if __name__ == "__main__":
    ancho = int ( input ( "Ingrese el ancho de la imagen: " ) )   #ancho de la imagen deseada
    alto = int ( input( "Ingrese el alto de la imagen: " ) )      #alto de la imagen deseada

    # crear una instancia imagen con el constructor de la clase importada
    imagen = imageShape(ancho, alto)
    # llamado del método generateShape
    imagen.generateShape()
    # llamado del método showShape
    imagen.showShape()
    # llamado del método getShape el cual retorna una imagen y un string
    imagenFig, tipoFigura = imagen.getShape()
    # llamado del método whatShape el cual retorna un string con el tipo de figura
    tipoFiguraResultante = imagen.whatShape(imagenFig)

    # compracion si la figura clasificada es correcta
    if tipoFigura == tipoFiguraResultante:
        print('La clasificación realizada es correcta')
    else:
        print('La clasificación realizada es incorrecta')



