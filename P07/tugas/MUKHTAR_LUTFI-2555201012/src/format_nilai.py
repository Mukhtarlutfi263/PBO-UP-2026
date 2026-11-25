"""Memformat beberapa tipe nilai menggunakan singledispatch."""

from functools import singledispatch


@singledispatch
def sebagai_teks(nilai: object) -> str:
    """Format nilai umum."""
    return str(nilai)


@sebagai_teks.register
def _(nilai: int) -> str:
    """Format bilangan bulat."""
    return f"Rp{nilai:,}".replace(",", ".")


@sebagai_teks.register
def _(nilai: float) -> str:
    """Format bilangan desimal."""
    return f"{nilai:.1f}%"


@sebagai_teks.register
def _(nilai: str) -> str:
    """Format teks."""
    return nilai


@sebagai_teks.register
def _(nilai: bool) -> str:
    """Format nilai boolean."""
    return str(nilai)
