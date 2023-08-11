from django.db import models


BINARY_CHOICES = [
    (1, 'Yes'),
    (0, 'No'),
]


class Patient(models.Model):
    """Patient parameters for lung cancer prediction."""
    name = models.CharField(
        max_length=150, verbose_name='Name', help_text='Write your name')
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
    smoking = models.PositiveSmallIntegerField(
        verbose_name='Smoking',
        help_text='Are you smoking? Yes/No',
        choices=BINARY_CHOICES)
    yellow_fingers = models.PositiveSmallIntegerField(
        verbose_name='Yellow fingers',
        help_text='Do you have yellow fingers? Yes/No',
        choices=BINARY_CHOICES)
    anxiety = models.PositiveSmallIntegerField(
        verbose_name='Anxiety',
        help_text='Do you feel anxiety? Yes/No',
        choices=BINARY_CHOICES
    )
    peer_pressure = models.PositiveSmallIntegerField(choices=BINARY_CHOICES)
    chronic_desease = models.PositiveSmallIntegerField(choices=BINARY_CHOICES)
    fatigue = models.PositiveSmallIntegerField(choices=BINARY_CHOICES)
    allergy = models.PositiveSmallIntegerField(choices=BINARY_CHOICES)
    wheezing = models.PositiveSmallIntegerField(choices=BINARY_CHOICES)
    alcohol_consuming = models.PositiveSmallIntegerField(
        verbose_name='Alcohol consuming',
        help_text='Do you drink alcohol? Yes/No',
        choices=BINARY_CHOICES
    )
    coughing = models.PositiveSmallIntegerField(choices=BINARY_CHOICES)
    shortness_of_breath = models.PositiveSmallIntegerField(
        verbose_name='Shortness of breath',
        help_text='Do you have shortness of breath? Yes/No',
        choices=BINARY_CHOICES
    )
    swallowing_difficulty = models.PositiveSmallIntegerField(
        verbose_name='Swallowing difficulty',
        help_text='Do you have swallowing difficulties? Yes/No',
        choices=BINARY_CHOICES
    )
    chest_pain = models.PositiveSmallIntegerField(choices=BINARY_CHOICES)

    def __str__(self):
        return self.name + ' cancer prediction'
