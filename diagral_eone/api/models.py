"""Api response models"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class LoginResponse:
    """Describe the Login response."""
    session_id: str | None
    diagral_id: str | None
    crypted_password: str | None
    username: str | None
    gender: str | None
    first_name: str | None
    last_name: str | None
    mobile: str | None
    locale: Optional[str]
    country: str | None
    postal_code: str | None
    city: str | None
    address: str | None
    newsletter: bool | None
    partners: Optional[str]
    accepted_cgu: bool | None
    cgu_url: str | None
    user_type: str | None
    expires_in: int | None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'LoginResponse':
        """Convert the dictionnary to response object."""
        return LoginResponse(
            session_id=data.get("sessionId"),
            diagral_id=data.get("diagralId"),
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
            newsletter=data.get("newsletter", ),
            partners=data.get("partners"),
            accepted_cgu=data.get("acceptedCGU"),
            cgu_url=data.get("cguUrl"),
            user_type=data.get("userType"),
            expires_in=data.get("expiresIn")
        )

@dataclass
class System:
    """Describe a Diagral system."""
    name: str | None
    id: int | None
    role: int | None
    installation_complete: bool | None
    standalone: bool | None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'System':
        """Convert the dictionnary to response object."""
        return System(
            name=data.get("name"),
            id=data.get("id"),
            role=data.get("role"),
            installation_complete=data.get("installationComplete"),
            standalone=data.get("standalone")
        )

@dataclass
class GetSystemsResponse:
    """Describe the GetSystems response."""
    diagral_id: str | None
    systems: List[System] = field(default_factory=list)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'GetSystemsResponse':
        """Convert the dictionnary to response object."""
        systems_data = data.get("systems", [])
        systems = [System.from_dict(system) for system in systems_data]
        return GetSystemsResponse(
            diagral_id=data.get("diagralId"),
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
    transmitter_id: str | None
    central_id: str | None
    installation_complete: bool | None
    name: str | None
    role: int | None
    rights: Rights
    id: int | None
    standalone: bool | None
    gprs_phone: Optional[str]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'GetConfigurationResponse':
        """Convert the dictionnary to response object."""
        return GetConfigurationResponse(
            transmitter_id=data.get("transmitterId"),
            central_id=data.get("centralId"),
            installation_complete=data.get("installationComplete"),
            name=data.get("name"),
            role=data.get("role"),
            rights=Rights.from_dict(data.get("rights", {})),
            id=data.get("id"),
            standalone=data.get("standalone"),
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
    box: str | None
    box_radio: str | None
    plug_knx: str | None
    raw_versions: str | None

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
    ttm_session_id: str | None
    system_state: str | None
    groups: List[str]
    group_list: List[str]
    gprs_connection: Optional[str]
    status: str | None
    versions: Versions
    connected_user_type: str | None
    code_index: int | None
    user_rights_configuration: Optional[str]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'ConnectResponse':
        """Convert the dictionnary to response object."""
        return ConnectResponse(
            message=data.get("message"),
            ttm_session_id=data.get("ttmSessionId"),
            system_state=data.get("systemState"),
            groups=data.get("groups", []),
            group_list=data.get("groupList", []),
            gprs_connection=data.get("gprsConnection"),
            status=data.get("status"),
            versions=Versions.from_dict(data.get("versions", {})),
            connected_user_type=data.get("connectedUserType"),
            code_index=data.get("codeIndex"),
            user_rights_configuration=data.get("userRightsConfiguration")
        )

@dataclass
class GetSystemStateResponse:
    """Describe the GetSystemState response."""
    message: Optional[str]
    system_state: str | None
    groups: List[str]
    defaults: str | None
    command_status: str | None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'GetSystemStateResponse':
        """Convert the dictionnary to response object."""
        return GetSystemStateResponse(
            message=data.get("message"),
            system_state=data.get("systemState"),
            groups=data.get("groups", []),
            defaults=data.get("defaults"),
            command_status=data.get("commandStatus")
        )

@dataclass
class GetDevicesResponse:
    """Describe the GetDevices response."""
    index: str | None
    name: str | None
    type: str | None
    application: str | None

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
    main_power_supply_alert: bool | None
    secondary_power_supply_alert: bool | None
    default_media_alert: bool | None
    autoprotection_mechanical_alert: bool | None
    autoprotection_wired_alert: bool | None
    radio_alert: bool | None
    active_groups: Dict[int, bool] | None
    system_state: int | None
    system_state_text: str | None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'CentralStatus':
        """Convert the dictionnary to response object."""
        return CentralStatus(
            main_power_supply_alert=data.get("mainPowerSupplyAlert"),
            secondary_power_supply_alert=data.get("secondaryPowerSupplyAlert"),
            default_media_alert=data.get("defaultMediaAlert"),
            autoprotection_mechanical_alert=data.get("autoprotectionMechanicalAlert"),
            autoprotection_wired_alert=data.get("autoprotectionWiredAlert"),
            radio_alert=data.get("radioAlert"),
            active_groups={int(k): v for k, v in data['activeGroups'].items()},
            system_state=data.get("systemState"),
            system_state_text=data.get("systemStateText")
        )


@dataclass
class CommandStatus:
    """The command status."""
    power_supply_alert: bool | None
    secondary_power_supply_alert: bool | None
    autoprotection_mechanical_alert: bool | None
    radio_alert: bool | None
    index: int | None

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
    media_adsl_alert: bool | None
    media_gsm_alert: bool | None
    media_rtc_alert: bool | None
    out_of_order_alert: bool | None
    main_power_supply_alert: bool | None
    secondary_power_supply_alert: bool | None
    autoprotection_mechanical_alert: bool | None
    radio_alert: bool | None
    index: int | None

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
    power_supply_alert: bool | None
    secondary_power_supply_alert: bool | None
    autoprotection_mechanical_alert: bool | None
    radio_alert: bool | None
    sensor_alert: bool | None
    loop_alert: bool | None
    mask_alert: bool | None
    ejected: bool | None
    number_of_supervisions: int | None
    index: int | None

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
    status: str | None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'LogoutResponse':
        """Convert the dictionnary to response object."""
        return LogoutResponse(
            status=data.get("status")
        )
