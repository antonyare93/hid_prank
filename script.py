import time

def idle_cursor(seconds):
    for i in range(seconds << 1):
        print('|' if i & 1 == 0 else ' ', end='\r')
        time.sleep(0.5)

def write_text(text):
    for i, char in enumerate(text):
        print(text[:i+1] + '|', end='\r')
        time.sleep(0.05)
    print(' ' * (len(text) + 2), end='\r')
    print(text)

def loading_bar(total_length):
    for i in range(total_length):
        bar = '|' + '=' * i + ' ' * (total_length - i - 1) + '|'
        print(bar + (' OK!' if i == total_length - 1 else ''), end='\r')
        time.sleep(0.01)

# Configuración
LEN = 50

# Ejecución
idle_cursor(2)
write_text('execute connection to server 168.131.202.196:1337')
time.sleep(1)
print('\nEstablishing connection to server 168.131.202.196:1337...')
loading_bar(LEN)
time.sleep(2)
print('\n\nConnection established!')
idle_cursor(1)

# Secuencia de descargas
downloads = ['Keylogger', 'FileEncoder', 'FileEncrypter', 'Ransomware script', 'Password decryptor']
write_text('download system_breaker.exe')
for item in downloads:
    loading_bar(LEN)
    print(f'\n{item} downloaded')

idle_cursor(4)
write_text('execute system_breaker.exe')

# Secuencia de activación
actions = ['System breached!', 'Keylogger activated', 'FileEncoder activated', 
           'FileEncrypter activated', 'Ransomware script running...', 
           'Password decryptor running...', 'Files encrypted', 'Files decrypted',
           'Files deleted', 'Files recovered', 'Files deleted', 
           'All passwords decrypted and sent to server']

for action in actions:
    loading_bar(LEN)
    print(f'\n{action}')

# Secuencias largas
write_text('compromise all the systems in the network')
loading_bar(LEN * 4)
print('\nAll system machines were compromised')

write_text('delete all backups')
loading_bar(LEN * 4)
print('\nAll backups were deleted')

# Mensaje final
msgs = [
    '!!==========================================================================================================================!!',
    '||=============================================THIS MACHINE IS COMPROMISED==================================================||',
    '||=============================================DO NOT TRY TO RESTORE THE FILES==============================================||',
    '||=============================================IF YOU TRY TO RESTORE THE FILES, THE SYSTEM WILL BE DESTROYED================||',
    '||=============================================DO NOT TRY TO RESTORE THE FILES==============================================||',
    '!!==========================================================================================================================!!'
]

for msg in msgs:
    write_text(msg)

idle_cursor(100)
