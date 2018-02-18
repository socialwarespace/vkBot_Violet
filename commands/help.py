import command_system


def help():
    message = ('Сейчас доступны следующие команды:\n'
               '"Привет" - Поприветствую тебя;\n'
               '"Список серий" - Покажу серии и их названия;\n'
               '"Фото" - Случайная картинка с нашей группы;\n'
               '"# серия" - Отправлю указанную серию в нашей озвучке\n'
               '"Отключить бота" - Не буду тебе мешать;\n'
               '"Включить бота" - Если захочешь вновь поговорить;\n\n'
               'Я еще учусь, но скоро смогу гораздо больше!')
    return message, ''


hello_command = command_system.Command()

hello_command.keys = ['помощь', 'help', 'ты умеешь']
hello_command.description = 'Помощь'
hello_command.process = help