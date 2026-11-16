
"""Kelas untuk pegawai tetap kantor kecamatan."""

from .pegawai import Pegawai


class PegawaiTetap(Pegawai):
    """Pegawai tetap yang mendapatkan tunjangan jabatan."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tunjangan_jabatan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if (
            isinstance(tunjangan_jabatan, bool)
            or not isinstance(tunjangan_jabatan, int)
        ):
            raise TypeError("Tunjangan harus berupa bilangan bulat.")
        if tunjangan_jabatan < 0:
            raise ValueError("Tunjangan tidak boleh negatif.")

        self._tunjangan_jabatan = tunjangan_jabatan

    @property
    def tunjangan_jabatan(self) -> int:
        return self._tunjangan_jabatan

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        """Menghitung gaji ditambah tunjangan jabatan."""
        penghasilan = super().hitung_penghasilan(jumlah_hari)
        return penghasilan + self._tunjangan_jabatan
