# -BOT-TG

### Инструкция по запуску телеграм-бота через Docker

**Требования**
1. Установленный Docker
2. Убедитесь, что ваш бот запускается локально

**Алгоритм запуска**
1. в терминале введите команду: **pip freeze >> requirements.txt** - создание файла, где хранятся все библиотеки использующиеся в программе ТГ-бота
2. в терминале введите команду: **sudo docker build.** - создание докер-контейнера
3. в терминале введите команду: **sudo docker images** - просмотр созданных докер-образов, необходимо скопировать IMAGE ID
4. в терминале введите команду: **sudo docker run -d IMAGE ID** - запуск докер-контейнера
5. в терминале введите команду: **sudo docker ps** - чтобы убедиться, что ваш докер-контейнер создан

**Проверка бота**
1. перейдите в ваш ТГ-Бот и проверьте работу

