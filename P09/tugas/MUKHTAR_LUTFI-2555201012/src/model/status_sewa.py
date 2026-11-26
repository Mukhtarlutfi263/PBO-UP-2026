"""Status transaksi penyewaan alat pertanian."""

from enum import Enum


class StatusSewa(Enum):
    """Daftar status yang tersedia dalam transaksi penyewaan."""

    DIPESAN = "Dipesan"
    BERJALAN = "Berjalan"
    SELESAI = "Selesai"
    BATAL = "Batal"

    def boleh_diubah(self) -> bool:
        """Memeriksa apakah transaksi masih boleh diubah."""
        return self in (StatusSewa.DIPESAN, StatusSewa.BERJALAN)
