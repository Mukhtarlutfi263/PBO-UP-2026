"""Pengujian penyusun laporan penghasilan pegawai."""

import pytest
from src.model.pegawai import Pegawai
from src.model.pegawai_harian import PegawaiHarian
from src.model.pegawai_kontrak import PegawaiKontrak
from src.model.pegawai_tetap import PegawaiTetap
from src.model.penyusun_laporan import PenyusunLaporan


@pytest.fixture
def laporan() -> PenyusunLaporan:
    """Menyediakan contoh laporan pegawai."""
    pegawai: list[Pegawai] = [
        PegawaiTetap("001", "Andi", 150000, 500000),
        PegawaiKontrak("002", "Budi", 120000, 2),
        PegawaiHarian("003", "Citra", 100000, 80000),
    ]
    return PenyusunLaporan(pegawai)


def test_rekap_penghasilan(laporan: PenyusunLaporan) -> None:
    hasil = laporan.rekap_penghasilan(5)
    assert hasil == [
        ("Andi", 1250000),
        ("Budi", 840000),
        ("Citra", 400000),
    ]


def test_penghasilan_tertinggi(laporan: PenyusunLaporan) -> None:
    assert laporan.penghasilan_tertinggi(5) == ("Andi", 1250000)


def test_penghasilan_terendah(laporan: PenyusunLaporan) -> None:
    assert laporan.penghasilan_terendah(5) == ("Citra", 400000)


def test_total_penghasilan(laporan: PenyusunLaporan) -> None:
    assert laporan.total_penghasilan(5) == 2490000


def test_daftar_pegawai_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        PenyusunLaporan([])


def test_jumlah_hari_nol_ditolak(laporan: PenyusunLaporan) -> None:
    with pytest.raises(ValueError):
        laporan.rekap_penghasilan(0)


def test_jumlah_hari_negatif_ditolak(laporan: PenyusunLaporan) -> None:
    with pytest.raises(ValueError):
        laporan.rekap_penghasilan(-1)


def test_jumlah_hari_bukan_bilangan_bulat_ditolak(
    laporan: PenyusunLaporan,
) -> None:
    with pytest.raises(TypeError):
        laporan.rekap_penghasilan(2.5)  # type: ignore[arg-type]


def test_pegawai_keempat_tetap_bisa_diproses() -> None:
    class PegawaiMagang(Pegawai):
        """Jenis pegawai tambahan untuk membuktikan polymorphism."""

        def hitung_penghasilan(self, jumlah_hari: int) -> int:
            return super().hitung_penghasilan(jumlah_hari) + 10000

    pegawai = PegawaiMagang("004", "Doni", 50000)
    laporan = PenyusunLaporan([pegawai])

    assert laporan.rekap_penghasilan(2) == [("Doni", 110000)]


def test_rekap_tidak_mengubah_daftar_asli() -> None:
    pegawai = PegawaiTetap("005", "Eka", 100000, 20000)
    daftar: list[Pegawai] = [pegawai]
    laporan = PenyusunLaporan(daftar)

    laporan.rekap_penghasilan(3)

    assert daftar == [pegawai]


def test_dua_pegawai_dengan_nip_berbeda() -> None:
    pegawai: list[Pegawai] = [
        PegawaiTetap("006", "Fajar", 100000, 0),
        PegawaiTetap("007", "Gina", 120000, 0),
    ]
    laporan = PenyusunLaporan(pegawai)

    assert laporan.total_penghasilan(2) == 440000
