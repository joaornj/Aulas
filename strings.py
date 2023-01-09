
a = "João"
b = "Nogueira"

#concatenar = a + " " + b  # Usa as aspas espacadas para dar espaco entre as duas strings
#print (concatenar) 

#tamanho = len(concatenar) # len traz o tamanho da string / o espaço tmbm é somado
#print(tamanho)

#print(a[0])   # Irá printar a posicao 0 da string

#print(concatenar[0:2])  # Irá printar até a posicao 2 da string

#print(concatenar[0:])  # Irá printar tudo


# Aplicar metodos nas strings


#a = "João"
#b = "Nogueira"

#concatenar = a + " " + b + "\n" # \n gera quebra de linha, remove espacos tmbm.
#print (concatenar.lower()) # aplicando metodo lower (passar para letra minuscula), obrigatorio parenteses
#print (concatenar.upper()) # aplicando metodo upper (passar para letra maiuscula), obrigatorio parenteses
#print (concatenar.strip()) # metodo strip remove o \n


# Metodo split

minha_string = "O rato roeu a roupa do rei de Roma"

#minha_lista = minha_string.split() # metodo split converteu a string separada por espacos.
#print(minha_lista)

#minha_lista = minha_string.split("r") # metodo split converteu a string separada por espacos e remove a letra r
#print(minha_lista)

# metodo busca

#busca = minha_string.find("rei") # metodo find faz a busca da posicao.
#print(busca)

# metodo replace

minha_string = minha_string.replace("o rei", "a rainha") # metodo replace substitui o rei pela a rainha
print(minha_string)
