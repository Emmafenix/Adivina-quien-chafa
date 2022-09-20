from turtle import end_fill

print("\n")
print("Hola , bienvenido a ¿Adivina quien? Version familiar")
print("¿Quieres intentarlo?")
print("\n")
print("Y/N")
print("\n")
start=float(input("Si 1, No 2\n"))
if start==(1):
    print("perfecto uwu\n Entonces comencemos con el juego!")
    print("Primera pregunta: ¿La persona en la que estas pensando es mayor que tu?")
    Q1=float(input("Si 1, No 2\n"))
    if Q1==(1):
        print("Va, Segunda pregunta\n")
        print("¿La persona en la que estas pensando es Mujer?")
        Q2=float(input("Si 1, No 2\n"))
        if Q2==(1):
            print("OK, Tercera pregunta\n")
            print("¿Estas pensando en alguien que usa lentes?")
            Q3=float(input("Si 1, No 2\n"))
            if Q3==(1):
                print("ok ok, Ultima pregunta\n")
                print("La persona en la que estas pensando ¿Tiene hijos?")
                Q4=float(input("Si 1, No 2\n"))
                if Q4==(1):
                    print("Estas pensando en tu abuelita paterna jajaja")
                else:
                    print("Estas pensando en tu hermanita mayor jaja")
            else:
                print("ok ok, Ultima pregunta\n")
                print("La persona en la que estas pensando ¿Tiene todos sus dientes?")
                Q4=float(input("Si 1, No 2\n"))
                if Q4==(1):
                    print("Estas pensando en tu Mamá jajaja")
                else:
                    print("Estas pensando en tu abuelita materna jaja")
        else:
            print("OK, Tercera pregunta\n")
            print("¿Estas pensando en alguien que usa lentes?")
            Q3=float(input("Si 1, No 2\n"))
            if Q3==(1):
                print("ok ok, Ultima pregunta\n")
                print("La persona en la que estas pensando ¿Tiene hijos?")
                Q4=float(input("Si 1, No 2\n"))
                if Q4==(1):
                    print("Estas pensando en tu abuelito materno jajaja")
                else:
                    print("Estas pensando en tu hermano mayor jaja")
            else:
                print("ok ok, Ultima pregunta\n")
                print("La persona en la que estas pensando ¿Tiene todos sus dientes?")
                Q4=float(input("Si 1, No 2\n"))
                if Q4==(1):
                    print("Estas pensando en tu Papá jajaja")
                else:
                    print("Estas pensando en tu abuelito paterno jaja")
    else:
        print("Va, segunda pregunta\n")
        print("¿La persona en la que estas pensando es Hombre?")
        Q2=float(input("Si 1, No 2\n"))
        if Q2==(1):
            print("OK, Tercera pregunta\n")
            print("¿Estas pensando en alguien que tiene pulgas?")
            Q3=float(input("Si 1, No 2\n"))
            if Q3==(1):
                print("Estas pensando en el Perro jajaja")
            else:
                print("Estas pensando en tu hermanito menor jaja")
        else:
            print("OK, Tercera pregunta\n")
            print("¿Estas pensando en alguna mascota?")
            Q3=float(input("Si 1, No 2\n"))
            if Q3==(1):
                print("Estas pensando en la gatita jajaja")
            else:
                print("Estas pensando en tu hermanita menor jaja")
        


else:
    print("\n Ta bien, vuelve cuando quieras")