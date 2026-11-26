"""Pengujian untuk kelas turunan AlatTani."""

import pytest
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor

# Pengujian Traktor

def test_traktor_valid() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150_000, 8)
    assert alat.tenaga_kuda == 8


def test_traktor_biaya_sewa_satu_hari() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150_000, 8)
    assert alat.biaya_sewa(1) == 250_000


def test_traktor_biaya_sewa_tiga_hari() -> None:
    alat = Traktor("TR-02", "Traktor Kubota", 150_000, 8)
    assert alat.biaya_sewa(3) == 750_000


def test_traktor_tenaga_kuda_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-03", "Traktor Kubota", 150_000, 0)


def test_traktor_tenaga_kuda_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-04", "Traktor Kubota", 150_000, -5)


def test_traktor_validasi_tarif_induk() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-05", "Traktor Kubota", 5_000, 8)


# Pengujian PompaAir

def test_pompa_air_valid() -> None:
    alat = PompaAir("PA-01", "Pompa Air", 75_000, 600)
    assert alat.debit == 600


def test_pompa_air_konsumsi_solar() -> None:
    alat = PompaAir("PA-02", "Pompa Air", 75_000, 600)
    assert alat.konsumsi_solar_harian() == 18


def test_pompa_air_biaya_sewa_satu_hari() -> None:
    alat = PompaAir("PA-03", "Pompa Air", 75_000, 600)
    assert alat.biaya_sewa(1) == 201_000


def test_pompa_air_debit_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-04", "Pompa Air", 75_000, 0)


def test_pompa_air_debit_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-05", "Pompa Air", 75_000, -100)


def test_pompa_air_debit_teks_ditolak() -> None:
    with pytest.raises(TypeError):
        PompaAir("PA-06", "Pompa Air", 75_000, "600")  # type: ignore[arg-type]


# Pengujian Perontok

def test_perontok_valid() -> None:
    alat = Perontok("PR-01", "Mesin Perontok", 200_000, 900)
    assert alat.kapasitas == 900


def test_perontok_minimum_dua_hari() -> None:
    alat = Perontok("PR-02", "Mesin Perontok", 200_000, 900)
    assert alat.biaya_sewa(1) == 400_000


def test_perontok_biaya_tiga_hari() -> None:
    alat = Perontok("PR-03", "Mesin Perontok", 200_000, 900)
    assert alat.biaya_sewa(3) == 600_000


def test_perontok_kapasitas_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-04", "Mesin Perontok", 200_000, 0)


def test_perontok_kapasitas_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-05", "Mesin Perontok", 200_000, -100)


def test_perontok_validasi_tarif_induk() -> None:
    with pytest.raises(ValueError):
        Perontok("PR-06", "Mesin Perontok", 5_000, 900)


 # Pengujian method khusus

def test_str_traktor() -> None:
    alat = Traktor("TR-10", "Traktor Kubota", 150_000, 8)
    assert "[TR-10]" in str(alat)
    assert "8 HP" in str(alat)


def test_repr_traktor() -> None:
    alat = Traktor("TR-11", "Traktor Kubota", 150_000, 8)
    assert "Traktor(" in repr(alat)
    assert "TR-11" in repr(alat)


def test_str_pompa_air() -> None:
    alat = PompaAir("PA-10", "Pompa Air", 75_000, 600)
    assert "[PA-10]" in str(alat)
    assert "600 L/mnt" in str(alat)


def test_str_perontok() -> None:
    alat = Perontok("PR-10", "Mesin Perontok", 200_000, 900)
    assert "[PR-10]" in str(alat)
    assert "minimum 2 hari" in str(alat)


def test_dua_traktor_kode_sama_dianggap_sama() -> None:
    alat1 = Traktor("TR-20", "Traktor Kubota", 150_000, 8)
    alat2 = Traktor("TR-20", "Traktor Lain", 200_000, 10)
    assert alat1 == alat2


def test_dua_pompa_kode_berbeda_tidak_sama() -> None:
    alat1 = PompaAir("PA-20", "Pompa Air", 75_000, 600)
    alat2 = PompaAir("PA-21", "Pompa Air", 75_000, 600)
    assert alat1 != alat2


def test_traktor_dibandingkan_dengan_teks() -> None:
    alat = Traktor("TR-30", "Traktor Kubota", 150_000, 8)
    assert alat != "TR-30"


def test_hash_traktor() -> None:
    alat = Traktor("TR-40", "Traktor Kubota", 150_000, 8)
    assert hash(alat) == hash("TR-40")


def test_traktor_sebagai_kunci_dict() -> None:
    alat1 = Traktor("TR-50", "Traktor Kubota", 150_000, 8)
    alat2 = Traktor("TR-50", "Traktor Lain", 200_000, 10)
    data = {alat1: "Sedang disewa"}

    assert data[alat2] == "Sedang disewa"


def test_pompa_air_sebagai_kunci_dict() -> None:
    alat = PompaAir("PA-50", "Pompa Air", 75_000, 600)
    data = {alat: "Tersedia"}

    assert data[alat] == "Tersedia"


def test_perontok_sebagai_kunci_dict() -> None:
    alat = Perontok("PR-50", "Mesin Perontok", 200_000, 900)
    data = {alat: "Tersedia"}

    assert data[alat] == "Tersedia"


 # Pengujian validasi dan perhitungan tambahan

def test_traktor_biaya_sewa_nol_hari() -> None:
    alat = Traktor("TR-60", "Traktor Kubota", 150_000, 8)
    assert alat.biaya_sewa(0) == 0


def test_traktor_biaya_sewa_hari_negatif_ditolak() -> None:
    alat = Traktor("TR-61", "Traktor Kubota", 150_000, 8)
    with pytest.raises(ValueError):
        alat.biaya_sewa(-1)


def test_traktor_tenaga_kuda_teks_ditolak() -> None:
    with pytest.raises(TypeError):
        Traktor("TR-62", "Traktor Kubota", 150_000, "delapan")  # type: ignore[arg-type]


def test_pompa_air_biaya_sewa_tiga_hari() -> None:
    alat = PompaAir("PA-60", "Pompa Air", 75_000, 600)
    assert alat.biaya_sewa(3) == 603_000


def test_pompa_air_biaya_sewa_nol_hari() -> None:
    alat = PompaAir("PA-61", "Pompa Air", 75_000, 600)
    assert alat.biaya_sewa(0) == 0


def test_pompa_air_biaya_sewa_hari_negatif_ditolak() -> None:
    alat = PompaAir("PA-62", "Pompa Air", 75_000, 600)
    with pytest.raises(ValueError):
        alat.biaya_sewa(-1)


def test_pompa_air_debit_float_ditolak() -> None:
    with pytest.raises(TypeError):
        PompaAir("PA-63", "Pompa Air", 75_000, 600.5)  # type: ignore[arg-type]


def test_perontok_biaya_sewa_nol_hari() -> None:
    alat = Perontok("PR-60", "Mesin Perontok", 200_000, 900)
    assert alat.biaya_sewa(0) == 400_000


def test_perontok_biaya_sewa_hari_negatif_ditolak() -> None:
    alat = Perontok("PR-61", "Mesin Perontok", 200_000, 900)
    with pytest.raises(ValueError):
        alat.biaya_sewa(-1)


def test_perontok_kapasitas_teks_ditolak() -> None:
    with pytest.raises(TypeError):
        Perontok("PR-62", "Mesin Perontok", 200_000, "sembilan ratus")  # type: ignore[arg-type]


def test_perontok_kapasitas_float_ditolak() -> None:
    with pytest.raises(TypeError):
        Perontok("PR-63", "Mesin Perontok", 200_000, 900.5)  # type: ignore[arg-type]


def test_perontok_hari_ditagih_satu_hari() -> None:
    alat = Perontok("PR-64", "Mesin Perontok", 200_000, 900)
    assert alat.hari_ditagih(1) == 2
