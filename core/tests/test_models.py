import pytest

from core.models import Demo


@pytest.mark.django_db
def test_demo() -> None:
    demo = Demo.objects.create(name="test")
    assert demo.name == "test"
