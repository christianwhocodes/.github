from django.core.validators import MaxValueValidator
from django.db import models


class Hero(models.Model):
    desktop_bg = models.ImageField(
        upload_to="home/hero",
        verbose_name="Background image",
        help_text="Upload a hero background image for desktop display",
    )
    mobile_bg = models.ImageField(
        upload_to="home/hero",
        verbose_name="Background image",
        help_text="Upload a hero background image for mobile display. If not provided, the desktop image will be used instead.",
        blank=True,
    )

    typed_item_1 = models.CharField(
        max_length=50,
        default="a child of the Most High God",
    )
    typed_item_2 = models.CharField(max_length=50, default="highly favored and adored")
    typed_item_3 = models.CharField(max_length=50, default="a friend of Jesus")
    typed_item_4 = models.CharField(max_length=50, default="... a Christian! 💯")

    def __str__(self):
        return f"Hero Section"


class Fact(models.Model):
    happy_clients = models.SmallIntegerField(blank=True)
    repositories = models.SmallIntegerField(blank=True)

    def __str__(self):
        return f"Facts Section"


class Skill(models.Model):
    name = models.CharField(max_length=50)
    value = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    # TODO: add icons to each skill

    def __str__(self):
        return self.name


class Resume(models.Model):
    file = models.FileField(upload_to="home/resume")

    def __str__(self):
        return f"Resume Section"
