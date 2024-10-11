# Strategy Interface
from agent.Agent import Agent

class AgentStrategy(ABC):
    @abstractmethod
    def play(self, grid:grille, agent:Agent):
        pass

class CowardStrategy(AgentStrategy):
    def play(self, grid:grille, agent:Agent):
        pass

class BoldStrategy(AgentStrategy):
    def play(self, grid:grille, agent:Agent):
        pass

class PatientStrategy(AgentStrategy):
    def play(self, grid:grille, agent:Agent):
        pass

class RandomStrategy(AgentStrategy):
    def play(self, grid:grille, agent:Agent):
        pass



