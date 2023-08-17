from django.http import HttpResponse
from django.views.generic import TemplateView


class Index(TemplateView):
    """
    Vite app here
    """
    title = "Wave - A social media website"
    template_name = "core/index.html"

    @property
    def test_data(self) -> dict:
        """
        Add dummy data to the demplate
        """
        return {
            "yes": True,
            "no": False,
            "none": None,
            "text": "Lorem ipsum dolor sit amet",
            "list": [
                123,
                True,
                False,
                None,
                {"key": "value"},
            ],
            "dict": {
                "foo": "bar",
                "eggs": "spam",
            },
        }
