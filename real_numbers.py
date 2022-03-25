import drawings 
from math import floor, ceil, sqrt, pi, e, trunc
from random import randint, uniform

def contents():
    """
    Cette fonction affiche les contenus du programme officiel de maths en 2de
    dans la rubrique "Manipuler les nombres"
    """
    print("\nContenus\n")
    content1 = "Ensemble ℝ des nombres réels, droite numérique."
    content2 = "Intervalles de ℝ. Notations +\u221E et -\u221E."
    content3 = "Notation |a|. Distance entre deux nombres réels."
    content4 = "Représentation de l’intervalle [a - r , a + r] puis caractérisation par la condition |x - a| ⩽ r."
    content5 = "Ensemble 𝔻 des nombres décimaux. Encadrement décimal d’un nombre réel à 10**-n près."
    content6 = "Ensemble ℚ des nombres rationnels. Nombres irrationnels ; exemples fournis par la géométrie, par exemple √2 et π."
    contenus = [content1, content2, content3, content4, content5, content6]
    for content in contenus: print(content)

def capacities():
    """
    Cette fonction affiche les capacités attendues du programme officiel de maths en 2de
    dans la rubrique "Manipuler les nombres"
    Et elle propose des exemples et des exercices pour chaque capacité
    """
    score = 0
    print("\nCapacités attendues\n")
    disp_c1 = "Associer à chaque point de la droite graduée un unique nombre réel et réciproquement."
    disp_c2 = "Représenter un intervalle de la droite numérique. Déterminer si un nombre réel appartient à un intervalle donné."
    disp_c3 = "Donner un encadrement, d’amplitude donnée, d’un nombre réel par des décimaux."
    disp_c4 = "Dans le cadre de la résolution de problèmes, arrondir en donnant le nombre de chiffres significatifs adapté à la situation étudiée.\n"
    disp_caps = [disp_c1, disp_c2, disp_c3, disp_c4]
    
    nb_action = True
    while nb_action:
        for i in range(len(disp_caps)): print(f"{i+1}) {disp_caps[i]}")
        nb_action = int(input("Entrer le numéro de la capacité à mettre en oeuvre : "))
        if nb_action == 1: print(c1(score))
        elif nb_action == 2: print(c2(score))
        elif nb_action == 3: print(c3(score))
        elif nb_action == 4: print(c4(score))
            
def c1(score):
    """
    Capacité 1 : Associer à chaque point de la droite graduée un unique nombre réel 
    et réciproquement.
    """
    menu_c1 = """
    Capacité 1 : Associer à chaque point de la droite graduée un unique nombre réel 
    et réciproquement.
    
    0) Quit
    1) Exemples
    2) Exercices
    -------------
    Votre choix : """
    choix_c1 = int(input(menu_c1))
    if choix_c1 == 1: return exemples_c1()
    elif choix_c1 == 2: return f"Score = {exos_c1(score)}"

def grad_denom():
    """
    Cette fonction propose un menu de choix de découpages fractionnaires (1/12e, 1/10e, ...)
    Elle affiche un exemple de graduation et renvoie le dénominateur choisi
    """
    graduations = drawings.real_line()
    menu_c1 = """
    Représenter la droite graduée fractionnée en : 
    1) Douzièmes (1/12, 2/12 = 1/6, 3/12 = 1/4, etc...)
    2) Dixièmes (0.1, 0.2, 0.3, etc...)
    3) Cinquièmes (1/5, 2/5, 3/5, etc...)
    4) Tiers (1/3, 2/3, 1, etc...)
    5) Demis (1/2, 1, 1.5, etc...)
    Votre choix : """
    c1_choice = int(input(menu_c1))
    if c1_choice == 1: 
        print(graduations[0])
        denom = 12
    elif c1_choice == 2: 
        print(graduations[1])
        denom = 10
    elif c1_choice == 3: 
        print(graduations[2])
        denom = 5
    elif c1_choice == 4: 
        print(graduations[3])
        denom = 3
    elif c1_choice == 5: 
        print(graduations[4])
        denom = 2
    return denom

def generate_classics():
    """
    Cette fonction sélectionne aléatoirement une constante classique parmi
    √2, (1+√5)/2, √3 et π
    Elle renvoie le nombre réel (float) et la chaîne de caractère associée
    """
    strings = ["√2", "\u03C6 = (1+√5)/2", "√3", "π"]
    index = randint(0, len(strings) - 1)
    string = strings[index]
    numbers = [sqrt(2), (1+sqrt(5))/2, sqrt(3), pi]
    number = numbers[index]
    return number, string 

def frame_between(denom, number):
    """
    Cette fonction prend 2 arguments en entrées :
    1) denom : le dénominateur du découpage choisi
    2) number : le nombre qu'on cherche à encadrer
    Elle renvoie les bornes inférieure et supérieure 
    """
    borne_inf = floor(denom*number) 
    borne_sup = ceil(denom*number)
    return borne_inf, borne_sup

def exemples_c1():
    print("Exemples pour illustrer la capacité 1 : ")
    denom = grad_denom()
    number, string = generate_classics()
    borne_inf, borne_sup = frame_between(denom, number)
    return f"{borne_inf}/{denom} < {string} < {borne_sup}/{denom}"

def check_ans(user_answer, right_answer, score):
    """
    Cette fonction vérifie la réponse de l'utilisateur et ajuste le score en fonction.
    """
    if user_answer == right_answer:
        print()
        bravo = "Bravo vous avez trouvé la bonne réponse !"
        print("=" * len(bravo))
        print(bravo)
        print("=" * len(bravo))
        print()
        score += 1
        print(f"Votre score vaut maintenant {score}")
    else: print(f"\nRaté ! La bonne réponse était : {right_answer}\n")
    return score

def exos_c1(score):
    print("Exercices pour tester la capacité 1 : ")
    denom = grad_denom()
    number, string = generate_classics()
    borne_inf, borne_sup = frame_between(denom, number)
    frame_num = "Encadrer le nombre "
    par_2_frac = "par 2 fractions avec le nombre"
    print(f"{frame_num} {string} {par_2_frac} {denom} au dénominateur.")
    capiche = "Avez-vous compris la consigne ?\n1) Oui\n0) Non\n"
    compris_ou_pas = int(input(capiche))
    
    if compris_ou_pas == 0: 
        find_ints = "Trouver les nombres entiers a et b tels que "
        equiv = "ou de façon équivalente "
        print(f"{find_ints} (a/{denom}) < π < (b/{denom}) {equiv} a < {denom}*π < b")
        
    a = int(input("Numérateur de la borne inférieure a = "))
    score = check_ans(a, borne_inf, score)
    print(f"Votre score vaut maintenant {score}")
        
    b = int(input("Numérateur de la borne supérieure b = "))
    score = check_ans(b, borne_sup, score)
    print(f"Votre score vaut maintenant {score}")

    space = "\n\t\t\t\t"
    intro = "En effet on a "
    print(f"{intro}:{space}({borne_inf}/{denom}) < {string} < ({borne_sup}/{denom})")
    intro = "Ou encore "
    print(f"{intro}:{space}({borne_inf/denom :.2f}) < {string} < ({borne_sup/denom:.2f})")
    return score



def c2(score):
    """
    Capacité 2 : Représenter un intervalle de la droite numérique. 
    Déterminer si un nombre réel appartient à un intervalle donné.
    """
    menu_c2 = """
    Capacité 2 : Représenter un intervalle de la droite numérique. 
    Déterminer si un nombre réel appartient à un intervalle donné.
    
    0) Quit
    1) Exemples
    2) Exercices
    -------------
    Votre choix : """
    
    choix_c2 = int(input(menu_c2))
    if choix_c2 == 1: return exemples_c2()
    elif choix_c2 == 2: return f"Score = {exos_c2(score)}"

def exemples_c2():
    print("Exemples pour illustrer la capacité 2 : ")
    exemples_intervalles = drawings.intervalles()
    index = randint(0, len(exemples_intervalles) - 1)
    return exemples_intervalles[index]
    

def questionner(born_inf, born_sup, number):
    elnum = f"Le nombre {number}"
    belong_to_int = "appartient-il à l'intervalle "
    return f"{elnum} {belong_to_int} [{born_inf}; {born_sup}] ?"

def repondre(bonne_rep, score):
    rep = int(input("1) Oui\t0) Non\n"))
    if rep == bonne_rep: 
        print("Bravo ! C'est la bonne réponse")
        score += 1
    else: print("Dommage, c'est la mauvaise réponse") 
    return score
    

def exos_c2(score):
    menu = """
    Exercices pour tester la capacité 2 : 
    
    0) Quit
    1) Représenter un intervalle de la droite numérique. 
    2) Déterminer si un nombre réel appartient à un intervalle donné.
    -----------------------------------------------------------------
    Votre choix : """
    
    continuer = int(input(menu))
    if continuer == 1:
        decoupages = [12, 10, 5, 3, 2]
        index_decoup = randint(0, 5)
        print(f"Représenter l'intervalle [0; 1] en {decoupages[index_decoup]}èmes")
        input("Si vous voulez voir la solution appuyez sur 'Entrée' ")
        print("Solution")
        exemples_intervalles = drawings.intervalles()
        return exemples_intervalles[index_decoup]
    elif continuer == 2:
        denom = randint(2, 13)
        phi = (1+sqrt(5))/2
        numbers = [sqrt(2), phi, sqrt(3), sqrt(5), sqrt(7), e, pi]
        index_num = randint(0, len(numbers))
        number = numbers[index_num]
        nb_decim = randint(0, 4)
        if nb_decim == 0:
            borne_inf, borne_sup = frame_between(1, number)
            print(questionner(borne_inf, borne_sup, number))
            return repondre(1, score)
        else:
            borne_inf, borne_sup = frame_between(denom, number)
            if denom*number < borne_inf or denom*number > borne_sup: bonne_rep = 0
            else: bonne_rep = 1
            print(questionner(borne_inf, borne_sup, number))
            return repondre(bonne_rep, score)

def c3(score):
    """
    Capacité 3 : Donner un encadrement, d’amplitude donnée, d’un nombre réel par des décimaux.
    """
    menu = """
    Capacité 3 : Donner un encadrement, d’amplitude donnée, d’un nombre réel par des décimaux.
    
    0) Quit
    1) Exemples
    2) Exercices
    -------------
    Votre choix : """
    
    continuer = int(input(menu))
    if continuer == 1: 
        amplitude = int(input("Amplitude = "))
        return exemples_c3(amplitude)
    elif continuer == 2: 
        amplitude = randint(1, 10)
        return f"Score = {exos_c3(amplitude, score)}"

def generate_floating_frame(action, amplitude):
    """
    Cette fonction prend 2 arguments en entrées :
    1) action : voici (exemple) ou donner (exercice)
    2) amplitude : précision de l'encadrement
    Et renvoie le réel généré et les bornes inf et sup 
    """
    
    a, b = randint(-amplitude, amplitude), randint(-amplitude, amplitude)
    a, b = min(a, b), max(a, b)
    reel = uniform(a, b)
    
    print(f"{action} un encadrement à 10**(-{amplitude}) près du nombre réel {reel}")
    
    arrondi = round(reel, amplitude)
    
    if arrondi < reel: borne_inf = arrondi
    else: borne_inf = round(reel - 10**(-amplitude), amplitude)

    borne_sup = round(reel + 10**(-amplitude), amplitude)

    return reel, borne_inf, borne_sup

def exemples_c3(amplitude):
    print("Exemples pour illustrer la capacité 3 : ")
    
    reel, borne_inf, borne_sup = generate_floating_frame("Voici", amplitude)
    
    print(f"La borne inférieure est {borne_inf}")
    print(f"La borne supérieure est {borne_sup}")
    
    return f"{borne_inf} < {reel} < {borne_sup}"
    

def exos_c3(amplitude, score):
    print("Exercices pour tester la capacité 3 : ")
    
    reel, borne_inf, borne_sup = generate_floating_frame("Donner", amplitude)
    
    b_inf = float(input("Borne inférieure = "))
    score = check_ans(b_inf, borne_inf, score)
    print(f"Votre score vaut maintenant {score}")
    
    b_sup = float(input("Borne supérieure = "))
    score = check_ans(b_sup, borne_sup, score)
    print(f"Votre score vaut maintenant {score}")

    return score

def c4(score): 
    """
    Capacité 4 : Dans le cadre de la résolution de problèmes, arrondir en donnant le nombre de chiffres significatifs adapté à la situation étudiée.
    """
    menu = """
    Capacité 4 : Dans le cadre de la résolution de problèmes, arrondir en donnant le nombre de chiffres significatifs adapté à la situation étudiée.
    
    0) Quit
    1) Exemples
    2) Exercices
    -------------
    Votre choix : """
    
    continuer = int(input(menu))
    if continuer == 1: return exemples_c4()
    elif continuer == 2: return f"Score = {exos_c4(score)}"

def exemples_c4():
    print("Exemples pour illustrer la capacité 4 : ")
    ex1 = "\nEn France, un homme mesure 1,78 m en moyenne : cela fait 3 chiffres significatifs."
    ex2 = "\nEn Allemagne, la moyenne est de 180,3 cm ce qui fait 4 chiffres significatifs."
    ex3 = "\nUne approximation du nombre π est 3,1416 soit 5 chiffres significatifs."
    exemples = [ex1, ex2, ex3]
    for ex in exemples: print(ex)
    
    return True

def exos_c4(score):
    print("Exercices pour tester la capacité 4 : ")

    msg = """
    Attention, en Python, comme dans la plupart des langages de programmation, 
    le séparateur décimal est le point et non la virgule.
    Cela signifie que lorsque vous écrivez des chaînes de caractères (str) 
    en français vous pouvez écrire 1,78 m mais lorsque vous saisissez un nombre (float) 
    il faudra écrire 1.78.
    """
    print(msg)
    
    exo1 = "En France, en 2020, la taille moyenne des femmes était 163,9 cm."
    q1 = "Indiquer la taille moyenne des françaises en m avec 4 chiffres significatifs."
    c1 = 1.639
    a1 = f"La taille moyenne des françaises en 2020 était de {c1} m."
    
    exo2 = "En 2020 en France l'IMC moyen des hommes était de 26 soit +1,2 par rapport à 2012."
    q2 = "Indiquer l'IMC moyen des français en 2012 avec 3 chiffres significatifs."
    c2 = 24.8
    a2 = f"L'IMC moyen des français en 2012 était de {c2}"
    
    exo3 = "Le poids moyen des françaises était de 67,3 kg en 2020."
    q3 = "Indiquer le poids moyen des françaises en 2020 en g avec 5 chiffres significatifs."
    c3 = 67300
    a3 = f"Le poids moyen des françaises en 2020 était de {c3} g."
    
    questions = [(exo1, q1), (exo2, q2), (exo3, q3)]
    right_answers = [(c1, a1), (c2, a2), (c3, a3)]

    for i in range(len(questions)):
        print(f"Enoncé {i+1} : {questions[i][0]}")
        print(f"Question {i+1} : {questions[i][1]}")
        user_answer = float(input("Votre réponses (uniquement le nombre) : "))
        right_answer = right_answers[i][0]
        print(right_answers[i][1])
        score = check_ans(user_answer, right_answer, score)
        print(f"Score = {score}")

    return score
        