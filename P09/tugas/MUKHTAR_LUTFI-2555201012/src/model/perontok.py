
"""Model alat pertanian berupa mesin perontok padi."""

from __future__ import annotations

from typing import Final

from .alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok padi dengan minimum dua hari sewa."""

    MINIMUM_HARI_SEWA: Final[int] = 2
    JUMLAH_KOLOM_CSV: Final[int] = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        kapasitas: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if not isinstance(kapasitas, int) or isinstance(kapasitas, bool):
            raise TypeError("Kapasitas harus berupa bilangan bulat.")
        if kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari nol.")

        self._kapasitas = kapasitas

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Perontok:
        """Membuat objek Perontok dari satu baris CSV."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV:
            raise ValueError(
                "Baris CSV Perontok harus berisi kode, nama, "
                "tarif harian, dan kapasitas."
            )

        kode, nama, tarif_teks, kapasitas_teks = bagian

        try:
            tarif = int(tarif_teks.strip())
            kapasitas = int(kapasitas_teks.strip())
        except ValueError:
            raise ValueError(
                "Tarif dan kapasitas harus berupa angka."
            ) from None

        return cls(kode.strip(), nama.strip(), tarif, kapasitas)

    @property
    def kapasitas(self) -> int:
        return self._kapasitas

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Menentukan jumlah hari yang harus dibayar."""
        if not isinstance(jumlah_hari, int) or isinstance(jumlah_hari, bool):
            raise TypeError("Jumlah hari harus berupa bilangan bulat.")
        if jumlah_hari < 0:
            raise ValueError("Jumlah hari tidak boleh negatif.")
        return max(jumlah_hari, self.MINIMUM_HARI_SEWA)

    def biaya_tambahan(self, _jumlah_hari: int) -> int:
        """Mesin perontok tidak memiliki biaya tambahan."""
        return 0

    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat penggunaan mesin perontok."""
        return "Gunakan di tempat yang datar dan kering."

    def keterangan(self) -> str:
        """Menampilkan informasi khusus mesin perontok."""
        return (
            f"{super().keterangan()} · {self.kapasitas} kg/jam "
            f"· minimum {self.MINIMUM_HARI_SEWA} hari"
        )
