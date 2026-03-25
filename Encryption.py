#نعرف متغيرين
message = input("Entre the messege that you want to encrypt it " )
number = int(input("Entre the number you want to be a number screet "))
#استيراد المكتبات
import string
lowercase_alphabets = string.ascii_lowercase
uppercase_alphabets = string.ascii_uppercase
punctuation = string.punctuation 
numbers = string.digits 
alphabets = lowercase_alphabets + uppercase_alphabets + punctuation + numbers
#نعرف دالة التشفير
def encryption(mes,num):
  x = ""
  for letter in mes:
    if letter in  alphabets:
      postion = alphabets.index(letter)
      new_postion = (num + postion) % len(alphabets) 
      letter = alphabets[new_postion]
      x += letter  
    else:
      x += letter
  print(x)
encryption(mes=message, num=number)        

message1 = input("Entre the messege that you want to dencrypt it\n" )
number1 = int(input("Entre the number you want to be a number screet\n "))
#نعرف دالة  فك التشفير
def dencry(mes,num):
  x = ""
  for letter in mes:
    if letter in  alphabets:
      postion = alphabets.index(letter) 
      new_postion = (postion - num) % len(alphabets)
      letter = alphabets[new_postion]
      x += letter
    else:
      x += letter
  print(x)
dencry(mes=message1,num=number1)