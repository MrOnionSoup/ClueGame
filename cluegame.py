
"""
Alumno: Luis Alexandro Castañeda Fragoso
Registro: 18310055
Grupo: 6E1

"""

import random
import os

def clear(): os.system('cls') 

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

people = ["MARCELO RAMIREZ","DAVID GARCIA","ANGELICA CASTILLO","DANIEL LOPEZ","ALEJANDRA VALDEZ"]
rooms = ["Cocina", "Baño", "Sala", "Cuarto de lavado" , "Estudio"]
weapons =["Picahielo", "Cuerda de guitarra", "Tapa de baño" , "Álgebra de Baldor" , "Cuchillo"]
questions = ("\n~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n|  1) ¿En qué lugar se encontraba usted? |\n|  2) ¿Reconoce el arma?                 | \n|  3) Volver a los sospechosos           |\n~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")
random.shuffle(people)
killer = random.choice(people)
people.remove(killer)

random.shuffle(rooms)
room = random.choice(rooms)
rooms.remove(room)

random.shuffle(weapons)
weapon = random.choice(weapons)
weapons.remove(weapon)
sospechoso0 =([killer,room])

random.shuffle(rooms)
random.shuffle(people)
innocent_locate1 = random.choice(rooms)
innocent_person1 = random.choice(people)
rooms.remove(innocent_locate1)
people.remove(innocent_person1)
sospechoso1 =([innocent_person1,innocent_locate1])

random.shuffle(rooms)
random.shuffle(people)
innocent_locate2 = random.choice(rooms)
innocent_person2 = random.choice(people)
rooms.remove(innocent_locate2)
people.remove(innocent_person2)
sospechoso2 =([innocent_person2,innocent_locate2])

random.shuffle(rooms)
random.shuffle(people)
innocent_locate3 = random.choice(rooms)
innocent_person3 = random.choice(people)
rooms.remove(innocent_locate3)
people.remove(innocent_person3)
sospechoso3 =([innocent_person3,innocent_locate3])

random.shuffle(rooms)
random.shuffle(people)
innocent_locate4= random.choice(rooms)
innocent_person4 = random.choice(people)
rooms.remove(innocent_locate4)
people.remove(innocent_person4)
sospechoso4 =([innocent_person4,innocent_locate4])

data = [sospechoso0,sospechoso1,sospechoso2,sospechoso3,sospechoso4]


print("@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@&/.   ./%@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@/                .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@&@@@@@@@@@@@@@@@@@@&@@@@@")
print("@@@@@@@@@@@                    .@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@&@@@@@@@@&#(/(@              .*&@@@@@")
print("@@@@@@@@&                      .@@@@@@@@@@@&@@@@@(////////((##(@@@@@(########@              .*@@@@@@")
print("@@@@@@@                        .@@         .@@@@@#############(@@&@@(########@              .*@@@@@@")
print("@@@@@,                 .....   .@@         .@@@@@############((@@@@@(########@       .*@@@@&&@@@@@@@")
print("@@@@.              .#@&&&&&&@@..@@         .@@@@@#############(@@@@@(########@              .@@@@@@@")
print("@@@%             .@@@@@@@@@@@@@@@@         .@@@@@@@@@#########(@@@@@(########@              .@@@@@@@")
print("@@@             .@@@@@@@@@@@@@@@@@         .@@@@@@@@@#########(@@@@@(########@              .@@@@@@@")
print("@@@              @@@@@@@@@@@@@@&@@         .@@@@@@@@@#########(@@@@@(########@        .&@@@@@&@@@@@@")
print("@@@              #@@@@@@@@@@@@@@@@         .@@@@@@@@@#########(@@@@@(########@         @&(.  .@@@@@@")
print("@@@                @@&@@@@@@@& .@@         .@@@@@@@@@%########((@@((########@@               .@@@@@@")
print("@@@*                           .@@         .       .&@#####################%@@               .@@@@@@")
print("@@@@                           .@@                 .&@@###################@&@@        ......,/@@@@@@")
print("@@@@@..                        .@@                 .&@@@################@&@@@@@@@@@@&&&&&&&@&@@@@@@@")
print("@@@@@@@.                       .@@                 .%@@@&&@@@&%%&@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@&@,.                    .@@    ......,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@&@@*...      ....(@@&&@@@@&&&&&&@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  By: Alex Castañeda  @@")
print("@@@@@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
input("Presiona enter para continuar...")
clear()

print("\n\nBuenas noches Detective, ha sido llamado para resolver un misterio esta noche.")
print("Aproximadamente a las 8:45 p.m. recibimos un llamado de emergencia por parte de los vecinos de esta casa,")
print("nos informaron que escucharon gritos de un hombre, aparentemente del señor identificado como Mario Mario.")
print("Al llegar a la casa, encontramos el cuerpo sin vida del Sr. Mario en ",color.BOLD + room + color.END," y aparentemente el arma homicida fue un@ ",color.RED + weapon + color.END," que estaba junto a él")
print("Reunimos a las 5 personas que se encontraban en la casa en el momento del asesinato listas para interrogación")
print("Confíamos en que podrá llegar al fondo de todo esto, buena suerte.\n\n")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@                                                                             @@")
print("@@  @@@@@@@@@@@@@@@@@@@@@@@@           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@")
print("@@  @@                    @@           @@                                 @@   @@")
print("@@  @@                    @@           @@                                 @@   @@")
print("@@  @@      CUARTO                                                        @@   @@")
print("@@  @@        DE                                                          @@   @@")
print("@@  @@      LAVADO        @@           @@                                 @@   @@")
print("@@  @@                    @@           @@              COCINA             @@   @@")
print("@@  @@                    @@           @@                                 @@   @@")
print("@@  @@@@@@@@@@@@@@@@@@@@@@@@           @@                                 @@   @@")
print("@@                                     @@                                 @@   @@")
print("@@  @@@@@@@@@@@@@@@@@@@@@@@@           @@                                 @@   @@")
print("@@  @@                    @@           @@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@   @@")
print("@@  @@                    @@                                                   @@")
print("@@  @@                    @@                                                   @@")
print("@@  @@      ESTUDIO                                                            @@")
print("@@  @@                                                                         @@")
print("@@  @@                    @@                                                   @@")
print("@@  @@                    @@           @@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@   @@")
print("@@  @@@@@@@@@@@@@@@@@@@@@@@@           @@                                 @@   @@")
print("@@                                     @@                                 @@   @@")
print("@@  @@@@@@@@@@@@@@@@@@@@@@@@           @@                                 @@   @@")
print("@@  @@                    @@           @@                                 @@   @@")
print("@@  @@                    @@           @@                                 @@   @@")
print("@@  @@                    @@                           SALA               @@   @@")
print("@@  @@       BAÑO                                                         @@   @@")
print("@@  @@                                 @@                                 @@   @@")
print("@@  @@                    @@           @@                                 @@   @@")
print("@@  @@                    @@           @@                                 @@   @@")
print("@@  @@@@@@@@@@@@@@@@@@@@@@@@           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@")
print("@@                                                                             @@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

random.shuffle(data)
interogatorio1 = random.choice(data)
data.remove(interogatorio1)

random.shuffle(data)
interogatorio2 = random.choice(data)
data.remove(interogatorio2)

random.shuffle(data)
interogatorio3 = random.choice(data)
data.remove(interogatorio3)

random.shuffle(data)
interogatorio4 = random.choice(data)
data.remove(interogatorio4)

random.shuffle(data)
interogatorio5 = random.choice(data)
data.remove(interogatorio5) 
def menu():

	print ("\n\nInterrogar a")
	print ("1) - Sospechoso 1")
	print ("2) - Sospechoso 2")
	print ("3) - Sospechoso 3")
	print ("4) - Sospechoso 4")
	print ("5) - Sospechoso 5")
	print ("6) - ¡Resuelve el misterio!\n")
  

while True:

        menu()
 
        choice = input("Seleccione un sospechoso>>")
              
        if choice == "1":
           print ("\n\nBuenas noches, mi nombre es", interogatorio1[0],"¿todo bien?\n")
           question = False
           while not question:
               print (questions)
               choice2 = input("Seleccione pregunta>>")
               if choice2 == "1":
                   print ("\n",interogatorio1[0],":")
                   print ("Me encontraba en", interogatorio1[1],"\n")
               elif choice2 =="2":
                        if interogatorio1[0] == killer: 
                                print ("\n",interogatorio1[0],":")
                                print ("Me parece familiar", weapon,"\n")
                        else:
                                print ("\n",interogatorio1[0],":")
                                print("No reconozco tal", weapon,"\n")
               elif choice2 =="3":
                    question = True
               else:
                   print("\n¿Esto es un juego para ti? ¡Hay una persona muerta!")


        elif choice == "2": 
           print ("\n\nBuenas noches, me llamo", interogatorio2[0],"y exijo hablar con mi abogado.\n")
           question = False
           while not question:
               print (questions)
               choice2 = input("Seleccione pregunta>>")
               if choice2 == "1":
                   print ("\n",interogatorio2[0],":")
                   print ("Me encontraba en ", interogatorio2[1],"\n")
               elif choice2 =="2":
                        if interogatorio2[0] == killer: 
                                print ("\n",interogatorio2[0],":")
                                print ("Sí he visto", weapon,"\n")
                        else:
                                print ("\n",interogatorio2[0],":")
                                print("No me parece familiar\n")
               elif choice2 =="3":
                    question = True
               else:
                   print("\n¿Te crees muy gracioso?")


        elif choice == "3":
           print ("\n\nHola, soy ", interogatorio3[0],"¿puede hacer esto rápido?\n")
           question = False
           while not question:
               print (questions)
               choice2 = input("Seleccione pregunta>>")
               if choice2 == "1":
                   print ("\n",interogatorio3[0],":")
                   print ("Estaba en ", interogatorio3[1],"\n")
               elif choice2 =="2":
                        if interogatorio3[0] == killer: 
                                print ("\n",interogatorio3[0],":")
                                print ("Reconozco tal ", weapon,"\n")
                        else:
                                print ("\n",interogatorio3[0],":")
                                print(" No l@ reconozco\n")
               elif choice2 =="3":
                    question = True
               else:
                   print("\n¡Concéntrese Detective!")


        elif choice == "4":
           print ("\n\nMi nombre es", interogatorio4[0],"y no me agradan los detectives\n")
           question = False
           while not question:
               print (questions)
               choice2 = input("Seleccione pregunta>>")
               if choice2 == "1":
                   print ("\n",interogatorio4[0],":")
                   print ("Fui a ", interogatorio4[1],"antes de ir a",interogatorio2[1],"\n")
               elif choice2 =="2":
                        if interogatorio4[0] == killer: 
                                print ("\n",interogatorio4[0],":")
                                print ("Tengo uno de esos", weapon,"\n")
                        else:
                                print ("\n",interogatorio4[0],":")
                                print(" Nunca había visto ", weapon,"\n")
               elif choice2 =="3":
                    question = True
               else:
                   print("\nEres una persona muy distraída para ser un detective") 


        elif choice == "5":
           print ("\n\nYo soy",interogatorio5[0],",no hice nada ¡lo juro!\n")
           question = False
           while not question:
               print (questions)
               choice2 = input("Seleccione pregunta>>")
               if choice2 == "1":
                   print ("\n",interogatorio5[0],":")
                   print ("Estaba en ",interogatorio5[1],"\n")
               elif choice2 =="2":
                        if interogatorio5[0] == killer: 
                                print ("\n",interogatorio5[0],":")
                                print ("Sí reconozco ", weapon,"oficial, señor Detective\n")
                        else:
                                print ("\n",interogatorio5[0],":")
                                print(" No me parece familiar ", weapon,"\n")
               elif choice2 =="3":
                    question = True
               else:
                   print("\n¿Comiste payaso?¬¬")


    
# descubridor de culpable  
        elif choice == "6":
            guilty = input("El culpable es (escribir nombre en mayúsculas)>>")
            if guilty == killer:
                print ("¡Lo has descubierto!", killer, "asesinó a Mario Mario en " ,room, "usando" ,weapon)
                break
            else:
                print ("Has fallado,", guilty, "no era el asesino. ¡",killer, "ha quedado libre!")
                break

        else:
                print("Esa no es una opción")