"""Program utama laporan penghasilan pegawai."""

from src.format_nilai import sebagai_teks
from src.model.pegawai import Pegawai
from src.model.pegawai_harian import PegawaiHarian
from src.model.pegawai_kontrak import PegawaiKontrak
from src.model.pegawai_tetap import PegawaiTetap
from src.model.penyusun_laporan import PenyusunLaporan
from src.ui.perintah_konsol import terjemahkan_perintah


def main() -> None:
    """Menjalankan contoh laporan penghasilan pegawai."""
    daftar_pegawai: list[Pegawai] = [
        PegawaiTetap("001", "Andi", 150000, 500000),
        PegawaiKontrak("002", "Budi", 120000, 2),
        PegawaiHarian("003", "Citra", 100000, 80000),
    ]

    laporan = PenyusunLaporan(daftar_pegawai)
    perintah = terjemahkan_perintah("daftar 5")

    print("=== LAPORAN PENGHASILAN PEGAWAI ===")

    if perintah[0] == "daftar":
        jumlah_hari = int(perintah[1])

        for nama, penghasilan in laporan.rekap_penghasilan(jumlah_hari):
            print(f"{nama}: {sebagai_teks(penghasilan)}")

        nama, penghasilan = laporan.penghasilan_tertinggi(jumlah_hari)
        print(f"Penghasilan tertinggi: {nama} ({sebagai_teks(penghasilan)})")

        print(
            "Total penghasilan:",
            sebagai_teks(laporan.total_penghasilan(jumlah_hari)),
        )


if __name__ == "__main__":
    main()
