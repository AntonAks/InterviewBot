# InterviewBot


![](readmefiles/Image1.png)

InterviewBot - це програма на Python для проведення інтерв'ю з кандидатами. Вона дозволяє створювати питання, записувати відповіді кандидатів і зберігати результати інтерв'ю.

## Встановлення

Спочатку склонуйте цей репозиторій на свій комп'ютер:

```
git clone https://github.com/AntonAks/InterviewBot.git
```
Перейдіть у директорію проекту:
```
cd InterviewBot
```

Активуйте ваше віртуальне середовище Poetry:
```
poetry shell
```

Встановіть залежності:
```
poetry install fastapi, uvicorn, asyncpg,
```

## Використання
Запустіть основний файл програми:
```
uvicorn main:app --reload
```
Перейдіть за адресою http://localhost:8000/docs у вашому веб-браузері.

Тепер ви можете створювати питання, проводити інтерв'ю та переглядати результати через інтерфейс користувача.
