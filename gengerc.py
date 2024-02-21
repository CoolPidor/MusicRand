import random
import os
from pydub import AudioSegment
from pydub.generators import Sine

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

import tkinter as tk

ming = 0
maxg = 22000


def main():
    global ming, maxg
    win = tk.Tk()

    win.resizable(False, False)
    win_width = 1200
    win_height = 600

    win.geometry(f'{win_width}x{win_height}+500+100')
    win.title('RandomMusic')
    win.configure(background='#404040')

    entry_name = tk.Entry()

    entry_name.pack(pady=(30, 0))

    label_entry_name = tk.Label(text='Имя конечного файла')
    label_entry_name.pack()

    entry_iterations = tk.Entry()
    entry_iterations.pack(pady=(30, 0))

    label_iterations = tk.Label(text='Количество итераций')
    label_iterations.pack()

    label_all_entries = tk.Label(text='', bg='#404040', fg='#fff', font='Arial 15')
    label_all_entries.pack(pady=(10, 0))

    label_min = tk.Label(text=str(ming))
    label_min.pack()

    def update_scale_min(v):
        global ming
        ming = int(v)
        label_min.configure(text=str(ming))

    scale_min = tk.Scale(win, from_=0, to=22000, orient=tk.HORIZONTAL, command=update_scale_min)
    scale_min.place(relx=0.38, rely=0.3)

    label_max = tk.Label(text=str(maxg))
    label_max.pack(side=tk.TOP)

    def update_scale_max(v):
        global maxg
        maxg = int(v)
        label_max.configure(text=str(maxg))

    scale_max = tk.Scale(win, from_=1, to=22000, orient=tk.HORIZONTAL, command=update_scale_max)
    scale_max.place(relx=0.53, rely=0.3)



    def start():
        global ming, maxg
        if entry_name.get() != '' and entry_iterations.get() != '':



            label_all_entries.configure(text='Надо заполнить все поля!')

            pygame.init()
            pygame.mixer.init()
            pygame.mixer.set_num_channels(20)


            try:
                c = int(entry_iterations.get())
            except ValueError:
                pass


            def simulate(cl, full_audio):
                global ming, maxg
                if ming > maxg:
                    r = ming
                    ming = maxg
                    maxg = r

                label_all_entries.configure(text=f'{round((cl / int(entry_iterations.get())) * 100, 2)}%')
                sine_wave = Sine(random.randint(ming, maxg))

                audio_segment = sine_wave.to_audio_segment(duration=random.randint(1, 500))
                full_audio += audio_segment
                audio_segment.export(f"{entry_name.get()}.mp3", format="mp3")

                sound = pygame.mixer.Sound(f'{entry_name.get()}.mp3')
                sound.play()

                if cl != c:
                    win.after(int(sound.get_length() * 1000), lambda: simulate(cl + 1, full_audio))

                else:
                    full_audio.export(f"{entry_name.get()}.mp3", format="mp3")

            simulate(0, AudioSegment.silent(duration=0))










        else:
            label_all_entries.configure(text='Надо заполнить все поля!')

    button_start = tk.Button(text='Начать', command=start)
    button_start.pack(pady=20)





    win.mainloop()


if __name__ == '__main__':
    main()
