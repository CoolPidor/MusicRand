import random
import tkinter as tk
import os
import time
from tkinter import filedialog
import keyboard

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

if not os.path.exists('history'):
    os.mkdir('history')

import pygame

notes = ['do', 'do_dies', 're', 're_dies', 'mi', 'fa', 'fa_dies', 'sol',
         'sol_dies', 'la', 'la_dies', 'si', 'do2']

win = tk.Tk()
win.resizable(False, False)
win_width = 1200
win_height = 600

cut_on = 50
save_history = False
history_name = time.time()
pause = 0

win.geometry(f'{win_width}x{win_height}+500+100')
win.title('RandomMusic')
win.configure(background='#404040')
win.iconbitmap('icon.ico')

entry = tk.Entry(win)

do_button = tk.Button(win, text="Do", fg="black", bg="white", width=win_width // 100, height=20,
                      command=lambda: play('do'))
do_dies_button = tk.Button(win, text="Do\ndies", fg="white", bg="black", width=win_width // 170, height=10,
                           command=lambda: play('do_dies'))
re_button = tk.Button(win, text="Re", fg="black", bg="white", width=win_width // 100, height=20,
                      command=lambda: play('re'))
re_dies_button = tk.Button(win, text="Re\ndies", fg="white", bg="black", width=win_width // 130, height=10,
                           command=lambda: play('re_dies'))
mi_button = tk.Button(win, text="Mi", fg="black", bg="white", width=win_width // 100, height=20,
                      command=lambda: play('mi'))
fa_button = tk.Button(win, text="Fa", fg="black", bg="white", width=win_width // 100, height=20,
                      command=lambda: play('fa'))
fa_dies_button = tk.Button(win, text="Fa\ndies", fg="white", bg="black", width=win_width // 130, height=10,
                           command=lambda: play('fa_dies'))
sol_button = tk.Button(win, text="Sol", fg="black", bg="white", width=win_width // 100, height=20,
                       command=lambda: play('sol'))
sol_dies_button = tk.Button(win, text="Sol\ndies", fg="white", bg="black", width=win_width // 130, height=10,
                            command=lambda: play('sol_dies'))
la_button = tk.Button(win, text="La", fg="black", bg="white", width=win_width // 100, height=20,
                      command=lambda: play('la'))
la_dies_button = tk.Button(win, text="La\ndies", fg="white", bg="black", width=win_width // 130, height=10,
                           command=lambda: play('la_dies'))
si_button = tk.Button(win, text="Si", fg="black", bg="white", width=win_width // 100, height=20,
                      command=lambda: play('si'))
do2_button = tk.Button(win, text="Do", fg="black", bg="white", width=win_width // 100, height=20,
                       command=lambda: play('do2'))


def main():
    do_button.pack(side=tk.LEFT, padx=5)

    do_dies_button.pack(side=tk.LEFT, padx=1, anchor='n', pady=win_height // 5.3)

    re_button.pack(side=tk.LEFT, padx=5)

    re_dies_button.pack(side=tk.LEFT, padx=1, anchor='n', pady=win_height // 5.3)

    mi_button.pack(side=tk.LEFT, padx=5)

    fa_button.pack(side=tk.LEFT, padx=5)

    fa_dies_button.pack(side=tk.LEFT, padx=1, anchor='n', pady=win_height // 5.3)

    sol_button.pack(side=tk.LEFT, padx=5)

    sol_dies_button.pack(side=tk.LEFT, padx=1, anchor='n', pady=win_height // 5.3)

    la_button.pack(side=tk.LEFT, padx=5)

    la_dies_button.pack(side=tk.LEFT, padx=1, anchor='n', pady=win_height // 5.3)

    si_button.pack(side=tk.LEFT, padx=5)

    do2_button.pack(side=tk.LEFT, padx=5)

    start_button = tk.Button(win, text="Start", fg="black", bg="#757474", width=win_width // 100, height=3,
                             command=lambda: start(0), font='Arial 15')
    start_button.place(relx=0.44, rely=0.82)

    entry.place(relx=0.2, rely=0.85)

    entry_label = tk.Label(win, text="Number of notes", fg="black", bg="#969292", width=win_width // 100, height=1,
                           font='Arial 10')
    entry_label.place(relx=0.21, rely=0.9)

    # Это нотный стан, который я не решился реализовать
    # sheet = tk.Label(win, text=(('_'*170)+'\n')*5)
    # sheet.place(relx=0.5, rely=0.05, anchor='n')

    keyboard.add_hotkey('1', one)
    keyboard.add_hotkey('2', two)
    keyboard.add_hotkey('3', three)
    keyboard.add_hotkey('4', fo)
    keyboard.add_hotkey('5', five)
    keyboard.add_hotkey('6', six)
    keyboard.add_hotkey('7', seven)
    keyboard.add_hotkey('8', eight)
    keyboard.add_hotkey('9', nine)
    keyboard.add_hotkey('0', zero)
    keyboard.add_hotkey('-', minus)
    keyboard.add_hotkey('+', plus)
    keyboard.add_hotkey('backspace', backspace)

    main_repeat()


def one():
    play('do')


def two():
    play('do_dies')


def three():
    play('re')


def fo():
    play('re_dies')


def five():
    play('mi')


def six():
    play('fa')


def seven():
    play('fa_dies')


def eight():
    play('sol')


def nine():
    play('sol_dies')


def zero():
    play('la')


def minus():
    play('la_dies')


def plus():
    play('si')


def backspace():
    play('do2')


def update_cut_var(v):
    global cut_on
    cut_on = int(v)
    label_cut_on_display.configure(text=f"Cutting notes: {cut_on} s/10")


scale = tk.Scale(win, from_=0, to=50, orient=tk.HORIZONTAL, command=update_cut_var)
scale.pack()
label_cut_on_display = tk.Label(win, text=f"Cutting notes: {cut_on} s/10")
label_cut_on_display.pack()
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(20)

save_history_var = tk.IntVar()


def toggle():
    global save_history_var, save_history, history_name, pause
    current_state = save_history_var.get()
    if current_state == 0:
        save_history = False
    else:
        save_history = True
        history_name = time.time()
        pause = 0


toggle_save_history_button = tk.Checkbutton(win, text="Save History", variable=save_history_var, command=toggle)
toggle_save_history_button.place(relx=0.25, rely=0.05)


def stop_sounds():
    global cut_on
    pygame.mixer.stop()
    r = cut_on
    cut_on = 0
    cut_on = r


stop_button = tk.Button(text='STOP', bg='red', width=10, height=2, command=stop_sounds)
stop_button.place(relx=0.75, rely=0.86)


def load_history():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    def simulate(c):

        note = open(file_path, 'r').readlines()[c].split(' ')[1][:-1]

        pause_locale = open(file_path, 'r').readlines()[c].split(' ')[3]
        play(note)

        if c + 1 < len(open(file_path, 'r').readlines()):
            win.after(int(pause_locale), lambda: simulate(c + 1))

        else:
            c += 1

    simulate(0)


load_history_button = tk.Button(text='Load History', command=load_history)
load_history_button.place(relx=0.65, rely=0.05)


def play(note):
    global save_history, history_name, pause
    eval(f'{note}_button.configure(bg="red")')

    sound = pygame.mixer.Sound(f'sounds/{note}.mp3')
    sound.play()

    def rcr():
        sound.stop()
        clr = 'black' if note.endswith('_dies') else 'white'

        eval(f'{note}_button.configure(bg="{clr}")')

    if cut_on < 50:
        win.after(cut_on * 100, rcr)

    else:
        win.after(round(sound.get_length()) * 1000, rcr)

    if save_history:
        with open(f'history/{history_name}.txt', 'a', encoding='UTF-8') as f:
            f.write(f'Note: {note}; Pause: {pause} milliseconds\n')
        pause = 0


def start(i):
    global entry
    play(random.choice(notes))

    if entry.get() != '' and i + 1 < int(entry.get()):
        win.after(random.randint(10, 1000), lambda: start(i + 1))


def main_repeat():
    global pause
    pause = pause + 10
    win.after(10, main_repeat)


if __name__ == '__main__':
    main()

win.mainloop()
