from utils.color_utils import (
    contrast_color,
    hex_to_rgb,
    is_dark,
    rgb_to_grayscale,
    rgb_to_hex,
)


def test_hex_to_rgb():
    assert hex_to_rgb("#ff0000") == (255, 0, 0)
    assert hex_to_rgb("0000ff") == (0, 0, 255)


def test_rgb_to_hex():
    assert rgb_to_hex(255, 0, 0) == "#ff0000"


def test_rgb_to_grayscale():
    assert rgb_to_grayscale(255, 255, 255) == 255
    assert rgb_to_grayscale(0, 0, 0) == 0


def test_is_dark():
    assert is_dark(0, 0, 0)
    assert not is_dark(255, 255, 255)


def test_contrast_color():
    assert contrast_color("#000000") == "#ffffff"
    assert contrast_color("#ffffff") == "#000000"
