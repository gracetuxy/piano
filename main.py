import tkinter as tk
import music as M
import pygame

pygame.init()

freq = { #frequencies of keys on the pianos in the 1st, 2nd, 3rd, 4th,... octaves
    "C": [16.35, 32.70, 65.41, 130.81, 261.63, 523.25, 1046.50, 2093.00, 4186.01],
    "Db":   [17.32, 34.65, 69.30, 138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92],
    "D":   [18.35, 36.71, 73.42, 146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.64],
    "Eb":   [19.45, 38.89, 77.78, 155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03],
    "E":   [20.60, 41.20, 82.41, 164.81, 329.63, 659.26, 1318.51, 2637.02],
    "F":   [21.83, 43.65, 87.31, 174.61, 349.23, 698.46, 1396.91, 2793.83],
    "Gb":   [23.12, 46.25, 92.50, 185.00, 369.99, 739.99, 1479.98, 2959.96],
    "G":   [24.50, 49.00, 98.00, 196.00, 392.00, 783.99, 1567.98, 3135.96],
    "Ab":   [25.96, 51.91, 103.83, 207.65, 415.30, 830.61, 1661.22, 3322.44],
    "A":   [27.50, 55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00],
    "Bb":   [29.14, 58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31],
    "B":   [30.87, 61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07]
}
b = M.core.Being() # b is our piano
b.fv_ = [1]  # vibrato frequency
b.nu_ = [0]  # vibrato depth in semitones (maximum deviation of pitch)
b.d_ = [1/3] # duration

def create_note(octave):
    for key in freq.keys():
        b.f_ = [freq[key][octave]]
        #  render the wavfile
        b.render(1, f"{key}{octave}.wav")

create_note(5)
create_note(4)
create_note(3)

def play_note(key, octave):
    sound = pygame.mixer.Sound(f"C:/Users/grace/PycharmProjects/Piano/{key}{octave}.wav")
    sound.play()

root = tk.Tk()
root.geometry("1500x356")
c3 = tk.Button(root, command=lambda:play_note("C",3), width=8, height=23, relief="raised")
c3.grid(row=1, column=1)
d3 = tk.Button(root, command=lambda:play_note("D",3), width=8, height=23, relief="raised")
d3.grid(row=1, column=2)
e3 = tk.Button(root, command=lambda:play_note("E",3), width=8, height=23, relief="raised")
e3.grid(row=1, column=3)
f3 = tk.Button(root, command=lambda:play_note("F",3), width=8, height=23, relief="raised")
f3.grid(row=1, column=4)
g3 = tk.Button(root, command=lambda:play_note("G",3), width=8, height=23, relief="raised")
g3.grid(row=1, column=5)
a3 = tk.Button(root, command=lambda:play_note("A",3), width=8, height=23, relief="raised")
a3.grid(row=1, column=6)
b3 = tk.Button(root, command=lambda:play_note("B",3), width=8, height=23, relief="raised")
b3.grid(row=1, column=7)
db3 = tk.Button(root, command=lambda:play_note("Db",3), width=6, height=12, relief="raised", bg="black")
db3.place(x=38, y=0)
eb3 = tk.Button(root, command=lambda:play_note("Eb",3), width=6, height=12, relief="raised", bg="black")
eb3.place(x=105, y=0)
gb3 = tk.Button(root, command=lambda:play_note("Gb",3), width=6, height=12, relief="raised", bg="black")
gb3.place(x=236, y=0)
ab3 = tk.Button(root, command=lambda:play_note("Ab",3), width=6, height=12, relief="raised", bg="black")
ab3.place(x=303, y=0)
bb3 = tk.Button(root, command=lambda:play_note("Bb",3), width=6, height=12, relief="raised", bg="black")
bb3.place(x=370, y=0)

c4 = tk.Button(root, command=lambda:play_note("C",4), width=8, height=23, relief="raised")
c4.grid(row=1, column=8)
d4 = tk.Button(root, command=lambda:play_note("D",4), width=8, height=23, relief="raised")
d4.grid(row=1, column=9)
e4 = tk.Button(root, command=lambda:play_note("E",4), width=8, height=23, relief="raised")
e4.grid(row=1, column=10)
f4 = tk.Button(root, command=lambda:play_note("F",4), width=8, height=23, relief="raised")
f4.grid(row=1, column=11)
g4 = tk.Button(root, command=lambda:play_note("G",4), width=8, height=23, relief="raised")
g4.grid(row=1, column=12)
a4 = tk.Button(root, command=lambda:play_note("A",4), width=8, height=23, relief="raised")
a4.grid(row=1, column=13)
b4 = tk.Button(root, command=lambda:play_note("B",4), width=8, height=23, relief="raised")
b4.grid(row=1, column=14)
db4 = tk.Button(root, command=lambda:play_note("Db",4), width=6, height=12, relief="raised", bg="black")
db4.place(x=501, y=0)
eb4 = tk.Button(root, command=lambda:play_note("Eb",4), width=6, height=12, relief="raised", bg="black")
eb4.place(x=568, y=0)
gb4 = tk.Button(root, command=lambda:play_note("Gb",4), width=6, height=12, relief="raised", bg="black")
gb4.place(x=699, y=0)
ab4 = tk.Button(root, command=lambda:play_note("Ab",4), width=6, height=12, relief="raised", bg="black")
ab4.place(x=766, y=0)
bb4 = tk.Button(root, command=lambda:play_note("Bb",4), width=6, height=12, relief="raised", bg="black")
bb4.place(x=832, y=0)

c5 = tk.Button(root, command=lambda:play_note("C",5), width=8, height=23, relief="raised")
c5.grid(row=1, column=15)
d5 = tk.Button(root, command=lambda:play_note("D",5), width=8, height=23, relief="raised")
d5.grid(row=1, column=16)
e5 = tk.Button(root, command=lambda:play_note("E",5), width=8, height=23, relief="raised")
e5.grid(row=1, column=17)
f5 = tk.Button(root, command=lambda:play_note("F",5), width=8, height=23, relief="raised")
f5.grid(row=1, column=18)
g5 = tk.Button(root, command=lambda:play_note("G",5), width=8, height=23, relief="raised")
g5.grid(row=1, column=19)
a5 = tk.Button(root, command=lambda:play_note("A",5), width=8, height=23, relief="raised")
a5.grid(row=1, column=20)
b5 = tk.Button(root, command=lambda:play_note("B",5), width=8, height=23, relief="raised")
b5.grid(row=1, column=21)
db5 = tk.Button(root, command=lambda:play_note("Db",5), width=6, height=12, relief="raised", bg="black")
db5.place(x=963, y=0)
eb5 = tk.Button(root, command=lambda:play_note("Eb",5), width=6, height=12, relief="raised", bg="black")
eb5.place(x=1030, y=0)
gb5 = tk.Button(root, command=lambda:play_note("Gb",5), width=6, height=12, relief="raised", bg="black")
gb5.place(x=1161, y=0)
ab5 = tk.Button(root, command=lambda:play_note("Ab",5), width=6, height=12, relief="raised", bg="black")
ab5.place(x=1228, y=0)
bb5 = tk.Button(root, command=lambda:play_note("Bb",5), width=6, height=12, relief="raised", bg="black")
bb5.place(x=1293, y=0)

root.mainloop()