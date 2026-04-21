#!/usr/bin/env python3
"""Unified CLI for all utils modules."""

import argparse
import json
import sys

from . import (
    __version__,
    truncate,
    is_palindrome,
    word_count,
    reverse_words,
    capitalize_words,
    strip_extra_spaces,
    parse_duration,
    format_duration,
    multiply_duration,
    subtract_durations,
    dumps_pretty,
    loads_safe,
    hex_to_rgb,
    rgb_to_hex,
    contrast_color,
    slugify,
    to_roman,
    from_roman,
    is_valid_email,
    is_valid_url,
    is_valid_phone,
    clamp,
    is_prime,
    lines,
    bullet_list,
)

CLI_PROG = "utils"


def _cmd_string(parser):
    sub = parser.add_subparsers(dest="string_cmd", required=True)
    # truncate
    p = sub.add_parser("truncate", help="Truncate string to max length")
    p.add_argument("text", help="Text to truncate")
    p.add_argument("max_len", type=int, help="Max length")
    p.add_argument("--suffix", default="...", help="Suffix when truncated")
    # palindrome
    p = sub.add_parser("palindrome", help="Check if string is palindrome")
    p.add_argument("text", help="Text to check")
    # word_count
    p = sub.add_parser("word-count", help="Count words")
    p.add_argument("text", help="Text to count")
    # strip-spaces
    p = sub.add_parser("strip-spaces", help="Collapse extra whitespace")
    p.add_argument("text", help="Text to process")
    # reverse-words
    p = sub.add_parser("reverse-words", help="Reverse order of whitespace-separated words")
    p.add_argument("text", help="Text to process")
    # capitalize-words
    p = sub.add_parser("capitalize-words", help="Capitalize first letter of each word")
    p.add_argument("text", help="Text to process")


def _run_string(args):
    if args.string_cmd == "truncate":
        print(truncate(args.text, args.max_len, args.suffix))
    elif args.string_cmd == "palindrome":
        print(is_palindrome(args.text))
    elif args.string_cmd == "word-count":
        print(word_count(args.text))
    elif args.string_cmd == "strip-spaces":
        print(strip_extra_spaces(args.text))
    elif args.string_cmd == "reverse-words":
        print(reverse_words(args.text))
    elif args.string_cmd == "capitalize-words":
        print(capitalize_words(args.text))


def _cmd_duration(parser):
    sub = parser.add_subparsers(dest="duration_cmd", required=True)
    p = sub.add_parser("parse", help="Parse duration string to seconds")
    p.add_argument("duration", help='e.g. "1h 30m"')
    p = sub.add_parser("format", help="Format seconds to duration string")
    p.add_argument("seconds", type=int, help="Total seconds")
    p = sub.add_parser("multiply", help="Multiply duration by factor")
    p.add_argument("duration", help='e.g. "1h 30m"')
    p.add_argument("factor", type=float, help="Factor to multiply by")
    p = sub.add_parser("subtract", help="Subtract second duration from first")
    p.add_argument("a", help='Minuend, e.g. "2h 15m"')
    p.add_argument("b", help='Subtrahend, e.g. "45m"')


def _run_duration(args):
    if args.duration_cmd == "parse":
        print(parse_duration(args.duration))
    elif args.duration_cmd == "format":
        print(format_duration(args.seconds))
    elif args.duration_cmd == "multiply":
        print(multiply_duration(args.duration, args.factor))
    elif args.duration_cmd == "subtract":
        print(subtract_durations(args.a, args.b))


def _cmd_json(parser):
    sub = parser.add_subparsers(dest="json_cmd", required=True)
    p = sub.add_parser("pretty", help="Pretty-print JSON string")
    p.add_argument("json_str", help="JSON string")
    p = sub.add_parser("parse", help="Parse JSON string (prints Python repr)")
    p.add_argument("json_str", help="JSON string")


def _run_json(args):
    if args.json_cmd == "pretty":
        obj = loads_safe(args.json_str)
        if obj is None:
            print("Invalid JSON", file=sys.stderr)
            sys.exit(1)
        print(dumps_pretty(obj))
    elif args.json_cmd == "parse":
        obj = loads_safe(args.json_str)
        print(obj)


def _cmd_color(parser):
    sub = parser.add_subparsers(dest="color_cmd", required=True)
    p = sub.add_parser("hex-to-rgb", help="Convert hex to RGB")
    p.add_argument("hex", help="#RRGGBB or RRGGBB")
    p = sub.add_parser("rgb-to-hex", help="Convert RGB to hex")
    p.add_argument("r", type=int)
    p.add_argument("g", type=int)
    p.add_argument("b", type=int)
    p = sub.add_parser("contrast", help="Get contrast color (black or white)")
    p.add_argument("hex", help="#RRGGBB")


def _run_color(args):
    if args.color_cmd == "hex-to-rgb":
        print(hex_to_rgb(args.hex))
    elif args.color_cmd == "rgb-to-hex":
        print(rgb_to_hex(args.r, args.g, args.b))
    elif args.color_cmd == "contrast":
        print(contrast_color(args.hex))


def _cmd_slugify(parser):
    parser.add_argument("text", help="Text to slugify")


def _cmd_roman(parser):
    sub = parser.add_subparsers(dest="roman_cmd", required=True)
    p = sub.add_parser("to-roman", help="Convert number to Roman numeral")
    p.add_argument("n", type=int)
    p = sub.add_parser("from-roman", help="Convert Roman numeral to number")
    p.add_argument("roman", help="Roman numeral string")


def _run_roman(args):
    if args.roman_cmd == "to-roman":
        print(to_roman(args.n))
    elif args.roman_cmd == "from-roman":
        print(from_roman(args.roman))


def _cmd_validation(parser):
    sub = parser.add_subparsers(dest="validation_cmd", required=True)
    p = sub.add_parser("email", help="Validate email")
    p.add_argument("value", help="Email to validate")
    p = sub.add_parser("url", help="Validate URL")
    p.add_argument("value", help="URL to validate")
    p = sub.add_parser("phone", help="Validate phone")
    p.add_argument("value", help="Phone to validate")


def _run_validation(args):
    if args.validation_cmd == "email":
        print(is_valid_email(args.value))
    elif args.validation_cmd == "url":
        print(is_valid_url(args.value))
    elif args.validation_cmd == "phone":
        print(is_valid_phone(args.value))


def _cmd_number(parser):
    sub = parser.add_subparsers(dest="number_cmd", required=True)
    p = sub.add_parser("clamp", help="Clamp number to range")
    p.add_argument("n", type=float)
    p.add_argument("low", type=float)
    p.add_argument("high", type=float)
    p = sub.add_parser("is-prime", help="Check if number is prime")
    p.add_argument("n", type=int)


def _run_number(args):
    if args.number_cmd == "clamp":
        print(clamp(args.n, args.low, args.high))
    elif args.number_cmd == "is-prime":
        print(is_prime(args.n))


def _cmd_text(parser):
    sub = parser.add_subparsers(dest="text_cmd", required=True)
    p = sub.add_parser("lines", help="Split text into non-empty lines")
    p.add_argument("text", help="Text (use - for stdin)")
    p = sub.add_parser("bullet-list", help="Format as bullet list")
    p.add_argument("items", nargs="+", help="Items")
    p.add_argument("--bullet", default="-", help="Bullet character")


def _run_text(args):
    if args.text_cmd == "lines":
        text = sys.stdin.read() if args.text == "-" else args.text
        for ln in lines(text):
            print(ln)
    elif args.text_cmd == "bullet-list":
        print(bullet_list(args.items, args.bullet))


def main():
    ap = argparse.ArgumentParser(prog=CLI_PROG, description="Unified utils CLI")
    ap.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    sub = ap.add_subparsers(dest="module", required=True)

    # string
    p = sub.add_parser("string", help="String utilities")
    _cmd_string(p)

    # duration
    p = sub.add_parser("duration", help="Duration parse/format")
    _cmd_duration(p)

    # json
    p = sub.add_parser("json", help="JSON utilities")
    _cmd_json(p)

    # color
    p = sub.add_parser("color", help="Color utilities")
    _cmd_color(p)

    # slugify
    p = sub.add_parser("slugify", help="Slugify text")
    _cmd_slugify(p)

    # roman
    p = sub.add_parser("roman", help="Roman numeral conversion")
    _cmd_roman(p)

    # validation
    p = sub.add_parser("validation", help="Validation utilities")
    _cmd_validation(p)

    # number
    p = sub.add_parser("number", help="Number utilities")
    _cmd_number(p)

    # text
    p = sub.add_parser("text", help="Text utilities")
    _cmd_text(p)

    args = ap.parse_args()

    if args.module == "string":
        _run_string(args)
    elif args.module == "duration":
        _run_duration(args)
    elif args.module == "json":
        _run_json(args)
    elif args.module == "color":
        _run_color(args)
    elif args.module == "slugify":
        print(slugify(args.text))
    elif args.module == "roman":
        _run_roman(args)
    elif args.module == "validation":
        _run_validation(args)
    elif args.module == "number":
        _run_number(args)
    elif args.module == "text":
        _run_text(args)


if __name__ == "__main__":
    main()
