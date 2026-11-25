"""Kelas induk untuk data pegawai kantor kecamatan."""


class Pegawai:
    """Menyimpan data dasar dan menghitung penghasilan pegawai."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
    ) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama pegawai tidak boleh kosong.")
        if isinstance(gaji_pokok, bool) or not isinstance(gaji_pokok, int):
            raise TypeError("Gaji pokok harus berupa bilangan bulat.")
        if gaji_pokok <= 0:
            raise ValueError("Gaji pokok harus lebih dari nol.")

        self._nip = nip.strip()
        self._nama = nama.strip()
        self._gaji_pokok = gaji_pokok

    @property
    def nip(self) -> str:
        return self._nip

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def gaji_pokok(self) -> int:
        return self._gaji_pokok

    def hitung_penghasilan(self, jumlah_hari: int) -> int:
        """Menghitung penghasilan berdasarkan jumlah hari kerja."""
        if isinstance(jumlah_hari, bool) or not isinstance(jumlah_hari, int):
            raise TypeError("Jumlah hari harus berupa bilangan bulat.")
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol.")

        return self._gaji_pokok * jumlah_hari

    def __str__(self) -> str:
        return f"{self._nama} (NIP: {self._nip})"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"nip={self._nip!r}, nama={self._nama!r}, "
            f"gaji_pokok={self._gaji_pokok!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pegawai):
            return NotImplemented
        return self._nip == other._nip

    def __hash__(self) -> int:
        return hash(self._nip)
