#!/usr/bin/env python3
from os import getenv
from dotenv import load_dotenv


CONFIG_VARS = [
    ("Mode", "MATRIX_MODE"),
    ("Database", "DATABASE_URL"),
    ("API Access", "API_KEY"),
    ("Log Level", "LOG_LEVEL"),
    ("Zion Network", "ZION_ENDPOINT"),
    ("Password", "PASSWORD"),
    ("Root", "ROOT_PASSWD")
]


def is_missing(value: str | None) -> bool:
    return value is None or value == ""


def load_configuration() -> tuple[dict[str, str | None], str | None, str | None, bool]:
    mode_env = getenv("MATRIX_MODE")
    dotenv_loaded = False
    if mode_env != "production":
        dotenv_loaded = load_dotenv(".env", override=False)
    configs = {key: getenv(key) for _, key in CONFIG_VARS}
    return configs, mode_env, configs.get("MATRIX_MODE"), dotenv_loaded


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    configs, mode_env, mode_value, dotenv_loaded = load_configuration()

    print("Configuration loaded:")
    missing = []
    for label, key in CONFIG_VARS:
        value = configs.get(key)
        if is_missing(value):
            missing.append(label)
            print(f"Missing {label} configuration!")
        else:
            print(f"{label}: {value}")

    print("\nEnvironment security check:")
    if mode_env == "production":
        print("[OK] Production mode detected")
        print("[OK] .env file skipped")
    else:
        if dotenv_loaded:
            print("[OK] Development mode: .env file loaded")
        else:
            print("[WARN] Development mode: .env file not found")
    print("[OK] Environment variables override .env values")
    if mode_env is None and mode_value == "production":
        print("[WARN] MATRIX_MODE=production should be set in the environment")

    if missing:
        print(f"WARNING: Missing configuration values: {', '.join(missing)}")
    else:
        print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()