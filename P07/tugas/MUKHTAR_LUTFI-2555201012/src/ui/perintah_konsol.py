"""Penerjemah perintah untuk laporan penghasilan pegawai."""


def terjemahkan_perintah(perintah: str) -> tuple[str, ...]:
    """Menerjemahkan teks perintah menjadi instruksi."""
    bagian = perintah.strip().split()
    hasil: tuple[str, ...]

    match bagian:
        case []:
            hasil = ("kosong",)

        case ["bantuan"] | ["?"]:
            hasil = ("bantuan",)

        case [aksi, hari] if (
            aksi in ("daftar", "tertinggi", "terendah", "total")
            and hari.isdigit()
            and int(hari) > 0
        ):
            hasil = (aksi, hari)

        case ["daftar", *_]:
            hasil = ("perintah_tidak_valid",)

        case _:
            hasil = ("tidak_dikenal",)

    return hasil
