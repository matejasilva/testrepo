import tempfile
import os

from file_utils import safe_filename, split_extension, ensure_dir, file_size_human, path_parts


def test_safe_filename():
    assert "a_b_c" in safe_filename('a<>b"c')
    assert safe_filename("  x  ") == "x"


def test_split_extension():
    base, ext = split_extension("/path/to/file.txt")
    assert ext == ".txt"
    base2, ext2 = split_extension("archive.tar.gz")
    assert ext2 == ".tar.gz"


def test_ensure_dir():
    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(tmp, "sub", "dir")
        ensure_dir(p)
        assert os.path.isdir(p)


def test_file_size_human():
    assert "1.0KB" in file_size_human(1024) or "1024" in file_size_human(1024)


def test_path_parts():
    assert path_parts("a/b/c") == ["a", "b", "c"]
    assert path_parts("a\\b\\c") == ["a", "b", "c"]
