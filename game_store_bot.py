
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
import telebot
from telebot import types
import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Наш адрес')
    item2 = types.KeyboardButton('Наш сайт')
    item3 = types.KeyboardButton('Контакт')
    item4 = types.KeyboardButton('Товары от SteelSeries')
    item5 = types.KeyboardButton('Доставка на дом')
    markup.add(item1,item2,item3,item4,item5)
    bot.send_message(message.chat.id,'Приветствуем вас {0.first_name} в нашем магазине SteelSeries'.format(message.from_user,
                                                                                                        bot.get_me()),
                                                                                                        parse_mode='html',reply_markup=markup)
    bot.send_photo(message.chat.id,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdmkN8HZM7TcaBrriWamAu9oo6gIdlLvLeRQ&usqp=CAU')    


@bot.message_handler(content_types=['text'])
def magazine_message(message):
    if message.text=='Наш адрес':
        bot.send_location(message.chat.id,'42.8699174','74.5961398')
        bot.send_message(message.chat.id,'Бразилия/Фавеллы/15квартал')

    elif message.text=='Наш сайт':
        bot.send_message(message.chat.id,'https://de.steelseries.com/')

    elif message.text=='Контакт':
        bot.send_contact(message.chat.id,'0703097702','SteelSeries')
    elif message.text =='Доставка на дом':
        bot.send_message(message.chat.id,'Сам забери посылку чувак,чо лень ходить,в твоем возрасте я с Сибири воду тоскал ,лучше заказывай такси🚕')

    elif message.text=='Товары от SteelSeries':
        markup = types.InlineKeyboardMarkup(row_width=6)
        button1 = types.InlineKeyboardButton('Клавиатуры',callback_data='key')
        button2 = types.InlineKeyboardButton('Мышки',callback_data='mouse')
        button3 = types.InlineKeyboardButton('Наушники',callback_data='ear')
        button4 = types.InlineKeyboardButton('Микрофоны',callback_data='micro')
        markup.add(button1,button2,button3,button4)
        bot.send_message(message.chat.id,'Выберите товар для покупки',reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def freddy(call):
    if call.message:
        if call.data =='key':
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton('Razer',callback_data='raz')
            button2 = types.InlineKeyboardButton('Bloody',callback_data='blo')
            button3 = types.InlineKeyboardButton('LogeTech',callback_data='log')
            markup.add(button1,button2,button3)
            bot.send_message(call.message.chat.id,' Oт какой компании нужна клавиатура',reply_markup=markup)
        if call.data =='raz':
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton('Razer BlackWidow V3',callback_data='black_widow')
            button2 = types.InlineKeyboardButton('Razer Ornata V2 ',callback_data='ornata')
            button3 = types.InlineKeyboardButton('Razer Cynosa V2',callback_data='cynosa')
            button4 = types.InlineKeyboardButton('Razer Huntsman Mini',callback_data='mini')
            markup.add(button3,button4,button2,button1)
            bot.send_message(call.message.chat.id,'Выберит версию клавиатуры Razor',reply_markup=markup)
        elif call.data=='black_widow':
            bot.send_message(call.message.chat.id,'Имя, с которого все началось, возвращается, чтобы подтвердить свое господство. Почувствуйте разницу с Razer BlackWidow V3 - первой и самой легендарной механической игровой клавиатурой, оснащенной новыми, улучшенными функциями, включая всемирно известные переключатели.')
            bot.send_message(call.message.chat.id,'Данная клавиатура имеется в наличии и стоимость 8 499сомов ')
            bot.send_photo(call.message.chat.id,'https://static.razer.ru/169749/blackwidow-bg-for-legacy-new-products-mobile.jpg')
        elif call.data=='ornata':
            bot.send_message(call.message.chat.id,'Обновленная игровая клавиатура с гибридными механическо-мембранными переключателями, многофункциональным цифровым колесиком, клавишами управления медиа и подсветкой Razer Chroma RGB.')
            bot.send_message(call.message.chat.id,'Данная клавиатура имеется в наличии и стоимость 5 599сомов ')
            bot.send_photo(call.message.chat.id,'https://www.memorykings.pe/files_contenidos/upload/images/MK027901DESCRIP(1).jpg')
        elif call.data=='mini':
            bot.send_message(call.message.chat.id,'Открой для себя новое измерение смертоносности с Razer Huntsman Mini — 60% игровой клавиатурой с ультрасовременными оптическими переключателями Razer™ Optical Switches. Максимальная портативность, идеально подходящая для изящных сетапов. Пришло время испытать молниеносный отклик в нашем самом компактном форм-факторе.')
            bot.send_photo(call.message.chat.id,'https://assets2.razerzone.com/images/razer-huntsman-mini/razer-huntsman-mini-2020-OGimg.jpg')
            bot.send_message(call.messahe.chat.id,'Данная клавиатура имеется в наличии и стоимость 7 199сомов ')
        elif call.data=='cynosa':
            bot.send_message(call.message.chat.id,'Раскрась свое погружение в игру настоящей подсветкой с Razer Cynosa V2 — игровой RGB клавиатурой. Смотри как оживает настраиваемая подсветка каждой клавиши пока  играешь в игры с интегрированной Chroma подсветкой, и наслаждайся игровым процессом от которого никогда не сможешь отказаться.')
            bot.send_photo(call.message.chat.id,'https://upweek.ru/wp-content/uploads/2020/12/Razer-Cynosa-V2_OGimage-1200x630-1.jpg')
            bot.send_message(call.message.chat.id,'Данная клавиатура имеется в наличии и стоимость 4 890сомов ')
        if call.data=='mouse':
            bot.send_photo(call.message.chat.id,'https://gomeovet.ru/images/articles/domashnie_krysy2.jpg')
            bot.send_photo(call.message.chat.id,'https://geekhero.ru/wp-content/uploads/2014/11/77711917_4278666_aboi_na_temu_filmi__48.jpg')
            bot.send_message(call.message.chat.id,'Есть только такая')

        if call.data=='ear':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item2 = types.InlineKeyboardButton('Без проводные',callback_data='bezprov')
            markup.add(item2)
            bot.send_message(call.message.chat.id,'Выберите наушники',reply_markup=markup)
        elif call.data =='bezprov':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Наушники  Razor с микрофоном/накладные/mini jack 3.5m/черные',callback_data='somic')
            item2 = types.InlineKeyboardButton('Наушники A4Tech Bloody G300',callback_data='rgb')
            markup.add(item1,item2)
            bot.send_message(call.message.chat.id,'Выберите type наушникa',reply_markup=markup)
        elif call.data=='rgb':
            bot.send_photo(call.message.chat.id,'https://object.pscloud.io/cms/cms/Uploads/30_4040.jpg')
            bot.send_message(call.message.chat.id,'Наушники A4Tech Bloody G3004908 (К')
            bot.send_message(call.message.chat.id,'Цена 7 500 ₽')
        elif call.data=='somic':
            bot.send_photo(call.message.chat.id,'https://hyperpc.ru/images/catalog/accessories/headsets/razer/nari_ultimate/content/razer-nari-ultimate-content-1-1.jpg')
            bot.send_message(call.message.chat.id,'Представляем Razer Nari Ultimate с технологией Razer HyperSense — беспроводную игровую гарнитуру оснащенную интеллектуальной технологией тактильной вибрации, разработанную компанией Lofelt™, эта технология преобразует звуковые сигналы в динамическую сенсорную обратную связь в режиме реального времени.')
            bot.send_message(call.message.chat.id,'Цена 18 190 ₽')
bot.polling(non_stop=True)

