import os
import time
# import colorama
# from colorama import init, Fore, Back, Style


stage = 0  # Этап
language = ('RUS', 'ENG') # Список всевозможных языков
user_language = [] # Выбранный пользователем язык

# You can add or remove modules from this list
modules = ('wheel', 'pandas', 'scipy', 'telebot', 'matplotlib', 'seaborn', 'keras', 'tensorflow', 'statsmodels', 'plotly', 'bokeh', 'spacy', 'gensim', 'nltk', 'dash', 'pygame', 'pillow', 'jmespath', 'requests', 'simplejson', 'emoji', 'dateutil.parser', 'progress', 'tqdm', 'ipython', 'homeassistant', 'flask', 'beautiful', 'discord')

RUS = ('Добро пожаловать в Установщик Модулей для Python!\nВ программе ' + str(len(modules)) + ' модулей.', 'Выберите опцию:', '1. Приступить к установке модулей', '2. Помощь', '3. Сменить язык', '4. Выйти', 'Нажмите enter..', 'Данная программа была созданна для простой установки модулей Python.\nВ программе вы можете включить как автоматическую установку всех модулей, так и установить нужные модули вручную.\n', 'Спасибо за использование моей программы!\n','Количество модулей:', 'Выберите тип установки:', '1. Автоматическая установка +обновить pip', '2. Установка модулей вручную', 'Отмена', '2. Обновить pip', 'Все модули установленны!', 'Модуль установлен', 'Pip обновлен!\n', 'Модуль НЕ установлен', 'Установка завершена! Выберите действие:', 'Продолжить установку', 'Вернуться в меню', 'Закрыть программу')

ENG = ('Welcome to the Python Module Installer!\nThe program has ' + str(len(modules)) + ' modules', 'Select option:', '1. Start installing modules', '2. Help', '3. Change language', '4. Exit', 'Press enter..', 'This program was created for easy installation of Python modules.\nIn the program, you can enable automatic installation of all modules, or install the necessary modules manually.\n', 'Thanks for using my program!', 'Number of modules:', 'Select installation type:', '1. Automatic installation +Update pip', '2. Installing modules manually', 'Cancel', '2. Update pip', 'All modules installed!', 'Module installed!', 'Pip updated!\n', 'Error: Module NOT installed', 'Installation completed! Select an action:', 'Continue installation', 'Back to menu', 'Close program')


# -------- Функции

def func_language(): # ----- Функция выбора языка
    l = 0
    func_stage = 0
    print('\n\nSelect language:')
    while func_stage == 0:
        try:
            print(str(l + 1) + ".", language[l])
            l += 1
        except IndexError:
            print()
            l = 0
            func_stage = 1
            while func_stage == 1:
                try:
                    select_l_num = int(input('(Enter the number) ->'))
                    if select_l_num <= 0:
                        print('Error: Incorrect Value!\n')
                    else:
                        select_l_num -= 1
                        selected_lang = language[select_l_num]
                        return selected_lang
                except IndexError:
                    func_stage = 1
                    print('Error: Incorrect Value!\n')
                except ValueError:
                    func_stage = 1
                    print('Error: Incorrect Value!\n')

def func_mod_download(): # ----- Функция начала установки модулей
    l = 3
    func_stage = 0
    while func_stage == 0:
        print('\n\n' + user_language[9], len(modules))
        print(user_language[10])
        print(user_language[11])
        print(user_language[12])
        print('3. ' + user_language[13] + '\n')
        func_stage = 0.5
        while func_stage == 0.5:
            select = str(input('->'))
            
            if select == '1': # --- Автоматическая установка модулей
                os.system('pip install update')
                os.system('python.exe -m pip install --upgrade pip')
                print(user_language[17])
                time.sleep(1.5)
                for i in modules:
                    x = os.system('pip install ' + str(i))
                    if x == 0:
                        print('\n' + user_language[16] + ': ' + i + '\n\n')
                        time.sleep(0.8)
                    else:
                        print('\n' + user_language[18] + ': ' + i + '\n\n')
                        time.sleep(0.8)
                        
                time.sleep(2)
                print('\n\n' + user_language[19])
                print('1. ' + user_language[21])
                print('2. ' + user_language[22] + '\n')
                func_stage = 1
                while func_stage == 1:
                    select = str(input('->'))
                    
                    if select == '1':
                        func_stage = 999
                        return 1
                        
                    elif select == '2':
                        func_stage = 999
                        return 0
                    else:
                        print('Error: Incorrect Value!\n')
                        func_stage = 1
                
            elif select == '2': # --- Установка модулей вручную
                func_stage = 0.7
                while func_stage == 0.7:
                    print('\n\n')
                    print('1. ' + user_language[13])
                    print(user_language[14])
                    print('--------------------------------------------------')
                    l = 3
                    for i in modules:
                        print(str(l) + '. ' + str(i))
                        l += 1
                    print()
                    func_stage = 1
                    
                    while func_stage == 1:
                        select = str(input('->'))
                        try:
                            if select == '1':
                                func_stage = 0
                                print('\n\n')
                            
                            elif select == '2':
                                os.system('pip install update')
                                os.system('python.exe -m pip install --upgrade pip')
                                time.sleep(0.8)
                                
                                print('\n\n' + user_language[19])
                                print('1. ' + user_language[20])
                                print('2. ' + user_language[21])
                                print('3. ' + user_language[22] + '\n')
                                func_stage = 2
                                while func_stage == 2:
                                    select = str(input('->'))
                                    
                                    if select == '1':
                                        func_stage == 0.7
                                    
                                    elif select == '2':
                                        func_stage = 999
                                        return 1
                                    
                                    elif select == '3':
                                        func_stage = 999
                                        return 0
                                    
                                    else:
                                        print('Error: Incorrect Value!\n')
                                        func_stage = 2                                        
                        
                                else:
                                    print('Error: Incorrect Value!\n')                                
                            
                            elif int(select) > l or int(select) <= 0:
                                print('Error: Incorrect Value!\n')
                            
                            elif int(select) > 2 and int(select) <= l:
                                selected_mod_num = (int(select) - 3)
                                selected_mod = modules[selected_mod_num]
                                
                                x = os.system('pip install ' + selected_mod)
                                if x == 0:
                                    print('\n' + user_language[16] + ': ' + selected_mod + '\n\n')
                                    time.sleep(0.8)
                                else:
                                    print('\n' + user_language[18] + ': ' + selected_mod + '\n\n')
                                    time.sleep(0.8)
                                print('\n\n' + user_language[19])
                                print('1. ' + user_language[20])
                                print('2. ' + user_language[21])
                                print('3. ' + user_language[22] + '\n')
                                func_stage = 3
                                while func_stage == 3:
                                    select = str(input('->'))
                                    
                                    if select == '1':
                                        func_stage = 0.7
                                    
                                    elif select == '2':
                                        func_stage = 999
                                        return 1
                                    
                                    elif select == '3':
                                        func_stage = 999
                                        return 0
                                    
                                    else:
                                        print('Error: Incorrect Value!\n')
                                        func_stage = 3
                        
                                else:
                                    print('Error: Incorrect Value!\n')
                                
                        except IndexError:
                            print('Error: Incorrect Value!\n')
                        except ValueError:
                            print('Error: Incorrect Value!\n')                        
                
            elif select == '3':
                func_stage = 999
                print()
                
            else:
                func_stage = 0.5
                print('Error: Incorrect Value!\n')
        

# -------- Начало программы

# Выбор языка
selected_in_func_lang = func_language()
if selected_in_func_lang == 'ENG':
    user_language = ENG
elif selected_in_func_lang == 'RUS':
    user_language = RUS
stage == 0

# -------- Начало программы (Для пользователя)

while stage == 0:
    print(3 * '\n' + user_language[0])
    stage = 0.5
    while stage == 0.5:
        print(user_language[1])
        print(user_language[2]) # 1. Приступить к установке модулей
        print(user_language[3]) # 2. Помощь
        print(user_language[4]) # 3. Сменить язык
        print(user_language[5] + '\n') # 4. Выход
        stage = 1
        while stage == 1:
            menu_select = str(input('->'))
            if menu_select == '1': # --- 1. Приступить к установке модулей
                y = func_mod_download()
                if y == 0:
                    print(user_language[8])
                    time.sleep(1.2)
                    stage = 999
                    break
                else:
                    stage = 0.5
                    print('\n\n')
    
            elif menu_select == '2': # --- 2. Помощь
                print()
                print(user_language[7])
                input(user_language[6])
                print('\n\n')
                stage = 0.5
    
            elif menu_select == '3': # --- 3. Сменить язык
                print()
                selected_in_func_lang = func_language()
                if selected_in_func_lang == 'ENG':
                    user_language = ENG
                elif selected_in_func_lang == 'RUS':
                    user_language = RUS
                print('\n\n')
                stage = 0.5
    
            elif menu_select == '4': # --- 4. Выход
                print(user_language[8])
                time.sleep(1.2)
                stage = 999
                break
    
            else:
                print('Error: Incorrect Value!\n')