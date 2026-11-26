
"""Pengujian untuk kelas induk abstrak AlatTani."""

import pytest
from src.model.alat_tani import AlatTani


class AlatTaniUji(AlatTani):
    """Kelas konkret untuk membantu pengujian AlatTani."""

    def biaya_tambahan(self, _jumlah_hari: int) -> int:
        """Tidak ada biaya tambahan pada alat pengujian."""
        return 0

    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat penggunaan alat pengujian."""
        return "Tidak ada syarat khusus."


def test_alat_tani_merupakan_kelas_abstrak() -> None:
    with pytest.raises(TypeError):
        AlatTani("AT-01", "Cangkul", 50_000)  # type: ignore[abstract]


def test_data_alat_tani_valid() -> None:
    alat = AlatTaniUji("AT-01", "Cangkul", 50_000)
    assert alat.kode == "AT-01"
    assert alat.nama == "Cangkul"
    assert alat.tarif_harian == 50_000


def test_biaya_sewa() -> None:
    alat = AlatTaniUji("AT-02", "Cangkul", 50_000)
    assert alat.biaya_sewa(2) == 100_000


def test_biaya_sewa_nol_hari() -> None:
    alat = AlatTaniUji("AT-03", "Cangkul", 50_000)
    assert alat.biaya_sewa(0) == 0


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTaniUji("", "Cangkul", 50_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTaniUji("AT-04", "", 50_000)


def test_tarif_di_bawah_minimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTaniUji("AT-05", "Cangkul", 5_000)


def test_tarif_di_atas_maksimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTaniUji("AT-06", "Cangkul", 6_000_000)


def test_jumlah_hari_negatif_ditolak() -> None:
    alat = AlatTaniUji("AT-07", "Cangkul", 50_000)
    with pytest.raises(ValueError):
        alat.biaya_sewa(-1)


def test_dua_alat_dengan_kode_sama_dianggap_sama() -> None:
    alat1 = AlatTaniUji("AT-08", "Cangkul", 50_000)
    alat2 = AlatTaniUji("AT-08", "Cangkul Besar", 75_000)
    assert alat1 == alat2


def test_objek_bisa_digunakan_sebagai_kunci_dictionary() -> None:
    alat = AlatTaniUji("AT-09", "Cangkul", 50_000)
    data = {alat: "Tersedia"}
    assert data[alat] == "Tersedia"
