
"""Model alat pertanian berupa mesin perontok padi."""

from typing import Final

from .alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok padi dengan minimum dua hari sewa."""

    MINIMUM_HARI_SEWA: Final[int] = 2

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

    @property
    def kapasitas(self) -> int:
        return self._kapasitas

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Menentukan jumlah hari yang harus dibayar."""
        if not isinstance(jumlah_hari, int) or isinstance(jumlah_hari, bool):
            raise TypeError("Jumlah hari harus berupa bilangan bulat.")
        if jumlah_hari < 0:
            raise ValueError("Jumlah hari tidak boleh negatif.")
        return max(jumlah_hari, Perontok.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya dengan ketentuan minimum dua hari."""
        return super().biaya_sewa(self.hari_ditagih(jumlah_hari))

    def keterangan(self) -> str:
        """Menampilkan informasi khusus mesin perontok."""
        return (
            f"{super().keterangan()} · {self.kapasitas} kg/jam "
            f"· minimum {self.MINIMUM_HARI_SEWA} hari"
        )
