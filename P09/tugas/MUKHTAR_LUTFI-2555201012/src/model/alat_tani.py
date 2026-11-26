
"""Model induk abstrak untuk seluruh alat pertanian."""

from abc import ABC, abstractmethod


class AlatTani(ABC):
    """Kelas induk yang menyimpan data umum alat pertanian."""

    TARIF_MINIMUM = 10_000
    TARIF_MAKSIMUM = 5_000_000
    PEMISAH_BARIS = ";"

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise ValueError("Kode alat tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama alat tidak boleh kosong.")
        if not isinstance(tarif_harian, int) or isinstance(tarif_harian, bool):
            raise TypeError("Tarif harian harus berupa bilangan bulat.")
        if not self.TARIF_MINIMUM <= tarif_harian <= self.TARIF_MAKSIMUM:
            raise ValueError("Tarif harian berada di luar batas yang ditentukan.")

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._tarif_harian = tarif_harian

    @abstractmethod
    def biaya_tambahan(self, jumlah_hari: int) -> int:
        """Menghitung biaya tambahan sesuai jenis alat."""
        raise NotImplementedError

    @abstractmethod
    def syarat_pemakaian(self) -> str:
        """Mengembalikan syarat penggunaan alat."""
        raise NotImplementedError

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Menentukan jumlah hari yang akan ditagihkan."""
        if not isinstance(jumlah_hari, int) or isinstance(jumlah_hari, bool):
            raise TypeError("Jumlah hari harus berupa bilangan bulat.")
        if jumlah_hari < 0:
            raise ValueError("Jumlah hari tidak boleh negatif.")
        return jumlah_hari

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa dan biaya tambahan alat."""
        hari = self.hari_ditagih(jumlah_hari)
        return self._tarif_harian * hari + self.biaya_tambahan(hari)

    def __str__(self) -> str:
        return self.keterangan()

    def keterangan(self) -> str:
        return (
            f"[{self.kode}] {self.nama} — "
            f"{self.format_rupiah(self.tarif_harian)}/hari"
        )

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"kode={self.kode!r}, nama={self.nama!r}, "
            f"tarif_harian={self.tarif_harian!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AlatTani):
            return NotImplemented
        return self.kode == other.kode

    def __hash__(self) -> int:
        return hash(self.kode)

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        return "Rp" + f"{nilai:,}".replace(",", ".")
