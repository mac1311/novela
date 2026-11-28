# =============================================================================
# Manual para (No) Asaltar Fortalezas
# =============================================================================

define narrador    = Character(None, what_color="#f0e8d0")
define flynn       = Character("Flynn")
define wanda       = Character("Wanda")
define oliver      = Character("Oliver")
define ork         = Character("Orkenhaimer", color="#ffffff")
define contratista = Character("Contratista")
define tabernero   = Character("Tabernero")
define guardia1    = Character("Guardia 1")
define guardia2    = Character("Guardia 2")

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

image bg boveda_magica:
    "images/bg/bg boveda magica.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg callejon:
    "images/bg/bg callejon.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg ciudad:
    "images/bg/bg ciudad.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg taberna:
    "images/bg/bg taberna.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg taberna_oscuro:
    "images/bg/bg taberna.jpg"
    xsize 1920 ysize 1080 fit "cover"
    matrixcolor BrightnessMatrix(-0.35)
    blur 8

image cg taberna_pelea:
    "images/assets/characters/Oliva/oliva_figting.jpg"
    xsize 1920 ysize 1080 fit "contain"

image bg ariete_humano:
    "images/assets/characters/Oliva/ariete_humano.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg ariete_humano_caida:
    "images/assets/characters/Oliva/ariete_humano_faling.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg castillo_ext:
    "images/bg/bg castillo ext.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg taller_orco:
    "images/bg/bg taller orco.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg mar:
    "images/bg/bg mar.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg ciudad_pez:
    "images/bg/bg ciudad pez.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg castillo_int:
    "images/bg/bg castillo int.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg carcel:
    "images/bg/bg carcel.jpg"
    xsize 1920 ysize 1080 fit "cover"

image bg camino:
    "images/bg/bg camino.jpg"
    xsize 1920 ysize 1080 fit "cover"

image castillo_flynn:
    "images/bg/castillo_flynn.jpg"
    xsize 1920 ysize 1080 fit "cover"

image flynn_caida:
    "images/bg/Flynn_caida_guardias.jpg"
    xsize 1920 ysize 1080 fit "cover"

image flynn_encerrado:
    "images/bg/flynn_encerrado.jpg"
    xsize 1920 ysize 1080 fit "cover"

image flynn_huida:
    "images/bg/final_flynn_huyendo.jpg"
    xsize 1920 ysize 1080 fit "cover"

image flynn_pobre:
    "images/bg/flynn_pobre.jpg"
    xsize 1920 ysize 1080 fit "cover"
# --------------- Posiciones (espacio para 3 personajes) ---------------

transform pos_izq:
    xcenter 0.18
    yalign 1.0

transform pos_centro:
    xcenter 0.50
    yalign 1.0

transform pos_der:
    xcenter 0.82
    yalign 1.0

transform flynn_intro:
    xcenter 0.50
    yalign 0.65
    zoom 1.4

# Personajes disponibles
image flynn_young       = "images/assets/characters/Flynn/flynn_young.jpg"

image flynn_normal:
    "images/assets/characters/Flynn/serious_flynn.png"
    zoom 0.48

image flynn_mad:
    "images/assets/characters/Flynn/angry_flynn.png"
    zoom 0.48

image oliver_normal:
    "images/assets/characters/Oliva/serious_oliva.png"
    zoom 0.38

image oliver_thinking:
    "images/assets/characters/Oliva/thinking_oliva.png"
    zoom 0.38

image oliver_pose:
    "images/assets/characters/Oliva/golden_oliva.png"
    zoom 0.40

image ork_normal:
    "images/assets/characters/Orkenhaimer/Serious_orkenhaimer.png"
    zoom 0.38

image ork_happy:
    "images/assets/characters/Orkenhaimer/happy_orkenhaimer.png"
    zoom 0.38

image monster_green:
    "images/assets/characters/monsters/green_monster.png"
    zoom 0.38

image monster_blue:
    "images/assets/characters/monsters/blue_monster.png"
    zoom 0.38

image wanda_normal:
    "images/assets/characters/Wanda/serious_wanda_upperhalf.png"
    zoom 0.48

image wanda_shy:
    "images/assets/characters/Wanda/shy_wanda_upper half.png"
    zoom 0.48

image tabernero_normal:
    "images/assets/characters/bartender/bartender.png"
    crop (0, 0, 1792, 1915)
    zoom 0.38

# Personajes pendientes (descomentá cuando tengas el archivo)
# image flynn_golpeado    = "images/assets/characters/Flynn/flynn_golpeado.png"

# =============================================================================
# PANTALLA DE FINALES
# =============================================================================

screen pantalla_final(titulo, subtitulo, es_victoria=False, reintentar_label=None):
    modal True
    zorder 100

    add "#0d0e15cc"

    $ color_acento = "#f1c40f" if es_victoria else "#e74c3c"
    $ etiqueta_estado = "★ FINAL COMPLETADO ★" if es_victoria else "✕ GAME OVER ✕"

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 1100
        xpadding 70
        ypadding 55
        background Solid("#161822ee")

        vbox:
            spacing 28
            xalign 0.5

            text etiqueta_estado:
                xalign 0.5
                size 26
                bold True
                color color_acento
                kerning 3

            text titulo:
                xalign 0.5
                text_align 0.5
                size 54
                bold True
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]

            null height 4

            text subtitulo:
                xalign 0.5
                text_align 0.5
                size 30
                color "#d5d8dc"

            null height 18

            hbox:
                spacing 35
                xalign 0.5

                if reintentar_label:
                    textbutton "Reintentar desde la última decisión":
                        action [Hide("pantalla_final"), Jump(reintentar_label)]
                        xpadding 32
                        ypadding 18
                        background Solid("#2c3e50")
                        hover_background Solid(color_acento)
                        text_size 26
                        text_color "#ffffff"
                        text_hover_color "#111111"

                textbutton "Volver al inicio":
                    action [Hide("pantalla_final"), Jump("start")]
                    xpadding 32
                    ypadding 18
                    background Solid("#2c3e50")
                    hover_background Solid(color_acento)
                    text_size 26
                    text_color "#ffffff"
                    text_hover_color "#111111"

# =============================================================================
# INICIO
# =============================================================================

label start:

    #play music "audio/A_Pocketful_of_Mischief.mp3" fadein 1.0

    # -------------------------------------------------------------------------
    # E01 — Prólogo: Presentación de Flynn
    # -------------------------------------------------------------------------

    scene flynn_pobre with fade


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

    scene bg boveda_magica with fade

    narrador "Flynn ha decidido robar el tesoro del conde, pero este está resguardado en una bóveda en lo más profundo de su castillo, por lo que Flynn debe comenzar a planear su atraco."
    narrador "El primer paso es decidir si vale la pena formar un equipo (teniendo que dividir las ganancias pero contando con las habilidades de tus compañeros) o hacerlo solo (mayor riesgo para el torpe Flynn pero todas las ganancias son para él)."

    # -------------------------------------------------------------------------
    # E02.3 / D00 — Decisión inicial
    # -------------------------------------------------------------------------

    scene bg boveda_magica with fade
    show flynn_normal at pos_centro with dissolve

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
    scene bg camino with fade
    show flynn_normal at pos_centro with dissolve

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
    scene bg castillo_ext with fade
    show flynn_mad at pos_centro with dissolve

    narrador "Flynn ha tomado la muy poco sabia decisión de hacer una incursión frontal contra las fuerzas del conde, llegando a la entrada del castillo tocando la puerta y golpeando al primer guardia que lo recibió."

    guardia1 "¡Ay! ¿Qué es eso?! ¿Quién me acaba de pegar?!"
    guardia2 "¡Alto ahí! ¿En serio tocaste la puerta principal para asaltar el castillo?!"
    flynn "Eh... ¿hola? Venía por el tesoro del conde."
    guardia1 "Atrapen al genio del siglo."

    narrador "Siendo este el escenario, no es sorpresa que el resultado fue que Flynn fue herido de gravedad y aprehendido por los guardias."

    # E11-2 — Game Over: Encarcelado
    scene flynn_encerrado with fade

    call screen pantalla_final(
        titulo="Encarcelado de inmediato",
        subtitulo="Flynn termina sus días en los calabozos del conde Marcus.",
        es_victoria=False,
        reintentar_label="rama_solitario"
    )


label solo_sigilo:

    # E12-1
    scene castillo_flynn with fade
    narrador "Flynn ha tomado la decisión de entrar de forma sigilosa en el castillo del conde."

    scene flynn_caida with fade

    narrador "Lastimosamente, mientras se escabullía por encima de las paredes se ha tropezado con su propio pie y se ha caído, siendo descubierto por los guardias y teniendo que huir de la ciudad para preservar su libertad."

    # E12-2 — Final cobarde
    scene flynn_huida with fade
    narrador "Flynn huye de la ciudad. En cada esquina aparece un cartel de SE BUSCA con su rostro y una recompensa considerable."

    call screen pantalla_final(
        titulo="Final Cobarde: Fuga Desesperada",
        subtitulo="Flynn escapa del reino con las manos vacías y una orden de captura.",
        es_victoria=False,
        reintentar_label="rama_solitario"
    )


# =============================================================================
# RAMA EN EQUIPO
# =============================================================================

label rama_equipo:

    # E20 — Intro taberna
    scene bg taberna with fade
    show flynn_normal at pos_centro with dissolve

    narrador "Nuestro protagonista ha decidido emprender la búsqueda de un equipo para su incursión, y no hay lugar más ideal para reunir uno que la taberna del centro de la ciudad, lugar donde se reúnen todos los aventureros."

    # E21-1 — Pelea de Oliver por un pago incumplido
    scene bg taberna_oscuro with fade
    show cg taberna_pelea at truecenter with dissolve

    narrador "Apenas Flynn cruza la puerta, una jarra sale volando y el bullicio se detiene en seco: un fisicoculturista descomunal sostiene en vilo por el cuello a un hombre aterrado."
    oliver "¡Un trato es un trato! Cargué tus carretas durante tres días y prometiste cincuenta monedas de oro. ¿Tienes idea de lo caro que es mantener este volumen muscular?"
    contratista "¡P-pero si solo te faltaron diez monedas! ¡Te juro que mañana te pago el resto!"
    oliver "Mis suplementos proteicos y aceites de posado de lujo no esperan a mañana. Si no hay oro, al menos servirás de mancuerna."
    narrador "Flynn observa el espectáculo con una sonrisa oportunista. Alguien con esa fuerza —y tan urgido de dinero— es justo lo que necesita."

    # E21-2 — Flynn convence a Oliver
    scene bg taberna with fade
    show flynn_normal at pos_centro with dissolve
    show oliver_normal at pos_der with dissolve

    flynn "Oye, grandulón. Suelta al pobre hombre antes de que le arruines la garganta… Tengo una oferta que paga mucho más que cincuenta monedas."
    narrador "Oliver deja caer al contratista, quien sale huyendo de la taberna sin mirar atrás, y clava su mirada seria en Flynn."
    oliver "Habla rápido, muchacho. Mi rutina de entrenamiento es sagrada."
    flynn "Me llamo Flynn y estoy armando la iniciativa Reivindicadores para el atraco del siglo: vaciar la bóveda del conde Marcus."
    flynn "Hay tanto oro ahí dentro que podrás comprar suplementos y aceites de posado por el resto de tu vida."

    hide oliver_normal
    show oliver_thinking at pos_der with dissolve

    oliver "Mmm… la bóveda del conde Marcus. ¿Y cuál es el plan exactamente?"
    flynn "Todo está calculado: tú pones la fuerza imparable, yo pongo la estrategia y el sigilo. Entrar y salir será pan comido. ¿Qué dices?"

    hide oliver_thinking
    show oliver_normal at pos_der with dissolve

    oliver "Si el botín es tan grande como prometes, cuenta con mis músculos… y con mi pose absoluta."

    # E22-1 — Wanda se acerca apenada tras escuchar la oferta
    show wanda_shy at pos_izq with dissolve

    narrador "Antes de que puedan cerrar el trato con un brindis, alguien carraspea tímidamente detrás de ellos. Es una joven maga con la túnica algo chamuscada y varios frascos humeantes en el cinturón."
    wanda "Disculpen… de verdad siento interrumpir, pero no pude evitar escuchar que necesitan un equipo y que la paga sería grande."
    flynn "¿Y tú eres…?"
    wanda "Me llamo Wanda. Me da un poco de pena pedirlo, pero mis últimos experimentos de alquimia salieron… algo mal, y me expulsaron de mi antiguo grupo."
    wanda "Acumulé una deuda enorme por los daños y necesito un gran golpe para pagarla. Mis pociones son muy útiles en un atraco, lo prometo… casi siempre."

    hide oliver_normal
    show oliver_thinking at pos_der with dissolve

    oliver "¿«Casi siempre»?"
    flynn "Bueno, una maga desesperada y un tanque invulnerable. ¡Bienvenida a los Reivindicadores, Wanda!"

    # E22-2 — Presentación del grupo completo
    hide wanda_shy
    show wanda_normal at pos_izq with dissolve

    narrador "Al cabo de un rato de charlar, nuestro grupo de aventureros estaba completo."
    narrador "Flynn: el líder del equipo y un ágil pero torpe ladrón."
    narrador "Oliver: la fuerza bruta, un fisicoculturista que ha adquirido la invulnerabilidad en su pose especial a través de la contracción de cada uno de sus músculos."
    narrador "Wanda: la maga de las pociones impredecibles, que lo único más loco que su personalidad son los efectos de su alquimia."

    jump primer_asalto


# =============================================================================
# PRIMER ASALTO AL CASTILLO (D01)
# =============================================================================

label primer_asalto:

    # E23-1
    scene bg castillo_ext with fade
    show wanda_normal at pos_izq with dissolve
    show flynn_normal at pos_centro with dissolve
    show oliver_thinking at pos_der with dissolve

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

    # E24-1 — Flynn explica el plan del ariete humano
    scene bg castillo_ext with fade
    show wanda_normal at pos_izq with dissolve
    show flynn_normal at pos_centro with dissolve
    show oliver_normal at pos_der with dissolve

    flynn "Escuchen bien, porque este plan es una obra maestra. Oliver, tu pose dorada te vuelve completamente indestructible, ¿verdad?"
    oliver "Así es. Cuando contraigo cada fibra de mi cuerpo, ni una catapulta podría hacerme un rasguño. El único detalle es que quedo inmóvil."
    flynn "¡Exacto! Por eso Wanda y yo te cargaremos en horizontal y te usaremos como un ariete humano para reventar esa puerta de un solo golpe."

    hide wanda_normal
    show wanda_shy at pos_izq with dissolve

    wanda "Espera, Flynn… ¿estás seguro de esto? Oliver parece pesar como un caballo… o dos."
    flynn "¡Pura física básica, Wanda! Un poco de impulso y entraremos como si nada. ¡Oliver, activa tu pose!"

    hide oliver_normal
    show oliver_pose at pos_der with dissolve

    oliver "Contemplen… el pináculo de la evolución humana."

    # E24-2 — Cargando a Oliver
    scene bg ariete_humano with fade

    narrador "Con más entusiasmo que sentido común, Flynn y Wanda logran levantar a la estatua dorada de ciento cincuenta kilos de puro músculo."
    flynn "¡Agh…! ¡Maldita sea, Oliver! ¿Qué desayunas, ladrillos?!"
    wanda "¡Mis brazos… no siento los brazos! ¡Creo que me va a estallar la espalda!"
    oliver "Mantengan la postura, muchachos. Un cuerpo perfecto exige una carga digna. ¡Ahora corran hacia la puerta!"
    flynn "¿¡Correr?! ¡Apenas puedo respirar…!"

    # E24-3 — La caída
    scene bg ariete_humano_caida with vpunch

    narrador "A los dos pasos, las piernas de Flynn y Wanda ceden al mismo tiempo y ambos se desploman de cara contra el suelo bajo el peso inamovible de su compañero."
    wanda "¡Ayy… mi sombrero! ¡Y mis pociones…!"
    flynn "¡Quítate de encima, Oliver… me estás aplastando las costillas!"
    oliver "Lo lamento, líder. No puedo desactivar la pose hasta relajar cada músculo… y además, el plan fue tuyo."
    narrador "Lo que Flynn no calculó es que, para usar a un fisicoculturista invulnerable como ariete, primero hay que tener la fuerza para cargarlo. Humillados y adoloridos, no les queda más remedio que retirarse."

    jump plan_b


label d01_pocion:

    # E25
    scene bg castillo_ext with fade
    show wanda_shy at pos_izq with dissolve
    show flynn_mad at pos_centro with dissolve
    # show flynn_golpeado at pos_centro

    narrador "Nuestro grupo ha decidido confiar en las habilidades alquímicas de Wanda. Lo que no esperaban era que dicha poción de invisibilidad los dejara ciegos de forma momentánea. Todo el mundo es invisible para una persona ciega…"

    jump plan_b


# =============================================================================
# PLAN B — Bifurcación principal (D02)
# =============================================================================

label plan_b:

    # E26-1 — Regreso derrotado a la taberna
    scene bg taberna with fade
    show wanda_shy at pos_izq with dissolve
    show flynn_mad at pos_centro with dissolve
    show oliver_normal at pos_der with dissolve

    narrador "Tras el desastroso fracaso del plan A, nuestro trío regresa derrotado a la taberna con el orgullo hecho pedazos."
    flynn "¡Mierda, ni siquiera nos acercamos a la bóveda! ¡El plan A fue un desastre total!"
    wanda "Lo siento… de verdad pensaba que esto iba a ser más fácil. A este paso nunca voy a poder pagar mis deudas."
    oliver "¿Rendirse tras un solo intento fallido? ¡Jamás! Ningún músculo crece sin resistencia. Si la puerta no cedió hoy, solo significa que necesitamos una herramienta más fuerte."

    hide wanda_shy
    show wanda_normal at pos_izq with dissolve
    hide flynn_mad
    show flynn_normal at pos_centro with dissolve
    hide oliver_normal
    show oliver_thinking at pos_der with dissolve

    narrador "Decididos a no darse por vencidos, se acercan a la barra. Si alguien en esta ciudad escucha rumores sobre reliquias raras y genios peligrosos, es el tabernero."
    flynn "Oye, amigo… una pregunta puramente hipotética. Si alguien quisiera atravesar una puerta enorme y supuestamente impenetrable —digamos, de una vieja ruina—, ¿qué usaría?"

    hide oliver_thinking with dissolve
    show tabernero_normal at pos_der with dissolve

    tabernero "¿Una «vieja ruina» en la colina del conde Marcus? Tranquilos, muchachos, no me importa a quién le roben mientras no me rompan más sillas."
    tabernero "Si de verdad buscan algo capaz de abrir lo impenetrable, solo he oído de dos opciones en todo el reino… y las dos suenan a suicidio."
    tabernero "La primera está en una ciudad hundida en el fondo del mar: unos hombres pez custodian un artefacto legendario capaz de cortar cualquier material de un solo tajo."
    tabernero "Y si no prefieren morir devorados por hombres pez, siempre pueden probar suerte con el loco de Orkenhaimer, el orco genio de los explosivos. Dicen que al menos una explosión te quema los nervios antes de que te duela."

    narrador "Con dos opciones monumentalmente mejores que el plan A —lo que confirma que la estrategia no es el fuerte de Flynn—, el grupo Rei debe elegir su siguiente paso."

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
    scene bg taller_orco with fade
    show wanda_normal at pos_izq with dissolve
    show oliver_normal at pos_centro with dissolve
    show ork_normal at pos_der with dissolve

    narrador "Después de seguir la cadena de rumores llegan hasta un orco llamado Orkenhaimer, el legendario orco genio pirómano con un arsenal infinito."
    narrador "Ahora la tarea que tienen en sus manos es lograr convencerlo y reclutarlo."

    # E27-2 / D03_A
    hide oliver_normal
    show oliver_thinking at pos_centro with dissolve
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
    scene bg taller_orco with vpunch
    show ork_normal at center with dissolve

    narrador "El grupo ha decidido mostrar su poderío y amenazar al orco, y por esto han terminado brutalmente derrotados por los explosivos de Orkenhaimer."
    narrador "¿Por qué creíste que es una buena decisión amenazar a un orco maniático de las explosiones?"

    call screen pantalla_final(
        titulo="Desintegrados por Orkenhaimer",
        subtitulo="Nunca amenaces a un orco maniático de los explosivos.",
        es_victoria=False,
        reintentar_label="rama_orkenhaimer"
    )


label ork_dinero:

    # E27-4
    scene bg taller_orco with fade
    show flynn_normal at pos_izq with dissolve
    show ork_happy at pos_der with dissolve

    narrador "Después de una no muy larga deliberación, decidieron hablar con el orco en el idioma universal: el dinero. El orco consideró su oferta y decidió ayudarlos."

    jump asalto_orkenhaimer


label ork_arma:

    # E27-5
    scene bg taller_orco with fade
    show flynn_normal at pos_izq with dissolve
    show ork_happy at pos_der with dissolve

    narrador "Tal parece que los orcos maniáticos de las explosiones tienen también su lado vanidoso. Tras convencerlo de demostrar el poder de su obra maestra, el orco está más que contento de ayudar."

    jump asalto_orkenhaimer


label asalto_orkenhaimer:

    # E27-6 — Asalto al castillo con Orkenhaimer
    scene bg castillo_ext with fade
    show flynn_normal at pos_izq with dissolve
    show ork_happy at pos_der with dissolve

    narrador "Tras reclutar exitosamente al orco, nuestro grupo emprende su asalto frontal al castillo mandando a volar por los aires a todos los guardias con los explosivos de Orkenhaimer hasta llegar a la bóveda."

    # E27-7 — Apertura de la bóveda
    scene bg boveda_magica with fade
    show oliver_pose at pos_centro with dissolve

    narrador "Ya habiendo llegado hasta la bóveda, usaron a Oliver como escudo con su pose legendaria para resguardarse de la explosión y abrir la bóveda."

    hide oliver_pose with dissolve
    show wanda_normal at pos_izq with dissolve
    show oliver_normal at pos_centro with dissolve
    show ork_happy at pos_der with dissolve

    narrador "El grupo huyó con el botín, consiguiendo su objetivo y finalizando esta historia."

    call screen pantalla_final(
        titulo="El Gran Golpe con Orkenhaimer",
        subtitulo="A fuerza de explosiones y usando a Oliver de escudo, el equipo Rei vacía la bóveda del conde.",
        es_victoria=True
    )


# =============================================================================
# RAMA MARÍTIMA (D02-B)
# =============================================================================

label rama_maritima:

    # E28-1
    scene bg mar with fade
    show wanda_normal at pos_izq with dissolve
    show flynn_normal at pos_centro with dissolve
    show oliver_normal at pos_der with dissolve

    narrador "Después de deliberar han decidido ir en búsqueda del artefacto marino. Para esto tuvieron que conseguir (y por conseguir digo robar) equipos de buceo que les permitan adentrarse al fondo del océano."

    # E28-2
    scene bg ciudad_pez with fade
    show monster_green at pos_izq with dissolve
    show monster_blue at pos_der with dissolve

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
    show oliver_pose at center with dissolve

    narrador "Decidido, Oliver se ofrece a encargarse de los guardianes y activa su pose legendaria. Pero no pasa absolutamente nada. ¿Qué pensaste que iba a hacer Oliver? Te recuerdo que no se puede mover cuando está en su pose."

    hide oliver_pose with dissolve
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
    scene bg ciudad_pez with fade
    show oliver_normal at pos_izq with dissolve
    show monster_green at pos_centro with dissolve
    show monster_blue at pos_der with dissolve

    narrador "Flynn, Wanda y Oliver han decidido atacar de frente a los guardianes. Por suerte para ellos, son peces de la cintura para arriba, por lo que se limitan a darles aletazos tan fuertes que se sienten como pequeñas caricias."

    jump mar_recuperar_artefacto


label mar_pocion:

    # E28-5 (poción)
    scene bg ciudad_pez with fade
    show wanda_shy at pos_izq with dissolve
    show monster_green at pos_centro with dissolve
    show monster_blue at pos_der with dissolve

    narrador "Por alguna razón han decidido confiar en las pociones de Wanda. Después de arrojarle el frasco a los guardianes se han dado cuenta de que es una poción de respiración, solo que es para respirar en tierra. Por lo que los guardianes han adquirido pulmones y murieron ahogados, dejando vía libre para que recuperen el artefacto."

    hide monster_green with dissolve
    hide monster_blue with dissolve

    jump mar_recuperar_artefacto


label mar_recuperar_artefacto:

    # E28-6 — Consiguen el artefacto
    scene bg ciudad_pez with fade
    show wanda_normal at pos_izq with dissolve
    show flynn_normal at pos_centro with dissolve
    show oliver_thinking at pos_der with dissolve

    narrador "Después de lidiar con los sorprendentemente inútiles guardianes, el grupo Rei consigue el artefacto. Resultó ser un sable láser capaz de cortar todo de un tajo. Se disponen a entrar en el castillo."

    # E28-7 — Infiltración y final
    scene bg castillo_int with fade

    narrador "Habiendo cortado la puerta de entrada y varios guardias en el camino, nuestro grupo llega hasta la bóveda y corta la puerta, dándoles acceso al botín y consiguiendo su objetivo."

    scene bg boveda_magica with fade
    show wanda_normal at pos_izq with dissolve
    show flynn_normal at pos_centro with dissolve
    show oliver_normal at pos_der with dissolve

    call screen pantalla_final(
        titulo="Robo Silencioso con Artefacto",
        subtitulo="Con el sable láser submarino, la banda corta cada cerrojo y se lleva el tesoro sin activar una sola alarma.",
        es_victoria=True
    )


# Fin del script
return
