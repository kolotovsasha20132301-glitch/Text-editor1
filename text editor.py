import tkinter as tk
from tkinter import ttk
import threading
import re

t9_map = {
    '2': 'абвг',
    '3': 'дежз',
    '4': 'ийкл',
    '5': 'мноп',
    '6': 'рсту',
    '7': 'фхцч',
    '8': 'шщъы',
    '9': 'ьэюя',
}

char_to_digit = {ch: dg for dg, chs in t9_map.items() for ch in chs}

word_list_raw = """
аббревиатура аббитуриент абонемент абонент абориген абсолютный абстрактный авангард авиапочта автобиография
автобус автомобиль авторитет агентство агрессия адаптация адвокат адекватный администратор администрация адрес
адъютант ажиотаж академия акваланг аквариум аккомпанемент аккомпанировать аккумулятор аккуратный акселерат
аксессуар активный алгоритм аллегория аллея алфавит альманах альтернатива алюминий амфитеатр аналитический аналогия
аннотация аннулировать аномалия ансамбль антагонизм антитеза антология антонимы апартаменты апелляция апельсин
аплодисменты аппарат аппаратура аппетит аппликация аптека арбуз аргумент арена аристократ арматура артиллерия
архипелаг архитектор ассистент ассортимент ассоциация асфальт атмосфера аттестат аудитория Б багаж багряный бадминтон
байдарка бакалавр баклажан бактерия баланс балет балкон балласт баллотироваться банальность баррикада барьер баскетбол
бассейн бастион бахрома безвкусный беззаветный беллетристика беречь беседовать бетонный библиография библиотека билет
бинокль биография бирюзовый благовонный благодарю благодаря тому что благородный благородство блестеть блистать богатство
богатырь бок о бок болото большинство бордовый брошюра будущее В в виду обстоятельств в насмешку в силу то что вагон
варежки вверху вдвоем вдвоём вдруг везде Великая Отечественная война великолепный велогонки велосипед вернисаж верование
вертикально ветер ветеран веять взаимный видимо-невидимо видит винегрет влево вместительный вмиг внезапно внизу воззрение
возражение воин вокзал волей-неволей воображение вопросительное воробей ворона ворота воротник восклицательное восток
восточнославянский вперед впечатляющий впоследствии вправо всегда всеобъемлющий вскоре вследствие того что встрепенуться
второстепенные втроём въезжать выразительный выровненный вьюга Г газета газификация галерея гараж гардероб генерал гениальный
гений герой гигант гигантский гимнастика гирлянда гитара горизонт город горячий гостиная гравюра гражданин гражданственность
грамматическая основа графика грейпфрут громадный группа гуманизм гуманный Д давным-давно двести дебаты дебют девиз девочка
девяносто дежурный декабрь декларация декоративный декорация делегат деликатес демократический депутат держит деятельный
диалог диапазон диафрагма диван дилетант диплом дипломат директор дискуссия дистанция для того чтобы до свидания доклад
дополнение дорога достоинство достопримечательность драгоценный Ё ёмкость Ж жеваный желанный желательный желать железо жечь
животное жюри З за границу забытьё заведующий завод завтра завтрак заглавие запад запечатлеть затеять заяц здание здесь
здоровье здравствуй(те) земляника знаменитый И идеал из-за из-под извините издалека изжелта-красный изобразить изредка
изумрудный иллюминация иллюстрация иллюстрированный иметь в виду инженер информировать искусственный искусный искусство
иссиня-черный истинный К кабинет кавалерия как будто календарь калитка каллиграфия канал кандидат каникулы капуста карандаш
карикатура карман карнавал карниз картина картон картофель карточка квадрат квартира квитанция класс классик кованный
коллектив коллекция колонна комбайн комбинат комендант комиссия комитет коммерсант композитор компонент компот компьютер
конвейер конверт конгресс консерватория контрабас конференция конфета концерт коньки корабль корзина корова корпорация
корректор космонавт космос костёр костюм косынка Кремль кровать кромешный кросс Л лаборатория ландшафт лауреат легенда
лейтенант лексика лестница лилипут лиловый лимон линейка лиственница лопата М магазин малина мало-помалу маляр мандарин
маневрировать маршрут масленица масса матч машина медицина медленный меньшинство меридиан месяц металл метро меценат мечта
миллиард миллион миниатюра митинг молодёжь молоко молоток монолог монополия монтаж мораторий морковь мороз Москва мужество
Н на глазок на днях на дом на лету на миг на память на протяжении на скаку на совесть на ходу на цыпочках назад налево
направо народ натюрморт не раз невиданный невосклицательное негодовать недосягаемый недоумевать нежданный ненавидеть неслыханный
несмотря на нечаянный ни разу никак никогда нисколечко ничуть О обед обелиск облако обращение обстоятельство объявление овощ
огонь огорчить огромный огурец одежда одиннадцать однажды однородные ожерелье окно октябрь омонимы опечалить определение
орех ориентироваться орнамент осина ослепительный отец отечество отовсюду отразить оттого что П пакет пальто памятник панорама
парашют паркет паром патриот педаль пейзаж пенал перила период периферия перрон перспектива песок пианино пилигрим пирог
платок платформа по двое по окончании по памяти по прибытии по совести победа побудительное повествовательное погода под силу
подвиг подлежащее подлинный подражать пожалуйста помидор помощь поражать поражение поразительный портрет портфель посетить
поскользнуться постамент постановление посуда потому что почерк почтальон правильный правительство прагматизм праздник
предварительный предложение президент президиум презирать прекратить прения преобразовать преодолеть препятствие
преследование претендовать претензия прецедент привередливый привет привилегия привыкать пригласить пригодиться приготовить
прийти приказать приключение прилежный присмотреться приспособить присутствовать причина приятный пролог прототип профессия
профиль пунктуация путешествие пшеница пьедестал пьеса Р работа ракета рапорт расписание распространённое рассвет рассказ
расстояние расстроить рассчитывать расцвет расчёт реальный регион регулировать режиссер резиденция резолюция реликвия ремень
ремонт репетиция республика реставрация реформа рисунок ровесник Родина Россия ружьё румяный русский рюкзак С с налету
с разбегу с тем чтобы саквояж салат салфетка салют сапог сатира сбить сверстник светофор свидетельство свиной свиристель
свобода священный сгиб сдать сегодня сезон сейчас секрет секретарь семафор семинар серенада сертификат серьёзный сеять
сжать сигнал силуэт симфония синонимы синтаксис сирень ситуация сиять сказуемое слева словосочетание слышит смотрит собака
солдат соловей солома соревноваться сорока состязание состязаться спартакиада спасибо специальность спортсмен справа
справедливый стадион старательно стереотип стеречь стипендия стоматолог стремиться суффикс съезд Т тавтология талант талантливый
таран тарелка таять телевизор телеграмма телефон терраса территория тетрадь типография товарищ топор торопиться точь-в-точь
традиция трактор трамвай транслировать тревога тренер тренироваться трибуна триста троллейбус труженик У удивлять улица
университет унифицировать урожай утрамбовать участвовать ученик учитель Ф фантазия фасоль февраль федерация фестиваль
фильмотека фиолетовый фонетика фонетический фотоаппарат футбол Х хозяин хоккей хороший хризантема хронология Ц центнер цитата
Ч чемодан чемпион чернила четверг четыреста чехол чувство чувствовать Ш шевелиться шинель шоколад шоссе шофёр штукатур Э
экземпляр экономить экскаватор экскурсия эксперимент экспериментировать эмигрант эмоция эпидемия эпилог эскалатор Ю юный Я
яблоко язык январский январь
"""

word_list = set()
for line in word_list_raw.strip().splitlines():
    words = re.findall(r'[а-яё]+', line.lower())
    for word in words:
        word_list.add(word)
        word_list.add(word.capitalize())
        word_list.add(word.upper())

phrases = [
    "потому что", "в силу того что", "вследствие того что", "для того чтобы",
    "в виду обстоятельств", "в насмешку", "бок о бок", "на скаку", "на лету",
    "на ходу", "на цыпочках", "на совесть", "на миг", "на память", "на глазок",
    "на протяжении", "впоследствии", "вдвоем", "вдвоём", "втроём", "по двое",
    "по окончании", "по прибытии", "по памяти", "по совести", "с разбегу", "с налету", "с тем чтобы", "точь-в-точь"
]
for phrase in phrases:
    word_list.add(phrase)
    word_list.add(phrase.capitalize())

def t9_to_words(digits):
    if not digits.isdigit():
        return []
    candidates = ['']
    for d in digits:
        if d not in t9_map:
            continue
        letters = t9_map[d]
        candidates = [c + letter for c in candidates for letter in letters]
    matches = [word for word in candidates if word in word_list]
    return matches[:10]

def correct_word(word):
    word = word.lower().strip(".,?!")
    if not word.isalpha():
        return word
    if word in word_list:
        return word
    best = word
    max_match = 0
    for w in word_list:
        if len(w) != len(word):
            continue
        match = sum(1 for a, b in zip(w, word) if a == b)
        if match > max_match and abs(len(w) - len(word)) <= 1:
            max_match = match
            best = w
    return best if max_match >= len(word) - 1 else word

punctuator = None

def load_punctuation_model():
    global punctuator
    try:
        from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
        tokenizer = AutoTokenizer.from_pretrained("EugeneMan/punctuation-restoration-russian")
        model = AutoModelForTokenClassification.from_pretrained("EugeneMan/punctuation-restoration-russian")
        punctuator = pipeline(
            "token-classification",
            model=model,
            tokenizer=tokenizer,
            aggregation_strategy="simple"
        )
    except Exception as e:
        status_var.set(f"Ошибка пунктуации: {e}")
    status_var.set("Готово. Введите цифры или текст.")

def punctuate_text(text):
    if not punctuator:
        return text.capitalize()
    try:
        result = punctuator(text.lower())
        output = text.lower()
        offset = 0
        for entity in result:
            label = entity['entity_group']
            start = entity['start'] + offset
            end = entity['end'] + offset
            if label == 'PERIOD':
                output = output[:end] + '.' + output[end:]
                offset += 1
            elif label == 'COMMA':
                output = output[:end] + ',' + output[end:]
                offset += 1
            elif label == 'QUESTION':
                output = output[:end] + '?' + output[end:]
                offset += 1
            elif label == 'EXCLAMATION':
                output = output[:end] + '!' + output[end:]
                offset += 1
        output = re.sub(r'\s+([.,?!])', r'\1', output)
        return output.strip().capitalize()
    except Exception:
        return text.capitalize()

root = tk.Tk()
root.title("T9-клавиатура с автозаполнением и пунктуацией")
root.geometry("600x500")

input_var = tk.StringVar()
status_var = tk.StringVar(value="Загрузка модели пунктуации...")

input_entry = ttk.Entry(root, textvariable=input_var, font=("Segoe UI", 14), justify='center')
input_entry.pack(pady=10, padx=20, fill='x')

suggestion_frame = ttk.LabelFrame(root, text="Варианты")
suggestion_frame.pack(pady=10, padx=20, fill='x')

suggestions = []
for i in range(3):
    label = ttk.Label(suggestion_frame, text="", font=("Segoe UI", 11), foreground="blue", cursor="hand2")
    label.pack(pady=2)
    suggestions.append(label)

output_text = tk.Text(root, height=6, font=("Segoe UI", 12), wrap='word', state="disabled")
output_text.pack(pady=10, padx=20, fill='both', expand=True)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

punct_button = ttk.Button(button_frame, text="Расставить знаки", command=lambda: apply_punctuation())
punct_button.pack(side='left', padx=5)

clear_button = ttk.Button(button_frame, text="Очистить", command=lambda: clear_all())
clear_button.pack(side='left', padx=5)

status_label = ttk.Label(root, textvariable=status_var, foreground="gray", font=("Segoe UI", 9))
status_label.pack(pady=5)


def on_input_change(*args):
    text = input_var.get().strip()
    if not text:
        return
    if text.isdigit():
        words = t9_to_words(text)
        for i, label in enumerate(suggestions):
            if i < len(words):
                word = words[i]
                label.config(text=word)
                label.bind("<Button-1>", lambda e, w=word: insert_word(w))
            else:
                label.config(text="")
                label.unbind("<Button-1>")
    else:
        for label in suggestions:
            label.config(text="")
            label.unbind("<Button-1>")


def insert_word(word):
    current = output_text.get(1.0, tk.END).strip()
    if current and not current.endswith(' '):
        current += ' '
    output_text.config(state='normal')
    output_text.insert(tk.END, word + ' ')
    output_text.config(state='disabled')
    input_var.set('')
    output_text.see(tk.END)


def apply_punctuation():
    text = output_text.get(1.0, tk.END).strip()
    if not text:
        return
    words = text.split()
    corrected = [correct_word(w) for w in words]
    corrected_text = ' '.join(corrected)
    punctuated = punctuate_text(corrected_text)
    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, punctuated)
    output_text.config(state='disabled')


def clear_all():
    input_var.set('')
    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.config(state='disabled')
    for label in suggestions:
        label.config(text="")
        label.unbind("<Button-1>")


input_var.trace_add("write", on_input_change)

threading.Thread(target=load_punctuation_model, daemon=True).start()

root.mainloop()
