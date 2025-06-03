from django import template

register = template.Library()

@register.simple_tag
def pagination_range(current_page, total_pages, delta=2):
    """
    Returns a list of page numbers and ellipses for smart pagination.
    """
    if total_pages <= 1:
        return []

    range_with_dots = []
    last_page = 0

    for num in range(1, total_pages + 1):
        if num == 1 or num == total_pages or abs(num - current_page) <= delta:
            if last_page + 1 != num:
                range_with_dots.append('…')
            range_with_dots.append(num)
            last_page = num

    return range_with_dots
