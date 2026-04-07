"""Utils package - collection of helper modules."""

__version__ = "0.1.0"

# Color utils
from .color_utils import (
    contrast_color,
    hex_to_rgb,
    is_dark,
    rgb_to_grayscale,
    rgb_to_hex,
)

# Dict utils
from .dict_utils import (
    deep_merge,
    filter_keys,
    flatten_keys,
    get_nested,
    invert,
    map_keys,
    map_values,
    omit_keys,
    set_nested,
    unflatten_keys,
)

# Duration
from .duration import (
    DurationFormatError,
    add_durations,
    format_duration,
    multiply_duration,
    parse_duration,
    subtract_durations,
)

# JSON utils
from .json_utils import (
    dump_file,
    dumps_pretty,
    get_path,
    load_file,
    loads_safe,
)

# Math utils
from .math_utils import is_prime

# Number utils
from .number_utils import clamp, digits, is_even, is_odd, sign

# Retry
from .retry import RetryError, retry

# Roman
from .roman import RomanNumeralError, from_roman, to_roman

# Slugify
from .slugify import SlugifyError, slugify

# String utils
from .string_utils import (
    capitalize_words,
    is_palindrome,
    reverse_words,
    strip_extra_spaces,
    truncate,
    word_count,
)

# Text utils
from .text_utils import (
    bullet_list,
    dedent,
    indent,
    lines,
    width_wrap,
)

# Validation utils
from .validation_utils import is_valid_email, is_valid_phone, is_valid_url

__all__ = [
    "__version__",
    # Color
    "hex_to_rgb",
    "rgb_to_hex",
    "rgb_to_grayscale",
    "is_dark",
    "contrast_color",
    # Dict
    "deep_merge",
    "flatten_keys",
    "unflatten_keys",
    "invert",
    "filter_keys",
    "omit_keys",
    "map_values",
    "map_keys",
    "get_nested",
    "set_nested",
    # JSON
    "loads_safe",
    "dumps_pretty",
    "load_file",
    "dump_file",
    "get_path",
    # String
    "truncate",
    "is_palindrome",
    "word_count",
    "reverse_words",
    "capitalize_words",
    "strip_extra_spaces",
    # Text
    "lines",
    "bullet_list",
    "indent",
    "dedent",
    "width_wrap",
    # Number
    "clamp",
    "sign",
    "is_even",
    "is_odd",
    "digits",
    # Retry
    "retry",
    "RetryError",
    # Math
    "is_prime",
    # Roman
    "to_roman",
    "from_roman",
    "RomanNumeralError",
    # Slugify
    "slugify",
    "SlugifyError",
    # Duration
    "parse_duration",
    "format_duration",
    "multiply_duration",
    "add_durations",
    "subtract_durations",
    "DurationFormatError",
    # Validation
    "is_valid_email",
    "is_valid_url",
    "is_valid_phone",
]
