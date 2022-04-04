from django_filters.views import FilterView


class PaginationFilterView(FilterView):
    """FilterView with pagination."""

    paginate_by = 30
    extra_context: dict = None

    def get_context_data(self, *args, **kwargs) -> dict:
        """
        Save the url lookup filters to use it in the url links.
        <a href="?page={{ page_obj.next_page_number }}&{{ parameters }}">
            Next
        </a>
        """
        _request_copy = self.request.GET.copy()
        _request_copy.__mutable = True
        parameters = _request_copy.pop("page", True) and _request_copy.urlencode()
        context = super().get_context_data(*args, **kwargs)
        context["parameters"] = parameters
        num_pages = context["paginator"].num_pages
        current_page = context["page_obj"].number
        context["pagination_range"] = [
            page_number
            for page_number in range(current_page - 2, current_page + 2)
            if page_number >= 1 and page_number <= num_pages
        ]
        context |= self.extra_context
        return context
