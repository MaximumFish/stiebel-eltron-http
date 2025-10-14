"""Constants for stiebel_eltron_http."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "stiebel_eltron_http"
HTTP_CONNECTION_TIMEOUT = 30  # seconds
EXPECTED_HTML_TITLE = "STIEBEL ELTRON Reglersteuerung"

INFO_SYSTEM_PATH = "/?s=1,0"
INFO_HEATPUMP_PATH = "/?s=1,1"
DIAGNOSIS_SYSTEM_PATH = "/?s=2,7"
PROFILE_NETWORK_PATH = "/?s=5,0"

# Sensor keys
ROOM_TEMPERATURE_KEY = "room_temperature"
ROOM_HUMIDITY_KEY = "room_relative_humidity"
OUTSIDE_TEMPERATURE_KEY = "outside_temperature"
TOTAL_HEAT_PRODUCED_KEY = "total_heat_produced"
HEAT_PRODUCED_TODAY_KEY = "heat_produced_today"
TOTAL_DHW_PRODUCED_KEY = "total_dhw_produced"
DHW_PRODUCED_TODAY_KEY = "dhw_produced_today"
TOTAL_HEATING_CONSUMED_KEY = "total_heating_consumed"
HEATING_CONSUMED_TODAY_KEY = "heating_consumed_today"
TOTAL_DHW_CONSUMED_KEY = "total_dhw_consumed"
DHW_CONSUMED_TODAY_KEY = "dhw_consumed_today"


# Other keys
MAC_ADDRESS_KEY = "mac_address"
