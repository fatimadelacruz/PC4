#PROBLEMA 2
import re
regex = r'^[456]{1}\d{15}$'
regex = r"#[0-9]"
lista_numeros = ['4123456789123456', '5123-4567-8912-3456', '61234-567-8912-3456', '4123356789123456', '5133-3367-8912-3456', '5123 - 3567 - 8912 - 3456']
for numero in lista_numeros:
    encontrado = re.match(regex, numero)
    re.search('-', numero)
    palabra1 = "-"
    encontrado1 = re.search(palabra1,  numero)
    re.search('_', numero)
    palabra2 = "_"
    encontrado2 = re.search(palabra2,  numero)
    if encontrado:
        print(numero, '-> Valid')
    elif encontrado1:
        print(numero, '-> Valid')
    elif encontrado2:
        print(numero, '-> Invalid')
    else:
        print(numero, '-> Invalid')

#PROBLEMAS DIVERSOS7
#FICHEROS
#PROBLEMA 1
n = int(input('Ingrese un nro del 1 al 10: '))
file = f'./tabla-{n}.txt'
with open(file, 'w') as f:
    for i in range(1,13):
        texto = f'{i} x {n} = {i*n}\n'
        f.write(texto)
with open(file) as f:
    texto = f.read()
    print(texto)

#PROBLEMA 2
n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())

#PROBLEMA 3
n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
else:
    lines = f.readlines()
    print(lines[m - 1])

#EXPRESIONES REGULARES
#PROBLEMA 1
import re
texto = "@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%>"
re.search('good', texto)
palabra = "good"
encontrado = re.search(palabra,  texto)
if encontrado:
    print("Se ha encontrado la palabra:", palabra)
else:
    print("No se ha encontrado la palabra:", palabra)

#PROBLEMA 2
import re
texto = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
re.search('User_mentions:9', texto)
palabra1 = "User_mentions:9"
encontrado1 = re.search(palabra1,  texto)
if encontrado1:
    print("Se ha encontrado el usuario:", palabra1)
else:
    print("No se ha encontrado lel usuario:", palabra1)

re.search('likes: 5', texto)
palabra2 = "likes: 5"
encontrado2 = re.search(palabra2,  texto)
if encontrado2:
    print("Se ha encontrado la cantidad de likes:", palabra2)
else:
    print("No se ha encontrado la cantidad de likes:", palabra2)

re.search('number of retweets: 4', texto)
palabra3 = "number of retweets: 4"
encontrado3 = re.search(palabra3,  texto)
if encontrado3:
    print("Se ha encontrado la cantidad de likes:", palabra3)
else:
    print("No se ha encontrado la cantidad de likes:", palabra3)
    
#PROBLEMA 3
import re
regex = r'#[a-u]{3,6}\n'
analisis_sentimientos = datos.read_pandas(path,780,782)
for tweet in analisis_sentimientos:
    print(tweet)
    (re.findall(regex, tweet))
    re.search('txt', analisis_sentimientos)
    palabra = "txt"
    encontrado1 = re.search(palabra,  tweet)

#PROBLEMA 4
import re
regex = r""
emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    re.search('@', example)
    palabra1 = "@"
    encontrado1 = re.search(palabra1,  example)
    re.search('.com', example)
    palabra2 = ".com"
    encontrado2 = re.search(palabra2,  example)
    if re.match(regex, example) and encontrado1 and encontrado2:
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))
