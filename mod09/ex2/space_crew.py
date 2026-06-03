#!/usr/bin/env python3
from __future__ import annotations
from datetime import datetime
from enum import Enum
from pydantic import (BaseModel,
                      Field,
                      model_validator)


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_id_checker(self) -> SpaceMission:
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID doesn't start with 'M'")
        return self

    @model_validator(mode='after')
    def cmd_cpt_checker(self) -> SpaceMission:
        if not any(member.rank in (Rank.commander, Rank.captain)
                   for member in self.crew):
            raise ValueError("Mission must have at least one Commander"
                             " or Captain")
        return self

    @model_validator(mode='after')
    def long_mission_checker(self) -> SpaceMission:
        experienced_count = sum(
            1 for member in self.crew if member.years_experience >= 5)
        if (self.duration_days > 365 and
                experienced_count * 2 < len(self.crew)):
            raise ValueError("Long missions (> 365 days) need 50% experienced"
                             " crew (5+ years)")
        return self

    @model_validator(mode='after')
    def active_crew_checker(self) -> SpaceMission:
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("======================================")

    crew_list = [CrewMember(member_id="12345",
                            name="Sarah Connor",
                            rank=Rank.commander,
                            age=20,
                            specialization="Mission Command",
                            years_experience=10,
                            is_active=True),
                 CrewMember(member_id="123456",
                            name="John Smith",
                            rank=Rank.lieutenant,
                            age=21,
                            specialization="Navigation",
                            years_experience=10,
                            is_active=True),
                 CrewMember(member_id="1234567",
                            name="Alice Johnson",
                            rank=Rank.officer,
                            age=22,
                            specialization="Engineering",
                            years_experience=10,
                            is_active=True)]

    space_crew: SpaceMission | None = None
    try:
        space_crew = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            launch_date=datetime(2002, 3, 21),
            duration_days=900,
            budget_millions=2500.0,
            crew=crew_list,
            mission_status="planned"
        )
    except ValueError as error_message:
        print(error_message)

    print("Valid contact report:")
    if space_crew is not None:
        print(f"Mission: {space_crew.mission_name}")
        print(f"ID: {space_crew.mission_id}")
        print(f"Destination: {space_crew.destination}")
        print(f"Duration: {space_crew.duration_days}")
        print(f"Budget: ${space_crew.budget_millions}M")
        print(f"Crew size: {len(crew_list)}")
        print("Crew members:")
        for member in crew_list:
            print(f"- {member.name} "
                  f"({member.rank.value}) - {member.specialization}")

    print("\n=========================================")
    invalid_crew_list = [
        CrewMember(
            member_id="12345",
            name="Sarah Connor",
            rank=Rank.cadet,
            age=20,
            specialization="Mission Command",
            years_experience=10,
            is_active=True
        ),
        CrewMember(
            member_id="123456",
            name="John Smith",
            rank=Rank.lieutenant,
            age=21,
            specialization="Navigation",
            years_experience=10,
            is_active=True
        ),
        CrewMember(
            member_id="1234567",
            name="Alice Johnson",
            rank=Rank.officer,
            age=22,
            specialization="Engineering",
            years_experience=10,
            is_active=True
            )
        ]

    invalid_space_crew: SpaceMission | None = None
    try:
        invalid_space_crew = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            launch_date=datetime(2002, 3, 21),
            duration_days=900,
            budget_millions=2500.0,
            crew=invalid_crew_list,
            mission_status="planned"
        )
    except ValueError as error_message:
        print(error_message)
        if invalid_space_crew is not None:
            print(f"Mission: {invalid_space_crew.mission_name}")
            print(f"ID: {invalid_space_crew.mission_id}")
            print(f"Destination: {invalid_space_crew.destination}")
            print(f"Duration: {invalid_space_crew.duration_days}")
            print(f"Budget: ${invalid_space_crew.budget_millions}M")
            print(f"Crew size: {len(invalid_crew_list)}")
            print("Crew members:")
            for member in invalid_crew_list:
                print(f"- {member.name} "
                      f"({member.rank.value}) - {member.specialization}")


if __name__ == "__main__":
    main()
