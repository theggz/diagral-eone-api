"""Class to communicate with the Diagral e-one API."""

import logging
from typing import Any

from aiohttp import ClientConnectorError, ClientResponseError, ClientSession

from .models import (ConnectResponse,
                     GetConfigurationResponse, GetDevicesResponse,
                     GetSystemAlertsResponse, GetSystemsResponse,
                     GetSystemStateResponse, IsConnectedResponse,
                     LoginResponse, LogoutResponse)

from .const import BASE_URL, HTTP_CALL_TIMEOUT
from .exceptions import (AuthorizationError, BadRequestError,
                        CloudConnectionError, DiagralCloudError,
                        TooManyRequestsError)

_LOGGER = logging.getLogger(__name__)

class DiagralEOneApi:
    """Diagral e-one API class."""

    def __init__(self, username: str, password: str, session: ClientSession | None) -> None:
        """Initialize the object."""
        self.base_url = BASE_URL
        self.session: ClientSession | None = session
        self.username = username
        self.password = password

    async def api_request(
        self,
        method: str,
        url: str,
        data: Any | None = None,
        bearer_token: str | None = None,
    ):
        """Make an API request."""
        if self.session is None:
            session = ClientSession()
        else:
            session = self.session

        if bearer_token is not None:
            session.headers.add("Authorization", f"Bearer {bearer_token}")

        try:
            async with session.request(
                method,
                url,
                json=data,
                raise_for_status=True,
                timeout=HTTP_CALL_TIMEOUT
            ) as response:
                response_json = await response.json()
        except ClientConnectorError as err:
            raise CloudConnectionError(err) from err
        except ClientResponseError as err:  # TODO: check if message and details properties in API response are retrieved in exception
            if err.status == 400:  # Bad request
                raise BadRequestError(err) from err
            if err.status == 401:  # Unauthorized
                raise AuthorizationError(err) from err
            if err.status == 429:  # Too many requests
                raise TooManyRequestsError(err) from err
            # Generic exception
            raise DiagralCloudError(err) from err
        finally:
            if self.session is None:
                await session.close()

        return response_json

    async def login(self) -> LoginResponse:
        """Login to the user account to retrieve the Bearer token."""
        url = f"{self.base_url}/authenticate/login"
        data = {"username": self.username, "password": self.password}

        response_json = await self.api_request("post", url, data)

        _LOGGER.debug("Login response: %s", response_json)

        return LoginResponse.from_dict(response_json)

    async def get_systems(self, session_id: str) -> GetSystemsResponse:
        """Get user alarm systems."""
        url = f"{self.base_url}/configuration/getSystems"

        response_json = await self.api_request("post", url, bearer_token=session_id)

        _LOGGER.debug("GetSystems response: %s", response_json)

        return GetSystemsResponse.from_dict(response_json)

    async def get_configuration(
        self, session_id: str, system_id: int, role: int
    ) -> GetConfigurationResponse:
        """Get the alarm system configuration data."""
        url = f"{self.base_url}/configuration/getConfiguration"
        data = {"systemId": system_id, "role": role}

        response_json = await self.api_request(
            "post", url, data=data, bearer_token=session_id
        )

        _LOGGER.debug("GetConfiguration response: %s", response_json)

        return GetConfigurationResponse.from_dict(response_json)

    async def is_connected(self, session_id: str, transmitter_id: str) -> IsConnectedResponse:
        """Verify that the system is connected to the internet."""
        url = f"{self.base_url}/installation/isConnected"
        data = {"transmitterId": transmitter_id}

        response_json = await self.api_request("post", url, data, bearer_token=session_id)

        _LOGGER.debug("IsConnected response: %s", response_json)

        return IsConnectedResponse.from_dict(response_json)

    async def connect(
        self, session_id: str, master_code: str, transmitter_id: str, system_id: int, role: int
    ) -> ConnectResponse:
        """Create a new session to communicate with the system."""
        url = f"{self.base_url}/authenticate/connect"
        data = {
            "masterCode": master_code,
            "transmitterId": transmitter_id,
            "systemId": system_id,
            "role": role,
        }

        response_json = await self.api_request("post", url, data, bearer_token=session_id)

        _LOGGER.debug("Connect response: %s", response_json)

        return ConnectResponse.from_dict(response_json)

    async def get_system_state(
        self, session_id: str, central_id: str, ttm_session_id: str
    ) -> GetSystemStateResponse:
        """Get the alarm system state."""
        url = f"{self.base_url}/status/getSystemState"
        data = {"centralId": central_id, "ttmSessionId": ttm_session_id}

        response_json = await self.api_request("post", url, data, bearer_token=session_id)

        _LOGGER.debug("GetSystemState response: %s", response_json)

        return GetSystemStateResponse.from_dict(response_json)

    async def get_devices(self, session_id: str, system_id: int, central_id: str, ttm_session_id: str):
        """Retrieve all devices."""
        url = f"{self.base_url}/api/scenarios/{system_id}/devices"
        data = {"centralId": central_id, "ttmSessionId": ttm_session_id}

        response_json = await self.api_request("get", url, data, bearer_token=session_id)

        _LOGGER.debug("GetDevices response: %s", response_json)

        return GetDevicesResponse.from_dict(response_json)

    async def get_system_alerts(
            self,
            session_id:str,
            central_id:str,
            transmitter_id:str,
            system_id:int,
            ttm_session_id:str):
        """Retrieve all battery and auto-protection informations."""
        url = f"{self.base_url}/configuration/getCentralStatusZone"
        data = {"centralId": central_id,
                "transmitterId": transmitter_id,
                "system_id": system_id,
                "ttmSessionId": ttm_session_id}

        response_json = await self.api_request("post", url, data, bearer_token=session_id)

        _LOGGER.debug("GetSystemAlerts response: %s", response_json)

        return GetSystemAlertsResponse.from_dict(response_json)

    async def disconnect(self, session_id:str, system_id:int, ttm_session_id:str):
        """Disconnect from the alarm system."""
        url = f"{self.base_url}/authenticate/disconnect"
        data = { "systemId": system_id, "ttmSessionId": ttm_session_id }

        response_json = await self.api_request("post", url, data, bearer_token=session_id)

        _LOGGER.debug("Disconnect response: %s", response_json)

        return LogoutResponse.from_dict(response_json)
    
    async def logout(self, session_id: str) -> LogoutResponse:
        """Logout from the user account."""
        url = f"{self.base_url}/authenticate/logout"
        data = {"systemId": "null"}

        response_json = await self.api_request("post", url, data, bearer_token=session_id)

        _LOGGER.debug("Logout response: %s", response_json)

        return LogoutResponse.from_dict(response_json)
