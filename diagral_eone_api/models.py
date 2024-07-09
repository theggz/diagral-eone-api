"""Api response models"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .exceptions import MissingFieldResponseError

@dataclass
class LoginResponse:
    """Describe the Login response."""
    session_id: str
    diagral_id: str
    crypted_password: Optional[str]
    username: Optional[str]
    gender: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    mobile: Optional[str]
    locale: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]
    city: Optional[str]
    address: Optional[str]
    newsletter: bool
    partners: Optional[str]
    accepted_cgu: bool
    cgu_url: Optional[str]
    user_type: Optional[str]
    expires_in_ms: int

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'LoginResponse':
        """Convert the dictionnary to response object."""

        session_id=data.get("sessionId")
        diagral_id=data.get("diagralId")

        if session_id is None:
            raise MissingFieldResponseError("Field 'sessionId' is missing in response.")
        if diagral_id is None:
            raise MissingFieldResponseError("Field 'diagralId' is missing in response.")

        return LoginResponse(
            session_id=session_id,
            diagral_id=diagral_id,
            crypted_password=data.get("cryptedPassword"),
            username=data.get("username"),
            gender=data.get("gender"),
            first_name=data.get("firstName"),
            last_name=data.get("lastName"),
            mobile=data.get("mobile"),
            locale=data.get("locale"),
            country=data.get("country"),
            postal_code=data.get("postalCode"),
            city=data.get("city"),
            address=data.get("address"),
            newsletter=data.get("newsletter", False),
            partners=data.get("partners"),
            accepted_cgu=data.get("acceptedCGU", True),
            cgu_url=data.get("cguUrl"),
            user_type=data.get("userType"),
            expires_in_ms=data.get("expiresIn", 3600000)
        )

@dataclass
class System:
    """Describe a Diagral system."""
    name: Optional[str]
    id: int
    role: int
    installation_complete: bool
    standalone: bool

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'System':
        """Convert the dictionnary to response object."""

        role=data.get("role")
        config_id=data.get("id")

        if role is None:
            raise MissingFieldResponseError("Field 'role' is missing in response.")
        if config_id is None:
            raise MissingFieldResponseError("Field 'id' is missing in response.")

        return System(
            name=data.get("name"),
            id=config_id,
            role=role,
            installation_complete=data.get("installationComplete", True),
            standalone=data.get("standalone", False)
        )

@dataclass
class GetSystemsResponse:
    """Describe the GetSystems response."""
    diagral_id: str
    systems: List[System] = field(default_factory=list)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'GetSystemsResponse':
        """Convert the dictionnary to response object."""

        diagral_id=data.get("diagralId")

        if diagral_id is None:
            raise MissingFieldResponseError("Field 'diagralId' is missing in response.")

        systems_data = data.get("systems", [])
        systems = [System.from_dict(system) for system in systems_data]
        return GetSystemsResponse(
            diagral_id=diagral_id,
            systems=systems
        )

@dataclass
class Rights:
    """Describe the rights."""
    alarms: str
    openings: str
    scenarios: str
    video: str
    lights: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Rights':
        """Convert the dictionnary to response object."""
        return Rights(
            alarms=data.get("UNIVERSE_ALARMS", "false"),
            openings=data.get("UNIVERSE_OPENINGS", "false"),
            scenarios=data.get("UNIVERSE_SCENARIOS", "false"),
            video=data.get("UNIVERSE_VIDEO", "false"),
            lights=data.get("UNIVERSE_LIGHTS", "false")
        )

@dataclass
class GetConfigurationResponse:
    """Describe the GetConfiguration response."""
    transmitter_id: str
    central_id: str
    installation_complete: bool
    name: Optional[str]
    role: int
    rights: Rights
    id: int
    standalone: bool
    gprs_phone: Optional[str]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'GetConfigurationResponse':
        """Convert the dictionnary to response object."""

        transmitter_id=data.get("transmitterId")
        central_id=data.get("centralId")
        role=data.get("role")
        config_id=data.get("id")

        if transmitter_id is None:
            raise MissingFieldResponseError("Field 'transmitterId' is missing in response.")
        if central_id is None:
            raise MissingFieldResponseError("Field 'centralId' is missing in response.")
        if role is None:
            raise MissingFieldResponseError("Field 'role' is missing in response.")
        if config_id is None:
            raise MissingFieldResponseError("Field 'id' is missing in response.")
        
        return GetConfigurationResponse(
            transmitter_id=transmitter_id,
            central_id=central_id,
            installation_complete=data.get("installationComplete", True),
            name=data.get("name"),
            role=role,
            rights=Rights.from_dict(data.get("rights", {})),
            id=config_id,
            standalone=data.get("standalone", False),
            gprs_phone=data.get("gprsPhone")
        )

@dataclass
class IsConnectedResponse:
    """Describe the IsConnected response."""
    is_connected: bool

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'IsConnectedResponse':
        """Convert the dictionnary to response object."""
        return IsConnectedResponse(
            is_connected=data.get("isConnected", False)
        )

@dataclass
class Versions:
    """Describe the system hardware versions."""
    box: Optional[str]
    box_radio: Optional[str]
    plug_knx: Optional[str]
    raw_versions: Optional[str]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Versions':
        """Convert the dictionnary to response object."""
        return Versions(
            box=data.get("box"),
            box_radio=data.get("boxRadio"),
            plug_knx=data.get("plugKnx"),
            raw_versions=data.get("rawVersions")
        )

@dataclass
class ConnectResponse:
    """Describe the Connect response."""
    message: Optional[str]
    ttm_session_id: str
    system_state: str
    groups: List[str]
    group_list: List[str]
    gprs_connection: Optional[str]
    status: str
    versions: Versions
    connected_user_type: Optional[str]
    code_index: Optional[int]
    user_rights_configuration: Optional[str]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'ConnectResponse':
        """Convert the dictionnary to response object."""

        ttm_session_id=data.get("ttmSessionId")
        system_state=data.get("systemState")
        status=data.get("status")

        if ttm_session_id is None:
            raise MissingFieldResponseError("Field 'ttmSessionId' is missing in response.")
        if system_state is None:
            raise MissingFieldResponseError("Field 'systemState' is missing in response.")
        if status is None:
            raise MissingFieldResponseError("Field 'status' is missing in response.")

        return ConnectResponse(
            message=data.get("message"),
            ttm_session_id=ttm_session_id,
            system_state=system_state,
            groups=data.get("groups", []),
            group_list=data.get("groupList", []),
            gprs_connection=data.get("gprsConnection"),
            status=status,
            versions=Versions.from_dict(data.get("versions", {})),
            connected_user_type=data.get("connectedUserType"),
            code_index=data.get("codeIndex"),
            user_rights_configuration=data.get("userRightsConfiguration")
        )

@dataclass
class GetSystemStateResponse:
    """Describe the GetSystemState response."""
    message: Optional[str]
    system_state: str
    groups: List[str]
    defaults: Optional[str]
    command_status: Optional[str]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'GetSystemStateResponse':
        """Convert the dictionnary to response object."""

        system_state = data.get("systemState")

        if system_state is None:
            raise MissingFieldResponseError("Field 'systemState' is missing in response.")

        return GetSystemStateResponse(
            message=data.get("message"),
            system_state=system_state,
            groups=data.get("groups", []),
            defaults=data.get("defaults"),
            command_status=data.get("commandStatus")
        )

@dataclass
class GetDevicesResponse:
    """Describe the GetDevices response."""
    index: Optional[str]
    name: Optional[str]
    type: Optional[str]
    application: Optional[str]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'GetDevicesResponse':
        """Convert the dictionnary to response object."""
        return GetDevicesResponse(
            index=data.get("index"),
            name=data.get("name"),
            type=data.get("type"),
            application=data.get("application")
        )

@dataclass
class CentralStatus:
    """The alarm central status."""
    main_power_supply_alert: Optional[bool]
    secondary_power_supply_alert: Optional[bool]
    default_media_alert: Optional[bool]
    autoprotection_mechanical_alert: Optional[bool]
    autoprotection_wired_alert: Optional[bool]
    radio_alert: Optional[bool]
    active_groups: Dict[int, bool]
    system_state: int
    system_state_text: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'CentralStatus':
        """Convert the dictionnary to response object."""

        system_state = data.get("systemState")
        system_state_text = data.get("systemStateText")

        if system_state is None:
            raise MissingFieldResponseError("Field 'systemState' is missing in response.")
        if system_state_text is None:
            raise MissingFieldResponseError("Field 'systemStateText' is missing in response.")

        return CentralStatus(
            main_power_supply_alert=data.get("mainPowerSupplyAlert"),
            secondary_power_supply_alert=data.get("secondaryPowerSupplyAlert"),
            default_media_alert=data.get("defaultMediaAlert"),
            autoprotection_mechanical_alert=data.get("autoprotectionMechanicalAlert"),
            autoprotection_wired_alert=data.get("autoprotectionWiredAlert"),
            radio_alert=data.get("radioAlert"),
            active_groups={int(k): v for k, v in data['activeGroups'].items()},
            system_state=system_state,
            system_state_text=system_state_text
        )


@dataclass
class CommandStatus:
    """The command status."""
    power_supply_alert: Optional[bool]
    secondary_power_supply_alert: Optional[bool]
    autoprotection_mechanical_alert: Optional[bool]
    radio_alert: Optional[bool]
    index: Optional[int]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'CommandStatus':
        """Convert the dictionnary to response object."""
        return CommandStatus(
            power_supply_alert=data.get("powerSupplyAlert"),
            secondary_power_supply_alert=data.get("secondaryPowerSupplyAlert"),
            autoprotection_mechanical_alert=data.get("autoprotectionMechanicalAlert"),
            radio_alert=data.get("radioAlert"),
            index=data.get("index")
        )

@dataclass
class TransmitterStatus:
    """The tranmitter status."""
    media_adsl_alert: Optional[bool]
    media_gsm_alert: Optional[bool]
    media_rtc_alert: Optional[bool]
    out_of_order_alert: Optional[bool]
    main_power_supply_alert: Optional[bool]
    secondary_power_supply_alert: Optional[bool]
    autoprotection_mechanical_alert: Optional[bool]
    radio_alert: Optional[bool]
    index: Optional[int]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'TransmitterStatus':
        """Convert the dictionnary to response object."""
        return TransmitterStatus(
            media_adsl_alert=data.get("mediaADSLAlert"),
            media_gsm_alert=data.get("mediaGSMAlert"),
            media_rtc_alert=data.get("mediaRTCAlert"),
            out_of_order_alert=data.get("outOfOrderAlert"),
            main_power_supply_alert=data.get("mainPowerSupplyAlert"),
            secondary_power_supply_alert=data.get("secondaryPowerSupplyAlert"),
            autoprotection_mechanical_alert=data.get("autoprotectionMechanicalAlert"),
            radio_alert=data.get("radioAlert"),
            index=data.get("index")
        )

@dataclass
class SensorStatus:
    """The sensor status."""
    power_supply_alert: Optional[bool]
    secondary_power_supply_alert: Optional[bool]
    autoprotection_mechanical_alert: Optional[bool]
    radio_alert: Optional[bool]
    sensor_alert: Optional[bool]
    loop_alert: Optional[bool]
    mask_alert: Optional[bool]
    ejected: Optional[bool]
    number_of_supervisions: Optional[int]
    index: Optional[int]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'SensorStatus':
        """Convert the dictionnary to response object."""
        return SensorStatus(
            power_supply_alert=data.get("powerSupplyAlert"),
            secondary_power_supply_alert=data.get("secondaryPowerSupplyAlert"),
            autoprotection_mechanical_alert=data.get("autoprotectionMechanicalAlert"),
            radio_alert=data.get("radioAlert"),
            sensor_alert=data.get("sensorAlert"),
            loop_alert=data.get("loopAlert"),
            mask_alert=data.get("maskAlert"),
            ejected=data.get("ejected"),
            number_of_supervisions=data.get("numberOfSupervisions"),
            index=data.get("index")
        )

@dataclass
class GetSystemAlertsResponse:
    """Describe the system alerts response."""
    central_status: CentralStatus
    commands_status: List[CommandStatus]
    transmitters_status: List[TransmitterStatus]
    sensors_status: List[SensorStatus]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'GetSystemAlertsResponse':
        """Convert the dictionnary to response object."""
        return GetSystemAlertsResponse(
            central_status=CentralStatus.from_dict(data.get('centralStatus', {})),
            commands_status=[CommandStatus.from_dict(item) for item in data.get('commandsStatus', [])],
            transmitters_status=[TransmitterStatus.from_dict(item) for item in data.get('transmittersStatus', [])],
            sensors_status=[SensorStatus.from_dict(item) for item in data.get('sensorsStatus', [])]
        )

@dataclass
class LogoutResponse:
    """Describe the Logout response."""
    status: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'LogoutResponse':
        """Convert the dictionnary to response object."""

        status = data.get("status")

        if status is None:
            raise MissingFieldResponseError("Field 'status' is missing in response.")

        return LogoutResponse(
            status=status
        )
