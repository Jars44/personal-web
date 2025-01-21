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
        ("Pop a couple pills in the daytime, uh", 0.050),
        ("Heard you got a friend, what her head like? Uh", 0.050),
        ("Probably should've fucked on the first night, uh", 0.050),
        ("Now I gotta wait for the green light, uh", 0.050),
        ("I don't wanna wait for no green light, uh", 0.050),
        ("Narcolepsy got me feeling stage fright, uh", 0.050),
        ("Luckily, I float at insane heights, yeah", 0.050),
        ("Luckily, luckily, luckily, yah", 0.050),
    ]
    delays = [0.3, 2, 3, 4, 5, 6, 7, 8]
    
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