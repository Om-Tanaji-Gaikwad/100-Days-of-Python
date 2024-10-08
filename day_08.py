# Caesar Cipher

def cipher(original_text,shift_number,encode_or_decode):
    shift_text = ""
    if encode_or_decode=="decode":
        shift_number*=-1
    for letter in original_text:
        if letter not in letters:
            shift_text += letter
        else:
            shift = letters.index(letter) + shift_number
            shift %= len(letters)
            shift_text += letters[shift]
    if encode_or_decode=="encode":
        print(f"The encoded message is {shift_text}")
    elif encode_or_decode=="decode":
        print(f"The decoded message is {shift_text}")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a=input("Enter your Message : \n").lower()
b=int(input("Enter Shift number : \n"))
c=input("Enter your chioce (encode or decode) : \n").lower()
if (c=="encode" or c=="decode"):
    cipher(a,b,c)
else:
    print("Invalid Choice!")
