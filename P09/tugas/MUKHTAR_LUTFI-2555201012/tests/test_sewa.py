"""Pengujian untuk transaksi, Enum, Protocol, dan daftar harga."""

import pytest
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.gerobak_dorong import GerobakDorong
from src.model.sewa import Sewa
from src.model.sewaan import Sewaan
from src.model.status_sewa import StatusSewa


def test_status_sewa_memiliki_empat_status() -> None:
    assert StatusSewa.DIPESAN.value == "Dipesan"
    assert StatusSewa.BERJALAN.value == "Berjalan"
    assert StatusSewa.SELESAI.value == "Selesai"
    assert StatusSewa.BATAL.value == "Batal"


def test_status_sewa_menolak_nilai_tidak_dikenal() -> None:
    with pytest.raises(ValueError):
        StatusSewa("Tidak dikenal")


def test_status_dipesan_boleh_diubah() -> None:
    assert StatusSewa.DIPESAN.boleh_diubah() is True


def test_status_berjalan_boleh_diubah() -> None:
    assert StatusSewa.BERJALAN.boleh_diubah() is True


def test_status_selesai_tidak_boleh_diubah() -> None:
    assert StatusSewa.SELESAI.boleh_diubah() is False


def test_status_batal_tidak_boleh_diubah() -> None:
    assert StatusSewa.BATAL.boleh_diubah() is False


def test_gerobak_dorong_memenuhi_protocol_sewaan() -> None:
    gerobak = GerobakDorong("GD-01", "Gerobak Dorong", 50_000)
    assert isinstance(gerobak, Sewaan)


def test_gerobak_dorong_bukan_turunan_alat_tani() -> None:

    gerobak = GerobakDorong("GD-02", "Gerobak Dorong", 50_000)
    assert not isinstance(gerobak, AlatTani)


def test_biaya_sewa_gerobak_dorong() -> None:
    gerobak = GerobakDorong("GD-03", "Gerobak Dorong", 50_000)
    assert gerobak.biaya_sewa(3) == 150_000


def test_daftar_harga_menerima_gerobak() -> None:
    daftar = DaftarHarga()
    gerobak = GerobakDorong("GD-04", "Gerobak Dorong", 50_000)

    daftar.tambah(gerobak)

    assert daftar.cari("GD-04") is gerobak


def test_daftar_harga_menolak_kode_duplikat() -> None:
    daftar = DaftarHarga()
    daftar.tambah(GerobakDorong("GD-05", "Gerobak Dorong", 50_000))

    with pytest.raises(ValueError):
        daftar.tambah(GerobakDorong("GD-05", "Gerobak Lain", 60_000))


def test_daftar_harga_menolak_objek_tidak_valid() -> None:
    daftar = DaftarHarga()

    with pytest.raises(TypeError):
        daftar.tambah(object())  # type: ignore[arg-type]


def test_transaksi_dimulai_dengan_status_dipesan() -> None:
    transaksi = Sewa("SW-01", "Mukhtar")
    assert transaksi.status is StatusSewa.DIPESAN


def test_transaksi_dapat_menambahkan_alat() -> None:
    transaksi = Sewa("SW-02", "Mukhtar")
    gerobak = GerobakDorong("GD-06", "Gerobak Dorong", 50_000)

    transaksi.tambah_alat(gerobak)

    assert gerobak in transaksi.daftar_alat


def test_transaksi_menghitung_total_biaya() -> None:
    transaksi = Sewa("SW-03", "Mukhtar")
    transaksi.tambah_alat(
        GerobakDorong("GD-07", "Gerobak Dorong", 50_000)
    )

    assert transaksi.total_biaya(3) == 150_000


def test_transaksi_menolak_alat_duplikat() -> None:
    transaksi = Sewa("SW-04", "Mukhtar")
    transaksi.tambah_alat(
        GerobakDorong("GD-08", "Gerobak Dorong", 50_000)
    )

    with pytest.raises(ValueError):
        transaksi.tambah_alat(
            GerobakDorong("GD-08", "Gerobak Lain", 60_000)
        )


def test_transaksi_selesai_menolak_penambahan_alat() -> None:
    transaksi = Sewa("SW-05", "Mukhtar")
    transaksi.ubah_status(StatusSewa.SELESAI)

    with pytest.raises(ValueError):
        transaksi.tambah_alat(
            GerobakDorong("GD-09", "Gerobak Dorong", 50_000)
        )


def test_transaksi_batal_menolak_penambahan_alat() -> None:
    transaksi = Sewa("SW-06", "Mukhtar")
    transaksi.ubah_status(StatusSewa.BATAL)

    with pytest.raises(ValueError):
        transaksi.tambah_alat(
            GerobakDorong("GD-10", "Gerobak Dorong", 50_000)
        )


def test_transaksi_selesai_menolak_perubahan_status() -> None:
    transaksi = Sewa("SW-07", "Mukhtar")
    transaksi.ubah_status(StatusSewa.SELESAI)

    with pytest.raises(ValueError):
        transaksi.ubah_status(StatusSewa.BATAL)


def test_transaksi_menolak_status_bukan_enum() -> None:
    transaksi = Sewa("SW-08", "Mukhtar")

    with pytest.raises(TypeError):
        transaksi.ubah_status("Selesai")  # type: ignore[arg-type]
