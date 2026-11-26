"""Model gerobak dorong yang memenuhi kontrak Sewaan."""



class GerobakDorong:
    """Gerobak dorong yang dapat disewakan tanpa mewarisi AlatTani."""

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("Kode gerobak tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama gerobak tidak boleh kosong.")
        if (
            not isinstance(tarif_harian, int)
            or isinstance(tarif_harian, bool)
        ):
            raise TypeError("Tarif harus berupa bilangan bulat.")
        if tarif_harian <= 0:
            raise ValueError("Tarif harus lebih dari nol.")

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    def biaya_sewa(self, jumlah_hari: int) -> int:
        if not isinstance(jumlah_hari, int) or isinstance(jumlah_hari, bool):
            raise TypeError("Jumlah hari harus berupa bilangan bulat.")
        if jumlah_hari < 0:
            raise ValueError("Jumlah hari tidak boleh negatif.")

        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        return (
            f"[{self.kode}] {self.nama} — "
            f"Rp{self._tarif_harian:,}".replace(",", ".")
            + "/hari"
        )
