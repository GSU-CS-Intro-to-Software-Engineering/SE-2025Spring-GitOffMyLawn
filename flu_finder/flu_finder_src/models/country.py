from dataclasses import dataclass, field
from models.state import State

@dataclass
class Country:
    name: str
    states: dict[str, State] = field(default_factory=dict)

    # Add a State to Country
    def add_state(self, state: State):
        self.states[state.name] = state

    # Calculate the total number of outbreaks and total flocksize for the Country
    def calculate_totals(self):
      total_outbreaks = sum(state.calculate_totals()[0] for state in self.states.values())
      total_flock_size = sum(state.calculate_totals()[1] for state in self.states.values())
      return total_outbreaks, total_flock_size

    # Prints the number of total outbreaks and total flocks size for the Country
    def get_summary(self) -> str:
      total_outbreaks, total_flock_size = self.calculate_totals()
      return f"{self.name}: {total_outbreaks} total outbreaks, {total_flock_size} total flock affected."