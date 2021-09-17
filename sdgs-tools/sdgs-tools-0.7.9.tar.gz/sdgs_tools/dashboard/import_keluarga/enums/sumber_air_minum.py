from enum import Enum
from sdgs_tools.dashboard.utils import make_str_to_enum

MAPPING = {
    "Ledeng/perpipaan berbayar/air isi ulang/kemasan": "1",
    "Mata air/perpipaan/sumur": "2",
    "Mata air/ sumur": "3",
    "Sungai/danau/embung": "4",
    "Tadah air hujan": "5",
    "Lainnya": "other",
}


class SumberAirMinum(Enum):
    PERPIPAAN_BERBAYAR = "1"
    PERPIPAAN = "2"
    MATA_AIR_SUMUR = "3"
    SUNGAI_DANAU_EMBUNG = "4"
    TADAH_AIR_HUJAN = "5"
    LAINNYA = "other"

    from_str = classmethod(make_str_to_enum(MAPPING, "1"))
