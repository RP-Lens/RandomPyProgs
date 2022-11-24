from scipy.integrate import odeint
import numpy as np
from tkinter import Tk, Canvas

#oliver sucks my juicy cock and licks it and twists it and bops it and nibbles on the cheese

#constants and shit
unstretchedL = 30
rate = 37
k = 0.1
m = 0.3
g = 9.8
steps = 1000

#state vectors - l, dl/dt, θ, dθ/dt
sv = [1, 1, 2, 1]

#diff shit
def diff_funcs(sv, time):
    #v
    func1 = sv[1]

    #((d^2)L)/d(t)^2
    func2 = (unstretchedL + sv[0]) * sv[3]**2 - (k / m * sv[0]) + g * np.cos(sv[2])
    #Ω
    func3 = sv[3]
    #((d^2)θ)/d(t)^2
    func4 = -(g * np.sin(sv[2]) + 2.0 * sv[1] * sv[3]) / (unstretchedL + sv[0])

    return np.array([func1, func2, func3, func4])

#solving shit idk
time = np.linspace(0, rate, steps)
sol = odeint(diff_funcs, sv, time)

xCo = (unstretchedL + sol[:, 0]) * np.sin(sol[:, 2])
yCo = (unstretchedL + sol[:, 0]) * np.cos(sol[:, 2])

#trying to make canvas
w = 250
h = 300
plotStep = 0

root = Tk()
canvas = Canvas(root, bg="LemonChiffon3", height=h, width=w)
canvas.pack(side='left')

def update():
    global plotStep

    #end shit
    if plotStep == steps:
        #repeat idk
        plotStep = 0
    

    x, y = int(xCo[plotStep] + w / 2), int(yCo[plotStep] + h / 2)

    #delete shit, make new shit
    canvas.delete('all')
    canvas.create_line(w / 2, 0, x, y, dash=(2, 1), width=1, fill='gold4')
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, outline='gold4', fill='lavender')
    
    plotStep += 1
    root.after(15, update)

update()
root.mainloop()
