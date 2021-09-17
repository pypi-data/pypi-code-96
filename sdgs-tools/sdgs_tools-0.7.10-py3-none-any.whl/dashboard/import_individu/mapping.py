from typing import Dict


MAPPING: Dict[str, str] = {
    "desa": "desa",
    "I.P103": "nama",
    "I.P104": "jenis_kelamin",
    "I.P105": "tempat_lahir",
    "I.P106": "tanggal_lahir",
    "I.P107": "usia",
    "I.P108": "status_pernikahan",
    "I.P109": "usia_menikah",
    "I.P110": "agama",
    "I.P111": "suku_bangsa",
    "I.P112": "warga_negara",
    "I.P113": "nomor_hp",
    "I.P114": "nomor_whatsapp",
    "I.P115": "alamat_email",
    "I.P116": "alamat_facebook",
    "I.P117": "alamat_twitter",
    "I.P118": "alamat_instagram",
    "I.P119": "aktif_internet",
    "I.P120": "akses_melalui",
    "I.P121": "kecepatan_internet",
    "I.P201": "kondisi_pekerjaan",
    "I.P202": "pekerjaan_utama",
    "I.P202-Comment": "pekerjaan_utama_comment",
    "I.P203": "jamsos_ketenagakerjaan",
    "I.P204": "penghasilan",
    "I.P204_penghasilan": "pekerjaan_penghasilan",
    "I.P401": "penyakit_diderita",
    "I.P402": "fasilitas_kesehatan",
    "I.P403": "jamsos_kesehatan",
    "I.P404": "disabilitas",
    "I.P405": "setahun_melahirkan",
    "I.P406": "mendapat_asi",
    "I.P501": "pendidikan_tertinggi",
    "I.P502": "tahun_pendidikan",
    "I.P503": "pendidikan_diikuti",
    "I.P504": "pelatihan_diikuti",
    "I.P505": "bahasa_permukiman",
    "I.P506": "bahasa_formal",
    "I.P507": "kerja_bakti",
    "I.P508": "siskamling",
    "I.P509": "pesta_rakyat",
    "I.P510": "menolong_kematian",
    "I.P511": "menolong_sakit",
    "I.P512": "menolong_kecelakaan",
    "I.P513": "memperoleh_pelayanan_desa",
    "I.P514": "pelayanan_desa",
    "I.P515": "saran_desa",
    "I.P516": "keterbukaan_desa",
    "I.P517": "terjadi_bencana",
    "I.P518": "terdampak_bencana",
    "kecamatan": "kecamatan",
    "kota": "kota",
    "nik": "nik",
    "no_kk": "no_kk",
    "provinsi": "provinsi",
    "rt": "rt",
    "rw": "rw",
}

MAPPING_COLS: Dict[str, str] = {
    "no_kk": "A",
    "nik": "B",
    "nama": "C",
    "jenis_kelamin": "D",
    "tempat_lahir": "E",
    "tanggal_lahir": "F",
    "usia": "G",
    "status_pernikahan": "H",
    "usia_menikah": "I",
    "agama": "J",
    "suku_bangsa": "K",
    "warga_negara": "L",
    "nomor_hp": "M",
    "nomor_whatsapp": "N",
    "alamat_email": "O",
    "alamat_facebook": "P",
    "alamat_twitter": "Q",
    "alamat_instagram": "R",
    "aktif_internet": "S",
    "akses_melalui": "T",
    "kecepatan_internet": "U",
    "kondisi_pekerjaan": "V",
    "pekerjaan_utama": "W",
    "pekerjaan_utama_comment": "X",
    "jamsos_ketenagakerjaan": "Y",
    # penghasilan: str = "Z"
    "pekerjaan_penghasilan": "AA",
    "penyakit_diderita": "AB",
    # fasilitas_kesehatan: str = "AC-AR"
    "jamsos_kesehatan": "AS",
    # disabilitas: str = "AT"
    "setahun_melahirkan": "AU",
    "mendapat_asi": "AV",
    "pendidikan_tertinggi": "AW",
    "tahun_pendidikan": "AX",
    "pendidikan_diikuti": "AY",
    "pelatihan_diikuti": "AZ",
    "bahasa_permukiman": "BA",
    "bahasa_formal": "BB",
    "kerja_bakti": "BC",
    "siskamling": "BD",
    "pesta_rakyat": "BE",
    "menolong_kematian": "BF",
    "menolong_sakit": "BG",
    "menolong_kecelakaan": "BH",
    "memperoleh_pelayanan_desa": "BI",
    "pelayanan_desa": "BJ",
    "saran_desa": "BK",
    "keterbukaan_desa": "BL",
    "terjadi_bencana": "BM",
    "terdampak_bencana": "BN",
}
