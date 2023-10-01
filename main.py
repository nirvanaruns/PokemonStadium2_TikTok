import time
import keyboard
import threading
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent

# Mapeo de palabras clave a teclas
key_mappings = {
    # Español
    "arriba": "w",
    "abajo": "s",
    "izquierda": "a",
    "derecha": "d",
    "botona": "q",
    "botonb": "e",
    "botonl": "o",
    "botonr": "p",  # Cambio de "1" a "p"
    "carriba": "y",
    "cabajo": "h",
    "cizquierda": "g",
    "cderecha": "j",
    "start": "m",
    "select": "l",
    # Inglés
    "up": "w",
    "down": "s",
    "left": "a",
    "right": "d",
    "buttona": "q",
    "buttonb": "e",
    "buttonl": "o",
    "buttonr": "p",  # Cambio de "1" a "p"
    "cup": "y",
    "cdown": "h",
    "cleft": "g",
    "cright": "j",
    "start": "m",
    "select": "l"
}

# Función para mantener una tecla presionada durante un tiempo específico
def hold_key(key_event, duration):
    keyboard.press(key_event)
    time.sleep(duration)
    keyboard.release(key_event)

# Función para procesar comentarios
def process_comment(comment):
    try:
        comentario = comment.lower()  # Convertir a minúsculas
        print(f"Comentario recibido: {comment}")

        if "botonr" in comentario or "buttonr" in comentario:
            # Mantener presionada la tecla "botonr" durante 10 segundos en un hilo separado
            thread = threading.Thread(target=hold_key, args=("p", 10))
            thread.start()
        else:
            # Liberar "botonr" si se presiona otra tecla del mapeo
            if "p" in keyboard._pressed_events:
                keyboard.release("p")
            # Buscar palabras clave en el comentario y ejecutar acciones de teclado
            for palabra, tecla in key_mappings.items():
                if palabra in comentario:
                    execute_key_event(tecla)

    except Exception as err:
        print(f"Error: {err}\nSaliendo del programa")
        time.sleep(4)
        quit()

# Función para ejecutar eventos de teclado
def execute_key_event(key_event):
    keyboard.press(key_event)
    time.sleep(0.3)
    keyboard.release(key_event)

# Función para manejar eventos de comentarios de TikTok
async def on_ttcomment(event: CommentEvent):
    process_comment(event.comment)

if __name__ == "__main__":
    tiktok_username = input("TIKTOK username: ")
    tiktok_client = TikTokLiveClient(unique_id="@" + tiktok_username)
    on_ttcomment = tiktok_client.on("comment")(on_ttcomment)
    print("Conectado a TikTok")
    tiktok_client.run()
