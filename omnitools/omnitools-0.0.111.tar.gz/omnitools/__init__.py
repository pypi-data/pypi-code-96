__version__ = "0.0.111"
__keywords__ = ["omnitools python utilities shortcuts misc"]


# if not __version__.endswith(".0"):
#     import re
#     print("version {} is deployed for automatic commitments only".format(__version__), flush=True)
#     print("install version " + re.sub(r"([0-9]+\.[0-9]+\.)[0-9]+", r"\g<1>0", __version__) + " instead")
#     import os
#     os._exit(1)


from .stdout import *
from .xtypes import *
from .encoding import *
from .hashing import *
from .rng import *
from .js import *
from .inspecting import *
from .tracing import *
from .misc import *
from .imaging import *
from .masking import *
from .dating import *
from .debugging import *
from .filing import *

