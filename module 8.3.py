class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        if not self.__is_valid_vin(self.__vin):
            raise IncorrectVinNumber("Некорректный тип vin номер или неверный диапазон для vin номера")
        if not self.__is_valid_numbers(self.__numbers):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров или неверная длина номера")

    # __is_valid_vin
    # Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
    # если передано не целое число. (тип данных можно проверить функцией isinstance).
    # Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
    # если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
    # Возвращает True, если исключения не были выброшены.
    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")

        if vin < 1000000 or vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        return True
    # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
    # если передана не строка. (тип данных можно проверить функцией isinstance).
    # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
    # переданная строка должна состоять ровно из 6 символов.
    # Возвращает True, если исключения не были выброшены.
    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")

        return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')