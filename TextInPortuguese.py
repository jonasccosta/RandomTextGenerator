# Create random text based on letter frequency in Portuguese

import pyautogui
import time
import random

alphabet = []

# Fills the alphabet list with letters and space, based on the frequency of those characters in Portuguese
# Frequency from https://www.gta.ufrj.br/grad/06_2/alexandre/criptoanalise.html#:~:text=O%20comprimento%20m%C3%A9dio%20das%20palavras,10%20letras%20%C3%A9%20de%204.88


def set_up():
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
