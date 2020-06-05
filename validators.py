from wtforms.validators import ValidationError


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
