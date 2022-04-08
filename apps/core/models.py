from django.db import models


class TimeStampedModel(models.Model):
    """
    A model to reuse the `created_at` and `updated_at` fields
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ! Skipped from coverage until used
class SingletonModel(models.Model):  # pragma: no cover
    """Model to handele single row models."""

    def delete(self, *args, **kwargs):
        """Avoids instance from being deleted."""
        pass

    @classmethod
    def load(cls):
        """Create an instance or returns the existing one."""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        """Save the instance without create new ones."""
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
