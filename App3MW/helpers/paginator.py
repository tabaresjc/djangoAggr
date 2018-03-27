from django.core.paginator import Paginator, EmptyPage
from django.utils.translation import ugettext_lazy as _

DEFAULT_PAGINATOR_LIMIT = 10


class PaginationHelper(Paginator):
    """
    Overrides some of functionalities of the core paginator.

    Should be used when the total number of objects, and the page number is already known.
    """

    def __init__(self, object_list, page, limit, total=None, **kwargs):
        self.total = None

        if isinstance(total, (int, long)):
            self.total = total

        if isinstance(page, (int, long)):
            self.number = page

        super(PaginationHelper, self).__init__(object_list, limit, **kwargs)

    @property
    def count(self):
        """
        Returns the total number of objects, across all pages.
        """
        if self.total:
            return self.total

        return super(PaginationHelper, self).count

    def get_items(self):
        """
        Returns the Page object for the given object list.
        """
        if self.total:
            return self._get_page(self.object_list[:self.total], self.number, self)
        else:
            raise Exception(_('This class must be instantiated with total and page'))

    @classmethod
    def get_paginator_items(cls, object_list, page=1, limit=DEFAULT_PAGINATOR_LIMIT, total=None, **kwargs):
        paginator = cls(object_list, page, limit, total=total, **kwargs)

        if total:
            return paginator.get_items()
        else:
            try:
                items = paginator.page(page)
            except EmptyPage:
                items = paginator.page(paginator.num_pages)

            return items
