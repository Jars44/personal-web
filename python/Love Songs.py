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
        ("I miss my cocoa butter kisses, hope you smile when you listen", 0.060),
        ("Ain't no competition, just competin' for attention", 0.080),
        ("And you like, i'm not on no games", 0.090),
        ("Well, baby, i been peepin', and you ain't been the same", 0.065),
        ("Like, who been on your mind? Who got your time?", 0.080),
        ("Who you been vibin' with and why i can't make you mine?", 0.065),
        ("You used to be texting me, checking me, calling me your smile", 0.070),
        ("And now you treat me like my worth less than a dime", 0.080),
    ]
    delays = [0.3, 4.5, 7.5, 11, 12, 13, 14, 15]
    
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