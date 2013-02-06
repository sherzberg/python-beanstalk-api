from .base import Base

class Release(Base):
    def __get__(self, repository_id=None, revision=None, is_diff=False, page=1, per_page=10):
        url =''
        return self._do_get(url)
