# print("Olá, mundo!!")



# a = 10
# b = 3


# soma = a + b   # 13
# subtracao = a - b    # 7
# multiplicacao = a * b    # 30
# divisao = a / b   # 3.333333333
# divisao_inteira = a // b   # 3
# modulo = a % b   # 1
# exponenciacao = a ** b   # 1000


# print(f"{soma}")
# print(f"{subtracao}")
# print(f"{multiplicacao}")
# print(f"{divisao}")
# print(f"{divisao_inteira}")
# print(f"{modulo}")
# print(f"{exponenciacao}")




# # a = 10
# # b = 3


# # igual = a == b   # False
# # diferente = a != b   # True
# # maior que = a > b   # True
# # menor que = a < b   # False
# # maior ou igual = a >= b   # True
# # menor ou igual = a <= b   # False



# # a = 10
# # b = 3


# # resultado_and = (a > 5) and (b < 5)   # True
# # resultado_or = (a > 15) or (b < 5)   # True
# # resultado_not = not (a > 5)   # False


# idade = int(input("digite sua idade: "))

# # if idade  < 18:
# #     print("você é menor de idade.")

# # elif idade >=18 and idade < 60:
# #     print("você é adulto.")

# # elif idade == 15:
# #     print("você tem 15 anos.")

# # elif idade == 60:
# #     print("feliz 60 anos!")

# # else:
# #     print("você é um adulto.")


# if idade <= 14:
#     print("vc tem menos dq 15 anos.")

# elif idade == 15:
#     print("vc tem 15 anos, parabens.")

# elif idade == 18:
#     print(" vc é de maior.")

# elif idade >= 19 and idade <= 59:
#     print(" vc é um adulto.")

# elif idade == 60:
#     print("parabens vc tem 60 anos.")

# else:        
#     print("vc é um idoso.")





# frutas = ["maçã", "banana", "laranja"]


# for fruta in frutas:
#     print(fruta)




# contador = 0


# while contador < 5:

#     print(contador)
#     contador += 1



# contador = 0


# while True:

#     print(contador)
#     contador += 1


#     if contador == 11:
#         break


# for i in range(10):

#     if i % 2 == 0:
#         continue
#     print(i)




# frutas = ["maçã", "banana", "laranja"]


# frutas.append("pera")
# print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]


# frutas.insert(1, "uva")
# print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]


# frutas.remove("banana")
# print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]


# fruta_removida = frutas.pop(2)
# print(frutas)  # Imprime ["maçã", "uva", "pera"]
# print(fruta_removida)  # Imprime "laranja"


# frutas.sort()
# print(frutas)  # Imprime ["maçã", "pera", "uva"]


# frutas.reverse()
# print(frutas)  # Imprime ["uva", "pera", "maçã"]



# números = [1, 2, 3, 4, 5]
# quadrados = [x ** 2 for x in números if x % 2 == 0]
# print(quadrados)  # Imprime [4, 16]




# minha_tupla = (1, 2, 3, 2, 4, 2)


# print (minha_tupla.index(2))   # Saída: 1

# print (minha_tupla.index(2, 2))   #Saída: 3

# print (minha_tupla.index(2, 2, 4))   #Saída: 3






# pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


# print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
# print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
# print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])


# pessoa.update({"profissao": "Engenheiro"})
# print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}






# frutas = {"maçã", "banana", "laranja"}


# frutas.add("pera")
# print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


# frutas.remove("banana")
# print(frutas)  # Imprime {"maçã", "laranja", "pera"}


# frutas.discard("maçã")
# print(frutas)  # Imprime {"maçã", "laranja", "pera"}


# frutas.clear()
# print(frutas)  # Imprime set()



# número = 7 
# if número % 2 == 0:
#         print  ("Par")
# else:
#         print  ("Impar")


