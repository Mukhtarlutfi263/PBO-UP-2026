
"""Program sederhana data pegawai Kantor Kecamatan Bangkinang Kota."""

from src.model.pegawai_harian import PegawaiHarian
from src.model.pegawai_kontrak import PegawaiKontrak
from src.model.pegawai_tetap import PegawaiTetap


def main() -> None:
    """Menampilkan data dan penghasilan beberapa jenis pegawai."""
    pegawai_tetap = PegawaiTetap(
        "001", "Andi Saputra", 150_000, 500_000
    )
    pegawai_harian = PegawaiHarian(
        "002", "Budi Santoso", 100_000, 125_000
    )
    pegawai_kontrak = PegawaiKontrak(
        "003", "Citra Lestari", 120_000, 2
    )

    daftar_pegawai = [
        pegawai_tetap,
        pegawai_harian,
        pegawai_kontrak,
    ]

    for pegawai in daftar_pegawai:
        penghasilan = pegawai.hitung_penghasilan(20)
        print(pegawai)
        print(f"Penghasilan: Rp{penghasilan:,}")
        print("-" * 35)


if __name__ == "__main__":
    main()
