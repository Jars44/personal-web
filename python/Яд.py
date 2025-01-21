import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Я тот случай, голову ломай", 0.1),
        ("Круче всех-всех сучек, просто понимай", 0.085),
        ("Ha высоту сам себя поднимай", 0.090),
        ("Свою пустоту мною не заполняй", 0.1),
        ("не заполняй", 0.1),
        ("Хочешь меня, сам себя поменяй", 0.1),
        ("сам себя поменяй", 0.090),
    ]
    delays = [0.3, 3.0, 6.8, 9.7, 14.5, 19.5, 24.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()