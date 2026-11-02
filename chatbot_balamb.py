import nltk
from nltk.chat.util import Chat, reflections

# 1. BASE DE CONOCIMIENTO (Reglas basadas en la tabla de diseño conversacional)
pares_balamb = [
    # 1. Intención: Saludo
    [
        r"(?i).*(buenas tardes|buenas noches|buenos d[ií]as|hola|oye|qu[eé] tal).*",
        [
            "¡Hola! Soy el asistente virtual de la preparatoria Balamb. ¿En qué puedo ayudarte hoy?"
        ]
    ],
    # 2. Intención: Inscripción y costos
    [
        r"(?i).*(inscripci[oó]n|colegiatura|requisitos|reinscripci[oó]n|pagos|costo).*",
        [
            "Requisitos para inscripción: certificado de secundaria, acta de nacimiento, comprobante de domicilio. Para realizar el trámite de inscripción, visita admisiones.balamb.edu"
        ]
    ],
    # 3. Intención: Calendario escolar
    [
        r"(?i).*(calendario|ex[aá]menes|vacaciones|fechas|inicio de clases).*",
        [
            "El inicio del semestre es el 10 de agosto. Los exámenes del parcial ocurren del 6 al 11 de octubre, y los exámenes finales suceden en la semana del 1 al 6 de diciembre. El fin de semestre es el 6 de diciembre. El calendario completo con todas las fechas se encuentra en la página escolar oficial."
        ]
    ],
    # 4. Intención: Materiales y libros
    [
        r"(?i).*(libros|lista de materiales|[uú]tiles escolares|materiales|librer[ií]a).*",
        [
            "Los materiales de cada semestre se encuentran en librería.balamb.edu. Se pueden comprar en la librería de la escuela, o comprarlos en línea."
        ]
    ],
    # 5. Intención: Recuperar contraseña
    [
        r"(?i).*(contrase[nñ]a|correo|olvid[eé]|acceso).*",
        [
            "Si quieres recuperar la contraseña de tu correo institucional, accede al portal de alumnos (alumnos.balamb.edu), da click en 'Recuperar contraseña', e ingresa tus datos. La contraseña la recibirás en el correo alterno que proporciones."
        ]
    ],
    # 6. Intención: Envío de tareas
    [
        r"(?i).*(tarea|error al entregar|pdf|plataforma|subir archivo).*",
        [
            "Si no puedes subir tu tarea a la plataforma, asegúrate que esté en el formato correcto (pdf o docx), y que el archivo pese menos de 20MB."
        ]
    ],
    # 7. Intención: Soporte de plataforma
    [
        r"(?i).*(canvas|sesi[oó]n|c[aá]mara|en l[ií]nea|micr[oó]fono).*",
        [
            "Si tienes problemas con las clases en línea, asegúrate de que hayas accedido con tu correo institucional (@Balamb.edu). Intenta usar otro dispositivo (computadora o tablet). Asegúrate de darle permiso al programa de usar tu micrófono y tu cámara. Si sigue sin funcionar, puedes ver las clases grabadas en el calendario de la plataforma."
        ]
    ],
    # 8. Intención: Contacto y soporte
    [
        r"(?i).*(oficinas|tel[eé]fono|persona|asesor|asesora|director|coordinador|ventanilla).*",
        [
            "Si quieres contactar el personal de la escuela, llama o manda WhatsApp a Dirección: 871-721-8787. Horario de atención: 8:00am a 4pm de lunes a viernes."
        ]
    ],
    # 9. Intención: Despedida
    [
        r"(?i).*(gracias|nos vemos|hasta luego|bye|adi[oó]s|ya ser[ií]a todo).*",
        [
            "¡Fue un placer! Si necesitas más ayuda, no dudes en contactarme!"
        ]
    ],
    # 10. Intención: Fallback (Manejo de consultas no reconocidas)
    [
        r"(.*)",
        [
            "Disculpa, no entiendo bien tu pregunta. Te puedo ayudar en estos temas: lista de materiales, calendarios escolares, o inscripciones. Si necesitas ayuda personalizada, escribe 'oficinas' para proporcionarte los contactos."
        ]
    ]
]

# 2. INICIALIZACIÓN DEL CHATBOT CON NLTK
bot_balamb = Chat(pares_balamb, reflections)

# 3. INTERFAZ DE EJECUCIÓN INTERACTIVA
def ejecutar_chat():
    print("=" * 65)
    print("ASISTENTE VIRTUAL PREPARATORIA BALAMB (Escribe 'salir' para cerrar)")
    print("=" * 65)
    while True:
        mensaje = input("\nUsuario: ")
        if mensaje.strip().lower() in ['salir', 'exit', 'quit']:
            print("\nAsistente: ¡Sesión terminada con éxito!")
            break
        respuesta = bot_balamb.respond(mensaje)
        print(f"\nAsistente: {respuesta}")

# Ejecutar el asistente
ejecutar_chat()
