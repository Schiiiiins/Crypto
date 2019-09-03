alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_crack(cipher_text):

    for key in range(len(alphabet)):

        plain_text = ""

        for c in cipher_text:
            index = alphabet.find(c)
            index = (index-key) % len(alphabet)
            plain_text = plain_text + alphabet[index]

        print("With key " + str(key) + ", the result is: " + plain_text)


if __name__ == "__main__":
    encrypted = input("Please enter the cipher-text: ")
    # encrypted = "VJKUBKUBCBOGUUCIG"
    caesar_crack(encrypted)
