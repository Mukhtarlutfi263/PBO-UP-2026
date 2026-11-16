
"""Program utama untuk menampilkan contoh penyewaan alat pertanian."""

from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def main() -> None:
    traktor = Traktor("TR-01", "Traktor Roda Dua Kubota", 150_000, 8)
    pompa = PompaAir("PA-01", "Pompa Air 3 Inci", 75_000, 600)
    perontok = Perontok("PR-01", "Mesin Perontok Padi", 200_000, 900)

    alat_pertanian = [traktor, pompa, perontok]

    for alat in alat_pertanian:
        print(alat.keterangan())
        print(
            f"    1 hari:   {alat.format_rupiah(alat.biaya_sewa(1))}"
            f"      3 hari:   {alat.format_rupiah(alat.biaya_sewa(3))}"
        )


if __name__ == "__main__":
    main()
