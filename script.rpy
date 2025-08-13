# Personagens
define AyaPapaya = Character("Aya Papaya")
define BromeliaBromelia = Character("Bromelia Bromelia")
define SteveApple = Character("Steve Apple")

# Imagem Personagens
# Aya Papaya
image AyaPapayaAngry = "images/Aya Papaya/Aya Papaiya Tatie Angry.png"
image AyaPapayaHappy = "images/Aya Papaya/Aya Papaiya Tatie Happy.png"
image AyaPapayaN1 = "images/Aya Papaya/Aya Papaiya Tatie normal 1.png"
image AyaPapayaN2 = "images/Aya Papaya/Aya Papaiya Tatie normal 2.png"
image AyaPapayaSad = "images/Aya Papaya/Aya Papaiya Tatie Sad.png"

# Bromelia Bromelia
image BromeliaBromeliaAngry = "images/Bromelia Bromelia/Bromelia Bromelia Angry.png"
image BromeliaBromeliaN1 = "images/Bromelia Bromelia/Bromelia Bromelia Normal.png"
image BromeliaBromeliaN2 = "images/Bromelia Bromelia/Bromelia Bromelia Normal 2.png"
image BromeliaBromeliaSad = "images/Bromelia Bromelia/Bromelia Bromelia Sad.png"

# Steve apple 
image BromeliaBromeliaSad = "images/Bromelia Bromelia/Steve apple sad.png"
image BromeliaBromeliaN1 = "images/Bromelia Bromelia/Steve apple normal.png"
image BromeliaBromeliaN2 = "images/Bromelia Bromelia/Steve apple normal 2.png"
image BromeliaBromeliaSmile = "images/Bromelia Bromelia/Steve apple smile.png"


# Fundo cenas
image bg_office = im.Scale("images/Background/bg office.png", config.screen_width, config.screen_height)




# The game starts here.

label start:
    #Capitulo 1 
    #Cena 1
    scene bg_office  # Fundo da primeira cena
    play soundOffice "audio/ambiente-escritorio.mp3" loop

    AyaPapaya "OII"
    BromeliaBromelia "OIIII!!"
    SteveApple "OIII"

    play clock "audio/clock.mp3" loop

    stop clock
    stop soundOffice

    scene bg_transito with fade  # Troca para outra cena com transição

    AyaPapaya "OII"
    BromeliaBromelia "OIIII!!"

    return