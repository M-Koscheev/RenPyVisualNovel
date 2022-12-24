init:
    # Определение персонажей игры.
    define Kirill = Character('Кирилл')
    define Mother = Character('Мама')
    define Teacher = Character('Учитель')
    define Gleb = Character('Глеб')
    define Oleg = Character('Олег')
    define Lesha = Character('Леша')
    define Zhenya = Character('Женя')
    define Storyteller = Character('Рассказчик')

    image kirill_image:
        "GG.png"
        xpos 250
        ypos 1300
        zoom 0.65
        rotate 180
        yzoom -1

    image mother_image:
        "mother.png"
        xpos 1900
        ypos 1150
        zoom 0.45

    image zhenya_image:
        "crushiha.png"
        zoom 0.7
        xpos 1600
        ypos 2100

    image teacher_image:
        "teacher.png"
        zoom 1.2
        xpos 800
        ypos 250

    image gleb_image:
        "nerd.png"

    image oleg_image:
        "clown.png"
        zoom 0.55

    image lesha_image:
        "villain.png"
    
    image home_background:
        "home_background.png"
        zoom 0.35

    image street_background:
        "street_background.png"
        zoom 0.5

    image first_ending_background:
        "first_ending_background.jpg"
        zoom 3

    image second_ending_background:
        "second_ending_background.jpg"

    image circle_background = "circle_background.png"

    default choice_sit_with = 0 # 1 = Gleb; 2 = Oleg; 3 = No one
    default tell_about_liked_girl_to_mom = 0 # 1 - lie 2 - say truth
    default save_choice_sit_with_choice = 0 # 1 - path to second ending 2 - to first

label start:
    call first_scene

    call second_scene

    call third_scene

    if choice_sit_with == 1:
        call fourth_scene_first_choice
    elif choice_sit_with == 2:
        call fourth_scene_second_choice
    elif choice_sit_with == 3:
        call fourth_scene_third_choice

    call fifth_scene

    if tell_about_liked_girl_to_mom == 1:
        call sixth_scene_first_choice
    elif tell_about_liked_girl_to_mom == 2:
        call sixth_scene_second_choice

        call seventh_scene

        call eighth_scene

    

    if choice_sit_with == 1:
        call nineth_scene_first_choice
    elif choice_sit_with == 2:
        call nineth_scene_second_choice
    elif choice_sit_with == 3:
        call nineth_scene_third_choice

    call tenth_scene

    if choice_sit_with == 1:
        menu:
            "Остаться сидеть с Глебом.":
                call eleventh_scene_first_first
            "Уйти от этого ботаника.":
                $ choice_sit_with = 2
                call eleventh_scene_first_second
    elif choice_sit_with == 2:
        menu:
            "Олег прикольный пацан, никуда от него не уйду.":
                call eleventh_scene_second_first
            "Олег - это здорово, но рыженькая - это просто прекрасно."
            "Пора вернуться к изначальной цели.":
                $ choice_sit_with = 1
                call eleventh_scene_second_second
    elif choice_sit_with == 3:
        call eleventh_scene_third

    if save_choice_sit_with_choice == 1:
        call twelve_first
    elif save_choice_sit_with_choice == 2:
        call twelve_second

    if save_choice_sit_with_choice == 1 and tell_about_liked_girl_to_mom == 1:
        call thirteen_first_first
    elif save_choice_sit_with_choice == 1 and tell_about_liked_girl_to_mom == 2:
        call thirteen_first_second
    elif save_choice_sit_with_choice == 2 and tell_about_liked_girl_to_mom == 1:
        call thirteen_second_first
    elif save_choice_sit_with_choice == 2 and tell_about_liked_girl_to_mom == 2:
        call thirteen_second_second
    
    if save_choice_sit_with_choice == 2:
        call first_ending
    else:
        if choice_sit_with == 3:
            call fourteen_first
            call second_ending
        else:
            call fourteen_second
            call second_ending

    return

label first_scene:
    scene home_background:
            zoom 1.7

    show kirill_image

    show mother_image

    Kirill "Да кому эти игры вообще нужны?"

    Kirill "Вернее, если уж и нужны, то точно для того, чтобы играть, а не для того, чтобы их создавать."

    Kirill "У нас, вон, машины столько лет не было, так вы в автосалон за ней пошли, а не сами пытались сделать."

    Mother "Кирилл, я всё понимаю, переходный возраст, лень вселенского масштаба, но это для твоего же блага."

    Mother "Мама тебе плохого не посоветует."

    Kirill "Мам, давай ты мне посоветуешь тарелку после гречки сразу помыть, одежду вывернуть перед тем, как закинуть стирать, ну и всякое такое, а со своим хобби я сам разберусь, ок?"

    Mother "Сынок, ты не понимаешь от чего отказываешься."

    Mother "Потом локти кусать будешь, просить чтоб записала, а уже будет нельзя."

    Mother "Да и вообще, я поговорила с мамой Лёши на собрании, и она сказала, что он сам попросил её записать себя на этот кружок."

    Mother "Видишь, как он о своём будущем заботится? Не то что ты, гуляешь целыми днями."

    Mother "Так что я тебя прошу, сходи на пару занятий, а потом уже решишь: нравится тебе или нет. Ради меня сходи, ок?"
    
    scene home_background:
        zoom 1.7

    show kirill_image
    
    Kirill "{i}Снова опять этот Лёша, в каждой бочке затычка. СыН мАмИноЙ ПодРуГи, конечно. Лёша выиграл это, Лёша сделал то, а ты оболтус. Угораздило же наших мам быть подругами.{/i}"

    scene home_background:
        zoom 1.7

    show kirill_image

    show mother_image

    Mother "Ну так что, сходишь?"

    Kirill "Схожу, схожу. Но помни - только ради тебя. Мне эта идея изначально не нравится."

    return


label second_scene:
    scene street_background:
        zoom 1.5

    show kirill_image

    Kirill "Ну зачем я согласился пойти на эту разработку? Щас все пацаны сидят в «Аппетитно и двоеточие», общаются, веселятся, а я как дурак дома поел и на автобус."

    Kirill "Ладно хоть всего пару раз так придётся съездить, а то через месяц я бы на стену лез от недостатка отдыха в крови."

    Storyteller "Достаёт телефон."

    Kirill "Даже здесь это ваше программирование."

    menu:
        "толстяк дебагер - ест твои ошибки и бьёт себя по лбу
        после каждой пропущенной ';'. Перестань кормить дебагера, он наелся.":
            pass
        "Стратег. \"Хмм, код не работает. Может ничего не менять и запустить его снова?\"":
            pass
        "Цифра 3. Почему ты выбрал цифру 3? У нас нет идей для третьего варианта":
            pass

    Kirill "Ну всё, домой приеду, распечатаю, в рамочку поставлю." 
    
    Kirill "О, а вот и моя остановочка"

    return
    
label third_scene:
    scene circle_background:
        zoom 2

    show kirill_image


    Kirill "{i}А вот и она - Красная комната.{/i}"

    Kirill "Ну, привет всем. Особо меня не запоминайте, через 2 недели меня уже здесь не будет."


    Kirill "{i}Ладно, ради приличия можно и взглянуть на бедолаг.{/i}"
    
    show zhenya_image

    Kirill "{i}Это….что…это кто такое красивое создание из рая выпустил? Я даже не знаю от чего сейчас щурюсь: от её лучезарности или от того, что я запрокинул голову наверх и сейчас мне в глаза светят лампочки?{/i}"

    Kirill "{i}Так, Кирилл, собери себя в руки, хватит кринжа наваливать. Встань нормально.{/i}"

    scene circle_background:
        zoom 2

    show teacher_image:
        zoom 0.5

    Teacher "Здравствуйте, дети. Сегодня мы с вами начинаем курс: «Первую игру я сделал(а) в 16 лет»."

    Teacher "Не люблю затягивать, поэтому начинаем опросик, чтобы сразу понять кто разбирается, а кто из-под палки пришёл."

    Teacher "Разбейтесь на пары и решайте задания"

    Kirill "{i}Что? Опять этот Лёша! Даже здесь умудряется малину испортить. Да и она видимо из тех, кто посередине останется, как папа говорил.{/i}"


    Kirill "{i}Так, ну ладно, этот курс становится интереснее.{/i}"


    Kirill "{i}Я должен буду разобраться в этой разработке игр и превзойти этого Лёшу, чтобы рыженькая сидела со мной!{/i}"

    menu:
        "Раз с ней сесть не получилось, надо бы выбрать того, с кем я проведу это время."
        "Сесть с Заучкой":
            $ choice_sit_with = 1
        "Сесть с Весёлым парнем":
            $ choice_sit_with = 2
        "Сесть одному":
            $ choice_sit_with = 3

    return


label fourth_scene_first_choice:
    scene circle_background:
        zoom 2

    show kirill_image


    Kirill "{i}Естественно! Парень в очках, линзы которого толще монитора, он то мне и поможет с заданиями, да и прокачаться в программировании с ним легче будет, чтобы добиться мою ненаглядную.{/i}"

    Kirill "Привет, я подсяду?"

    show gleb_image at right:
        zoom 1

    Gleb "Подсесть ты бы мог, если бы уже сидел, а ты же сейчас стоишь, поэтому правильно сказать присяду."


    Kirill "{i}Ну что ещё я мог ожидать? Ладно, надеюсь, что он всё будет делать, а я просто посижу.{/i}"

    Kirill "Хорошо. Меня Кирилл зовут, а тебя как?"

    Gleb "А меня Мефодий."

    Gleb "Хахахахах вот это я пошутил. Я Глеб."

    Kirill "Теперь будем сидеть вместе."

    Gleb "Ага."

    return


label fourth_scene_second_choice:
    scene circle_background:
        zoom 2

    show kirill_image


    Kirill "{i}Парень, который сделал скриншот рабочего стола, удалил все иконки и поставил его на фон?{/i}"


    Kirill "{i}Мой вариант! С ним хотя бы весело будет.{/i}"

    show oleg_image at right:
        zoom 0.5

    Kirill "Привет, я подсяду?"

    Oleg "Что-то ты не очень похож на девочку в радужной кофте."

    Oleg "Ну ладно. Меня зовут Олег, но друзья зовут играть меня в баскетбол, а тут из-за мамы оказался."

    Kirill "О, какое совпадение, я тоже."

    Kirill "Я Кирилл, кстати. Теперь мы вместе."

    Oleg "Сидим?"

    Kirill "Ну, как пойдёт)"

    return


label fourth_scene_third_choice:
    scene circle_background:
        zoom 2

    show kirill_image

    Kirill "Ну и правильно. Сидеть ещё с кем-то, знакомиться, бе-е."

    Kirill "Тем более никто не будет мешать ботать =). Но и помогать тоже =( ."

    Kirill "Ладно, вижу цель, не вижу препятствий!"

    return


label fifth_scene:
    scene home_background:
            zoom 1.7

    show kirill_image

    show mother_image

    Mother "Ну что, как прошло первое занятие?"

    Kirill "Да как обычно. Ничего интересного."

    Kirill "Посидел, ничего не понял, уехал. Бесполезно время провёл."

    menu:
        "Ну, что, даже ни с кем не познакомился? Никто не приглянулся?"
        "Соврать":
            $ tell_about_liked_girl_to_mom = 1
        "Сказать честно":
            $ tell_about_liked_girl_to_mom = 2

    return


label sixth_scene_first_choice:
    scene home_background:
            zoom 1.7

    show kirill_image
    show mother_image


    Kirill "Нет, ты что? Смог бы я за раз в кого-то влю...кхм кхм всмотреться."


    Mother "Ну ладно. Знаешь, я тут подумала, если тебе совсем не понравилось, то чё я тебя буду мучить? Я же не тиран."

    Mother "Можешь больше никуда не ездить."

    Kirill "Да знаешь, я же мужчина, если сказал, что на пару занятий схожу ради тебя, значит пару занятий точно отхожу."

    Mother "Ой, какой у меня мужчи-ина растёт. Ну, иди руки мыть, щас есть наложу."

    return


label sixth_scene_second_choice:
    scene home_background:
        zoom 1.7

    show kirill_image

    show mother_image

    Kirill "Если честно, есть там одна девочка…"

    Mother "Ах, кто-то влюбился))))) Ну, рассказывай, какая она?"

    return


label seventh_scene:
    scene home_background:
        zoom 1.7

    show kirill_image

    show mother_image

    Kirill "Мам, это нечто. 160 см, под 90 кг, брови сросшиеся, рот держит постоянно открытым."

    Mother "Серьёзно?"

    Kirill "Да ладно, угораю. На самом деле я даже не совсем запомнил какая она."

    Kirill "Как только мой взгляд упал на неё, я смог отвести его только через силу. Помню только, что у неё рыжие волосы."

    return


label eighth_scene:
    scene home_background:
            zoom 1.7

    show kirill_image

    show mother_image

    Mother "А ты идти не хотел. Видишь, какая я молодец?"

    Kirill "Но есть одно но..."

    Mother "Какое?"

    Kirill "Училка первым делом нет, что бы познакомиться, организовала мини опрос, а так как Лёша что-то знает, ответил на все вопросы."

    Kirill "Все поняли, что он самый крутой, и она села с ним делать задания. Просто так я к ней не подойду, чтобы попросить сесть вместе со мной, вдруг ещё поймёт, что она мне нравится, поэтому мне надо срочно обогнать по знаниям Лёшу."

    Mother "Ну да, ситуация не из приятных. Но не всё так плохо. Пойду запишу тебя к репетитору и быстро обгонишь Лёшу."
    
    Kirill "Мам, какой репетитор по кружку? Да и где я время на него найду, если у меня школа и программирование?"

    Mother "А, точно, это и так «репетитор». Ну ладно, но ты всё равно можешь рассчитывать на мою помощь."

    return


label nineth_scene_first_choice:
    scene circle_background:
        zoom 2

    show kirill_image

    show gleb_image at right:
        zoom 1

    Gleb "О, ты всё-таки пришёл? Я уж думал, что для тебя это слишком трудно и ты не захочешь что-либо делать."

    Gleb "Ну ладно, садись, я уже пару заданий решил."

    Kirill "Но урок же начинается через 5 минут 0_0"

    Gleb "А, да я просто гулял по кабинету и увидел, что у преподавательницы документ с заданиями открыт."

    Kirill "Её компьютер выключен."

    Gleb "Ну, я там…"

    Kirill "...подошёл к ней и выпросил задания, чтобы удовлетворить свою дотошную душонку?"

    Gleb "Что ты докопался? Вообще всё не так было…"

    Gleb "Ладно, всё так и было. Но я не дотошный! Слышишь? Я не дотошный и вот тебе 4 причины почему."

    Gleb "Первая – …"

    Kirill "{i}Надо ли оно мне было? Повеселился, молодец. Начинается занятие.{/i}"

    return


label nineth_scene_second_choice:
    scene circle_background:
        zoom 2

    show kirill_image

    show oleg_image at right:
        zoom 0.5

    Oleg "О, здарова. А я всё думал, когда же ты появишься? Ну, чё, как оно?"

    Kirill "Всё ништяк, мээн."

    Oleg "Айоу, мээн."

    Kirill "Мэээн"

    Oleg "Мэээээн. Начинается занятие."
    
    return


label nineth_scene_third_choice:
    scene circle_background:
        zoom 2

    show kirill_image

    Kirill "Здесь снова опять не занято. Даже грустно как-то. Начинается занятие."

    return


label tenth_scene:
    scene circle_background:
        zoom 2

    show kirill_image

    show zhenya_image
    

    Kirill "{i}Ах, какая красота! Ну как так можно было в один миг взять и наполнить мою жизнь смыслом?{/i}"


    Kirill "{i}Всё, надо перестать пялиться{/i}"

    scene circle_background:
        zoom 2

    # show kirill_image at left:
    #     zoom 0.5

    show teacher_image:
        zoom 0.5

    Teacher "Здравствуйте, дети. Сегодня мы продолжаем изучать разработку игр."
    Teacher "На сегодня задание очень простое, второе занятие ведь. Чтобы играть, нужно зайти в игру, поэтому сегодня будем учиться делать стартовое меню. Приступайте!"

    return

label eleventh_scene_first_first:
    scene circle_background:
        zoom 2

    show kirill_image

    Kirill "А этот ботаник не такой уж и бесполезный."

    hide kirill_image

    show teacher_image:
        zoom 0.5

    Teacher "Есть такие кто всё сделал?"

    hide teacher_image

    hide teacher_image

    show lesha_image at right:
        zoom 0.3

    Lesha "Как? 0_0"

    hide lesha_image

    show zhenya_image

    Zhenya "(проявляет интерес)"

    show kirill_image

    Kirill "ААооаоаааао она на меня ПОСМОТРЕЛАААА."

    Kirill "Мне надо быстрее изучить эту разработку игр, пока у меня сердце не разорвалось от счастья."

    hide zhenya_image

    hide kirill_image

    show teacher_image:
        zoom 0.5

    Teacher "Хорошо, сейчас посмотрю и можете идти."

    $ save_choice_sit_with_choice = 1

    return

label eleventh_scene_first_second:
    scene circle_background:
        zoom 2

    show kirill_image

    show gleb_image at right:
        zoom 1

    Kirill "Слушай, это, конечно, всё хорошо, что ты сам почти задание сделал и мне ничего не надо делать, но я решил, что это не моё."

    Kirill "Я, наверное, пересяду….вон к тому парню"

    hide gleb_image

    show oleg_image at right:
        zoom 0.5

    Kirill "Он выглядит как человек, у которого в голове есть что-то кроме скучной информатики."

    Kirill "Да, по правде говоря, у него её вообще в голове нет."

    hide oleg_image

    show gleb_image at right:
        zoom 1

    Gleb "Это не просто информатика, это разработка игр."

    Gleb "Программирование, в крайнем случае."

    Kirill "Прощай."

    hide gleb_image

    show oleg_image at right:
        zoom 0.5

    Kirill "Привет, я подсяду?"

    Oleg "Что-то ты не очень похож на девочку в радужной кофте."

    Oleg "Ну ладно. Меня зовут Олег, но друзья зовут играть меня в баскетбол, я тут из-за мамы оказался."

    Kirill "О, какое совпадение, я тоже. Я Кирилл, кстати."

    $ save_choice_sit_with_choice = 2

    return

label eleventh_scene_second_first:
    scene circle_background:
        zoom 2

    show kirill_image

    show oleg_image at right:
        zoom 0.5

    Oleg "Слушай, может ну его?"
    
    Oleg "Чё-то вообще мутное. Погнали в бравл лучше?"

    Kirill "Да, погнали"

    $ save_choice_sit_with_choice = 2

    return

label eleventh_scene_second_second:
    scene circle_background:
        zoom 2

    show kirill_image

    show oleg_image at right:
        zoom 0.5

    Kirill "Слушай, я наверное порешаю."

    Oleg "Как хочешь. Я ничего делать не буду."

    Kirill "Я тогда к тому парню в очках пересяду."

    Oleg "Всё, развод?"

    Kirill "Получается так."

    hide oleg_image

    show gleb_image at right:
        zoom 1

    Kirill "Привет, я подсяду?"

    Gleb "Подсесть ты бы мог, если бы уже сидел, а ты же сейчас стоишь, поэтому правильно сказать присяду."

    Kirill "{i}Ну что ещё я мог ожидать?{/i}"

    Kirill "{i}Ладно, надеюсь, что он всё будет делать, а я просто посижу.{/i}"

    Kirill "Хорошо. Меня Кирилл зовут, а тебя как?"

    Gleb "А меня Мефодий. Хахахахах вот это я пошутил. Я Глеб"

    $ save_choice_sit_with_choice = 1

    return

label eleventh_scene_third:
    scene circle_background:
        zoom 2

    Storyteller "Задания даются ему с трудом, но всё-таки даются, и в конечном счёте он выполняет их все."

    Storyteller "Кирилл - работяга." 
    
    Storyteller "В своё свободное время сидит и разбирает разработку игр, а в награду  за работу получает лишь зелёные рамки после заданий."

    Storyteller "Кирилл - молодец, будь как Кирилл"

    $ save_choice_sit_with_choice = 1

    return

label twelve_first:
    scene circle_background:
        zoom 2

    show teacher_image:
        zoom 0.5

    Teacher "Что ж, ребяты, сегодня все отлично поработали."

    Teacher "До следующей встречи"

    return

label twelve_second:
    scene home_background:
        zoom 1.7

    show mother_image

    show kirill_image

    Mother "Привет, программист. Ну, что, как занятие?"

    Kirill "Мам, я даже не знаю. Я всё время провёл за игрой с новым знакомым."

    Kirill "Мы с ним разговорились и это как будто мой человек. Нас даже обоих заставили туда пойти."

    Mother "….Не такое я ожидала услышать."

    Kirill "Ну, мам, пойми, эта разработка реально не моё."

    Kirill "Я пробыл на двух уроках и запомнил только имя нового знакомого, а понял ещё меньше."

    Kirill "Не удивительно, что у меня пропал интерес."

    Mother "…Может быть ты прав, но прошу, не руби с плеча, дай ещё один шанс хобби."

    Mother "Если им не воспользуешься, то что тогда делать, уйдёшь."

    Kirill "Хорошо, каждый достоин второго шанса."

    Storyteller "Кирилл действительно сел после разговора за решение задач с занятий и даже сидел дольше обычного,"
    
    Storyteller "но что бы он ни делал, какие бы ролики в интернете не смотрел, задания никак не решались, а осознание не приходило в голову. "

    Storyteller "Кирилл окончательно разочаровался в своём хобби и немного в себе..."  
    
    Storyteller "После того, как он всё обдумал, он подошёл к маме:"

    return

label thirteen_first_first:
    scene home_background:
        zoom 1.7

    show mother_image

    show kirill_image

    Mother "Привет, мужчина. В этот раз не всё так бесполезно?"

    Kirill "Прикинь, лёд тронулся. Я решил задание. Сам!"

    Mother "Ого, поздравляю. Счастливый ходишь последнее время тоже из-за задания?)"

    Kirill "Сегодня да. Вчера просто настроение хорошее было."

    Mother "Ладно, ладно. Потом отмазки нормальные придумаешь."

    Mother "Мой руки и за стол, я рыбную запеканку сделала."

    Kirill "Ну ма-а-ам"

    Mother "Что «ну мам»?"

    Kirill "Ничего, спасибо. Щас приду."

    hide Kirill

    Mother "{i}Странно, никогда не любил эту запеканку, а сейчас «спасибо».{/i}"

    Mother "{i}Точно что-то на этих занятиях с ним происходит.{/i}"

    return

label thirteen_first_second:
    scene home_background:
        zoom 1.7

    show mother_image

    show kirill_image

    Mother "Ну что, покорил сердце рыжей бестии?"

    Kirill "Ма-а-ам, ну ты вообще капец."

    Kirill "Нет, не покорил, но зато я САМ сделал задание, прикинь."

    Mother "Красавчик, что сказать? И даже номер не спросил?"

    Kirill "Ма-а-ам"

    Mother "Ладно – ладно. И сам не дал?)"

    Kirill "Ой, всё, я пошёл."

    Mother "Да чё ты сразу? Ты уже совершил главную ошибку: рассказал о симпатии своей маме, а мама у тебя девушка такая, интересующаяся."

    Mother "Главное, чтобы ты с ней в разговоре чего-нибудь не ляпнул, поэтому когда станете общаться ближе, сразу мне скажи, хорошо?"

    Kirill "Да уже не охота чего-то."

    Mother "Как хочешь. Всё равно по тебе всё пойму"

    return

label thirteen_second_first:
    scene home_background:
        zoom 1.7

    show mother_image

    show kirill_image

    Kirill "Мам, всё, я железно решил, что это было моё последнее занятие"

    Mother "А как же девочка?"

    Kirill "Какая девочка?"

    Mother "Да, значит на кружке её увидел. Ты думаешь, что я ничего не понимаю и не замечаю?"

    Mother "Светится он, радостный весь ходит. Ты когда после первого занятия пришёл, в прихожей можно было свет не включать."

    Mother "И ещё это «я же мужчина, если сказал, то сделаю». Ты посуду тоже говоришь, что помоешь, но почему-то вечером эту гору я убираю."

    hide mother_image

    Kirill "{i}Вау, просто вау. А я думал, что не заметит никто{/i}"

    show mother_image

    Kirill "…Да знаешь, чтобы заполучить её внимание, надо этого Лёшу переумничать, а как я это смогу сделать, если я ничего не понимаю?"

    Kirill "Ещё домашки неадекватно тяжёлые."

    Kirill "Я решил пойти по пути наименьшего сопротивления и вместо наслаждения от любви, решил довольствоваться хорошим другом"

    Mother "Я тебе ничего сейчас не скажу насчёт друга или той девочки, но то, что ты упускаешь возможность с детства освоить перспективную профессию, ты должен сам понимать."

    return

label thirteen_second_second:
    scene home_background:
        zoom 1.7

    show mother_image

    show kirill_image

    Kirill "Мам, всё, я железно решил, что это было моё последнее занятие"

    Mother "А как же девочка?"

    Kirill "…Да знаешь, чтобы заполучить её внимание, надо этого Лёшу переумничать, а как я это смогу сделать, если я ничего не понимаю?"

    Kirill "Ещё домашки неадекватно тяжёлые."

    Kirill "Я решил пойти по пути наименьшего сопротивления и вместо наслаждения от любви, решил довольствоваться хорошим другом"

    Mother "Я тебе ничего сейчас не скажу насчёт друга или той девочки, но то, что ты упускаешь возможность с детства освоить перспективную профессию, ты должен сам понимать."

    return

label fourteen_first:
    scene circle_background:
        zoom 2

    show teacher_image:
        zoom 0.5

    Kirill "{i}Делает и сдаёт задание{/i}"

    Teacher "Молодец, всё правильно."

    Teacher "Иди, помоги Лёше с Женей."

    hide teacher_image

    show kirill_image

    show lesha_image at right:
        zoom 0.3

    Kirill "Чем вам помочь?"

    Lesha "Знаешь, ничем не надо. Мы сами справимся. Чуть попозже, но сами."

    hide lesha_image

    show zhenya_image

    Zhenya "А мне нужна помощь. Пошли отойдём?"

    hide zhenya_image

    Kirill "{i}ааоаоооаоа вдвоём ))){/i}"

    show zhenya_image

    Kirill "Пошли"

    Zhenya "Я помню, что ты тоже сидел вначале и ничего не делал, а сейчас уже сам без помощи выполняешь задания."

    Zhenya "Как так? Я и телефон искала под столом у тебя, и ещё что-нибудь, но нет, сидишь и сам пишешь."

    Zhenya "В чём твой секрет?"

    Kirill "Да знаешь, кто-то кхм кхм что-то мне понравилось на этих занятиях, в душу запало, вот и мотивация появилась."

    Kirill "Теперь сижу дома и вместо активных занятий бравлом, смотрю обучающие ролики, сам что-то пишу."

    Zhenya "Вау, ну ты внатуре псих) В хорошем плане))"

    hide zhenya_image

    Kirill "{i}аааааааааа она мне улыбается и кокетничает!!!{/i}"

    Kirill "{i}Главное в обоморок не упасть{/i}"

    show zhenya_image

    Kirill "Ну да, есть немного."

    Kirill "А ты что-то хотела сказать, раз отойти попросила?"

    Zhenya "Да. Ты знаешь, с этим Лёшей сидеть уже нет никакого удовольствия, а с тебя я давно удивляюсь..."

    Zhenya "...вроде нормальный парень, а сидишь один, ни с кем не общаешься."

    Zhenya "Толстовка у тебя прикольная. В общем, ты не против, если я к тебе подсяду?"

    hide zhenya_image

    Kirill "{i}Виу-виу, мы пожарные. Приехали тушить пожар в сердце{/i}"

    show zhenya_image

    Kirill "Отлич.. хорошая, то есть обычная идея, давай! Я не против"

    Zhenya "Хахаха, а ты смешной."

    Zhenya "Я Женя"

    Kirill "А я самый счастливый человек на данный момент"

    Zhenya "Что?"

    Kirill "Да это….. мем такой."

    Zhenya "Хорошо, кириешка, пошли, объяснять мне будешь)"

    return

label fourteen_second:
    scene circle_background:
        zoom 2

    show kirill_image

    show gleb_image at right

    Kirill "Смотри, можно вместо этой конструкции воспользоваться методом и тогда можно будет убрать эти строчки."

    Kirill "А ещё измени название переменной, потому что нынешнее не удовлетворяет правилам."

    Gleb "Ого, и правда. Ты сильно прибавил в программировании за то время, что мы сидим вместе."

    Gleb "У тебя какая-то бешеная мотивация?"

    Kirill "Да. До 10 разрешат гулять, а не до 9."

    Kirill "Шутка."

    Kirill "Вот она моя мотивация сидит, смотрит, как Лёша задания за них двоих делает."

    Gleb "Ты серьёзно? Ты из-за неё в таком темпе разбираешь это всё?"

    Kirill "Ну да, а чё?"

    Gleb "Так у тебя нет шансов."

    Gleb "Вряд ли спустя столько времени она такая:"

    Gleb "«Так, парень, с которым я сижу уже больше месяца и нашла общий язык, я от тебя ухожу..."

    Gleb "...к мальчику, на которого в первый раз обратила внимания из-за того, что он ответил самый первый на вопросы нашей училки и научился программировать»."

    Kirill "Ну, это мы ещё посмотрим, мистер хейтер."

    Gleb "Если так произойдёт, то я выполняю твоё желание."

    Kirill "Ну, смотри, тебя никто за язык не тянул. Начинается урок."

    hide gleb_image

    show zhenya_image

    Zhenya "Привет"

    Kirill "ПпрРивет"

    hide zhenya_image

    show gleb_image at right

    Gleb "(молча в шоке)"

    hide gleb_image

    show zhenya_image

    Zhenya "Я помню, ты в начале как и я сидел и ничего не делал, потому что ничего не понимал..."

    Zhenya "...а сейчас уже настолько разбираться начал, что смог зазнайку Лёшу обойти."

    Kirill "Да что-то заинтересовало меня на занятиях, вот я чуть-чуть и начал разбираться"

    Zhenya "Ты молодец"

    hide zhenya_image

    Kirill "{i}ааоооааа молодец{/i}"

    show zhenya_image

    Zhenya "Знаешь, ещё этот Лёша такой лицемер"

    Kirill "Угу-угу, слушаю"

    Zhenya "Весь из себя такой крутой в программах этих, отвечал постоянно первый."

    Zhenya "Ты думаешь, что знает он много? Нифига подобного, гуглит он много."

    Zhenya "Серьёзно, самые быстрые пальцы на диком западе, а задания просто списывает."

    Kirill "Ах он какой, этот Лёша. …… А я всегда его ненавидел!"

    Zhenya "И есть за что!"

    hide zhenya_image

    Kirill "{i}ааааааа она со мной согласна!!!)))!)!!!{/i}"

    show zhenya_image

    Zhenya "Так, ладно, ближе к делу."

    Zhenya "Я не просто так подошла."

    Zhenya "Мне немного некомфортно сидеть с этим Лёшей, смотреть на его обманы, а про тебя я знаю..."

    Zhenya "что ты весь такой честный, сам добился своих знаний, хороший в общем."

    Zhenya "Поэтому….может сядем вместе?"

    hide zhenya_image

    Kirill "{i}Виу-виу, мы пожарные. Приехали тушить пожар в сердце{/i}"

    show zhenya_image

    Kirill "Отлич.. хорошая, то есть обычная идея, давай! Я не против"

    Zhenya "Ой, похоже свободного компьютера нет, видимо в сле.."

    Kirill "Как нет? Вот же, рядом со мной"

    Kirill "А Коля сейчас пойдёт.."

    hide zhenya_image

    show gleb_image at right

    Gleb "Глеб"

    hide gleb_image

    show zhenya_image

    Kirill "А Глеб сейчас пойдёт исправлять Лёшу. Так сказать превращать в человека. Да ведь, Глеб?"

    hide zhenya_image

    show gleb_image at right

    Gleb "(До сих пор в шоке) Да, давно хотел."

    Gleb "Мы с Кириллом так и думали, что он хитрит."

    hide gleb_image

    show zhenya_image

    Zhenya "Ну вот и хорошо. Я Женя"

    return

label second_ending:
    scene second_ending_background

    Storyteller "Теперь Кирилл и Женя сидят вместе. Он рад, она тоже."

    Storyteller "Конечно, ведь Кирилл – парень не промах, а он так её любит, что кошки молоко не так любят, как Кирилл Женю."

    Storyteller "Уже добавили друг друга в соцсетях, имеют общий диалог, но что-то мешает им поднять их общение на новый уровень."

    Storyteller "И спустя пару недель, посмотрев на ситуацию со стороны, до Кирилла дошло: в переписке она спрашивает как сделать то-то в программе, на занятиях тоже только о разработке игр говорят."

    Storyteller "А за это время он даже не узнал её знак зодиака, любимый цвет и как её собака мило спит на обуви."

    Storyteller "Одним словом: он ей нужен был лишь для того, чтобы легко решать задания и лучше разобраться в разработке игр, а на него, как на личность, ей всё равно."

    Storyteller "На самом деле не удивительно, ведь девочкам не нужны ходячие энциклопедии, пусть даже эти энциклопедии перспективные."

    Storyteller "Девочкам нужен тот, кто может поддержать любой разговор, а не только по одной тематике, будет уделять ей много внимания, замечать любую стрижку, даже подравнивание кончиков, и хвалить маник без намёков на это."

    Storyteller "(Если серьёзно, то для каждой девочки этот список свой, но что точно не нравится никому, так это если парень душнила, коим и стал наш подопечный Кирилл)."

    Storyteller "Поняв это, Кирилл прекратил такое общение и уже на следующем занятии подтвердил свои домыслы насчёт истинных намерений Жени: она села к Глебу."

    Storyteller "Начал думать о том, чтобы бросить кружок, забить на это программирование и вернуться к друзьям и своему пролежню на диване, но за то время, пока он добивался её, разработка игр понравилась ему, он поистине загорелся этим."

    Storyteller "Теперь он получает удовольствие не от нового выбитого героя или достижения высокого ранга, а когда успешно составляет программу, после пары-тройки часов, проведённых за ней."

    Storyteller "Кирилл думает остаться до 11, а потом с 1 курса совмещать учёбу в университете и работу на фрилансе."

    Storyteller "Девушки теперь не интересуют Кирилла, друзья практически тоже."

    Storyteller "Интерес представляет лишь оффер, но до него надо ещё пару лет в таком же темпе попахать…"

    return

label first_ending:
    scene first_ending_background

    Storyteller "Кирилл, наслушавшись советов от нового знакомого, не стал доучиваться до «бесполезного» 11 класса и пошёл за ним в самую известную шарагу своего города."

    Storyteller "Поначалу всё было шоколадно: новые прикольные люди, можно было стрелять сигарету даже у преподавателей, да и красивых девочек хоть отбавляй, а не 1 на всю группу!"

    Storyteller "Так он и доучился, не зная горя (кроме постоянных разборок и пивного живота)."

    Storyteller "Нашёл ту самую, свою ненаглядную, с которой живёт и снимает квартиру."

    Storyteller "Жизнь идёт своим чередом: он доставляет продукты, она же работает в доставке."

    Storyteller "Они в этом плане редкие – работают по специальности."

    Storyteller "Иногда срываются на выходных к друзьям, иногда друг на друга."

    Storyteller "Так бы всё и продолжалось, если бы не одно но:"

    Storyteller "Каждый раз, когда Кирилл с девушкой собирались с друзьями потусить, каждый раз, когда выезжали куда-то на природу..."

    Storyteller "или просто друзья звали поподтягиваться, а точнее попотягивать пару другую бутылок, у него в голове возникал ряд вопросов:"

    Storyteller "«А в нужном ли месте я нахожусь?"

    Storyteller "Нравятся ли мне люди, что окружают меня, по-настоящему?»"

    Storyteller "Ну и главное: «Правильно ли тогда я поступил, когда пошёл по пути наименьшего сопротивления?"

    Storyteller "Щас бы был программистом и какие никакие деньги получал, а если бы развивался, то ой как припеваючи бы жил»."

    Storyteller "Так и не дают ему покоя эти вопросы, на которые, чем старше он становится, тем всё больше склоняется ответить – нет..."
    
    return