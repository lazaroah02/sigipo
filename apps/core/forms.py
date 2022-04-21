from django.forms import ModelForm


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
