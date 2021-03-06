from project.risks.helpers import RiskScore

class RiskMetaClass(type):
    pattern: str
    def __getattr__(cls, attr): ...
    ##############################################################
    # FACTORY METHODS
    ##############################################################
    def rare_probability_high_impact(cls, risk_name: str) -> "Risk": ...
    def rare_probability_medium_impact(cls, risk_name: str) -> "Risk": ...
    def rare_probability_low_impact(cls, risk_name: str) -> "Risk": ...
    def unlikely_probability_high_impact(cls, risk_name: str) -> "Risk": ...
    def unlikely_probability_medium_impact(cls, risk_name: str) -> "Risk": ...
    def unlikely_probability_low_impact(cls, risk_name: str) -> "Risk": ...
    def moderate_probability_high_impact(cls, risk_name: str) -> "Risk": ...
    def moderate_probability_medium_impact(cls, risk_name: str) -> "Risk": ...
    def moderate_probability_low_impact(cls, risk_name: str) -> "Risk": ...
    def likely_probability_high_impact(cls, risk_name: str) -> "Risk": ...
    def likely_probability_medium_impact(cls, risk_name: str) -> "Risk": ...
    def likely_probability_low_impact(cls, risk_name: str) -> "Risk": ...
    def certain_probability_high_impact(cls, risk_name: str) -> "Risk": ...
    def certain_probability_medium_impact(cls, risk_name: str) -> "Risk": ...
    def certain_probability_low_impact(cls, risk_name: str) -> "Risk": ...

class Risk(metaclass=RiskMetaClass):
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
