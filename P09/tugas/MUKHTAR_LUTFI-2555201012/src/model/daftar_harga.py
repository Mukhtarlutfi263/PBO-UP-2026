"""Pengelolaan daftar harga untuk seluruh objek yang dapat disewakan."""

from src.model.sewaan import Sewaan


class DaftarHarga:
    """Menyimpan dan menampilkan daftar objek yang memenuhi kontrak Sewaan."""

    def __init__(self) -> None:
        self._daftar: list[Sewaan] = []

    def tambah(self, barang: Sewaan) -> None:
        """Menambahkan objek ke daftar harga."""
        if not isinstance(barang, Sewaan):
            raise TypeError("Objek tidak memenuhi kontrak Sewaan.")

        if any(item.kode == barang.kode for item in self._daftar):
            raise ValueError(f"Kode {barang.kode} sudah terdaftar.")

        self._daftar.append(barang)

    def semua(self) -> tuple[Sewaan, ...]:
        """Mengembalikan seluruh daftar sebagai tuple."""
        return tuple(self._daftar)

    def cari(self, kode: str) -> Sewaan:
        """Mencari objek berdasarkan kode."""
        for barang in self._daftar:
            if barang.kode == kode:
                return barang

        raise ValueError(f"Barang dengan kode {kode} tidak ditemukan.")

    def tampilkan(self) -> None:
        """Menampilkan informasi dan biaya sewa setiap objek."""
        for barang in self._daftar:
            print(barang.keterangan())
            print(
                f"    1 hari: "
                f"Rp{barang.biaya_sewa(1):,}".replace(",", ".")
                + f"      3 hari: "
                f"Rp{barang.biaya_sewa(3):,}".replace(",", ".")
            )
