#!/usr/bin/env python3
from pydantic import (BaseModel,
                      Field,
                      ValidationError)
from datetime import datetime


class SpaceStation(BaseModel):
    # Pydantic model with constraints to validate station data.
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    # Example with valid data to show successful validation output.
    valid_station: SpaceStation | None = None
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2002, 3, 21),
            is_operational=True,
            notes="GABRIELLLLLLL"
            )
    except ValidationError as error_message:
        print(error_message)

    if valid_station is not None:
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Last Maintenance: {valid_station.last_maintenance}")
        status = ('Operational' if
                  valid_station.is_operational else
                  'Not Operational')
        print(f"Status: {status}")
        print(f"Notes: {valid_station.notes}")

    print("\n========================================")
    # Example with invalid data to show validation errors.
    invalid_station: SpaceStation | None = None
    try:
        invalid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2002, 3, 21),
            is_operational=False
            )
    except ValidationError as error_message:
        print(error_message)

    if invalid_station is not None:
        print("Expected validation error:")
        print(f"ID: {invalid_station.station_id}")
        print(f"Name: {invalid_station.name}")
        print(f"Crew: {invalid_station.crew_size} people")
        print(f"Power: {invalid_station.power_level}%")
        print(f"Oxygen: {invalid_station.oxygen_level}%")
        print(f"Last Maintenance: {invalid_station.last_maintenance}")
        status = ('Operational' if
                  invalid_station.is_operational else
                  'Not Operational')
        print(f"Status: {status}")


if __name__ == "__main__":
    main()
