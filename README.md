# calculate shape area

Проект библиотеки для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам.

## Установка

1. Установите `uv` (если ещё не установлен):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
2. Создайте виртуальное окружение и активируйте его:
   ```bash
   uv venv
   source .venv/bin/activate
   ```
3. Установите зависимости из `uv.lock` файла:
   ```bash
   uv sync
   ```
## Запуск тестов
Для запуска тестов и генерации html отчета необходимо воспользоваться командой:
   ```bash
   pytest --html=report.html
   ```
Результаты тестирования будут сохранены в файл `report.html`

## Использование
   ```python
from shapes import Circle, Triangle, calculate_area

c = Circle(5)
print(c.area())   # Площадь круга

t = Triangle(3, 4, 5)
print(t.area())   # Площадь треугольника
print(t.is_right())  # Проверка треугольника на равные стороны (True)

print(calculate_area(c))
print(calculate_area(t))
   ```
