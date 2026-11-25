"""Pengujian fungsi format nilai dengan singledispatch."""

from src.format_nilai import sebagai_teks


def test_format_bilangan_bulat() -> None:
    assert sebagai_teks(150000) == "Rp150.000"


def test_format_bilangan_bulat_nol() -> None:
    assert sebagai_teks(0) == "Rp0"


def test_format_bilangan_desimal() -> None:
    assert sebagai_teks(75.5) == "75.5%"


def test_format_teks() -> None:
    assert sebagai_teks("Laporan Pegawai") == "Laporan Pegawai"


def test_format_tipe_data_lain() -> None:
    assert sebagai_teks(True) == "True"
