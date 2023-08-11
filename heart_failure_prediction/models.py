from django.db import models


class Patient(models.Model):
    """Patient parameters for Heart Failure prediction."""
    gender = models.PositiveSmallIntegerField(
        verbose_name='Your gender',
        help_text='Choose your gender',
        choices=[
            (0, 'female'),
            (1, 'male')
        ]
    )
    age = models.PositiveSmallIntegerField(
        verbose_name='Age',
        help_text='Write your age'
    )
    cp = models.BooleanField()
    chol = models.BooleanField()

    def __str__(self):
        return self.name + ' Heart Failure prediction'
