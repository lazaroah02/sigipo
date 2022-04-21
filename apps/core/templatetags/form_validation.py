from django.template import Library

register = Library()


@register.filter(name="add_attr")
def add_attribute(field, css):
    attrs = {}
    definition = css.split(",")

    for attr in definition:
        if ":" not in attr:
            attrs["class"] = attr
        else:
            key, val = attr.split(":")
            attrs[key] = val

    return field.as_widget(attrs=attrs)
