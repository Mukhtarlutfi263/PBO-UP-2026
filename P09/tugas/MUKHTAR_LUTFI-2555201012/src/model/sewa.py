"""Model transaksi penyewaan alat pertanian."""

from src.model.sewaan import Sewaan
from src.model.status_sewa import StatusSewa


class Sewa:
    """Mengelola transaksi penyewaan beberapa objek."""

    def __init__(self, kode: str, penyewa: str) -> None:
        if not kode.strip():
            raise ValueError("Kode transaksi tidak boleh kosong.")
        if not penyewa.strip():
            raise ValueError("Nama penyewa tidak boleh kosong.")

        self._kode = kode.strip()
        self._penyewa = penyewa.strip()
        self._status = StatusSewa.DIPESAN
        self._daftar_alat: list[Sewaan] = []

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def penyewa(self) -> str:
        return self._penyewa

    @property
    def status(self) -> StatusSewa:
        return self._status

    @property
    def daftar_alat(self) -> tuple[Sewaan, ...]:
        return tuple(self._daftar_alat)

    def ubah_status(self, status: StatusSewa) -> None:
        """Mengubah status transaksi."""
        if not isinstance(status, StatusSewa):
            raise TypeError("Status harus berupa StatusSewa.")

        if not self._status.boleh_diubah():
            raise ValueError("Transaksi yang sudah selesai tidak dapat diubah.")

        self._status = status

    def tambah_alat(self, alat: Sewaan) -> None:
        """Menambahkan alat ke transaksi yang masih dapat diubah."""
        if not self._status.boleh_diubah():
            raise ValueError("Tidak dapat menambah alat pada transaksi ini.")

        if not isinstance(alat, Sewaan):
            raise TypeError("Objek tidak memenuhi kontrak Sewaan.")

        if any(item.kode == alat.kode for item in self._daftar_alat):
            raise ValueError(f"Alat dengan kode {alat.kode} sudah ditambahkan.")

        self._daftar_alat.append(alat)

    def total_biaya(self, jumlah_hari: int) -> int:
        """Menghitung total biaya seluruh alat dalam transaksi."""
        if not isinstance(jumlah_hari, int) or isinstance(jumlah_hari, bool):
            raise TypeError("Jumlah hari harus berupa bilangan bulat.")
        if jumlah_hari < 0:
            raise ValueError("Jumlah hari tidak boleh negatif.")

        return sum(
            alat.biaya_sewa(jumlah_hari)
            for alat in self._daftar_alat
        )
