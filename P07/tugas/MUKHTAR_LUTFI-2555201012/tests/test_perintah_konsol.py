"""Pengujian penerjemah perintah konsol."""

from src.ui.perintah_konsol import terjemahkan_perintah


def test_perintah_kosong() -> None:
    assert terjemahkan_perintah("") == ("kosong",)


def test_perintah_bantuan() -> None:
    assert terjemahkan_perintah("bantuan") == ("bantuan",)


def test_perintah_tanda_tanya() -> None:
    assert terjemahkan_perintah("?") == ("bantuan",)


def test_perintah_daftar_valid() -> None:
    assert terjemahkan_perintah("daftar 5") == ("daftar", "5")


def test_perintah_tertinggi_valid() -> None:
    assert terjemahkan_perintah("tertinggi 5") == ("tertinggi", "5")


def test_perintah_terendah_valid() -> None:
    assert terjemahkan_perintah("terendah 5") == ("terendah", "5")


def test_perintah_total_valid() -> None:
    assert terjemahkan_perintah("total 5") == ("total", "5")


def test_perintah_daftar_tanpa_hari() -> None:
    assert terjemahkan_perintah("daftar") == ("perintah_tidak_valid",)


def test_perintah_daftar_hari_nol() -> None:
    assert terjemahkan_perintah("daftar 0") == ("perintah_tidak_valid",)


def test_perintah_daftar_hari_teks() -> None:
    assert terjemahkan_perintah("daftar lima") == ("perintah_tidak_valid",)


def test_perintah_daftar_terlalu_banyak_argumen() -> None:
    assert terjemahkan_perintah("daftar 5 besok") == ("perintah_tidak_valid",)


def test_perintah_tidak_dikenal() -> None:
    assert terjemahkan_perintah("hapus") == ("tidak_dikenal",)


def test_perintah_tidak_dikenal_dengan_argumen() -> None:
    assert terjemahkan_perintah("cetak semua") == ("tidak_dikenal",)


def test_perintah_tanpa_spasi_yang_benar() -> None:
    assert terjemahkan_perintah("daftar5") == ("tidak_dikenal",)


def test_spasi_perintah_tetap_diterima() -> None:
    assert terjemahkan_perintah("  daftar 5  ") == ("daftar", "5")
