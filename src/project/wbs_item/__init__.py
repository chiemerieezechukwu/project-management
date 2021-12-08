class WBSItem:
    def __init__(self, work_item_name: str, start_date, duration: int) -> None:
        self.work_item_name = work_item_name
        self.start_date = start_date
        self.duration = duration
        self._status = None # 'ACTIVE', 'ON HOLD', 'COMPLETE' as possible values
        self._objective = None
        self._resource = None
        self._depends_on = None
        self._percent_complete = None