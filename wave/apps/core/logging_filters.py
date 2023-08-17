from logging import Filter

from django.views.debug import SafeExceptionReporterFilter

CLEANSED_SUBSTITUTE = "*" * 6


class CustomExceptionFilter(SafeExceptionReporterFilter):
    """
    This filter is used to substitute all parameters that contain special
    post keys and to replace them with hidde values
    """

    def get_post_parameters(self, request):
        cleaned_data = super(CustomExceptionFilter, self).get_post_parameters(request)

        secret_keys = [
            'password',
            'token',
            'secret',
            'code',
        ]
        try:
            if cleaned_data:
                cleaned_data = cleaned_data.copy()
                for key, value in cleaned_data.items():
                    for secret_key in secret_keys:
                        if secret_key in key:
                            cleaned_data[key] = CLEANSED_SUBSTITUTE

        except Exception:
            pass

        return cleaned_data


class DisabledLogFilter(Filter):
    def filter(self, record):
        name = getattr(record, 'name', "")
        if (
            name.startswith('s3') or
            "boto" in name or
            "urllib3" in name or
            "lml." in name or
            "pyexcel" in name
        ):
            return False

        return True
