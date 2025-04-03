#M2C3 Python Assignment

#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

#String 
nombre = "Lidia"

#Number 
edad = 14

#List 
lista_hobbies  = [  "tenis", "danza", "lectura "]

#Boolean
habla_ingles  = True

print(nombre)
print(edad)
print(lista_hobbies)
print (habla_ingles)

#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

nombre = "Lidia"
nombre[:3]  # Toma los primeros 3 caracteres
print(seleccion)


#Exercise 3: Use an index to grab the first element from your list.

lista_hobbies = ["tenis", "música", "danza"]
primer_elemento = lista_hobbies[0]
print(primer_elemento) 

#Exercise 4: Create a new number variable that adds 10 to your original number.

numero = 14
nuevo_numero = numero + 10 
print(nuevo_numero) 

#Exercise 5: Use an index to get the last element in your list.

lista_hobbies = ["tenis", "música", "danza"]
primer_elemento = lista_hobbies[-1]  #Using a negative index
print(primer_elemento) 

#Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
lista = names.split(',')
print(lista)

#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string..*/
frase = " Yo me llamo Lidia."
# Eliminar espacios en los extremos y dividir en palabras
palabras = frase.strip().split()
# Convertir la primera palabra a mayúsculas
primera_mayuscula = palabras[0].upper()
# Reconstruir la frase con la primera palabra en mayúsculas
nueva_frase = primera_mayuscula + " " + " ".join(palabras[1:])

print(nueva_frase)



#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.*/


nombre = "Lidia"

edad = 14

saludo = f"Hola {nombre} de {edad} años!"

print(saludo)

#Exercise 9: Print “hello world”./

saludo= "hello world"
print(saludo) 


