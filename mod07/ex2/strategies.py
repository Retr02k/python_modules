from abc import ABC, abstractmethod
from ex0.creatures import Creature

class BattleStrategy(ABC):
    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self):
        self.attack()
    
    def is_valid(self, creature: Creature):
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self):
        