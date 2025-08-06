from itertools import chain
from functools import total_ordering


class AvgGradeMixin:
    @property
    def avg_grade(self):
        grades = list(chain.from_iterable(self.grades.values()))
        return round(sum(grades) / len(grades), 1) if grades else 0.0


@total_ordering
class CompareMixin:
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.avg_grade == other.avg_grade
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.avg_grade < other.avg_grade
        return NotImplemented
