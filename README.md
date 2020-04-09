# TaskD2_10
 Для работы необходимо установить модуль sentry-sdk
 
 pip3 install --upgrade 'sentry-sdk[bottle]==0.14.3'
 
 Необходимо определить переменную окружения SENTRY_DSN.
 
 Локально запускается на порту 8080
 http://localhost:8080/ - Проверка работы сервера.
 http://localhost:8080/success - ответ 200 ОК
 http://localhost:8080/fail - Проверка отправки ошибки
 
