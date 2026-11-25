"""Menyusun laporan penghasilan seluruh pegawai."""

from src.model.pegawai import Pegawai


class PenyusunLaporan:
    """Mengolah penghasilan pegawai secara seragam."""

    def __init__(self, pegawai: list[Pegawai]) -> None:
        if not pegawai:
            raise ValueError("Daftar pegawai tidak boleh kosong.")

        self._pegawai = list(pegawai)

    def rekap_penghasilan(self, jumlah_hari: int) -> list[tuple[str, int]]:
        """Menghasilkan rekap nama dan penghasilan setiap pegawai."""
        return [
            (pegawai.nama, pegawai.hitung_penghasilan(jumlah_hari)) for pegawai in self._pegawai
        ]

    def penghasilan_tertinggi(self, jumlah_hari: int) -> tuple[str, int]:
        """Mengambil pegawai dengan penghasilan tertinggi."""
        return max(
            self.rekap_penghasilan(jumlah_hari),
            key=lambda data: data[1],
        )

    def penghasilan_terendah(self, jumlah_hari: int) -> tuple[str, int]:
        """Mengambil pegawai dengan penghasilan terendah."""
        return min(
            self.rekap_penghasilan(jumlah_hari),
            key=lambda data: data[1],
        )

    def total_penghasilan(self, jumlah_hari: int) -> int:
        """Menjumlahkan seluruh penghasilan pegawai."""
        return sum(penghasilan for _, penghasilan in self.rekap_penghasilan(jumlah_hari))
