# internship

## Тестовое задание
Тестовое задание доступно по ссылке: https://docs.google.com/document/d/181G7wIkK_haGnaDW10m4sDcfhibkuwFbK8fuG4bq6Fk/edit?tab=t.0

## Решение тестового задания:

### Тестовое задание 1
Вариант 1: После echo вводим числа
```bash
echo 1,-2,77,-4,0 | python task1.py
```
Вариант 2: вводим числа вручную
```bash
python task1.py 
# 2,6,-5,7,-10,1
```


### Тестовое задание 2
Активируем виртуальное окружение:
```bash
python -m venv venv
# mac/linux
source env/bin/activate
# windows
source venv/Scripts/activate

pip install -r requirements.txt
python task2.py
```