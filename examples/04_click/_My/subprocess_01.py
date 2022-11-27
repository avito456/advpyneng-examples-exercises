import subprocess

result = subprocess.run('ls') # Возвращает код возврата
result1 = subprocess.run(['ls', '-ls']) # Команда с параметрами
result2 = subprocess.run('ls -ls *.py', shell=True) # Команда с wildcard-выражениями

# Получение результата выполнения команды
result3 = subprocess.run(['ls', '-ls'], stdout=subprocess.PIPE) # Стандартный вывод
result4 = subprocess.run(['ls', '-ls'], stdout=subprocess.PIPE, encoding='utf-8') # Стандартный поток вывода
result5 = subprocess.run(['ls', '-ls'], stdout=subprocess.DEVNULL, encoding='utf-8') # Отключение вывода

# Работа со стандартным потоком ошибок
result6 = subprocess.run(['ping', '-c', '3', '-n', 'a'], stderr=subprocess.PIPE, encoding='utf-8')

# Примеры использования модуля
def ping_ip(ip_adress):
    """
    Примеры использования модуля
    """
    reply = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8']
                           , stdout=subprocess.PIPE
                           , stderr=subprocess.PIPE
                           , encoding='UTF-8')
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stderr


print('----------------')
result_ip, message_ip = ping_ip('8.8.8.8')
print(message_ip)
print('----------------')




#print(result)