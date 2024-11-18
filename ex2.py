def encrypt(plain_text: str, key: str):
  plain_text = plain_text.replace(" ", "")
  key = key.lower().replace(" ", "")
  len_key = len(key)
  len_plain_text = len(plain_text)

  cipher_text = ""
  for key_char in sorted(key):
    index_of_key_char = key.find(key_char)
    for i in range(index_of_key_char, len_plain_text, len_key):
      cipher_text += plain_text[i]
  
  return cipher_text

cipher_text = encrypt(plain_text="please transfer one million dollars to my swiss bank account six two two", key="megabuck")

print(cipher_text)
