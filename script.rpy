# Personagens
define AyaPapaya = Character("Aya Papaya")
define BromeliaBromelia = Character("Bromelia Bromelia")
define SteveApple = Character("Steve Apple")
define LaranjaAnja = Character("Laranja")
define p = Character("Principal")
define Monstro = Character("Monstro")

default preferences.text_cps= 35

# Imagem Personagens
# Aya Papaya
image AyaPapayaAngry = im.Scale("images/Aya Papaya/Aya Papaiya Tatie Angry.png", 500, 800)
image AyaPapayaHappy = im.Scale("images/Aya Papaya/Aya Papaiya Tatie Happy.png", 500, 800)
image AyaPapayaN1 = im.Scale("images/Aya Papaya/Aya Papaiya Tatie normal 1.png", 500, 800)
image AyaPapayaN2 = im.Scale("images/Aya Papaya/Aya Papaiya Tatie normal 2.png", 500, 800)
image AyaPapayaSad = im.Scale("images/Aya Papaya/Aya Papaiya Tatie Sad.png", 500, 800)

# Bromelia Bromelia
image BromeliaBromeliaAngry = im.Scale("images/Bromelia Bromelia/Bromelia Bromelia Angry.png", 500, 800)
image BromeliaBromeliaN1 = im.Scale("images/Bromelia Bromelia/Bromelia Bromelia Normal.png", 500, 800)
image BromeliaBromeliaN2 = im.Scale("images/Bromelia Bromelia/Bromelia Bromelia Normal 2.png", 500, 800)
image BromeliaBromeliaSad = im.Scale("images/Bromelia Bromelia/Bromelia Bromelia Sad.png", 500, 800)

# Steve apple 
image SteveAppleSad = im.Scale("images/Steve apple/Steve apple sad.png", 500, 800)
image SteveAppleN1 = im.Scale("images/Steve apple/Steve apple normal.png", 500, 800)
image SteveAppleN2 = im.Scale("images/Steve apple/Steve apple normal 2.png", 500, 800)
image SteveAppleSmile = im.Scale("images/Steve apple/Steve apple smile.png", 500, 800)

# Laranja Anja
image LaranjaAnjaAngry = im.Scale("images/Laranja Anja/Laranja Anja Angry.png", 500, 800)
image LaranjaAnjaSmile = im.Scale("images/Laranja Anja/Aya Papaiya Tatie Smile.png", 500, 800)
image LaranjaAnjaN1 = im.Scale("images/Laranja Anja/Laranja Anja Normal.png", 500, 800)
image LaranjaAnjaN2 = im.Scale("images/Laranja Anja/Laranja Anja Normal 2.png", 500, 800)


define leftpos = Position(xalign=-0.2, yalign=1.0)
define midleftpos = Position(xalign=0.3, yalign=1.0)
define midrightpos = Position(xalign=0.7, yalign=1.0)
define rightpos = Position(xalign=1.2, yalign=1.0)

transform half_body:
    zoom 1.3        # aumenta o tamanho da personagem
    yalign -0.10      # desce um pouco (do tronco pra cima!!)

# Fundo cenas
image bg_escritorio = im.Scale("images/Background/bg office.png", config.screen_width, config.screen_height)
image bg_quarto = im.Scale("images/Background/bg_quarto.jpg", config.screen_width, config.screen_height)
image bg_rua = im.Scale("images/Background/bg_rua.jpg", config.screen_width, config.screen_height)
image bg_parque_tarde = im.Scale("images/Background/bg_parque_tarde.jpg", config.screen_width, config.screen_height)
#image bg_parque_tarde_baguncado = im.Scale("images/Background/bg_parque_tarde_baguncado.png", config.screen_width, config.screen_height)

#image = RECEPCAO
#image = DA RUA
image bg_casa_noite = im.Scale("images/Background/bg_casa_noite.jpg", config.screen_width, config.screen_height)

#image = CASA (lado de dentro "dia")


# Sons adicionais
define sound_breath = "audio/respiracao.mp3"
define sound_rua = "audio/passos.mp3"
define sound_birds = "audio/passaros.mp3"
define sound_heartbeat = "audio/coracao.mp3"
# define sound_engasgo = "audio/engasgo.mp3"
#define sound_vento = "audio/vento_leve.mp3"
#define sound_voz_fundo = "audio/vozes_ao_fundo.mp3"

# The game starts here.

label start:
    scene bg_escritorio 
        
    "Em mais um dia normal de trabalho..."
    "O (principal) trabalha normalmente juntamente de colegas de trabalho em mais um entardecer de mais um dia."
    #sound effect de escritorio e um teclado barulhento

    p "Mais um dia cansativo..."
    #PRINCIPAL DESANIMADO

    "Sentado em sua cadeira, diante do monitor, a feição de desmotivado e pálido de Principal se torna evidente."
    "Ao refletir vagamente sobre aquele momento, o principal olha levemente ao seu redor, e percebe o desânimo também presente em seus colegas de trabalho no escritório."

    p "Pelo visto eles também..."
    #PRINCIPAL DESANIMADO

    "Principal retoma o foco em seu trabalho..."
    "Alguns minutos depois..."
    "20:00"
    #sound effect de relogio

    p "Hora de voltar para casa."
    "começa arrumar sua mesa, e preparar suas coisas para voltar para casa."

    jump cap1cena2

    #---------------------------------------------------------------------------------------------------
    #CAPITULO1 CENA2
    label cap1cena2:
    #image = RECEPCAO

    "Apos o Principal bater o ponto ele finalmente vai pra casa."

    jump cap1cena3

    #---------------------------------------------------------------------------------------------------
    #CAPITULO1 CENA3
    label cap1cena3:
    #IMAGEM DA RUA

    "Ao caminho de casa diante do transito, as luzes refletem o ambiente e as pessoas que seguem de volta para suas casas."
    "Principal percebe que as pessoas ao seu redor parecem entristecidas... Desanimadas."
    #barulho de transito

    p "O que está acontecendo com o pessoal..."
    #Principal refletindo
    p "Se bem que estou parecido..."
    ##IMAGEM CASA (lado de fora, noite)
    p "Enfim em casa."



    #---------------------------------------------------------------------------------------------------
    #CAPITULO1 CENA4

    #IMAGEM CASA (lado de dentro "noite")
    scene bg_casa_noite

    "Ao chegar na casa, o Principal vai largando suas coisas pelo caminho e deixando sua casa bagunçada."
    #IMAGEM CORREDOR DE ENTRADA MEIO BAGUNCADA
    "Ao entrar na sala Princiapl senta-se em seu sofa."
    #IMAGEM SALA MEIO BAGUNCADA
    p "Que fome, vou pedir algo pra comer."
    "Ele pedi diversas comidas em seu aplicativo, encomenda lanches, fritas, sorvete e outras porcarias."
    "Apos alguns instantes... Seu pedido chega."
    "Ao voltar para a sala, Principal começa a devorar sua comida como se estivesse faminto. Mas quando percebe que a fome parece insaciável começa a chorar enquanto continua comendo..."
    "Isso aconteceu por causa da compulsão alimentar que o Principal desenvolveu por causa de seus conflitos emocionais recentes."

    jump cap1cena5

    #---------------------------------------------------------------------------------------------------
    #CAPITULO1 CENA5
    label cap1cena5:
    #IMAGEM CASA (lado de fora "dia")
    scene bg_quarto

    "Depois de uma longa noite, o dia amanhece."

    #IMAGEM CASA (lado de dentro "dia")
    "Principal começa a se arrumar para o trabalho, e quando vai ao banheiro se depara com algo inusitado."

    p "O QUE ESTA ACONTECENDO?!! O QUE É ISSO?! ISSO SOU EU?!"
    #IMAGEM PRINCIPAL SE OLHANDO NO ESPELHO

    "Quando está prestes a terminar de se arrumar, Principal se olha no espelho e percebe diversas escamas espalhas pelo seu corpo." 
    "Seu corpo começa a se transformar, seus dedos começam a virar batatas fritas, escamas de nugetts se espalham pelo seu pescoço."
    "Além de sua palidez aumentar por conta da pressão arterial."





    #Capitulo 2
    # Cena 1 — Quarto do Principal
    scene bg_quarto
    play sound sound_breath loop

    narrator "O desespero toma conta. Ele tenta arrancar os nuggets que brotam de sua pele, mas não importa quantas vezes retire, eles sempre voltam."
    
    p "Não!! Não para de sair!!! Ai! Ai!!!"
    p "Ahh, ahh...!!! Socorro! Alguém!!! Alguém me ajuda!!!"

    narrator "O ambiente está silencioso. Sua voz ecoa pela casa, apenas acompanhada pela respiração ofegante."
    narrator "Nenhuma resposta vem."

    stop sound

    narrator "Após alguns segundos, ele para e respira fundo, tentando se acalmar. Ele olha para o relógio..."
    
    p "Droga! Estou atrasado para o trabalho!"

    narrator "Ele corre até o guarda-roupa, pega um cachecol para cobrir as escamas de nuggets, coloca luvas para esconder os dedos em forma de batata frita, pega sua bolsa com papéis inacabados e sai apressado."

    # Cena 2 — Rua
    scene bg_rua with fade
    play sound sound_rua loop

    narrator "Ele corre até a empresa, desviando das pessoas, sempre com a cabeça baixa para esconder o rosto."

    stop sound

    # Cena 3 — Parque (tarde)
    scene bg_parque_tarde with fade
    play sound sound_birds loop

    narrator "Já às 15h, no horário atrasado do almoço, o Principal se senta sozinho em um banco do parque."
    narrator "Ele abre um hambúrguer enorme, recheado de carne e molho, e começa a comer para matar a fome acumulada."
    narrator "Ao olhar para o lado, vê sua colega de trabalho sentada no banco ao lado. Ela devora donuts um atrás do outro, mordendo grandes pedaços e engolindo quase sem mastigar."

    narrator "Ele observa assustado, mas tenta ignorar e continua comendo."

    # Cena 4 — Parque (transformação da colega)
    # play sound sound_engasgo

    narrator "De repente, um barulho seco interrompe o momento."
    narrator "Sua colega começa a se engasgar, contraindo o corpo em dor."
    narrator "Ela perde a consciência e grita como um animal enfurecido, batendo com força no próprio peito, que incha de forma grotesca."
    narrator "Chocolate rosa começa a escorrer pelo seu rosto, confetes coloridos caem pelo chão."
    narrator "O corpo dela encolhe e se deforma."

    p "O que é isso?! O que está acontecendo???"

    # Cena 5 — Parque 
    # stop sound
    play sound sound_heartbeat loop

    narrator "Ele deixa o hambúrguer cair no chão. Suas mãos tremem."
    narrator "O medo o paralisa."
    narrator "As imagens da transformação que ele mesmo começou a sofrer pela manhã voltam à sua mente: os dedos em batata frita, as escamas de nuggets..."

    # (falta coisa)
    # show transformation_image

    stop sound
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #CAPITULO3 CENA1
    label cap3cena1:
    #IMAGEM PARQUE

    show BromeliaBromeliaAngry at leftpos, half_body
    BromeliaBromelia "Cuidado!!"
    #espectro de sombra

    "Principal se esbarra com uma jovem e ambos caem no chao."

    BromeliaBromelia "Fuja logo! Antes que voce se transforme em um Cronico!"

    p "Cronico?! O Que isso?!"

    hide BromeliaBromeliaAngry
    show BromeliaBromeliaN1 at leftpos, half_body
    show AyaPapayaN1 at rightpos, half_body
    AyaPapaya "Voce ja esta contaminado pela DECENT, se continuar desse jeito ira se transformar igual aquele monstro!"

    hide BromeliaBromeliaN1
    hide AyaPapayaN1
    "Sem entender Principal é puxado por um rapaz de oculos."

    show SteveAppleN1 at midleftpos, half_body
    SteveApple "Levanta!"

    Monstro "AAAAAAAAAAAAAARRRRGH"

    "Ao gritar  o monstro começa a jogar donuts em diversas pessoas, fazendo elas absorverem, ficando obesos, contraindo DECENT, para transforma-los em Cronicos."

    hide SteveAppleN1
    show BromeliaBromeliaAngry at leftpos, half_body
    show AyaPapayaN1 at rightpos, half_body
    BromeliaBromelia "Rapido! Precisamos fazer algo!"

    "Aiya e Bromelia se encaram e juntas golpeiam o Cronico."

    "Aiya e Bromelia" "HHAAAAAAAAAAAAAAAAAAAAAA."

    show LaranjaAnjaN1 at midrightpos, half_body
    "Logo em seguida chegam mais reforços, Laranja Anja reforça os ataques da equipe, juntos controlando os monstros no local."

    hide AyaPapayaN1
    hide BromeliaBromeliaAngry
    hide LaranjaAnjaN1
    #Capitulo 4
    # Cena 1 — Parque (após a batalha)
    #scene bg_parque_tarde_baguncado with fade
    #play wind sound_vento loop
    #play voz sound_voz_fundo loop

    
    narrator "O Principal respira com dificuldade, ainda atordoado pelo que viu. Ao seu redor, as quatro figuras misteriosas se aproximam."

    # Cena 2 — Diálogo inicial
    show AyaPapayaHappy at leftpos, half_body
    AyaPapaya "Você está bem?"

    show SteveAppleSmile at midleftpos, half_body
    SteveApple "Ele parece estar assustado..."

    show BromeliaBromeliaN2 at midrightpos, half_body
    BromeliaBromelia "Claro que está! Olha só o olhar de morto dele! kkkkkk"

    show LaranjaAnjaN1 at rightpos, half_body
    LaranjaAnja "Você quer um suco de laranja?"

    p "Ahhhhhhh... Não? Pera... O que aconteceu???"

    # Cena 3 — Revelação
    # Cena revelação
    
    BromeliaBromelia "Nós explicaremos! Somos fadas da Alimentação Saudável!"


    AyaPapaya "Estamos aqui para prevenir as DCNTs!"

    p "DCNT? O que é isso?"


    SteveApple "São Doenças Crônicas Não Transmissíveis. Aquelas doenças que você pode desenvolver comendo de forma não saudável."

    #---------------------------------------------------------------------------------------------------
    #CAPITULO4 CENA3
    label cap3cena3:
    #IMAGEM PARQUE (fim de tarde, cenário levemente bagunçado pela luta)

    # Mostrando todos os personagens já posicionados
 

    LaranjaAnja "Os mais comuns são hipertensão, obesidade e diabetes. E nós podemos ver que você está com início de transformação do Monstro #DCNT, isso acontece quando você ultrapassa de apenas uma doença para uma mutação corporal."


    AyaPapaya "E você não pode continuar desse jeito, você está totalmente péssimo. Estressado, olhe para esses olhos sem brilho, parece até um peixe morto!"


    BromeliaBromelia "Nós podemos te ajudar, mas isso só vai funcionar se você realmente querer."

    p "eu..... Eu não sei...... Eu estou com medo. Mas não sei se eu vou conseguir..."


    SteveApple "Você consegue sim, estamos aqui para ajudar todos que precisam de ajuda."

    "Todas as fadas" "SIM!"


    SteveApple "Vamos ir para algum lugar mais confortável, temos que explicar tudo certinho."

    

    return