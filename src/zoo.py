"""Класс Zoo, демонстрирующий композицию и управление коллекцией."""

from typing import List, Optional
from src.animal import Animal


class Zoo:
    """
    Класс Zoo, управляющий коллекцией животных.
    """

    def __init__(self, name: str, location: str) -> None:
        """
        Инициализация зоопарка.
        
        Аргументы:
            name: Название зоопарка
            location: Локация зоопарка
        """
        self._name = name
        self._location = location
        self._animals: List[Animal] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return self._location

    @property
    def animals(self) -> List[Animal]:
        # Возвращаем копию, чтобы снаружи не ломали внутренний список
        return list(self._animals)

    def add_animal(self, animal: Animal) -> None:
        """Добавить животное в зоопарк."""
        if animal is None:
            raise ValueError("animal cannot be None")
        self._animals.append(animal)

    def remove_animal(self, animal: Animal) -> bool:
        """
        Удалить животное из зоопарка.

        Возвращает True, если удалили, иначе False.
        """
        try:
            self._animals.remove(animal)
            return True
        except ValueError:
            return False

    def get_animal_by_name(self, name: str) -> Optional[Animal]:
        """Найти первое животное по имени (если у Animal есть атрибут name)."""
        for a in self._animals:
            if getattr(a, "name", None) == name:
                return a
        return None

    def count_animals(self) -> int:
        """Количество животных в зоопарке."""
        return len(self._animals)

    def clear(self) -> None:
        """Удалить всех животных."""
        self._animals.clear()

        """Вернуть количество животных (для тестов)."""
        return len(self._animals)

    def find_animal_by_name(self, name: str) -> Optional[Animal]:
        """Найти животное по имени (метод для тестов)."""
        return self.get_animal_by_name(name)

    def get_all_sounds(self) -> List[str]:
        """Вернуть список звуков всех животных."""
        sounds = []
        for animal in self._animals:
            if hasattr(animal, "make_sound"):
                sounds.append(animal.make_sound())
        return sounds
    
    def get_species_count(self, species):
        return len([animal for animal in self._animals if animal.species == species])

    def count_animals(self) -> int:
        """Количество животных в зоопарке."""
        return len(self._animals)

    def clear(self) -> None:
        """Удалить всех животных."""
        self._animals.clear()

    def get_animal_count(self):
        return len(self._animals)