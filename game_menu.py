print("""
    Menu title:
    -----------
    1) Action One
    2) Action Two
    3) Action Three
    0) Quit
""")

option = input("ENter option: ")
if option == '1':
    print("Performing the action one")
elif option == '2':
    print("Performing the action two")
elif option == '3':
    print("Performing the action three")
elif option == '4':
    print("Quitting...")
else:
    print("Error")