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
TOTAL_HEATING_PRODUCED_KEY = "total_heating_produced"
HEATING_PRODUCTION_TODAY_KEY = "heating_production_today"
TOTAL_DHW_PRODUCED_KEY = "total_dhw_produced"
DHW_PRODUCTION_TODAY_KEY = "dhw_production_today"
TOTAL_HEATING_CONSUMED_KEY = "total_heating_consumed"
HEATING_CONSUMPTION_TODAY_KEY = "heating_consumption_today"
TOTAL_DHW_CONSUMED_KEY = "total_dhw_consumed"
DHW_CONSUMPTION_TODAY_KEY = "dhw_consumption_today"


# Other keys
MAC_ADDRESS_KEY = "mac_address"
