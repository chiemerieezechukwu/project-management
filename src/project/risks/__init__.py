from .helpers import RiskCounterMeasure, RiskImpact, RiskProbabilty, RiskScore


class Risk:
    def __init__(self, name: str, risk_prob: int, risk_impact: int) -> None:
        self.risk_name = name
        self._risk_owner = None
        self._description = None
        self._counter_measure = None
        self.risk_probability = risk_prob  # a value between 0 and 1
        self.risk_impact = risk_impact  # a value between 0 and 1

    def get_risk_score(self):
        return RiskScore.get_risk_score(
            int(self.risk_probability * self.risk_impact * 100)
        )

    @property
    def risk_owner(self):
        return self._risk_owner

    def assign_risk_owner(self, value):
        self._risk_owner = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def counter_measure(self):
        return self._counter_measure

    def set_counter_measure(self, counter_measure: str):
        """counter_measure is a value to be chosen from the RiskCounterMeasure Enum"""
        allowed_values = RiskCounterMeasure.list_allowed_values()
        assert counter_measure.upper() in allowed_values, "%s is not in %s" % (
            counter_measure,
            allowed_values,
        )
        self._counter_measure = RiskCounterMeasure(counter_measure.upper())

    ##############################################################
    # FACTORY METHODS
    ##############################################################

    @classmethod
    def rare_probability_high_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.RARE.value
        risk_impact = RiskImpact.HIGH.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def rare_probability_medium_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.RARE.value
        risk_impact = RiskImpact.MEDIUM.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def rare_probability_low_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.RARE.value
        risk_impact = RiskImpact.LOW.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def unlikely_probability_high_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.UNLIKELY.value
        risk_impact = RiskImpact.HIGH.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def unlikely_probability_medium_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.UNLIKELY.value
        risk_impact = RiskImpact.MEDIUM.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def unlikely_probability_low_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.UNLIKELY.value
        risk_impact = RiskImpact.LOW.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def moderate_probability_high_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.MODERATE.value
        risk_impact = RiskImpact.HIGH.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def moderate_probability_medium_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.MODERATE.value
        risk_impact = RiskImpact.MEDIUM.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def moderate_probability_low_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.MODERATE.value
        risk_impact = RiskImpact.LOW.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def likely_probability_high_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.LIKELY.value
        risk_impact = RiskImpact.HIGH.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def likely_probability_medium_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.LIKELY.value
        risk_impact = RiskImpact.MEDIUM.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def likely_probability_low_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.LIKELY.value
        risk_impact = RiskImpact.LOW.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def certain_probability_high_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.CERTAIN.value
        risk_impact = RiskImpact.HIGH.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def certain_probability_medium_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.CERTAIN.value
        risk_impact = RiskImpact.MEDIUM.value
        return cls(risk_name, risk_prob, risk_impact)

    @classmethod
    def certain_probability_low_impact(cls, risk_name: str):
        risk_prob = RiskProbabilty.CERTAIN.value
        risk_impact = RiskImpact.LOW.value
        return cls(risk_name, risk_prob, risk_impact)
