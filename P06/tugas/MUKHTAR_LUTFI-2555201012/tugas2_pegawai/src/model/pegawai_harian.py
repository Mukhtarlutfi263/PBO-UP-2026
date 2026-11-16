
"""Kelas untuk pegawai harian kantor kecamatan."""

from .pegawai import Pegawai


class PegawaiHarian(Pegawai):
    """Pegawai yang dibayar berdasarkan tarif harian."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tarif_harian: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if isinstance(tarif_harian, bool) or not isinstance(tarif_harian, int):
            raise TypeError("Tarif harian harus berupa bilangan bulat.")
        if tarif_harian <= 0:
            raise ValueError("Tarif harian harus lebih dari nol.")

        self._tarif_harian = tarif_harian

    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        """Menghitung penghasilan dari tarif harian."""
        if isinstance(jumlah_hari, bool) or not isinstance(jumlah_hari, int):
            raise TypeError("Jumlah hari harus berupa bilangan bulat.")
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol.")

        return self._tarif_harian * jumlah_hari
