from django.core.validators import RegexValidator
from django.forms import ValidationError

from . import models


def city_name_validator(value):
    RegexValidator(
        regex=r'^[-а-яА-Я\s]+$',
        message='Название города должно содержать только русские буквы.'
    )(value)
