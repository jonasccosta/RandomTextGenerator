# Create random text based on letter frequency in English

import pyautogui
import time
import random

alphabet = []

# Fills the alphabet list with letters and space, based on the frequency of those characters in English
# Frequency from https://en.wikipedia.org/wiki/Letter_frequency


def set_up():
    a = ['a'] * 820
    alphabet.extend(a)

    b = ['b'] * 150
    alphabet.extend(b)

    c = ['c'] * 280
    alphabet.extend(c)

    d = ['d'] * 430
    alphabet.extend(d)

    e = ['e'] * 1300
    alphabet.extend(e)

    f = ['f'] * 220
    alphabet.extend(f)

    g = ['g'] * 200
    alphabet.extend(g)

    h = ['h'] * 610
    alphabet.extend(h)

    i = ['i'] * 700
    alphabet.extend(i)

    j = ['j'] * 15
    alphabet.extend(j)

    k = ['k'] * 77
    alphabet.extend(k)

    l = ['l'] * 400
    alphabet.extend(l)

    m = ['m'] * 240
    alphabet.extend(m)

    n = ['n'] * 670
    alphabet.extend(n)

    o = ['o'] * 750
    alphabet.extend(o)

    p = ['p'] * 190
    alphabet.extend(p)

    q = ['q'] * 9
    alphabet.extend(q)

    r = ['r'] * 600
    alphabet.extend(r)

    s = ['s'] * 630
    alphabet.extend(s)

    t = ['t'] * 910
    alphabet.extend(t)

    u = ['u'] * 280
    alphabet.extend(u)

    v = ['v'] * 98
    alphabet.extend(v)

    w = ['w'] * 240
    alphabet.extend(w)

    x = ['x'] * 15
    alphabet.extend(x)

    y = ['y'] * 200
    alphabet.extend(y)

    z = ['z'] * 7
    alphabet.extend(z)

    space = [' '] * 3000
    alphabet.extend(space)

    random.shuffle(alphabet)


def main():
    set_up()

    # How many characters will be pressed
    text_length = 1000

    # Time to click on a word processor, such as Microsoft Word
    time.sleep(5)

    previous = ""
    for i in range(text_length):
        letter = random.choice(alphabet)

        # Avoids double Spaces
        if previous != " " or letter != " ":
            pyautogui.press(letter)
        previous = letter


main()