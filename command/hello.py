import command_system

def hello():
   message = 'Привет, друг!\nЯ новый чат-бот.'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте']
hello_command.description = 'Поприветствую тебя, кожаный уб**людак нинавижу тя ка*пец еще и запикали всё ууу'
hello_command.process = hello
