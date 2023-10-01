import time
import keyboard
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent

key_mappings = {
    # Español test
    "arriba": "z",
    "abajo": "x",
    "izquierda": "c",
    "derecha": "v",
    "botona": "b",
    "botonb": "n",
    "start": "m",
    "select": "l",
    # Inglés
    "up": "z",
    "down": "x",
    "left": "c",
    "right": "v",
    "buttona": "n",
    "buttonb": "b",
    "start": "m",
    "select": "l"
}

def execute_key_event(key_event):
    keyboard.press(key_event)
    time.sleep(0.3)
    keyboard.release(key_event)

async def on_ttcomment(event: CommentEvent):
    try:
        comentario = event.comment.lower()  # Convertir a minúsculas
        with open("log.txt", 'a', encoding="utf-8") as log_file:
            log_file.write(f"{event.user.nickname} -> {event.comment}\n")
        print(f"{event.user.nickname} -> {event.comment}")

        for palabra, tecla in key_mappings.items():
            if palabra in comentario:
                execute_key_event(tecla)

    except Exception as err:
        print(f"{err}\n Quitting now")
        time.sleep(4)
        quit()

if __name__ == "__main__":
    tiktok_username = input("TIKTOK username: ")
    tiktok_client = TikTokLiveClient(unique_id="@" + tiktok_username)
    on_ttcomment = tiktok_client.on("comment")(on_ttcomment)
    print("connected")
    tiktok_client.run()

    while True:
        time.sleep(1)