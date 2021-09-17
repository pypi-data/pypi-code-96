import attr
from typing import Dict, Optional

from .enums import YaTidak


MAPPING = {
    "BLT DD": "blt_dd",
    "PKH": "pkh",
    "BST": "bst",
    "Banpres": "banpres",
    "UMKM": "umkm",
    "Bantuan Pekerja": "bantuan_pekerja",
    "Bantuan Pendidikan Anak": "bantuan_pendidikan_anak",
    "Lainnya": "lainnya",
}


@attr.dataclass
class BantuanPemerintah:
    blt_dd: YaTidak = YaTidak.TIDAK
    pkh: YaTidak = YaTidak.TIDAK
    bst: YaTidak = YaTidak.TIDAK
    banpres: YaTidak = YaTidak.TIDAK
    umkm: YaTidak = YaTidak.TIDAK
    bantuan_pekerja: YaTidak = YaTidak.TIDAK
    bantuan_pendidikan_anak: YaTidak = YaTidak.TIDAK
    lainnya: YaTidak = YaTidak.TIDAK

    def todict(self) -> Dict[str, str]:
        return {
            "1": self.blt_dd.value,
            "2": self.pkh.value,
            "3": self.bst.value,
            "4": self.banpres.value,
            "5": self.umkm.value,
            "6": self.bantuan_pekerja.value,
            "7": self.bantuan_pendidikan_anak.value,
            "8": self.lainnya.value,
        }

    @classmethod
    def from_str(cls, val: Optional[str], t=None) -> "BantuanPemerintah":
        if not val:
            return cls()
        data: Dict[str, YaTidak] = dict()
        for key, name in MAPPING.items():
            if key in val:
                data[name] = YaTidak.YA
            else:
                data[name] = YaTidak.TIDAK
        return cls(**data)
