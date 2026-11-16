
"""Model alat pertanian berupa traktor."""

from typing import Final

from .alat_tani import AlatTani


class Traktor(AlatTani):
    """Traktor roda dua yang wajib dioperasikan petugas UPJA."""

    ONGKOS_OPERATOR_HARIAN: Final[int] = 100_000

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        tenaga_kuda: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if tenaga_kuda <= 0:
            raise ValueError(
                f"Tenaga kuda harus lebih dari nol, diterima {tenaga_kuda}"
            )

        self._tenaga_kuda = tenaga_kuda

    @property
    def tenaga_kuda(self) -> int:
        return self._tenaga_kuda

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Biaya dasar ditambah ongkos operator setiap hari."""
        dasar = super().biaya_sewa(jumlah_hari)
        return dasar + Traktor.ONGKOS_OPERATOR_HARIAN * jumlah_hari

    def keterangan(self) -> str:
        """Menampilkan informasi khusus traktor."""
        return f"{super().keterangan()} · {self.tenaga_kuda} HP · termasuk operator"
