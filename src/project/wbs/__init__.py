class WBS:
    def __init__(self) -> None:
        self._wbs_items = []
        self._percent_complete = None  # an aggregation of the % complete of the individual work items
        self._critical_path = None
        self._start_date = None
        self._finish_date = None
        self._consolidated_duration = None

    def get_critical_path(self):
        """calculate the critical path"""

    def add_wbs_item(self, wbs_item):
        self._wbs_items.append(wbs_item)
