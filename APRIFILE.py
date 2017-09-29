def aprifile(percorso):

    try:
        with open(percorso, "r") as ptrfile:
            settings = ptrfile.readlines()
            return (settings)

    except:
        print("File not found")
        exit()

def scrivifile(text, percorso):
    try:
        with open(percorso, "a") as ptrfile:
            ptrfile.write("\n")
            ptrfile.write(text)

    except:
        print("Error")
