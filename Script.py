import base64, subprocess, pyfiglet
# Ask the user if they want to encrypt or
while True:
    print('')
    logo = pyfiglet.figlet_format("My user Mrfa0gh")
    print(logo)
    action = input("Do you want to encrypt (Enc) or decrypt (Dec) or quit (Q)? ")

    # If the user wants to operate on plaintext, ask for the text input
    if action.lower() == "enc":
        logo = pyfiglet.figlet_format("encrypt")
        print(logo)
        plaintext = input("Enter the plaintext: ")
        print('')

        # Ask the user which encryption algorithm to use
        encryption_algorithm = input("Which encryption algorithm do you want to use? (Ascii, Base 32, Base 64, Binary, or Hex): ")
        if encryption_algorithm.lower() == "ascii":
            subprocess.run('cls', shell=True)
            # encrypt using ASCII encryption algorithm
            ciphertext = ""
            for char in plaintext:
                ciphertext += str(ord(char)) + " "
                subprocess.run('cls', shell=True)
            print("The ciphertext is:", ciphertext)
        elif encryption_algorithm.lower() == "base 32":
            subprocess.run('cls', shell=True)
            # encrypt using Base32 encryption algorithm
            ciphertext = base64.b32encode(plaintext.encode()).decode()
            print("The ciphertext is:", ciphertext)
        elif encryption_algorithm.lower() == "base 64":
            subprocess.run('cls', shell=True)
            # encrypt using Base64 encryption algorithm
            ciphertext = base64.b64encode(plaintext.encode()).decode()
            print("The ciphertext is:", ciphertext)
        elif encryption_algorithm.lower() == "binary":
            subprocess.run('cls', shell=True)
            # encrypt using binary encryption algorithm
            ciphertext = ""
            for char in plaintext:
                binary = bin(ord(char))[2:]
                padded_binary = binary.zfill(8)
                ciphertext += padded_binary + " "
            print("The ciphertext is:", ciphertext)
        elif encryption_algorithm.lower() == "hex":
            subprocess.run('cls', shell=True)
            # encrypt using hexadecimal encryption algorithm
            ciphertext = plaintext.encode().hex()
            print("The ciphertext is:", ciphertext)
        else:
            print("Invalid encryption algorithm.")
    elif action.lower() == "dec":
        logo = pyfiglet.figlet_format("decrypt")
        print(logo)
        # If the user wants to operate on ciphertext, ask for the ciphertext input
        ciphertext = input("Enter the ciphertext: ")
        decryption_algorithm = input("Which decryption algorithm do you want to use? (Ascii, Base 32, Base 64, Binary, or Hex): ")
        if decryption_algorithm.lower() == "ascii":
            subprocess.run('cls', shell=True)
            # decrypt using ASCII decryption algorithm
            plaintext = ""
            for num in ciphertext.split():
                plaintext += chr(int(num))
            print("The plaintext is:", plaintext)
        elif decryption_algorithm.lower() == "base 32":
            subprocess.run('cls', shell=True)
            # decrypt using Base32 decryption algorithm
            plaintext = base64.b32decode(ciphertext.encode()).decode()
            print("The plaintext is:", plaintext)
        elif decryption_algorithm.lower() == "base 64":
            subprocess.run('cls', shell=True)
            # decrypt using Base64 decryption algorithm
            plaintext = base64.b64decode(ciphertext.encode()).decode()
            print("The plaintext is:", plaintext)
        elif decryption_algorithm.lower() == "binary":
            subprocess.run('cls', shell=True)
            # decrypt using binary decryption algorithm
            plaintext = ""
            binary_list = ciphertext.split()
            for i in range(len(binary_list)):
                binary = binary_list[i]
                if i == len(binary_list) - 1:
                    binary = binary.rstrip()
                plaintext += chr(int(binary, 2))
            print("The plaintext is:", plaintext)
        elif decryption_algorithm.lower() == "hex":
            subprocess.run('cls', shell=True)
            # decrypt using hexadecimal decryption algorithm
            plaintext = bytes.fromhex(ciphertext).decode()
            print("The plaintext is:", plaintext)
        else:
            print("Invalid decryption algorithm.")
    elif action.lower() == 'q':
        # Quit the script
        print('Quitting...')
        break
    else:
        print("Invalid action. Please enter either Enc or Dec or quit (Q)? ")
