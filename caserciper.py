import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(direction, text, shift):
    encrypt = ''
    if direction == "encrypt":
        for i in text:
            possition = alphabet.index(i)
            new_possition = possition+shift
            new_letter = alphabet[new_possition]
            encrypt += new_letter
        print(f"Your encoded massage : {encrypt}")

    decrypt =''
    if direction == "decrypt":
        for i in text:
            possition = alphabet.index(i)
            new_possition = possition-shift
            new_letter = alphabet[new_possition]
            decrypt += new_letter
        print(f"Your encoded massage : {decrypt}")

while True:
    yes_or_no= input("If you want to used ceserciper then type \"yes\" and if you want to exit then type \"no\" : ").lower()
    if yes_or_no =="yes":
        direction = input( "Enter \"Encrypt\" for encode the text or \"Decrypt\" to decode the text :").lower()
        text = input("Type your text ").lower()
        shift= int(input("Give how much shift you need : "))
        encrypt(direction, text, shift)
    elif yes_or_no == "no":
        print("You have suceessfully exited the ceserciper ")
        break
