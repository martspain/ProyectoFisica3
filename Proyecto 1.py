import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math as mt

#########################################################
# Función para graficar la trayectoria de manera animada
#########################################################
def plotingAnimated(time, xvel, yvel, accel, animSpeed):
    x_data = []
    y_data = []
    
    fig, ax = plt.subplots()
    
    ###############################################################################################
    # Se definen los limites de la gráfica dependiendo de la dirección de las distancias recorridas
    ###############################################################################################
    
    # Para la distancia horizontal se compara el signo de la velocidad en X multiplicada por el tiempo
    if xvel*time > 0:
        ax.set_xlim(0,xvel*time)
    elif xvel*time < 0:
        ax.set_xlim(xvel*time,0)
    elif xvel*time == 0:
        ax.set_xlim(-1,1)
    
    # Para la distancia vertical se compara el signo de la velocidad en Y multiplicada por el tiempo menos un medio de la aceleración por el tiempo al cuadrado.
    # si lo anterior resultase ser 0 significa que el recorrrido tiene forma de parabola, por lo que se considera con la mitad del tiempo que sería en su
    # altura máxima.
    if yvel*time-0.5*accel*mt.pow(time,2) > 0:
        ax.set_ylim(0, yvel*time-0.5*accel*mt.pow(time,2))
    elif yvel*time-0.5*accel*mt.pow(time,2) < 0:
        ax.set_ylim(yvel*time-0.5*accel*mt.pow(time,2), 0)
    elif yvel*time-0.5*accel*mt.pow(time,2) == 0:
        if yvel*time/2-0.5*accel*mt.pow(time/2,2) > 0:
            ax.set_ylim(0, yvel*time/2-0.5*accel*mt.pow(time/2,2))
        elif yvel*time/2-0.5*accel*mt.pow(time/2,2) < 0:
            ax.set_ylim(yvel*time/2-0.5*accel*mt.pow(time/2,2), 0)
        elif yvel*time/2-0.5*accel*mt.pow(time/2,2) == 0:
            ax.set_xlim(-1,1)
        
    line, = ax.plot(0,0,'r-o')
    
    def animation_frame(i):
        if i <= 50:
            x_data.append(xvel*(time*i)/50)
            y_data.append(yvel*(time*i)/50 - 0.5*accel*mt.pow(((time*i)/50),2))
        
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        
        return line,

    
    plt.xlabel('X Axis (m)')
    plt.ylabel('Y Axis (m)')
    plt.title("Particle's Animated Trajectory")
    
    
    animation = FuncAnimation(fig, func= animation_frame, frames= 50, interval= animSpeed)
    plt.show()
    

#Inicialización de variables
mass = 0.0
charge = 0.0
electricField = 0.0
acceleration = 0.0
totalTime = 0.0
velocityVec = 0.0
verticalVel = 0.0
horizontalVel = 0.0
velocityDegrees = 0.0
velocityRadians = 0.0
xCoords = []
yCoords = []

#Se muestra el banner y el título al usuario
print("|||      |||  \\\\\            ///  ||||||||||||")
print("|||      |||   \\\\\          ///   |||         ")
print("|||      |||    \\\\\        ///    |||         ")
print("|||      |||     \\\\\      ///     |||  |||||||")
print("|||      |||      \\\\\    ///      |||      |||")
print("|||      |||       \\\\\  ///       |||      |||")
print("||||||||||||        \\\\\///        ||||||||||||")
print("\n")
print("***** Simulador: Trayectoria de partículas ***** \n")

active = True

#########################
# Inicio del programa
#########################
while active:
    #Reinicio de variables
    mass = 0.0
    charge = 0.0
    electricField = 0.0
    acceleration = 0.0
    totalTime = 0.0
    velocityVec = 0.0
    verticalVel = 0.0
    horizontalVel = 0.0
    velocityDegrees = 0.0
    velocityRadians = 0.0
    xCoords = []
    yCoords = []
    
    #Se muestran las opciones y se solicita el input al usuario
    print("\n¿Qué desea hacer?")
    optionOne = input("1. Realizar simulación \n2. Salir \n")
    if optionOne == "1":
        print("\nSeleccione la partícula que desea ingresar a la simulación... \n")
        optionTwo = input("1. Electrón \n2. Positrón \n3. Protón \n4. Neutrón \n5. Partícula Alfa \n6. Núcleo de deuterio \n7. Muón \n8. Tauón \n9. Antimuón \n10. Antitauón \n11. Otra... \n12. Regresar \n")
        if optionTwo == "1":
            #######################################
            #             ELECTRON                #
            #######################################
            
            charge = -1.6E-19
            mass = 9.1E-31
            print("\n*********************************************")
            print("Partícula seleccionada: Electrón")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 2*(mt.fabs(verticalVel)/mt.fabs(acceleration))
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
                    
        elif optionTwo == "2":
            #######################################
            #             POSITRON                #
            #######################################
            charge = 1.6E-19
            mass = 9.1E-31
            print("\n*********************************************")
            print("Partícula seleccionada: Positrón")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 2*(mt.fabs(verticalVel)/mt.fabs(acceleration))
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
                    
        elif optionTwo == "3":
            #######################################
            #               PROTON                #
            #######################################
            charge = 1.602E-19
            mass = 1.674E-27
            print("\n*********************************************")
            print("Partícula seleccionada: Protón")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 2*(mt.fabs(verticalVel)/mt.fabs(acceleration))
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
                    
        elif optionTwo == "4":
            #######################################
            #              NEUTRON                #
            #######################################
            charge = 0.0
            mass = 1.6749E-27
            print("\n*********************************************")
            print("Partícula seleccionada: Neutrón")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 0.01
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
                    
        elif optionTwo == "5":
            #######################################
            #           PARTICULA ALFA            #
            #######################################
            charge = 3.2E-19
            mass = 6.64E-27
            print("\n*********************************************")
            print("Partícula seleccionada: Partícula Alfa")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 2*(mt.fabs(verticalVel)/mt.fabs(acceleration))
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
                    
        elif optionTwo == "6":
            #######################################
            #         NUCLEO DE DEUTERIO          #
            #######################################
            charge = 1.602E-19
            mass = 3.343E-27
            print("\n*********************************************")
            print("Partícula seleccionada: Núcleo de Deuterio")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 2*(mt.fabs(verticalVel)/mt.fabs(acceleration))
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
                    
        elif optionTwo == "7":
            #######################################
            #                 MUON                #
            #######################################
            charge = -1.602E-19
            mass = 1.8912E-28
            print("\n*********************************************")
            print("Partícula seleccionada: Muón")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 2*(mt.fabs(verticalVel)/mt.fabs(acceleration))
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
                    
        elif optionTwo == "8":
            #######################################
            #                 TAU                 #
            #######################################
            charge = -1.602E-19
            mass = 3.1805E-27
            print("\n*********************************************")
            print("Partícula seleccionada: Tauón")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 2*(mt.fabs(verticalVel)/mt.fabs(acceleration))
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
        
        elif optionTwo == "9":
            #######################################
            #               ANTIMUON              #
            #######################################
            charge = 1.602E-19
            mass = 1.8912E-28
            print("\n*********************************************")
            print("Partícula seleccionada: Antimuón")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 2*(mt.fabs(verticalVel)/mt.fabs(acceleration))
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
        
        elif optionTwo == "10":
            #######################################
            #              ANTITAUON              #
            #######################################
            charge = 1.602E-19
            mass = 3.1805E-27
            print("\n*********************************************")
            print("Partícula seleccionada: Antitauón")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 2*(mt.fabs(verticalVel)/mt.fabs(acceleration))
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
                    
        elif optionTwo == "11":
            #######################################
            #           OTRA PARTICULA            #
            #######################################
            try:
                charge = (float)(input("Ingrese la carga de la partícula en Coulumbs: "))
            except:
                print("Porfavor ingrese una opción valida de la carga. Reinicie el programa.")
                break
            try:
                mass = (float)(input("Ingrese la masa de la partícula en kg: "))
            except:
                print("Porfavor ingrese una opción valida de la masa. Reinicie el programa.")
                break
            print("\n*********************************************")
            print("Partícula seleccionada: Desconocida")
            print("*********************************************")
            print("Masa: ",mass, "kg")
            print("Carga: ",charge,"C")
            
            # Se solicita al usuario la magnitud del Campo Eléctrico
            try:
                electricField = (float)(input("Ingrese la magnitud del campo eléctrico (positiva hacia arriba y negativa hacia abajo) en N/C: "))
            except:
                print("Porfavor ingrese una opción valida del Campo Electrico. Reinicie el programa.")
                break
            
            # Se solicita al usuario la magnitud de la velocidad inicial
            try:
                velocityVec = (float)(input("Ingrese la magnitud de la velocidad inicial en m/s: "))
            except:
                print("Porfavor ingrese una opción valida de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se solicita al usuario el ángulo de la velocidad inicial
            try:
                velocityDegrees = (float)(input("Ingrese el angulo de la velocidad inicial en grados: "))
            except:
                print("Porfavor ingrese una opción valida del Ángulo de la Velocidad Inicial. Reinicie el programa.")
                break
            
            # Se convierten los grados a radianes
            velocityRadians = mt.radians(velocityDegrees)
            
            # Se calcula la aceleración a = F/m sabiendo que la fuerza es igual a la carga por el campo electrico F = q*E
            acceleration = (charge*electricField)/mass
            
            # Se calcula la velocidad horizontal inicial (se considerará constante en todo el recorrido)
            horizontalVel = velocityVec * mt.cos(velocityRadians)
            
            # Se calcula la velocidad vertical inicial
            verticalVel = velocityVec * mt.sin(velocityRadians)
            
            # Se calcula el tiempo total de vuelo
            totalTime = 2*(mt.fabs(verticalVel)/mt.fabs(acceleration))
            
            subactive = True
            
            while subactive:
                print("\n************************ \n¿Qué gráfica desea observar?")
                suboption = input("\n1. Trayectoria estática \n2. Trayectoria animada \n3. Regresar \n")
                if suboption == "1":
                    # Se calculan los puntos (coordenadas X y Y) en un ciclo for que "recorre" el tiempo
                    for time in np.arange(0,totalTime,totalTime/50):
                        xCoords.append(horizontalVel * time)
                        yCoords.append((verticalVel*time)-(0.5*acceleration*mt.pow(time,2)))
                    
                    with plt.style.context('dark_background'):
                        plt.plot(xCoords,yCoords, 'r-o')
                    plt.xlabel('X Axis (m)')
                    plt.ylabel('Y Axis (m)')
                    plt.title("Particle's Trajectory")
                    plt.show()
                    
                elif suboption == "2":
                    speedOption = input("¿Qué velocidad de reproducción desea ejecutar? \n1. Lenta (250 FPS) \n2. Normal (60 FPS) \n3. Rápida (10 FPS) \n")
                    speed = 50
                    if speedOption == "1":
                        speed = 250
                        print("Reproduciendo en velocidad lenta...")
                    elif speedOption == "2":
                        speed = 60
                        print("Reproduciendo en velocidad normal...")
                    elif speedOption == "3":
                        speed = 10
                        print("Reproduciendo en velocidad rápida...")
                    else:
                        print("Reproduciendo en velocidad default...")
                        
                    plotingAnimated(totalTime, horizontalVel, verticalVel, acceleration, speed)
                elif suboption == "3":
                    subactive = False
                else:
                    print("Por favor, ingrese una opción válida.")
        elif optionTwo == "12":
            print("Regresando al menu principal... \n")
        else:
            print("Por favor, ingrese una opción válida.")
            
    elif optionOne == "2":
        print("Gracias por utilizar la simulación! Vuelva pronto!")
        active = False
        
    else:
        print("Ingrese una opción válida")
