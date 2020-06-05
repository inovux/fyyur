from wtforms.validators import ValidationError
import re


def multiple_field_validation(values):
    message = 'Given value(s), must be one of: {0}.'.format(', '.join(values))

    def _validate(form, field):
        error = False
        for value in field.data:
            if value not in values:
                error = True

        if error:
            raise ValidationError(message)

    return _validate


def is_valid_phone(form, field):
    if not re.search(r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$", field.data):
        raise ValidationError("Phone number is invalid.")
