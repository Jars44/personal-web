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
        ("I'm a jagaban", 0.045),
        ("Classy, bougie, riffraff", 0.050),
        ("Only fuck with good vibes", 0.060),
        ("Hennessy with no chaser", 0.060),
        ("Only thing i chase is paper", 0.060),
        ("I'm a jagaban", 0.045),
        ("Classy, bougie, riffraff", 0.050),
        ("Only fuck with good vibes", 0.050),
        ("Hennessy with no chaser", 0.060),
        ("Only thing i chase is paper", 0.065),
        ("Only thing i chase is paper", 0.065),
        ("Only thing i chase is paper", 0.060), 
        ("Only thing i chase is paper", 0.060),
        ("Because i am a jagaban-ban-ban, a jagaban", 0.080) 
    ]
    delays = [0.3, 1.6, 3.6, 4.9, 6.5, 8.5, 9.8, 11.8, 13.5, 14.3, 16.8, 19.3, 21.3, 23.8, 25.3, 27.6, 28.0]
    
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