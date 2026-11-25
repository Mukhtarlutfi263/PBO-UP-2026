"""Kelas untuk pegawai kontrak kantor kecamatan."""

from .pegawai import Pegawai


class PegawaiKontrak(Pegawai):
    """Pegawai kontrak dengan tambahan hari kerja."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        hari_tambahan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if isinstance(hari_tambahan, bool) or not isinstance(hari_tambahan, int):
            raise TypeError("Hari tambahan harus berupa bilangan bulat.")
        if hari_tambahan < 0:
            raise ValueError("Hari tambahan tidak boleh negatif.")

        self._hari_tambahan = hari_tambahan

    @property
    def hari_tambahan(self) -> int:
        return self._hari_tambahan

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        """Menambahkan hari kerja sebelum menghitung penghasilan."""
        if isinstance(jumlah_hari, bool) or not isinstance(jumlah_hari, int):
            raise TypeError("Jumlah hari harus berupa bilangan bulat.")
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol.")

        hari_dibayar = jumlah_hari + self._hari_tambahan
        return super().hitung_penghasilan(hari_dibayar)
