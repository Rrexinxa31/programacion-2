# un diccionario donde pongo las traducciones
JDRC_diccionario = {
    "hello": {"es": "hola", "fr": "bonjour"},
    "world": {"es": "mundo", "fr": "monde"},
    "cat": {"es": "gato", "fr": "chat"},
    "dog": {"es": "perro", "fr": "chien"},
    "book": {"es": "libro", "fr": "livre"},
    "food": {"es": "comida", "fr": "nourriture"},
    "water": {"es": "agua", "fr": "eau"},
    "house": {"es": "casa", "fr": "maison"},
    "sun": {"es": "sol", "fr": "soleil"},
    "computer": {"es": "computadora", "fr": "ordinateur"}
}

# una funcion para hacer las traducciones
def JDRC_traducir_palabra(JDRC_palabra, JDRC_idioma):
    # para hallar la palabra en el dicc
    if JDRC_palabra in JDRC_diccionario:
        return JDRC_diccionario[JDRC_palabra][JDRC_idioma]
    else:
        # si no esta la agrega 
        JDRC_traduccion = input(f"No conozco '{JDRC_palabra}'. ¿Cómo se traduce al {JDRC_idioma}? ")
        JDRC_diccionario[JDRC_palabra] = {JDRC_idioma: JDRC_traduccion}
        return JDRC_traduccion

# sirvepara traducir una frase completa
def JDRC_traducir_frase(JDRC_frase, JDRC_idioma):
    # tepara la frase en palabras
    JDRC_palabras = JDRC_frase.split()
    # traduce cada palabra
    JDRC_traduccion = []
    for JDRC_palabra in JDRC_palabras:
        JDRC_traduccion.append(JDRC_traducir_palabra(JDRC_palabra.lower(), JDRC_idioma))
    # pega las palabras traducidas en una frase
    return " ".join(JDRC_traduccion)

# funcion principal
def JDRC_traductor():
    while True:
        print("\nTraductor simple: inglés a español o francés")
        # Pide el idioma de destino
        while True:
            JDRC_idioma = input("¿A qué idioma quieres traducir? (es para español / fr para francés): ").strip().lower()
            if JDRC_idioma in ["es", "fr"]:
                break
            else:
                print("Por favor, elige un idioma válido (es para español o fr para francés).")
        
        # pide la frase en ingles
        JDRC_frase = input("Escribe una frase en inglés: ")
        
        # traduce la frase
        JDRC_resultado = JDRC_traducir_frase(JDRC_frase, JDRC_idioma)
        
        # muestra la traduccion
        print("Traducción:", JDRC_resultado)
        
        #inicia denuevo

#llama la funcion para iniciar de nuevo
JDRC_traductor()
