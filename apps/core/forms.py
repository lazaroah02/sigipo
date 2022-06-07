from django.forms import ModelForm, TypedChoiceField


class ChoiceField(TypedChoiceField):
    def __init__(
        self,
        choices=(),
        empty_label=None,
        required=True,
        widget=None,
        label=None,
        initial=None,
        help_text=None,
        empty_value=None,
        *args,
        **kwargs,
    ):

        # prepend an empty label if it exists (and field is not required!)
        if not required and empty_label is not None:
            choices = tuple([(None, empty_label)] + list(choices))  # pragma: no cover

        super().__init__(
            choices=choices,
            required=required,
            widget=widget,
            label=label,
            initial=initial,
            help_text=help_text,
            empty_value=empty_value,
            *args,
            **kwargs,
        )


class ModelForm(ModelForm):
    """Class to handle form validation."""

    def is_valid(self) -> bool:
        """
        Returns if form is valid and adds css clases according to field valid state.
        """
        result = super().is_valid()
        if not result:
            for key, field in self.fields.items():
                if "class" in field.widget.attrs:
                    if key in self.errors:
                        field.widget.attrs["class"] = (
                            "is-invalid " + field.widget.attrs["class"]
                        )
                    else:
                        field.widget.attrs["class"] = (
                            "is-valid " + field.widget.attrs["class"]
                        )
        return result
