result = ''
message = ''
choice = ''

while choice != '3':
    choice = input("\n¿Que es lo que desea hacer?\nEnter [1] to Encriptar, \nEnter [2] to Desencriptar, \nEnter [3] to Exit Program: ")

    if choice == '1':
        message = input("\nEnter the message to encrypt: ")

        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 5)

        print (result + '\n\n')
        result = ''

    elif choice == '2':
        message = input("\nEnter the message to decrypt: ")

        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 5)

        print (result + '\n\n')
        result = ''

    elif choice != '3' and choice!= '1' and choice != '2':
        print ("You have entered an invalid choice. Please try again.\n\n")
