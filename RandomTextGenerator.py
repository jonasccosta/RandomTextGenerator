# Create random text based on letter frequency in Portuguese

import pyautogui
import time
import random


# Fills the alphabet list with letters and space, based on the frequency of those characters in Portuguese
# Frequency from https://www.gta.ufrj.br/grad/06_2/alexandre/criptoanalise.html#:~:text=O%20comprimento%20m%C3%A9dio%20das%20palavras,10%20letras%20%C3%A9%20de%204.88


def set_up_portuguese_alphabet():
    alphabet = []

    a = ['a'] * 1463
    alphabet.extend(a)

    b = ['b'] * 104
    alphabet.extend(b)

    c = ['c'] * 388
    alphabet.extend(c)

    d = ['d'] * 499
    alphabet.extend(d)

    e = ['e'] * 1257
    alphabet.extend(e)

    f = ['f'] * 102
    alphabet.extend(f)

    g = ['g'] * 130
    alphabet.extend(g)

    h = ['h'] * 128
    alphabet.extend(h)

    i = ['i'] * 618
    alphabet.extend(i)

    j = ['j'] * 40
    alphabet.extend(j)

    k = ['k'] * 2
    alphabet.extend(k)

    l = ['l'] * 278
    alphabet.extend(l)

    m = ['m'] * 474
    alphabet.extend(m)

    n = ['n'] * 505
    alphabet.extend(n)

    o = ['o'] * 1073
    alphabet.extend(o)

    p = ['p'] * 252
    alphabet.extend(p)

    q = ['q'] * 120
    alphabet.extend(q)

    r = ['r'] * 653
    alphabet.extend(r)

    s = ['s'] * 781
    alphabet.extend(s)

    t = ['t'] * 434
    alphabet.extend(t)

    u = ['u'] * 463
    alphabet.extend(u)

    v = ['v'] * 167
    alphabet.extend(v)

    w = ['w'] * 1
    alphabet.extend(w)

    x = ['x'] * 21
    alphabet.extend(x)

    y = ['y'] * 1
    alphabet.extend(y)

    z = ['z'] * 47
    alphabet.extend(z)

    space = [' '] * 5000
    alphabet.extend(space)

    random.shuffle(alphabet)

    return alphabet


# Fills the alphabet list with letters and space, based on the frequency of those characters in English
# Frequency from https://en.wikipedia.org/wiki/Letter_frequency


def set_up_english_alphabet():
    alphabet = []

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

    return alphabet


def main():
    portuguese = set_up_portuguese_alphabet()
    english = set_up_english_alphabet()

    # How many characters will be pressed
    text_length = 1000

    # Time to click on a word processor, such as Microsoft Word
    time.sleep(5)

    previous = ""
    for i in range(text_length):

        # Choose alphabet
        letter = random.choice(portuguese)

        # Avoids double Spaces
        if previous != " " or letter != " ":
            pyautogui.press(letter)
        previous = letter


main()
