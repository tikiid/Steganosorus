import string

# Utilisation de listes pour ne pas saturer la mémoire
# L = [number for number in range (0,100,2)]
# print(L)

'''

def chiffre_cesar (message, key):
    
    if type(key) != int:
        print("la clé n'est pas un entier")
        return None
    message = str(message)
    list_of_crypted_carac =  []
    alphabet = string.printable
    
    for carac in message:
        alphabet_index = (key + alphabet.index(carac)) % len(alphabet)
        
        list_of_crypted_carac.append(alphabet[alphabet_index])
    
    crypted_message = "".join(list_of_crypted_carac)
    return crypted_message

def cesar_decrypt (message, key):
    return chiffre_cesar(message, -(key))
'''
string.printable = string.printable.replace("\r", "à")

def cesar_ciffer(message, key):
	if type(key) != int :
		print("la clef doit être un entier")
		return None

	message = str(message)

	list_of_crypted_caracs = []
	
	for carac in message:
		crypted_index = (string.printable.index(carac) + key) % len(string.printable)
		crypted_carac = string.printable[crypted_index]
	
		list_of_crypted_caracs.append(crypted_carac)
	
	crypted_message = "".join(list_of_crypted_caracs)

	return crypted_message

def cesar_decrypt(crypted_message, key):
	return cesar_ciffer(crypted_message, -key)

def vigenere(message, password, ciffer):
	if ciffer:
		list_of_keys = [string.printable.index(password_carac) for password_carac in password]
	else:
		list_of_keys = [- string.printable.index(password_carac) for password_carac in password]
	
	list_of_crypted_caracs = []

	for index_carac, carac in enumerate(message):
		current_key = list_of_keys[index_carac % len(list_of_keys)]
		list_of_crypted_caracs.append(cesar_ciffer(carac, current_key))

	crypted_message = "".join(list_of_crypted_caracs)

	return crypted_message


crypted_message = cesar_ciffer("j'ai envie de manger gratin de pates avec des lardons", 104)
print(crypted_message)
cesar_decrypt(crypted_message, 104)
# # print(crypted_message)
# # print(cesar_decrypt(crypted_message, 762))


# # print("Je suis un hacker")
# # print("#"*30)
# # for possible_key in range(0, len(string.printable)):
# # 	print(cesar_decrypt(crypted_message, possible_key))
# # print("#"*30)


print(vigenere(message="hakim", password="abc", ciffer=True))
print(vigenere(message="rlwsx", password="abc", ciffer=False))

def chiffre_vigenere(message, key):
    
    list_of_crypted_carac = []
    counter = 0
    print(message)
    print(len(message))
    for caractere in message:
        if(counter >= len(key) - 1):
            counter = 0
        print(counter)
        list_of_crypted_carac.append(cesar_ciffer(caractere, key[counter]))
        counter += 1
        
    crypted_message = "".join(list_of_crypted_carac)
    return crypted_message

def vigenere_decrypted(message, key):
    for index_of_key in range(len(key)):
        key[index_of_key] = -key[index_of_key]
    chiffre_vigenere(message, key)

def vigenere_ciffer(message, password, ciffer):
    # compréhension de liste : une phrase de programmation ne doit pas dépasser les 79 caractères (PEP 8)
    #               ce qu'on append                            | la boucle
    if ciffer: 
        list_of_keys = [string.printable.index(password_carac) for password_carac in password]
    else: 
        list_of_keys = [ - string.printable.index(password_carac) for password_carac in password]
    
    list_of_crypted_carac = []
    
    for index_carac, carac  in enumerate(message):
        current_key = list_of_keys[index_carac % len(list_of_keys)]
        list_of_crypted_carac.append(cesar_ciffer(carac, current_key))

    return "".join(list_of_crypted_carac)


# clé de césar pour 3, 103, 203 ne marche pas 

# vigenere_ciffer(message="hakim", password="abc")



'''
key_list=[5, 9, 77, 111]

crypted_message = chiffre_vigenere("Chocolat", key_list)
print(crypted_message)
print(vigenere_decrypted(crypted_message,  key_list))

'''

# crypted_message = cesar_ciffer("Chocolat oh lala ça fait beaucoup", 4)
# print(crypted_message)
# print(cesar_decrypt(crypted_message, 45481891))
