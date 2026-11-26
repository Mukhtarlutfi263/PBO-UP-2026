"""Program utama untuk menampilkan contoh penyewaan alat pertanian."""

from src.model.daftar_harga import DaftarHarga
from src.model.gerobak_dorong import GerobakDorong
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def main() -> None:
    daftar = DaftarHarga()

    daftar.tambah(
        Traktor("TR-01", "Traktor Roda Dua Kubota", 150_000, 8)
    )
    daftar.tambah(
        PompaAir("PA-01", "Pompa Air 3 Inci", 75_000, 600)
    )
    daftar.tambah(
        Perontok("PR-01", "Mesin Perontok Padi", 200_000, 900)
    )
    daftar.tambah(
        GerobakDorong("GD-01", "Gerobak Dorong", 50_000)
    )

    daftar.tampilkan()


if __name__ == "__main__":
    main()
