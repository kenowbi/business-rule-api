def validate_source(source: str) -> bool:
    available_locations =["IBE", "MMB", "FLAIROCI", "Airport", "FLAIRMIS", "FLAIRDIR", "FLAIRIND"]
    if source in available_locations:
        return True
    return False