class Bird:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):

    def __init__(self, name, size, color, full):
        super().__init__(name, size)
        self.color = color

    # Переопределите метод describe().
    def describe(self):
        if
            return print(f'Попугай {self.name} — заметная птица, окрас её перьев — {self.color}, '
                         f'а размер — {self.size}. Интересный факт: попугаи чувствуют ритм, '
                         f'а вовсе не бездумно двигаются под музыку. Если сменить композицию, '
                         f'то и темп движений птицы изменится.')
        else:
            return super().describe(self)


class Penguin(Bird):

    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    # Переопределите метод describe().
    def describe(self):
        if super().describe(full=False):
            return print(f'Размер пингвина {self.name} из рода {self.genus} — {self.size}. '
                         f'Интересный факт: однажды группа геологов-разведчиков '
                         f'похитила пингвинье яйцо, и их принялась преследовать вся стая, '
                         f'не пытаясь, впрочем, при этом нападать. Посовещавшись, '
                         f'похитители вернули птицам яйцо, и те отстали.')
        else:
            return super().describe(self)


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
kesha.describe()
kowalski.describe(True)
