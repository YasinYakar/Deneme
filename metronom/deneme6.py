import tkinter as tk
from tkinter import Frame
import simpleaudio, time

theme_colors = {'bg': '#CDC8B1', 'text':'#8B7355', 'label_bg':'#FFFFE0', 'scale_through':'#A3CEC5'}
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

#Sol frame
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

# orta frame
# tempoyu adını arayüzde gösterme  
tempo_label =tk.Label(midFrame, text='120', font=(theme_fonts[0], 90, 'bold'),
                      justify='center', fg = theme_colors['text'], bg = theme_colors['label_bg'], anchor='s')
tempo_label.pack(fill='both', expand=1)

marking_label =tk.Label(midFrame, text='Allegretto', font=(theme_fonts[0], 90, 'bold'),
                      justify='center', fg = theme_colors['text'], bg = theme_colors['label_bg'], anchor='n')
marking_label.pack(fill='both', expand=1)

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

window.mainloop()