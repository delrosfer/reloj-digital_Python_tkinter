import time
import tkinter as tk


ventana = tk.Tk()
ventana.geometry("400x200")
ventana.resizable(False,False)
ventana.title("Reloj Digital con Tkinter y Python")
ventana.config(background='#C0C0C0')
time_label = tk.Label(text=time.strftime('%H:%M:%S'), font=('Arial', 54), fg='#00FF00', bg='#ffffff', pady=10, padx=10)
time_label.place(x=50, y=40)
print(time_label['text'])

def update_reloj():
	ahora = time.strftime('%H:%M:%S')

	if time_label['text'] != ahora:
		time_label['text'] = ahora

	ventana.after(1000, update_reloj)

update_reloj()

ventana.mainloop()