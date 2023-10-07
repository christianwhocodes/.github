import json
from datetime import date
from pathlib import Path

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class WaksKevin(models.Model):
    logo = ThumbnailerImageField(upload_to="base/WaksKevin")
    theme_color = models.CharField(max_length=255, default="#EDE9DD")
    profile_picture = models.ImageField(upload_to="base/WaksKevin")
    author = models.CharField(max_length=100, default="Kevin Wakhisi")
    title = models.TextField(default="Software Engineer & Student @ UON")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.author
    
    #########################################################

    birthday = models.DateField(default=date(2002, 5, 2))
    degree = models.CharField(
        max_length=50,
        choices=[
            ("Bachelor", "Bachelor"),
            ("Master", "Master"),
        ],
        default="Bachelor",
    )
    freelance_status = models.CharField(
        max_length=100,
        choices=[
            ("Available", "Available"),
            ("Unavailable", "Unavailable"),
            ("Busy", "Busy"),
        ],
        default="Available",
    )

    def get_age(self):
        today = date.today()
        dob = self.birthday
        age = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1
        return age

    #########################################################

    email = models.EmailField(default="wakskevin@outlook.com")
    phone = models.CharField(max_length=100, default="+254 706 965 904")
    address = models.CharField(max_length=100, default="Nairobi, Kenya")
    website = models.URLField(default="https://www.kevinwakhisi.info")

    #########################################################

    linkedin = models.URLField(
        blank=True, default="https://www.linkedin.com/in/WaksKevin/"
    )
    github = models.URLField(blank=True, default="https://github.com/WaksKevin/")
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    #########################################################

    manifest = models.FileField(upload_to="base/WaksKevin")

    def get_logo_name(self):
        return self.logo.name.split("/")[-1]

    def save(self, *args, **kwargs):
        def get_first_name(name):
            name_parts = name.split()
            return name_parts[0]

        data = {
            "scope": "/",
            "start_url": "/",
            "display": "standalone",
            "icons": [
                {
                    "sizes": "512x512",
                    "type": "image/png",
                    "src": f"{self.get_logo_name()}",
                }
            ],
            "name": self.author,
            "short_name": get_first_name(self.author),
            "theme_color": self.theme_color,
            "background_color": "#262626",
        }

        content = json.dumps(data)
        prefix = Path("media")
        file_path = Path("base", "WaksKevin", "manifest.webmanifest")
        ispath = prefix / file_path

        ispath.parent.mkdir(parents=True, exist_ok=True)  # making sure directory exists

        with open((prefix / file_path).resolve(), "w") as file:
            file.write(content)

        self.manifest.name = str(file_path)
        super().save(*args, **kwargs)
