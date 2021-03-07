from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

support_ids = [
    1648372036,
    558671635,
    868965709,
]

'''
Эржан: 1648372036
Айдана: 558671635
Ширин: 868965709
'''