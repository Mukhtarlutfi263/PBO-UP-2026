
"""Pengujian untuk kelas induk AlatTani."""

import pytest
from src.model.alat_tani import AlatTani


def test_data_alat_tani_valid() -> None:
    alat = AlatTani("AT-01", "Cangkul", 50_000)

    assert alat.kode == "AT-01"
    assert alat.nama == "Cangkul"
    assert alat.tarif_harian == 50_000


def test_biaya_sewa() -> None:
    alat = AlatTani("AT-02", "Cangkul", 50_000)

    assert alat.biaya_sewa(3) == 150_000


def test_biaya_sewa_nol_hari() -> None:
    alat = AlatTani("AT-03", "Cangkul", 50_000)

    assert alat.biaya_sewa(0) == 0


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("", "Cangkul", 50_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("AT-04", "", 50_000)


def test_tarif_di_bawah_minimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("AT-05", "Cangkul", 5_000)


def test_tarif_di_atas_maksimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("AT-06", "Cangkul", 6_000_000)


def test_jumlah_hari_negatif_ditolak() -> None:
    alat = AlatTani("AT-07", "Cangkul", 50_000)

    with pytest.raises(ValueError):
        alat.biaya_sewa(-1)


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150_000) == "Rp150.000"


def test_dua_alat_dengan_kode_sama_dianggap_sama() -> None:
    alat1 = AlatTani("AT-08", "Cangkul", 50_000)
    alat2 = AlatTani("AT-08", "Cangkul Besar", 75_000)

    assert alat1 == alat2


def test_objek_bisa_digunakan_sebagai_kunci_dictionary() -> None:
    alat = AlatTani("AT-09", "Cangkul", 50_000)
    data = {alat: "Tersedia"}

    assert data[alat] == "Tersedia"
