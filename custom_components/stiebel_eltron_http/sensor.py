"""Sensor platform for Stiebel Eltron ISG without Modbus."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import PERCENTAGE, UnitOfEnergy, UnitOfTemperature

from custom_components.stiebel_eltron_http.const import LOGGER

from .const import (
    OUTSIDE_TEMPERATURE_KEY,
    ROOM_HUMIDITY_KEY,
    ROOM_TEMPERATURE_KEY,
    DHW_TEMPERATURE_KEY,
    TOTAL_HEAT_PRODUCED_KEY,
    HEAT_PRODUCED_TODAY_KEY,
    TOTAL_DHW_PRODUCED_KEY,
    DHW_PRODUCED_TODAY_KEY,
    TOTAL_HEATING_CONSUMED_KEY,
    HEATING_CONSUMED_TODAY_KEY,
    TOTAL_DHW_CONSUMED_KEY,
    DHW_CONSUMED_TODAY_KEY,
)
from .entity import StiebelEltronHttpEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import StiebelEltronHttpDataUpdateCoordinator
    from .data import StiebelEltronHttpConfigEntry


ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key=ROOM_TEMPERATURE_KEY,
        name="Room temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=DHW_TEMPERATURE_KEY,
        name="Hot water temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ROOM_HUMIDITY_KEY,
        name="Room relative humidity",
        icon="mdi:water-percent",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=OUTSIDE_TEMPERATURE_KEY,
        name="Outside temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TOTAL_HEAT_PRODUCED_KEY,
        name="Total heating energy produced",
        icon="mdi:radiator",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=HEAT_PRODUCED_TODAY_KEY,
        name="Heating energy produced today",
        icon="mdi:radiator",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=TOTAL_DHW_PRODUCED_KEY,
        name="Total hot water energy produced",
        icon="mdi:water-boiler",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=DHW_PRODUCED_TODAY_KEY,
        name="Hot water energy produced today",
        icon="mdi:water-boiler",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=TOTAL_HEATING_CONSUMED_KEY,
        name="Total heating energy consumed",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=HEATING_CONSUMED_TODAY_KEY,
        name="Heating energy consumed today",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),

    SensorEntityDescription(
        key=TOTAL_DHW_CONSUMED_KEY,
        name="Total hot water energy consumed",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=DHW_CONSUMED_TODAY_KEY,
        name="Hot water energy consumed today",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: StiebelEltronHttpConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities(
        StiebelEltronHttpSensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class StiebelEltronHttpSensor(StiebelEltronHttpEntity, SensorEntity):
    """Stiebel Eltron HTTP Sensor class."""

    def __init__(
        self,
        coordinator: StiebelEltronHttpDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator, entity_description)

    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        LOGGER.debug("Coordinator update received: %s", self.coordinator.data)

        new_value = self.coordinator.data.get(self.entity_description.key)
        LOGGER.debug(
            "Sensor %s updated with new value: %s",
            self.entity_description.key,
            new_value,
        )
        # update the sensor state based on the coordinator data
        self._attr_native_value = new_value

        return super()._handle_coordinator_update()
