from enum import Enum


class RiskProbabilty(Enum):
    """
    Characterizes the likelihood that a particular risk arises during a particular project

    Some arbitrary values are defined here and the upper bounds chosen

    * RARE = 0% < x ≤ 5%
    * UNLIKELY = 5% < x ≤ 300%
    * POSSIBLE = 30% < x ≤ 50%
    * LIKELY = 50% < x ≤ 80%
    * CERTAIN = 80% < x ≤ 100%
    """

    RARE = 0.05
    UNLIKELY = 0.3
    MODERATE = 0.5
    LIKELY = 0.8
    CERTAIN = 1


class RiskImpact(Enum):
    """Defines how a particular risk can affect the progress of a project"""

    HIGH = 1
    MEDIUM = 0.5
    LOW = 0.1


class RiskScore(Enum):
    VERY_HIGH = range(80, 101)  # 80% - 100%
    HIGH = range(50, 80)  # 50% - 79%
    MODERATE = range(30, 50)  # 30% - 49%
    LOW = range(0, 30)  # 0 - 29%

    @classmethod
    def get_risk_score(cls, value):
        for val in cls:
            if value in val.value:
                return val


class RiskCounterMeasure(Enum):
    REDUCE = "REDUCE"
    PREVENT = "PREVENT"
    ACCEPT = "ACCEPT"
    TRANSFER = "TRANSFER"

    @classmethod
    def list_allowed_values(cls):
        return list(map(lambda c: c.value, cls))
