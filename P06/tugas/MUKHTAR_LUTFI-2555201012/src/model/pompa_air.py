
"""Model alat pertanian berupa pompa air."""

from typing import Final

from .alat_tani import AlatTani


class PompaAir(AlatTani):
    """Pompa air dengan tambahan biaya bahan bakar."""

    HARGA_SOLAR_PER_LITER: Final[int] = 7_000
    LITER_PER_SERATUS_DEBIT: Final[int] = 3

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        debit: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if not isinstance(debit, int) or isinstance(debit, bool):
            raise TypeError("Debit pompa harus berupa bilangan bulat.")
        if debit <= 0:
            raise ValueError("Debit pompa harus lebih dari nol.")

        self._debit = debit

    @property
    def debit(self) -> int:
        return self._debit

    def konsumsi_solar_harian(self) -> int:
        """Menghitung konsumsi solar berdasarkan debit pompa."""
        return (
            self._debit * PompaAir.LITER_PER_SERATUS_DEBIT
        ) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa termasuk biaya solar."""
        dasar = super().biaya_sewa(jumlah_hari)
        solar = (
            self.konsumsi_solar_harian()
            * PompaAir.HARGA_SOLAR_PER_LITER
        )
        return dasar + solar * jumlah_hari

    def keterangan(self) -> str:
        """Menampilkan informasi khusus pompa air."""
        return (
            f"{super().keterangan()} · {self.debit} L/mnt "
            f"· ±{self.konsumsi_solar_harian()} L solar/hari"
        )
