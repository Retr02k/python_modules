from alchemy import grimoire

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    try:
        result = grimoire.light_spell_record("Fantasy", "fire")
        print(f"Testing record light spell: {result}")
    except ImportError as error_message:
        print(error_message)