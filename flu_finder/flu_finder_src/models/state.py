from dataclasses import dataclass, field
from typing import List
# from models.case import Case  // Will uncomment when class is created

@dataclass
class State:
  name: str
  cases: List[Case] = field(default_factory=list)

  # Adds a case to the State
  def add_case(self, case: Case):
    self.cases.append(case)

  # Calculates total out breaks and total flock size for the State
  def calculate_totals(self):
    total_outbreaks = len(self.cases)
    total_flock_size = sum(case.flock_size for case in self.cases)
    return total_outbreaks, total_flock_size

  # Prints the number of total outbreaks and total flocks size for the state
  def get_summary(self) -> str:
    total_outbreaks, total_flock_size = self.calculate_totals()
    return f"{self.name}: {total_outbreaks} outbreaks, {total_flock_size} total flock affected"

  # Returns cases from the State with a specific flock type
  def filter_cases_by_flock_type(self, flock_type: str) -> List[Case]:
    return [case for case in self.cases if case.flock_type == flock_type]