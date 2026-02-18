class DurationFormatError(ValueError):
    pass


_TIME_UNITS = {
    "h": 3600,
    "m": 60,
    "s": 1,
}


def parse_duration(duration: str) -> int:
    """
    Parse duration string like:
    "1h 30m 15s"
    into total seconds.
    """
    if not duration or not isinstance(duration, str):
        raise DurationFormatError("Invalid duration format")

    parts = duration.strip().split()
    total_seconds = 0
    seen_units = set()

    for part in parts:
        if len(part) < 2:
            raise DurationFormatError("Invalid duration segment")

        value_part = part[:-1]
        unit = part[-1]

        if unit not in _TIME_UNITS:
            raise DurationFormatError(f"Invalid time unit: {unit}")

        if unit in seen_units:
            raise DurationFormatError(f"Duplicate unit: {unit}")

        if not value_part.isdigit():
            raise DurationFormatError("Invalid numeric value")

        total_seconds += int(value_part) * _TIME_UNITS[unit]
        seen_units.add(unit)

    return total_seconds


def format_duration(seconds: int) -> str:
    """
    Convert seconds into formatted duration string.
    Example: 5400 -> "1h 30m"
    """
    if not isinstance(seconds, int) or seconds < 0:
        raise DurationFormatError("Seconds must be non-negative integer")

    if seconds == 0:
        return "0s"

    parts = []

    for unit, multiplier in _TIME_UNITS.items():
        value = seconds // multiplier
        if value > 0:
            parts.append(f"{value}{unit}")
            seconds -= value * multiplier

    return " ".join(parts)
