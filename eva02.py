'''
Este programa deja administrar el stock de la tienda
'''
print('*'*50)
print('stock'.center(50,'*'))
print('*'*50)
productos = {'escoba':5,'huevos':25,'leche':9}
menup = ['ver stock de productos','ajustar stock','añadir nuevo producto','eliminar producto','salir']
import os
while True:
    for ind in range(len(menup)):
        print(f'{ind+1}.{menup[ind]}')
    ans = input('que quieres hacer?\n')
    if ans == '1':
        os.system('cls')
        for a, b in productos.items():
            print(f'{a.center}:{b}')
            print()
    elif ans == '2':
        os.system('cls')
        cantidad = input('ingresa el producto al cual ajustar')
        input('ingresa la nueva cantidad')
        cantidad.replace(' ','').isalpha()
        for b in productos.items():
            pass
        #por intentar simplemente
    elif ans == '3':
        os.system('cls')
        while True:
            nom = input('ingresa el nombre del nuevo producto\n')
            if nom.replace(' ','').isalpha():
                break
            if nom.lower() in productos:
                os.system('cls')
                print('error el producto ya existe\n')
                continue
            else:
                os.system('cls')
                productos[nom.lower()] = 0
                print('Producto agregado exitosamente\n')
    elif ans == '4':
        os.system('cls')
        while True:
            nom = input('ingresa el nombre del producto a eliminar\n')
            if nom.replace(' ','').isalpha():
                break
            if nom.lower() in productos:
                os.system('cls')
                del productos[nom.lower()]
                print('produco eliminado exitosamente\n')
            else:
                os.system('cls')
                print('error, producto no existente\n')
    elif ans == '4':
        os.system('cls')
        exit('Adios\n')
    else:
        os.system('cls')
        print('error, caracter invalido\n')
