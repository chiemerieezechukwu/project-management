from typing_extensions import Self

from project.risks.helpers import RiskScore

class Risk:
    risk_name: str
    def __init__(self, risk_name: str, probability: int, impact: int) -> None: ...
    def get_risk_score(self) -> RiskScore | None: ...
    @property
    def risk_owner(self): ...
    @risk_owner.setter
    def risk_owner(self, value) -> None: ...
    def assign_risk_owner(self, value) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value) -> None: ...
    @property
    def probability(self) -> int: ...
    @probability.setter
    def probability(self, value: int): ...
    @property
    def impact(self) -> int: ...
    @impact.setter
    def impact(self, value: int): ...
    @property
    def counter_measure(self): ...
    def set_counter_measure(self, counter_measure: str): ...
    ##############################################################
    # FACTORY METHODS
    ##############################################################
    @classmethod
    def rare_probability_high_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def rare_probability_medium_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def rare_probability_low_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def unlikely_probability_high_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def unlikely_probability_medium_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def unlikely_probability_low_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def moderate_probability_high_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def moderate_probability_medium_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def moderate_probability_low_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def likely_probability_high_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def likely_probability_medium_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def likely_probability_low_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def certain_probability_high_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def certain_probability_medium_impact(cls, risk_name: str) -> Self: ...
    @classmethod
    def certain_probability_low_impact(cls, risk_name: str) -> Self: ...
