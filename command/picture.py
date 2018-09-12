import commands
import vkapi
import setting

def picture():
   # Получаем случайную картинку из паблика
   attachment = vkapi.get_random_wall_picture(-32015300, settings.access_token)
   message = 'Вот тебе картинка=))0)\nВ следующий раз я пришлю другую картинку.'
   return message, attachment

picture_command = command_system.Command()
picture_command.keys = ['коммент', 'комент', 'пикчу', 'скинь смешняшку', 'анекдот', 'скинь']
picture_command.description = 'Пришлю смешной скрин'
picture_command.process = get_picture
