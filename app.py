import openai
import speech_recognition as sr
import pyttsx3

# Configurar tu clave API de OpenAI
openai.api_key = 'PONER_API_KEY_AQUI'

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

def reconocer_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
    try:
        print("Reconociendo...")
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"Tú dijiste: {texto}")
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return None
    except sr.RequestError:
        print("Error al conectarse al servicio de reconocimiento de voz")
        return None

def obtener_respuesta_de_gpt(texto):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=texto,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error al conectarse a la API de OpenAI: {e}")
        return None

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def asistente_de_voz():
    while True:
        texto = reconocer_voz()
        if texto:
            respuesta = obtener_respuesta_de_gpt(texto)
            if respuesta:
                print(f"GPT-3: {respuesta}")
                hablar(respuesta)

if __name__ == "__main__":
    asistente_de_voz()
