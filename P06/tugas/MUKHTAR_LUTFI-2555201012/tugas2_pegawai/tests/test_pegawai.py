
"""Pengujian untuk kelas Pegawai dan kelas turunannya."""

import pytest
from src.model.pegawai import Pegawai
from src.model.pegawai_harian import PegawaiHarian
from src.model.pegawai_kontrak import PegawaiKontrak
from src.model.pegawai_tetap import PegawaiTetap

HASIL_GAJI_DASAR = 3_000_000
HASIL_PEGAWAI_TETAP = 3_500_000
HASIL_PEGAWAI_HARIAN = 2_500_000
HASIL_PEGAWAI_KONTRAK = 2_640_000


def test_pegawai_menghitung_penghasilan() -> None:
    pegawai = Pegawai("001", "Andi", 150_000)
    assert pegawai.hitung_penghasilan(20) == HASIL_GAJI_DASAR


def test_pegawai_menampilkan_nama_dan_nip() -> None:
    pegawai = Pegawai("001", "Andi", 150_000)
    assert str(pegawai) == "Andi (NIP: 001)"


def test_pegawai_memiliki_repr() -> None:
    pegawai = Pegawai("001", "Andi", 150_000)
    assert "Pegawai" in repr(pegawai)
    assert "001" in repr(pegawai)


def test_dua_pegawai_dengan_nip_sama_dianggap_sama() -> None:
    pegawai1 = Pegawai("001", "Andi", 150_000)
    pegawai2 = Pegawai("001", "Budi", 200_000)
    assert pegawai1 == pegawai2


def test_pegawai_memiliki_hash_yang_sama() -> None:
    pegawai1 = Pegawai("001", "Andi", 150_000)
    pegawai2 = Pegawai("001", "Budi", 200_000)
    assert hash(pegawai1) == hash(pegawai2)


def test_pegawai_tetap_mendapat_tunjangan() -> None:
    pegawai = PegawaiTetap("002", "Budi", 150_000, 500_000)
    assert pegawai.hitung_penghasilan(20) == HASIL_PEGAWAI_TETAP


def test_pegawai_harian_menggunakan_tarif_harian() -> None:
    pegawai = PegawaiHarian("003", "Citra", 100_000, 125_000)
    assert pegawai.hitung_penghasilan(20) == HASIL_PEGAWAI_HARIAN


def test_pegawai_kontrak_menambah_hari_kerja() -> None:
    pegawai = PegawaiKontrak("004", "Dedi", 120_000, 2)
    assert pegawai.hitung_penghasilan(20) == HASIL_PEGAWAI_KONTRAK


def test_nip_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Andi", 150_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("001", "", 150_000)


def test_gaji_pokok_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("001", "Andi", 0)


def test_gaji_pokok_bukan_bilangan_bulat_ditolak() -> None:
    with pytest.raises(TypeError):
        Pegawai("001", "Andi", 150_000.5)


def test_jumlah_hari_nol_ditolak() -> None:
    pegawai = Pegawai("001", "Andi", 150_000)
    with pytest.raises(ValueError):
        pegawai.hitung_penghasilan(0)


def test_tunjangan_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiTetap("002", "Budi", 150_000, -100_000)


def test_tarif_harian_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiHarian("003", "Citra", 100_000, 0)


def test_hari_tambahan_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiKontrak("004", "Dedi", 120_000, -2)

def test_pegawai_dapat_menjadi_kunci_dict() -> None:
    pegawai = Pegawai("001", "Andi", 150_000)
    catatan = {pegawai: "Sedang bekerja"}

    assert catatan[pegawai] == "Sedang bekerja"
