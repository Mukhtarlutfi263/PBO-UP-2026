
from src.kios import Kios


def main() -> None:
    produk = Kios(
        kode="BRG001",
        nama_produk="Beras",
        harga_modal=10000,
        harga_jual=12000,
        stok=20,
    )

    print(Kios.NAMA_KIOS)
    print("-" * 40)
    print(f"{'Kode':<10} {'Nama Produk':<15} {'Harga Jual':>12} {'Stok':>6}")
    print("-" * 40)
    print(
        f"{produk.kode:<10} "
        f"{produk.nama_produk:<15} "
        f"{produk.harga_jual:>12,} "
        f"{produk.stok:>6}"
    )


if __name__ == "__main__":
    main()
