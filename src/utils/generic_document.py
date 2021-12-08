import time
from abc import ABC, abstractmethod


class AbstractBaseDocument(ABC):
    def __init__(self, doc_title) -> None:
        super().__init__()
        self.doc_title = doc_title
        self.time_created = time.ctime()
