# =============================================================================
# Manual para (No) Asaltar Fortalezas
# =============================================================================

define narrador = Character(None, what_color="#f0e8d0")
define flynn    = Character("Flynn")
define wanda    = Character("Wanda")
define oliver   = Character("Oliver")
define ork      = Character("Orkenhaimer", color="#ffffff")

# --------------- Imágenes ---------------

# Fondos disponibles
image bg e01:
    "images/bg/bg e01.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg e02:
    "images/bg/bg e02.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg boveda:
    "images/bg/bg boveda.jpg"
    xsize 1920 ysize 1080 fit "cover"

# Fondos pendientes (descomentá cuando tengas el archivo)
# image bg callejon       = "images/bg/bg_callejon.jpg"
# image bg ciudad         = "images/bg/bg_ciudad.jpg"
# image bg taberna        = "images/bg/bg_taberna.jpg"
# image bg castillo_ext   = "images/bg/bg_castillo_ext.jpg"
# image bg taller_orco    = "images/bg/bg_taller_orco.jpg"
# image bg mar            = "images/bg/bg_mar.jpg"
# image bg ciudad_pez     = "images/bg/bg_ciudad_pez.jpg"
# image bg castillo_int   = "images/bg/bg_castillo_int.jpg"
# image bg carcel         = "images/bg/bg_carcel.jpg"
# image bg camino         = "images/bg/bg_camino.jpg"

# Personajes disponibles
image flynn_young       = "images/assets/characters/Flynn/flynn_young.jpg"
image flynn_mad         = "images/assets/characters/Flynn/flynn_mad.png"

# Personajes pendientes (descomentá cuando tengas el archivo)
# image flynn_normal      = "images/assets/flynn_normal.png"
# image flynn_golpeado    = "images/assets/flynn_golpeado.png"
# image wanda_normal      = "images/assets/wanda_normal.png"
# image oliver_normal     = "images/assets/oliver_normal.png"
# image oliver_pose       = "images/assets/oliver_pose.png"
# image ork_normal        = "images/assets/ork_normal.png"
# image conde_normal      = "images/assets/conde_normal.png"

# =============================================================================
# INICIO
# =============================================================================

label start:

    play music "audio/A_Pocketful_of_Mischief.mp3" fadein 1.0

    # -------------------------------------------------------------------------
    # E01 — Prólogo: Presentación de Flynn
    # -------------------------------------------------------------------------

    scene bg e01 with fade
    show flynn_young at center

    narrador "Flynn es un huérfano que para sobrevivir se dedicó a ser un ladrón. Siendo marginado debido a su profesión, ha estado en una larga búsqueda de la idea que le permita ganar fama, riqueza y pasar a la historia."
    narrador "Aunque no se dejen engañar por su apariencia porque Flynn puede llegar a ser más torpe de lo que parece."

    # -------------------------------------------------------------------------
    # E02.1 — Introducción a la idea de Flynn
    # -------------------------------------------------------------------------

    scene bg e02 with fade

    narrador "En esta ciudad habita uno de los nobles con mayores riquezas de todo el reino, el conde Marcus."
    narrador "Aparte de tener de las reservas de tesoros más grandes también es un personaje que a muy pocos ciudadanos les agrada, lo que le ha dado a Flynn la idea perfecta."

    # -------------------------------------------------------------------------
    # E02.2 — Presentación del plan y la bóveda
    # -------------------------------------------------------------------------

    scene bg boveda with fade

    narrador "Flynn ha decidido robar el tesoro del conde, pero este está resguardado en una bóveda en lo más profundo de su castillo, por lo que Flynn debe comenzar a planear su atraco."
    narrador "El primer paso es decidir si vale la pena formar un equipo (teniendo que dividir las ganancias pero contando con las habilidades de tus compañeros) o hacerlo solo (mayor riesgo para el torpe Flynn pero todas las ganancias son para él)."

    # -------------------------------------------------------------------------
    # E02.3 / D00 — Decisión inicial
    # -------------------------------------------------------------------------

    scene bg boveda with fade
    show flynn_young at center

    menu:
        "¿Qué hace Flynn?"

        "Aventura en solitario":
            jump rama_solitario

        "Conseguir un grupo":
            jump rama_equipo


# =============================================================================
# RAMA EN SOLITARIO
# =============================================================================

label rama_solitario:

    # E10.1 — Intro rama solitaria
    # scene bg camino with fade
    # show flynn_normal at center

    narrador "Flynn ha tomado la decisión de emprender su aventura en solitario, por lo que procede a pensar en el siguiente paso en su plan."
    narrador "Un ataque frontal es bastante arriesgado y acarrea un gran peligro al tener que enfrentarse a todas las fuerzas del conde."
    narrador "Por otro lado, una entrada sigilosa tiene más probabilidades de éxito confiando en que la torpeza de Flynn no le juegue en contra."

    # E10.2 / D_SOLO — Decisión método solitario
    menu:
        "¿Cómo intenta entrar Flynn?"

        "Incursión frontal":
            jump solo_frontal

        "Entrada sigilosa":
            jump solo_sigilo


label solo_frontal:

    # E11-1
    # scene bg castillo_ext with fade
    # show flynn_golpeado at center

    narrador "Flynn ha tomado la muy poco sabia decisión de hacer una incursión frontal contra las fuerzas del conde, llegando a la entrada del castillo tocando la puerta y golpeando al primer guardia que lo recibió."
    narrador "Siendo este el escenario, no es sorpresa que el resultado fue que Flynn fue herido de gravedad y aprehendido por los guardias."

    # E11-2 — Game Over: Encarcelado
    # scene bg carcel with fade
    # show flynn_golpeado at center

    narrador "— FIN — Flynn termina sus días en los calabozos del conde Marcus."

    menu:
        "¿Qué querés hacer?"

        "Reintentar desde la última decisión":
            jump rama_solitario

        "Volver al inicio":
            jump start


label solo_sigilo:

    # E12-1
    # scene bg castillo_ext with fade
    # show flynn_golpeado at center

    narrador "Flynn ha tomado la decisión de entrar de forma sigilosa en el castillo del conde. Lastimosamente, mientras se escabullía por encima de las paredes se ha tropezado con su propio pie y se ha caído, siendo descubierto por los guardias y teniendo que huir de la ciudad para preservar su libertad."

    # E12-2 — Final cobarde
    # scene bg camino with fade
    # show flynn_golpeado at center

    narrador "Flynn huye de la ciudad. En cada esquina aparece un cartel de SE BUSCA con su rostro y una recompensa considerable."
    narrador "— FIN COBARDE — Fuga desesperada de la ciudad."

    menu:
        "¿Qué querés hacer?"

        "Reintentar desde la última decisión":
            jump rama_solitario

        "Volver al inicio":
            jump start


# =============================================================================
# RAMA EN EQUIPO
# =============================================================================

label rama_equipo:

    # E20 — Intro taberna
    # scene bg taberna with fade
    # show flynn_normal at left

    narrador "Nuestro protagonista ha decidido emprender la búsqueda de un equipo para su incursión, y no hay lugar más ideal para reunir uno que la taberna del centro de la ciudad, lugar donde se reúnen todos los aventureros."

    # E21-1 — Reclutamiento de Wanda (presentación)
    # show wanda_normal at right

    narrador "Flynn entra en la taberna y fija sus ojos en las únicas dos personas que están por su cuenta: un fisicoculturista y una bruja."
    narrador "Decidido a reclutarlos, se dirige primero en dirección a la maga que se encuentra en la barra con una jarra de cerveza."

    # E21-2
    flynn "Hola, me llamo Flynn, veo que estás bebiendo por tu cuenta, ¿me puedo sentar a tu lado?"

    # E21-3
    wanda "Hola Flynn, me llamo Wanda. Adelante, siéntate."

    # E21-4
    flynn "Mira, me he acercado a hablarte porque estoy formando un equipo, la iniciativa Reivindicadores, y vengo a reclutarte para el trabajo más grande y más importante que alguna vez te han propuesto. Naturalmente también el más riesgoso."

    # E21-5
    wanda "Cuéntame más sobre este trabajo…"

    # E21-6
    # show oliver_normal at right

    narrador "Después de un rato hablando, Flynn convence a Wanda y se une el primer miembro al grupo, por lo que junto a su nueva compañera se acercan al fisicoculturista que se encuentra en la mesa del rincón."

    # E22-1
    flynn "Hola, me llamo Flynn y esta es mi compañera Wanda, ¿te podemos hablar un momento?"

    # E22-2
    oliver "Adelante."

    # E22-4
    # hide wanda_normal
    # hide oliver_normal

    narrador "Al cabo de un rato de charlar, nuestro grupo de aventureros estaba completo."
    narrador "Flynn: el líder del equipo y un ágil pero torpe ladrón."
    narrador "Wanda: la maga de las pociones impredecibles, que lo único más loco que su personalidad son los efectos de su alquimia."
    narrador "Oliver: la fuerza bruta, un fisicoculturista que ha adquirido la invulnerabilidad en su pose especial a través de la contracción de cada uno de sus músculos."

    jump primer_asalto


# =============================================================================
# PRIMER ASALTO AL CASTILLO (D01)
# =============================================================================

label primer_asalto:

    # E23-1
    # scene bg castillo_ext with fade
    # show flynn_normal at left
    # show wanda_normal at center
    # show oliver_normal at right

    narrador "Después de unas semanas de ardua planeación nuestro grupo ha conseguido concretar su plan. Primero, para el plan A están decidiendo entre dos opciones:"
    narrador "La primera: Un ataque frontal usando la invulnerabilidad de Oliver para penetrar el castillo."
    narrador "La segunda: Una poción de \"invisibilidad\" de Wanda, quién sabe qué otros efectos pueda tener…"

    # E23-2 / D01
    menu:
        "¿Cuál es el plan de entrada?"

        "Ariete humano":
            jump d01_ariete

        "Poción de \"invisibilidad\"":
            jump d01_pocion


label d01_ariete:

    # E24
    # scene bg castillo_ext with fade
    # show flynn_golpeado at left
    # show wanda_normal at right

    narrador "Habiéndose decidido por la primera opción, usaron a Oliver en su pose legendaria para reventar la puerta del castillo. Lo que no pensaron es que para reventar la puerta del castillo tienen que tener la fuerza física suficiente para cargarlo y atravesar la puerta, fuerza la cual no tenían."

    jump plan_b


label d01_pocion:

    # E25
    # scene bg castillo_ext with fade
    # show flynn_golpeado at left
    # show wanda_normal at right

    narrador "Nuestro grupo ha decidido confiar en las habilidades alquímicas de Wanda. Lo que no esperaban era que dicha poción de invisibilidad los dejara ciegos de forma momentánea. Todo el mundo es invisible para una persona ciega…"

    jump plan_b


# =============================================================================
# PLAN B — Bifurcación principal (D02)
# =============================================================================

label plan_b:

    # E26-1
    # scene bg taberna with fade
    # show flynn_normal at left
    # show wanda_normal at center
    # show oliver_normal at right

    narrador "Después del fracaso del plan A, nuestro trío de aventureros decidió irse con el plan B. Para este plan tienen dos opciones que son monumentalmente mejores, por lo que el hecho de que este sea el plan B y no el A solo se explica con la torpeza del líder Flynn."
    narrador "Opción 1: Seguir la cadena de rumores hasta el gran orco genio de los explosivos. Con su conocimiento y arsenal, entrar a la bóveda debe ser como robarle un dulce a un bebé (o explotarle el dulce a uno)."
    narrador "Opción 2: Una raza de hombres pez resguarda un artefacto legendario capaz de cortar cualquier material de un tajo. El grupo Rei planea ir y traerlo consigo, y quién sabe, tal vez traigan un plato de sushi también."

    # E26-2 / D02
    menu:
        "¿Cuál es el plan B?"

        "Buscar al orco":
            jump rama_orkenhaimer

        "Artefacto oceánico":
            jump rama_maritima


# =============================================================================
# RAMA ORKENHAIMER (D02-A)
# =============================================================================

label rama_orkenhaimer:

    # E27-1
    # scene bg taller_orco with fade
    # show flynn_normal at left
    # show wanda_normal at center
    # show oliver_normal at right

    narrador "Después de seguir la cadena de rumores llegan hasta un orco llamado Orkenhaimer, el legendario orco genio pirómano con un arsenal infinito."
    narrador "Ahora la tarea que tienen en sus manos es lograr convencerlo y reclutarlo."

    # E27-2 / D03_A
    narrador "Antes de hablar con Orkenhaimer el grupo Rei tiene que definir cómo será su acercamiento para facilitar el poder reclutarlo."
    narrador "Opción 1: Demostrar el poderío del grupo y amenazar al orco para que coopere sin exigir una recompensa más que su propia vida."
    narrador "Opción 2: Ofrecerle parte del botín para que financie su investigación sobre explosivos."
    narrador "Opción 3: Intentar convencerlo de que es la oportunidad perfecta de probar su arma y demostrar el poder de su obra maestra."

    menu:
        "¿Cómo convencen a Orkenhaimer?"

        "Amenazar al orco":
            jump ork_amenaza

        "Ofrecer parte del botín":
            jump ork_dinero

        "Convencer al orco de probar su arma":
            jump ork_arma


label ork_amenaza:

    # E27-3 — Game Over: Desintegrados
    # scene bg taller_orco with fade
    # show ork_normal at center

    narrador "El grupo ha decidido mostrar su poderío y amenazar al orco, y por esto han terminado brutalmente derrotados por los explosivos de Orkenhaimer."
    narrador "¿Por qué creíste que es una buena decisión amenazar a un orco maniático de las explosiones?"

    menu:
        "¿Qué querés hacer?"

        "Volver a intentar":
            jump rama_orkenhaimer


label ork_dinero:

    # E27-4
    # scene bg taller_orco with fade
    # show ork_normal at right
    # show flynn_normal at left

    narrador "Después de una no muy larga deliberación, decidieron hablar con el orco en el idioma universal: el dinero. El orco consideró su oferta y decidió ayudarlos."

    jump asalto_orkenhaimer


label ork_arma:

    # E27-5
    # scene bg taller_orco with fade
    # show ork_normal at right
    # show flynn_normal at left

    narrador "Tal parece que los orcos maniáticos de las explosiones tienen también su lado vanidoso. Tras convencerlo de demostrar el poder de su obra maestra, el orco está más que contento de ayudar."

    jump asalto_orkenhaimer


label asalto_orkenhaimer:

    # E27-6 — Asalto al castillo con Orkenhaimer
    # scene bg castillo_ext with fade
    # show ork_normal at right

    narrador "Tras reclutar exitosamente al orco, nuestro grupo emprende su asalto frontal al castillo mandando a volar por los aires a todos los guardias con los explosivos de Orkenhaimer hasta llegar a la bóveda."

    # E27-7 — Apertura de la bóveda
    # scene bg boveda with fade
    # show oliver_pose at center

    narrador "Ya habiendo llegado hasta la bóveda, usaron a Oliver como escudo con su pose legendaria para resguardarse de la explosión y abrir la bóveda."
    narrador "El grupo huyó con el botín, consiguiendo su objetivo y finalizando esta historia."

    narrador "— FIN: EL GRAN GOLPE CON ORKENHAIMER —"

    menu:
        "¿Querés jugar de nuevo?"

        "Volver al inicio":
            jump start


# =============================================================================
# RAMA MARÍTIMA (D02-B)
# =============================================================================

label rama_maritima:

    # E28-1
    # scene bg mar with fade
    # show flynn_normal at left
    # show wanda_normal at center
    # show oliver_normal at right

    narrador "Después de deliberar han decidido ir en búsqueda del artefacto marino. Para esto tuvieron que conseguir (y por conseguir digo robar) equipos de buceo que les permitan adentrarse al fondo del océano."

    # E28-2
    # scene bg ciudad_pez with fade

    narrador "Ya habiendo encontrado la ciudad perdida en el fondo del mar, se disponen a ir por el artefacto. Pero a lo lejos alcanzan a ver varios ejemplares de una especie de hombres pez que custodian la ciudad y cuidan con su vida el artefacto. Siendo este el caso, el grupo debería:"

    # E28-3 / D03_B
    menu:
        "¿Cómo enfrentan a los guardianes del mar?"

        "Dejar que Oliver se encargue":
            jump mar_oliver

        "Pelear contra los peces":
            jump mar_pelea

        "Poción de Wanda":
            jump mar_pocion


label mar_oliver:

    # E28-4 — Bucle cómico
    # show oliver_pose at center

    narrador "Decidido, Oliver se ofrece a encargarse de los guardianes y activa su pose legendaria. Pero no pasa absolutamente nada. ¿Qué pensaste que iba a hacer Oliver? Te recuerdo que no se puede mover cuando está en su pose."

    jump rama_maritima_decision


label rama_maritima_decision:

    menu:
        "¿Querés intentar de otra forma?"

        "Pelear contra los peces":
            jump mar_pelea

        "Poción de Wanda":
            jump mar_pocion


label mar_pelea:

    # E28-5 (pelea)
    # scene bg ciudad_pez with fade

    narrador "Flynn, Wanda y Oliver han decidido atacar de frente a los guardianes. Por suerte para ellos, son peces de la cintura para arriba, por lo que se limitan a darles aletazos tan fuertes que se sienten como pequeñas caricias."

    jump mar_recuperar_artefacto


label mar_pocion:

    # E28-5 (poción)
    # scene bg ciudad_pez with fade

    narrador "Por alguna razón han decidido confiar en las pociones de Wanda. Después de arrojarle el frasco a los guardianes se han dado cuenta de que es una poción de respiración, solo que es para respirar en tierra. Por lo que los guardianes han adquirido pulmones y murieron ahogados, dejando vía libre para que recuperen el artefacto."

    jump mar_recuperar_artefacto


label mar_recuperar_artefacto:

    # E28-6 — Consiguen el artefacto
    # scene bg ciudad_pez with fade

    narrador "Después de lidiar con los sorprendentemente inútiles guardianes, el grupo Rei consigue el artefacto. Resultó ser un sable láser capaz de cortar todo de un tajo. Se disponen a entrar en el castillo."

    # E28-7 — Infiltración y final
    # scene bg castillo_int with fade

    narrador "Habiendo cortado la puerta de entrada y varios guardias en el camino, nuestro grupo llega hasta la bóveda y corta la puerta, dándoles acceso al botín y consiguiendo su objetivo."

    narrador "— FIN: ROBO SILENCIOSO CON ARTEFACTO —"

    menu:
        "¿Querés jugar de nuevo?"

        "Volver al inicio":
            jump start


# Fin del script
return
