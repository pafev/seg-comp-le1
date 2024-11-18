import pprint

# Funcoes aux
def get_num_by_char(char: str):
  if [' ', ',', '.', ';', ':'].count(char) == 0:
    return ord(char.lower()) - 97
  return char


def get_char_by_num(char_num):
  if type(char_num) == int:
    return chr(char_num + 97)
  return char_num


def encrypt_char_num(char_num, key: int):
  if type(char_num) == int:
    return (char_num + key) % 26
  return char_num


def decrypt_char_num(char_num, key: int):
  if type(char_num) == int:
    return (char_num - key) % 26
  return char_num


# Main
def encrypt(plain_text: str, key: int):
  cypher_text = ""
  for char in plain_text:
    char_num = get_num_by_char(char)
    encrypted_char_num = encrypt_char_num(char_num, key)
    cypher_text += get_char_by_num(encrypted_char_num)
  return cypher_text


def decrypt_with_brute_force(cypher_text: str): # ordem de 26*n
  possible_results = {}
  for k in range(26):
    possible_plain_text = ""
    for char in cypher_text:
      char_num = get_num_by_char(char)
      decrypted_char_num = decrypt_char_num(char_num, k)
      possible_plain_text += get_char_by_num(decrypted_char_num)
    possible_results[k] = possible_plain_text
  return possible_results


def decrypt_with_frequency_distribution(cypher_text: str): # ordem de de 4*n para as tres chaves mais provaveis
  possible_results = {}

  max_count = 0
  max_count_char = ""
  for char in cypher_text:
    if [' ', ',', '.', ';', ':'].count(char) == 0:
      count_char = cypher_text.count(char)
      if count_char > max_count:
        max_count = count_char
        max_count_char = char
  
  k1 = get_num_by_char(max_count_char) - get_num_by_char("a") # chave mais provavel
  k2 = get_num_by_char(max_count_char) - get_num_by_char("e") # segunda chave mais provavel
  k3 = get_num_by_char(max_count_char) - get_num_by_char("o") # terceira chave mais provavel

  for k in [k1, k2, k3]:
    possible_plain_text = ""
    for char in cypher_text:
      char_num = get_num_by_char(char)
      decrypted_char_num = decrypt_char_num(char_num, k)
      possible_plain_text += get_char_by_num(decrypted_char_num)
    possible_results[k] = possible_plain_text
  
  return possible_results

cypher_text = encrypt(plain_text="alianca nova", key=3)
result1 = decrypt_with_brute_force(cypher_text)
result2 = decrypt_with_frequency_distribution(cypher_text)

pprint.pprint(result1)
pprint.pprint(result2)