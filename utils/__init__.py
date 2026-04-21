"""Utils package - collection of helper modules."""

__version__ = "0.1.0"

# Color utils
from .color_utils import (
    hex_to_rgb,
    rgb_to_hex,
    rgb_to_grayscale,
    is_dark,
    contrast_color,
)

# Dict utils
from .dict_utils import (
    deep_merge,
    flatten_keys,
    unflatten_keys,
    invert,
    filter_keys,
    omit_keys,
    map_values,
    map_keys,
    get_nested,
    set_nested,
)

# JSON utils
from .json_utils import (
    loads_safe,
    dumps_pretty,
    load_file,
    dump_file,
    get_path,
)

# String utils
from .string_utils import (
    truncate,
    is_palindrome,
    word_count,
    reverse_words,
    capitalize_words,
    strip_extra_spaces,
)

# Text utils
from .text_utils import (
    lines,
    bullet_list,
    indent,
    dedent,
    width_wrap,
)

# Number utils
from .number_utils import clamp, sign, is_even, is_odd, digits

# Retry
from .retry import retry, RetryError

# Math utils
from .math_utils import is_prime

# Roman
from .roman import to_roman, from_roman, RomanNumeralError

# Slugify
from .slugify import slugify, SlugifyError

# Duration
from .duration import (
    parse_duration,
    format_duration,
    multiply_duration,
    add_durations,
    subtract_durations,
    DurationFormatError,
)

# Validation utils
from .validation_utils import is_valid_email, is_valid_url, is_valid_phone

# Iterator / sequence utils
from .iter_utils import (
    batched,
    chunk,
    concat,
    cons,
    drop,
    drop_while,
    duplicates,
    duplicates_all,
    enumerate_from,
    first,
    flatten,
    flatten_depth,
    group_consecutive,
    interleave,
    last,
    nth,
    pad_none,
    pairwise,
    partition,
    run_length_encode,
    scan,
    sliding_window,
    spy,
    take,
    take_while,
    unique_ordered,
)

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
    # Iterator / sequence
    "batched",
    "chunk",
    "concat",
    "cons",
    "drop",
    "drop_while",
    "duplicates",
    "duplicates_all",
    "enumerate_from",
    "first",
    "flatten",
    "flatten_depth",
    "group_consecutive",
    "interleave",
    "last",
    "nth",
    "pad_none",
    "pairwise",
    "partition",
    "run_length_encode",
    "scan",
    "sliding_window",
    "spy",
    "take",
    "take_while",
    "unique_ordered",
]
