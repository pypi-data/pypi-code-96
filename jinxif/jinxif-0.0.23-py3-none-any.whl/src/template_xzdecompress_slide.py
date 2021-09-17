########
# title: template_xzdecompress_slide.py
#
# author: Jenny, bue
# license: GPLv>=3
# version: 2021-06-25
#
# description:
#     template script for decompressing xz compressed files.
#
# instruction:
#     use jinxif.util.decompress_xz_spawn function to generate and run executables from this template.
#####

# libraries
from jinxif import util
import resource
import time

# set variables
poke_s_slide = 'peek_s_slide'
poke_b_tiff_raw = peek_b_tiff_raw
poke_b_czi_splitscene = peek_b_czi_splitscene
poke_s_rawdir = 'peek_s_rawdir'
poke_s_format_rawdir = 'peek_s_format_rawdir'
poke_s_czidir = 'peek_s_czidir'
poke_s_format_czidir_splitscene = 'peek_s_format_czidir_splitscene'

# off we go
r_time_start = time.time()

# tiff raw
if poke_b_tiff_raw:
    util.decompress_tiff_raw(
        s_slide = poke_s_slide,
        s_rawdir = poke_s_rawdir,  # input and output
        s_format_rawdir = poke_s_format_rawdir,  # s_rawdir, s_slide
    )

# czi splitscene
if poke_b_czi_splitscene:
    util.decompress_czi_splitscene(
        s_slide = poke_s_slide,
        s_czidir = poke_s_czidir,  # input and output
        s_format_czidir_splitscene = poke_s_format_czidir_splitscene,  # s_czidir, s_slide
    )

# rock to the end
r_time_stop = time.time()
print('done jinxif.util.decompress_xz!')
print(f'run time: {(r_time_stop - r_time_start) / 3600}[h]')
print(f'run max memory: {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000000}[GB]')
