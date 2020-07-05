import pytest
from workscheduler import create_app

@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    return app
