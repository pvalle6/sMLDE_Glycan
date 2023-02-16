
run = True
protein = input("ENTER PROTEIN SEQUENCE:\n")
while(run):
    start = int(input("ENTER START RESIDUE:\n"))
    end = int(input("ENTER END RESIDUE:\n"))

    domain = protein[start-1:end]
    print(domain)
    checkRun = input("AGAIN?")
    if checkRun == 'y':
        run = True
    else:
        run = False