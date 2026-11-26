
"""Model alat pertanian berupa pompa air."""

from __future__ import annotations

from typing import Final

from .alat_tani import AlatTani


class PompaAir(AlatTani):
    """Pompa air dengan tambahan biaya bahan bakar."""

    HARGA_SOLAR_PER_LITER: Final[int] = 7_000
    LITER_PER_SERATUS_DEBIT: Final[int] = 3
    JUMLAH_KOLOM_CSV: Final[int] = 4

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

    @classmethod
    def dari_baris_csv(cls, baris: str) -> PompaAir:
        """Membuat objek PompaAir dari satu baris CSV."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError(
                "Baris CSV PompaAir harus berisi kode, nama, "
                "tarif harian, dan debit."
            )

        kode, nama, tarif_teks, debit_teks = bagian

        try:
            tarif = int(tarif_teks.strip())
            debit = int(debit_teks.strip())
        except ValueError:
            raise ValueError(
                "Tarif dan debit harus berupa angka."
            ) from None

        return cls(kode.strip(), nama.strip(), tarif, debit)

    @property
    def debit(self) -> int:
        return self._debit

    def konsumsi_solar_harian(self) -> int:
        """Menghitung konsumsi solar berdasarkan debit pompa."""
        return (
            self._debit * self.LITER_PER_SERATUS_DEBIT
        ) // 100

    def biaya_tambahan(self, jumlah_hari: int) -> int:
        """Menghitung biaya solar berdasarkan jumlah hari."""
        solar = (
            self.konsumsi_solar_harian()
            * self.HARGA_SOLAR_PER_LITER
        )
        return solar * jumlah_hari

    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat penggunaan pompa air."""
        return "Pastikan sumber air dan bahan bakar tersedia."

    def keterangan(self) -> str:
        """Menampilkan informasi khusus pompa air."""
        return (
            f"{super().keterangan()} · {self.debit} L/mnt "
            f"· ±{self.konsumsi_solar_harian()} L solar/hari"
        )
