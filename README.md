# MenuBot

Telegram бот - Для просмотра и редактирования меню.

### Взаимодействие с пользователем:

На любое сообщение от обычного пользователя бот выводит меню.

### Взаимодействие с админами:

Админ имеет доступ к командам:  
- `/edit` - добавить / удалить / изменить пункт меню.
- `/hire` - добавить админа
- `/fire` - удалить админа

Приглашение происходит через QR кода со ссылкой вида:  
`https://t.me/bot_name?start=invitation`  
где `invitation` — временный код приглашения.

Инициализация первого админа происходит через QR код выводимый в терминал.
