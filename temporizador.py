import subprocess

print("*Bienvenido al Programador de Apagado Automatico para Windows*")
print()
print("Que desea hacer?")
print("Coloque 1 para programar un apagado automatico")
print("Coloque 2 para deshacer el programado anteriormente hecho")
r=int(input())
if r == 1:
    print("Digito el tiempo de apagado en minutos") 
    tiempo = input()
    tiempo = int(tiempo)*60
    comando = "shutdown /s /t " + str(tiempo)
    subprocess.run(comando, shell=True)
    tiempo_ref = tiempo/60
    print("Está seguro de tener el tiempo de ",tiempo_ref," minutos?")
    respuesta = str(input())
    if (respuesta) == "Y" or (respuesta)== "y" or (respuesta)=="YES" or (respuesta)=="yes" or (respuesta)=="Si" or (respuesta)=="SI" or (respuesta)=="s" or (respuesta)=="S":
      print("Entendido su PC se apagará en ",tiempo_ref," minutos.")
    else:
      subprocess.run("shutdown /a", shell=True)
      print("Se acaba de cancelar la programacion de apagado de su PC vuelva a abrir el programa")
else:
    subprocess.run("shutdown /a", shell=True)
    print("Se ha cancelado la programacion de apagado de su PC")