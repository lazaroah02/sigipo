from django.template import Library
from django.utils.html import format_html

register = Library()


@register.simple_tag(takes_context=True)
def create_header_column(
    context: dict, field_to_sort: str, column_name: str, clases: str = "text-center"
) -> str:
    """
    Generate the column with the link to sort.
    """
    url_start = context["url_lookup"]
    print(url_start)
    order_up = True
    first_sort = True
    if f"o={field_to_sort}" in url_start:
        order_up = False
        first_sort = False
        url_start = url_start.replace(f"&o={field_to_sort}", "")
        url_start = url_start.replace(f"o={field_to_sort}", "")
    if f"o=-{field_to_sort}" in url_start:
        first_sort = False
        url_start = url_start.replace(f"&o=-{field_to_sort}", "")
        url_start = url_start.replace(f"o=-{field_to_sort}", "")
    url_start = (url_start + "&") if url_start != "" else ""
    print(url_start)
    return format_html(
        """
        <th class="column-sorted {classes}">
            <div>
                {column_name}
                <div class="sort-options {show_sort}">
                    <a href="?{url_start}o={order}{field_to_sort}" role="button" title="{ordering_text}"><i class="fa-solid fa-sort{sort_direction}"></i></a>
                </div>
                <div class="sort-options">
                    <a href="?{url_start}" class="{hide_cancel}" role="button" title="Quitar del orden"><i class="fa-solid fa-ban"></i></a>
                </div>
            </div>
        </th>""",
        url_start=url_start,
        order="" if order_up else "-",
        sort_direction="" if first_sort else "-up" if not order_up else "-down",
        field_to_sort=field_to_sort,
        column_name=column_name,
        ordering_text=f"Ordenar por {column_name}" if first_sort else "Alternar orden",
        classes=clases,
        hide_cancel="hidden" if first_sort else "",
        show_sort="show" if not first_sort else "",
    )
