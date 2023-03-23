
respondeEstimulos = input("¿Responde a Estimulos? (Si/No): ").lower()

while respondeEstimulos not in ['si','no']:
    print("\nSolo ingrese Si/No.")
    respondeEstimulos = input("¿Responde a Estimulos? (Si/No): ").lower()

if respondeEstimulos == 'si':
    print("Valorar la necesidad de llevarlo al hospital más cercano.\n")
else:
    print("\nAbrir la vía Aérea")
    respira = input("¿Respira? (Si/No): ").lower()
    
    while respira not in ['si','no']:
        print("\nSolo ingrese Si/No.")
        respira = input("¿Respira? (Si/No): ").lower()
        
    if respira == 'si':
        print("\nPermitirle posición de suficiente ventilación\n")
    else:
        print("\nAdministrar 5 Ventilaciones y llamar a Ambulancia\n")
        
        llegoAmbulancia = 'no'
        while llegoAmbulancia == 'no':
            signosVida = input("¿Signos de Vida? (Si/No): ").lower()  
            
            while signosVida not in ['si','no']:
                print("\nSolo ingrese Si/No.")
                signosVida = input("¿Signos de Vida? (Si/No): ").lower()  
                 
            if signosVida == 'si':
                print("Reevaluar a la espera de la Ambulancia.\n")
            elif signosVida == 'no':
                print("Administrar Compresiones Torácicas hasta que llegue ambulancia.\n")
                
            llegoAmbulancia = input("¿Llegó la ambulancia? (Si/No): ").lower()
            
print("Programa finalizado!\n")