
"""API test class."""

from faker import Faker

from diagral_eone_api.client import DiagralEOneApi

class TestApi:
    """API test."""
    fake = Faker()
    username = fake.user_name()
    password = fake.password()

    def test_api_init(self):
        """Test initializer."""
        diagral_api = DiagralEOneApi(self.username, self.password, None)
        assert diagral_api.username == self.username
        assert diagral_api.password == self.password
