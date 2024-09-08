# Inicio del proceso
def proceso_fin_relacion():
    # Pregunta inicial: Terminas una relación
    print("Terminaste una relación.")
    
    # Primer paso: ¿Estoy triste?
    triste = input("¿Estás triste? (si/no): ").lower()
    
    if triste == 'no':
        print("Sigo con mi vida normal.")
        return
    else:
        # Si estás triste, entonces: ¿Puedo recuperarme solo?
        recuperarse_solo = input("¿Puedes recuperarte solo? (si/no): ").lower()
        
        if recuperarse_solo == 'si':
            print("Sigo con mi vida normal.")
            return
        else:
            # Si no puedes recuperarte solo, buscas ayuda con amigos
            print("Buscando ayuda con amigos o seres cercanos.")
            
            # Después de buscar ayuda: ¿Me siento mejor?
            mejor = input("¿Te sientes mejor? (si/no): ").lower()
            
            if mejor == 'si':
                print("Sigo con mi vida normal.")
                return
            else:
                # Si no te sientes mejor, buscas ayuda profesional
                print("Buscando ayuda profesional.")
                
                # Suponiendo que después de ayuda profesional te sientas mejor
                print("Con ayuda profesional, sigo con mi vida normal.")

# Ejecutar el proceso
proceso_fin_relacion()
