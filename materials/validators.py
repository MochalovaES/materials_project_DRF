import re

from rest_framework.exceptions import ValidationError


class URLValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('youtube.com')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.findall(tmp_val)):
            raise ValidationError('URL должен содержать адрес youtube.com')
