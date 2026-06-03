#!/usr/bin/env python3
from __future__ import annotations
from datetime import datetime
from enum import Enum
import json
from pathlib import Path
import sys
from pydantic import (BaseModel,
                      Field,
                      ValidationError,
                      model_validator)


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def contact_id_checker(self) -> AlienContact:
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        return self

    @model_validator(mode="after")
    def physical_contact_checker(self) -> AlienContact:
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode="after")
    def telepathic_contact_checker(self) -> AlienContact:
        if (self.contact_type == ContactType.telepathic and
                self.witness_count < 3):
            raise ValueError("Telepathic contact requires at"
                             "least 3 witnesses")
        return self

    @model_validator(mode="after")
    def strong_signals_checker(self) -> AlienContact:
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should"
                             "include received messages")
        return self


def run_generated_data_checks() -> None:
    base_dir = Path(__file__).resolve().parents[1]
    data_dir = base_dir / "generated_data"
    if not data_dir.exists():
        print("generated_data folder not found. Run data_exporter.py first.")
        return

    datasets = ["alien_contacts.json", "invalid_contacts.json"]
    for filename in datasets:
        file_path = data_dir / filename
        if not file_path.exists():
            print(f"Missing {filename}.")
            continue
        items = json.loads(file_path.read_text())
        ok = 0
        errors = 0
        for item in items:
            try:
                AlienContact(**item)
                ok += 1
            except ValidationError:
                errors += 1
        print(f"{filename}: {ok} valid, {errors} errors")


def main() -> None:
    if "--generated-data" in sys.argv:
        run_generated_data_checks()
        return
    print("Alien Contact Log Validation")
    print("======================================")

    alien_contact: AlienContact | None = None
    try:
        alien_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2002, 3, 21),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )
    except ValueError as error_message:
        print(error_message)

    print("Valid contact report:")
    if alien_contact is not None:
        print(f"ID: {alien_contact.contact_id}")
        print(f"Type: {alien_contact.contact_type}")
        print(f"Location: {alien_contact.location}")
        print(f"Signal: {alien_contact.signal_strength}/10")
        print(f"Duration: {alien_contact.duration_minutes} minutes")
        print(f"Witnesses: {alien_contact.witness_count}")
        print(f"Message: {alien_contact.message_received}")

    print("\n======================================")
    invalid_alien_contact: AlienContact | None = None
    try:
        invalid_alien_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2002, 3, 21),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )
    except ValueError as error_message:
        print(error_message)

    if invalid_alien_contact is not None:
        print(f"ID: {invalid_alien_contact.contact_id}")
        print(f"Type: {invalid_alien_contact.contact_type}")
        print(f"Location: {invalid_alien_contact.location}")
        print(f"Signal: {invalid_alien_contact.signal_strength}/10")
        print(f"Duration: {invalid_alien_contact.duration_minutes}")
        print(f"Witnesses: {invalid_alien_contact.witness_count}")
        print(f"Message: {invalid_alien_contact.message_received}")


if __name__ == "__main__":
    main()
