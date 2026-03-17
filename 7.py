
correo="adso"
prom=0
contraseña=3174404
con=0
cont=0
proM=0
promh=0
promg1=0
promg2=0
promg3=0
promg4=0
promg5=0
promg=0
prom_grade=0
suma=0
prom_m=0
prom_h=0
for i in range (1,4):
    correo=input("correo: ")
    contraseña=int(input("contraseña: "))
    if correo=="adso" and contraseña==3174404:
        print("inicio de sesion")
        grade=int(input("cantidad de grados" ))
        for i in range(grade):
            ant=prom_grade
            for j in range (5):
                asig=input("asignatura destacable ")
                N=int(input("cantidad de estudiantes de la materia"))
                for i in range(N):
                    nombre=input("escriba su nombre ")
                    genero=("su genero")
                    if genero=="mujer":
                        cont=cont+1
                        proM=proM+prom
                    elif genero=="hombre":
                        con=con+1
                        promh=promh+prom
                    nota1=float(input("su nota1 "))
                    nota2=float(input("su nota2 "))
                    nota3=float(input("su nota3 "))
                    prom=nota1*0.3+nota2*0.3+nota3*0.4
                    print(f"{nombre}su promedio para esta materia {asig} es",prom)
                    if prom>2.9:
                        print("aprobo")
                    else:
                        print("reprobo")
                if j==1:
                    promg=promg+prom
    
                elif j==2:
                    promg=promg+prom
                elif j==3:
                    promg=promg+prom
                elif j==4:
                    promg=promg+prom
                elif j==5:
                    promg=promg+prom
            print(f"el promedio de {asig}",promg)
        prom_grade=prom_grade+promg
        if prom_grade>ant:
            mayor=promg_grade
        print(f"el grado con mayorpromedio es {mayor}",i)
        print("el promedio por grado es",prom_grade)
        suma=suma+promg
        prom_m:proM/cont
        prom_h:promh/con
        print("promedio de asig:natura",asig,"es",promg)
        if prom_m>prom_h:
            
            print("las mujeres sacaron mayor promedio con",prom_m)
        else:
            print("los hombres sacaron mayor promedio",prom_h)
            break
    else:
        print("usuario invalido",i)
print("se ah quedado sin intentos")
