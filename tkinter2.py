from tkinter import *
from math import *

#Ventana
ventana =Tk()
ventana.title("Temperatura")
ventana.geometry("392x600")
ventana.configure(background="gray")

#Cristal
Salida=Entry(ventana,font=('arial',20,'bold'),width=22,bd=20,insertwidth=4,bg="white",justify="right").place(x=10,y=60)

#Cristal1


Salida=Entry(ventana,font=('arial',10,'bold'),width=12,bd=10,insertwidth=4,bg="white",justify="right").place(x=10,y=250)
boton1=Button(ventana,text="Celsius").place(x=10,y=295)


#Cristal2
Salida=Entry(ventana,font=('arial',10,'bold'),width=12,bd=10,insertwidth=4,bg="white",justify="right").place(x=200,y=250)
boton1=Button(ventana,text="Farenheit").place(x=200,y=295)

ventana.mainloop()