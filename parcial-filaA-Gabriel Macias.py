# Parcial Gabriel Macias
# Punto 1:
n_llantas = float(input('Digite la cantida de llantas: '))
if n_llantas < 5:
     total = 300 * n_llantas
     v_llanta = total / n_llantas 
     print(f'El valor de la compra es: $ {total}')
     print(f'El valor de cada llanta es de: $ {v_llanta}')
elif n_llantas >= 5 and n_llantas <= 10:
     total = 250 * n_llantas
     v_llanta = total / n_llantas 
     print(f'El valor de la compra es: $ {total}')
     print(f'El valor de cada llanta es de: $ {v_llanta}')
else: 
     total = 200 * n_llantas
     v_llanta = total / n_llantas 
     print(f'El valor de la compra es: $ {total}')
     print(f'El valor de cada llanta es de: $ {v_llanta}') 
    

# Punto 2:
valor_tv = float(input('Digite el valor de la TV: $ '))
cantidad_tv = int(input('Digite la cantidad de TV: '))
n_cc = str(input('Digite los dos numeros finales de la cedula: '))
totalp = valor_tv * cantidad_tv
if n_cc == '01':
    descuento = totalp * 0.1
    total = totalp - descuento
    print(f'El valor final de la compra es: $ {total}')
elif n_cc == '25':
    descuento = totalp * 0.2
    total = totalp - descuento
    print(f'El valor final de la compra es: $ {total}') 
elif n_cc == '44':
    descuento = totalp * 0.35
    total = totalp - descuento
    print(f'El valor final de la compra es: $ {total}')
elif n_cc == '57':
    descuento = totalp * 0.5
    total = totalp - descuento
    print(f'El valor final de la compra es: $ {total}')
else:
    print(f'El valor de la compra no tiene descuento y es el siguiente: $ {totalp}')       
    
# Punto 3:
valor_c = float(input('Digite el valor del colchon: '))    
cant_colch = int(input('Digite la cantidad de colchones: '))
if cant_colch < 3:
    total = valor_c * cant_colch
    print(f'El valor de la compra es: $ {total} ')
elif cant_colch >=3 and  cant_colch < 6:
    valort = valor_c * cant_colch
    descuento = valort * 0.2
    total = valort - descuento
    print(f'El valor de la compra es: $ {total} ')
elif cant_colch >=6 and  cant_colch <8:
    valort = valor_c * cant_colch
    descuento = valort * 0.25
    total = valort - descuento
    print(f'El valor de la compra es: $ {total} ')
else:
    valort = valor_c * cant_colch
    descuento = valort * 0.3
    total = valort - descuento
    print(f'El valor de la compra es: $ {total} ')

# Punto 4
cant_est = int(input('Digite la cantidad de estudiantes: '))
if cant_est < 20:
    muestra = cant_est * 0.5
    print(f'La cantidad de estudiantes para la encuesta es de: {muestra}')    
elif cant_est >= 20 and cant_est <= 30:
    muestra = cant_est * 0.6
    print(f'La cantidad de estudiantes para la encuesta es de: {muestra}')
else:
    muestra = cant_est * 0.7
    print(f'La cantidad de estudiantes para la encuesta es de: {muestra}')    
    