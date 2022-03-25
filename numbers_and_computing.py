import real_numbers 

numbers_menu = """
Nombres et calculs

0) Quit
1) Manipuler les nombres
-------------------------
Votre choix : """

continuer = True
while continuer:
    continuer = int(input(numbers_menu))
    if continuer == 1: 
        manip_nb_menu = """
        Manipuler les nombres réels 
        
        0) Quit
        1) Contenus
        2) Capacités attendues
        -----------------------
        Votre choix : """
        
        manip_nb_action = True
        while manip_nb_action:
            manip_nb_action = int(input(manip_nb_menu))
            if manip_nb_action == 1: real_numbers.contents()
            elif manip_nb_action == 2: real_numbers.capacities()
                