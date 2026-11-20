# Coloca el código de tu juego en este archivo.

#Canciones
define msc1 = "audio/A_Pocketful_of_Mischief.mp3"
define msc2 = "audio/Seven_Iron_Locks.mp3"

#imágenes personajes

#Fondos para el juego 
image bg e01:
    "images/bg/bg e01.jpg"
    xsize 1920 ysize 1080

image bg e02:
    "images/bg/bg e02.jpg"
    xsize 1920 ysize 1080

image bg boveda:
    "images/bg/bg boveda.jpg"
    xsize 1920 ysize 1080


# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define f = Character("Flynn")
define w = Character("Wanda")
define o = Character("Oliver")
define ork = Character("Orkenhaimer",color="#ffffff") 

transform flynn_pos:
    xalign 0.02
    yalign 0.65   # Lo despega del fondo para que la caja de texto no lo tape
    zoom 1.4      # Ajustá la escala a tu gusto

# El juego comienza aquí.

label start:

    #Música de fondo:
    play music msc2 volume 0.3 fadein 1.0

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" o "bg room.jpg" para que se muestre aquí.

    scene bg e01

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show flynn_young at flynn_pos

    # Presenta las líneas del diálogo.

    "FLynn es un huérfano que para sobrevivir se dedicó a ser un ladrón. Siendo marginado debido a su profesión, ha estado en una larga búsqueda de la idea que le permita ganar fama, riqueza y pasar a la historia."

    "Aunque no se dejen engañar por su apariencia porque Flynn puede llegar a ser más torpe de lo que parece."


    scene bg e02
    
    "En esta ciudad habita uno de los nobles con mayores riquezas de todo el reino, el conde Marcus."
    "Aparte de tener de las reservas de tesoros más grandes también es un personaje que a muy pocos ciudadanos les agrada, lo que le ha dado a Flynn la idea perfecta"

    scene bg boveda
    "Flynn ha decidido robar el tesoro del conde, pero este está resguardado en una bóveda en lo más profundo de su castillo, por lo que Flynn debe comenzar a planear su atraco"
    "El primer paso es decidir si vale la pena formar un equipo (teniendo que dividir las ganancias pero contando con las habilidades tus compañeros) o hacerlo solo (Mayor riesgo para el torpe Flynn pero todas las ganancias son para él)"


    # Finaliza el juego:

    return
