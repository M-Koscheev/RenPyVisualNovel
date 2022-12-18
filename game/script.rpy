init:
    # Определение персонажей игры.
    define Kirill = Character('Кирилл')
    define Mother = Character('Мама')
    define Teacher = Character('Учитель')
    define Zanuda = Character('Зануда')
    define Clown = Character('Весельчак')
    define Villain = Character('Лёша')
    define Crush = Character("Крашиха")

    image gg = "GG.png"

    image mother_image = "mother.png"
    image crush_image = "crushiha.png"
    image teacher_image = "teacher.png"
    image nerd_image = "nerd.png"
    image clown_image = "clown.png"
    image villain_image = "villain.png"
    
    image home_background = "home_background.png"
    image street_background = "street_background.png"
    image circle_background = "circle_background.png"

    default choice_sit_with = 0 # 1 = Nerd; 2 = Clown; 3 = With no one
    default tell_about_liked_girl_to_mom = 0 # 1 - lie 2 - say truth

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
        call eleventh_scene_first_choice
    elif choice_sit_with == 2:
        call eleventh_scene_first_choice # TODO
    elif choice_sit_with == 3:
        call eleventh_scene_first_choice # TODO

    return


label first_scene:
    scene home_background:
            zoom 1.7

    show gg at right:
        zoom 0.5

    show mother_image at left:
        zoom 0.35

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

    show gg at right:
        zoom 0.5
    
    Kirill "{i}Снова опять этот Лёша, в каждой бочке затычка. СыН мАмИноЙ ПодРуГи, конечно. Лёша выиграл это, Лёша сделал то, а ты оболтус. Угораздило же наших мам быть подругами.{/i}"

    scene home_background:
        zoom 1.7

    show gg at right:
        zoom 0.5

    show mother_image at left:
        zoom 0.35

    Mother "Ну так что, сходишь?"

    Kirill "Схожу, схожу. Но помни - только ради тебя. Мне эта идея изначально не нравится."

    return


label second_scene:
    scene street_background:
        zoom 1.5

    show gg:
        zoom 0.5

    Kirill "Ну зачем я согласился пойти на эту разработку? Щас все пацаны сидят в «Аппетитно и двоеточие», общаются, веселятся, а я как дурак дома поел и на автобус."

    Kirill "Ладно хоть всего пару раз так придётся съездить, а то через месяц я бы на стену лез от недостатка отдыха в крови."

    Kirill "О, а вот и моя остановочка."

    # черный экран конец сцены

    return
    
label third_scene:
    scene circle_background:
        zoom 2

    show gg at left:
        zoom 0.5

    Kirill "{i}А вот и она - Красная комната.{/i}"

    Kirill "Ну, привет всем. Особо меня не запоминайте, через 2 недели меня уже здесь не будет."

    Kirill "{i}Ладно, ради приличия можно и взглянуть на бедолаг.{/i}"
    
    # исправить изображение девушки
    show crush_image at right:
        zoom 0.5
    
    Kirill "{i}Это….что…это кто такое красивое создание из рая выпустил? Я даже не знаю от чего сейчас щурюсь: от её лучезарности или от того, что я запрокинул голову наверх и сейчас мне в глаза светят лампочки?{/i}"

    # Убрать надпись в голове и сделать это как надпись в имени героя
    Kirill "{i}Так, Кирилл, собери себя в руки, хватит кринжа наваливать. Встань нормально.{/i}"

    # second_part of third_scene

    scene circle_background:
        zoom 2

    show teacher_image:
        zoom 0.5

    Teacher "Здравствуйте, дети. Сегодня мы с вами начинаем курс: «Первую игру я сделал(а) в 16 лет»."

    Teacher "Не люблю затягивать, поэтому начинаем опросик, чтобы сразу понять кто разбирается, а кто из-под палки пришёл."

    Teacher "Разбейтесь на пары и решайте задания"

    # жесткий движ с тем как они пересаживаются

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

    show gg at left:
        zoom 0.5

    Kirill "{i}Естественно! Парень в очках, линзы которого толще монитора, он то мне и поможет с заданиями, да и прокачаться в программировании с ним легче будет, чтобы добиться мою ненаглядную.{/i}"

    Kirill "Привет, я подсяду?"

    show nerd_image at right:
        zoom 1

    Zanuda "Подсесть ты бы мог, если бы уже сидел, а ты же сейчас стоишь, поэтому правильно сказать присяду."

    Kirill "{i}Ну что ещё я мог ожидать? Ладно, надеюсь, что он всё будет делать, а я просто посижу.{/i}"

    Kirill "Хорошо. Меня Кирилл зовут, а тебя как?"

    Zanuda "А меня Мефодий."

    Zanuda "Хахахахах вот это я пошутил. Я Глеб."

    Kirill "Теперь будем сидеть вместе."

    Zanuda "Ага."

    return


label fourth_scene_second_choice:
    scene circle_background:
        zoom 2

    show gg at left:
        zoom 0.5

    Kirill "{i}Парень, который сделал скриншот рабочего стола, удалил все иконки и поставил его на фон?{/i}"

    Kirill "{i}Мой вариант! С ним хотя бы весело будет.{/i}"

    show clown_image at right:
        zoom 0.5

    Kirill "Привет, я подсяду?"

    Clown "Что-то ты не очень похож на девочку в радужной кофте."

    Clown "Ну ладно. Меня зовут Олег, но друзья зовут играть меня в баскетбол, а тут из-за мамы оказался."

    Kirill "О, какое совпадение, я тоже."

    Kirill "Я Кирилл, кстати. Теперь мы вместе."

    Clown "Сидим?"

    Kirill "Ну, как пойдёт)"

    return


label fourth_scene_third_choice:
    scene circle_background:
        zoom 2

    show gg at left:
        zoom 0.5

    Kirill "Ну и правильно. Сидеть ещё с кем-то, знакомиться, бе-е."

    Kirill "Тем более никто не будет мешать ботать =). Но и помогать тоже =( ."

    Kirill "Ладно, вижу цель, не вижу препятствий!"

    return


label fifth_scene:
    scene home_background:
            zoom 1.7

    show gg at right:
        zoom 0.5

    show mother_image at left:
        zoom 0.35

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

    show gg at right:
        zoom 0.5

    show mother_image at left:
        zoom 0.35

    Kirill "Нет, ты что? Смог бы я за раз в кого-то влю...кхм кхм всмотреться."

    Mother "Ну ладно. Знаешь, я тут подумала, если тебе совсем не понравилось, то чё я тебя буду мучить? Я же не тиран."

    Mother "Можешь больше никуда не ездить."

    Kirill "Да знаешь, я же мужчина, если сказал, что на пару занятий схожу ради тебя, значит пару занятий точно отхожу."

    Mother "Ой, какой у меня мужчи-ина растёт. Ну, иди руки мыть, щас есть наложу."

    return


label sixth_scene_second_choice:
    scene home_background:
            zoom 1.7

    show gg at right:
        zoom 0.5

    show mother_image at left:
        zoom 0.35

    Kirill "Если честно, есть там одна девочка…"

    Mother "Ах, кто-то влюбился))))) Ну, рассказывай, какая она?"

    return


label seventh_scene:
    scene home_background:
            zoom 1.7

    show gg at right:
        zoom 0.5

    show mother_image at left:
        zoom 0.35

    Kirill "Мам, это нечто. 160 см, под 90 кг, брови сросшиеся, рот держит постоянно открытым."

    Mother "Серьёзно?"

    Kirill "Да ладно, угораю. На самом деле я даже не совсем запомнил какая она."

    Kirill "Как только мой взгляд упал на неё, я смог отвести его только через силу. Помню только, что у неё рыжие волосы."

    return


label eighth_scene:
    scene home_background:
            zoom 1.7

    show gg at right:
        zoom 0.5

    show mother_image at left:
        zoom 0.35

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

    show gg at left:
        zoom 0.5

    show nerd_image at right:
        zoom 1

    Zanuda "О, ты всё-таки пришёл? Я уж думал, что для тебя это слишком трудно и ты не захочешь что-либо делать."

    Zanuda "Ну ладно, садись, я уже пару заданий решил."

    Kirill "Но урок же начинается через 5 минут 0_0"

    Zanuda "А, да я просто гулял по кабинету и увидел, что у преподавательницы документ с заданиями открыт."

    Kirill "Её компьютер выключен."

    Zanuda "Ну, я там…"

    Kirill "...подошёл к ней и выпросил задания, чтобы удовлетворить свою дотошную душонку?"

    Zanuda "Что ты докопался? Вообще всё не так было…"

    Zanuda "Ладно, всё так и было. Но я не дотошный! Слышишь? Я не дотошный и вот тебе 4 причины почему."

    Zanuda "Первая – …"

    # В голове
    Kirill "{i}Надо ли оно мне было? Повеселился, молодец. Начинается занятие.{/i}"

    return


label nineth_scene_second_choice:
    scene circle_background:
        zoom 2

    show gg at left:
        zoom 0.5

    show clown_image at right:
        zoom 0.5

    Clown "О, здарова. А я всё думал, когда же ты появишься? Ну, чё, как оно?"

    Kirill "Всё ништяк, мээн."

    Clown "Айоу, мээн."

    Kirill "Мэээн"

    Clown "Мэээээн. Начинается занятие."
    
    return


label nineth_scene_third_choice:
    scene circle_background:
        zoom 2

    show gg at left:
        zoom 0.5

    Kirill "Здесь снова опять не занято. Даже грустно как-то. Начинается занятие."

    return


label tenth_scene:
    scene circle_background:
        zoom 2

    show gg at left:
        zoom 0.5

    show crush_image at right:
        zoom 0.5
    
    Kirill "{i}Ах, какая красота! Ну как так можно было в один миг взять и наполнить мою жизнь смыслом?{/i}"

    Kirill "{i}Всё, надо перестать пялиться{/i}"

    scene circle_background:
        zoom 2

    show gg at left:
        zoom 0.5

    show teacher_image at right:
        zoom 0.5

    Teacher "Здравствуйте, дети. Сегодня мы продолжаем изучать разработку игр."

    Teacher "На сегодня задание очень простое, второе занятие ведь. Чтобы играть, нужно зайти в игру, поэтому сегодня будем учиться делать стартовое меню. Приступайте!"

    return


label eleventh_scene_first_choice:
    scene circle_background:
        zoom 2

    show gg at left:
        zoom 0.5

    Kirill "{i}А этот ботаник не такой уж и бесполезный.{/i}"

    scene circle_background:
        zoom 2

    show gg at left:
        zoom 0.5

    show nerd_image at left:
        zoom 1

    show teacher_image at right:
        zoom 0.33

    # жесткий движ с репликами кучи героев

    Teacher "Есть такие кто всё сделали?"

    Kirill "Да, мы."

    Villain "Как? 0_0"

    Crush "(проявляет интерес)"

    Kirill "{i}ААооаоаааао она на меня ПОСМОТРЕЛАААА. Мне надо быстрее изучить эту разработку игр, пока у меня сердце не разорвалось от счастья.{/i}"

    Teacher "Хорошо, сейчас посмотрю и можете идти."

    Kirill "Слушай, это, конечно, всё хорошо, что ты сам почти задание сделал и мне ничего не надо делать, но я решил, что это не моё. Я, наверное, пересяду….вон к тому парню"

    # ???
    Kirill "Он выглядит как человек, у которого в голове есть что-то кроме скучной информатики. Да, по правде говоря, у него её вообще в голове нет."

    Zanuda "Это не просто информатика, это разработка игр. Программирование, в крайнем случае."

    Kirill "Прощай."

    scene circle_background:
        zoom 2

    show gg at left:
        zoom 0.5

    show clown_image at left:
        zoom 1

    Kirill "Привет, я подсяду?"

    Clown "Что-то ты не очень похож на девочку в радужной кофте."

    Clown "Ну ладно. Меня зовут Олег, но друзья зовут играть меня в баскетбол, а тут из-за мамы оказался."

    Kirill "О, какое совпадение, я тоже."

    Kirill "Я Кирилл, кстати. Теперь мы вместе."

    return