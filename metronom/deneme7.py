import tkinter as tk
from tkinter import Frame
import simpleaudio, time

theme_colors = {'bg': '#52767D', 'text':'#FFFFE6', 'label_bg':'#3D998D', 'scale_through':'#A3CEC5'}
theme_fonts = ['Helvetica']
tempo_range = [30, 230]
defaults = {'tempo': 120, 'scale_length': 550}

# Ana pencere
window = tk.Tk()
window.title('Metronome')
window.geometry('900x300')

# 3 frame oluşturma
leftFrame = Frame(window)
leftFrame.config(bg=theme_colors['bg'])
leftFrame.pack(side='left',fill='both')

midFrame = Frame(window)
midFrame.pack(side='left', fill='both')

rightFrame = Frame(window)
rightFrame.pack(side='left', fill='both', expand=1)

# sol frame
time_signatures = {1: [' 2 / 4', (2, 4)], 2: [' 3 / 4',(3 ,4)], 3: [' 4 / 4',(4, 4)], 4: [' 2 / 2',(2, 2)],
                   5: [' 6 / 8',(6, 8)], 6: [' 9 / 8',(9, 8)], 7: ['12/ 8',(12, 8)],
                   8: [' * / 4',(-1, 4)], 9: [' * / 2',(-1,2)], 10: [' * / 8',(-1,8)]}
ts_mode = tk.IntVar(leftFrame)
for mode in time_signatures.keys():
    radio_button = tk.Radiobutton(leftFrame, text = time_signatures[mode][0], variable = ts_mode,
                    value = mode, fg=theme_colors['text'],
                    bg=theme_colors['bg'], anchor='w', font=(theme_fonts[0], 17))
    if time_signatures[mode][-1] == (4, 4): # Select 4/4 by default
        radio_button.select()
    radio_button.pack(fill='x')

# orta framede
# tempoyu adını arayüzde gösterme 
tempo_label =tk.Label(midFrame, text='120', font=(theme_fonts[0], 90, 'bold'),
                      justify='center', fg = theme_colors['text'], bg = theme_colors['label_bg'], anchor='s')
tempo_label.pack(fill='both', expand=1)

marking_label =tk.Label(midFrame, text='Allegretto', font=(theme_fonts[0], 90, 'bold'),
                      justify='center', fg = theme_colors['text'], bg = theme_colors['label_bg'], anchor='n')
marking_label.pack(fill='both', expand=1)

import simpleaudio, time 
strong_beat = simpleaudio.WaveObject.from_wave_file('strong_beat.wav')
weak_beat = simpleaudio.WaveObject.from_wave_file('weak_beat.wav')
sub_strong_beat = simpleaudio.WaveObject.from_wave_file('sub_strong_beat.wav')

time_list = [1648565267.9251342, 1648565268.482229, 1648565269.013833, 1648565269.560467, 1648565270.105812, 1648565270.644593, 1648565271.175668]

def tempo_estimate(time_list):
    list_len = len(time_list)
    N = 6
    if list_len < 6:
        interval = (time_list[-1] - time_list[0]) / (list_len - 1)
    else:
        interval = (time_list[-1] - time_list[-N]) / (N - 1)
    temp = int(60/interval)
    return temp

print('The estimated tempo is {} BPM.'.format(tempo_estimate(time_list)))


markings = {'Largo': [40, 60], 'Adagio': [66 ,76], 'Andante': [76, 108],
            'Allegretto': [112, 120], 'Allegro': [120, 156], 'Presto':[168, 200],
            'Prestissimo':[200, 330]}
# tempo adını bulan fonksiyon
def tempo_marking_of(tempo):
    for key in markings.keys():
        if tempo >= markings[key][0] and tempo <= markings[key][1]:
            marking = key
            break
        else:
            marking = ''
    return marking
# fonksiyonu test etme
for tempo in range(30, 230, 40):
    print("The marking of {} BPM is {}.".format(tempo, tempo_marking_of(tempo)))

# tempoyu değiştirmek için kaydırmalı çubuk
scale = tk.Scale(midFrame,
             from_=tempo_range[0],
             to= tempo_range[1],
             orient=tk.HORIZONTAL,
             length=defaults['scale_length'],
             showvalue=0,
             troughcolor = theme_colors['scale_through'],
             bd = 0,
             activebackground = theme_colors['text'],
             bg = theme_colors['label_bg'],
             sliderlength = 30,
             font=(theme_fonts[0]))
scale.set(defaults['tempo'])
scale.pack(side='bottom',fill='both', expand='0')

# sağdaki frame
# Toplam vuruş sayısını gösterme
count_label =tk.Label(rightFrame, text='0', fg=theme_colors['text'], bg =theme_colors['bg'], width=3, font=(theme_fonts[0], 180, 'bold'), justify='left')
count_label.pack(fill='both', expand=1)

tempo = 120
time_signature = time_signatures[ts_mode.get()][-1]
interval_ms = int((60/tempo) * (4/time_signature[-1]) * 1000)

def play():
    strong_beat.play()
    window.after(interval_ms, play)

window.after(interval_ms, play)

window.mainloop()