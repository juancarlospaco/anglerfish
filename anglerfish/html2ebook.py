#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""HTML2eBook a tiny function that converts HTML5 to eBook,Mobile Friendly."""


import os
import zipfile

from collections import deque
from datetime import datetime
from getpass import getuser
from locale import getdefaultlocale
from pathlib import Path
from platform import node, platform
from uuid import uuid4

try:
    from .make_autochecksum import autochecksum
    from .stealth2string import stealth2string
    from .make_zip_comment import set_zip_comment
except ImportError:
    from anglerfish import autochecksum
    from anglerfish import stealth2string
    from anglerfish import set_zip_comment


CONTAINER = stealth2string("​﻿﻿​​﻿​﻿​﻿​​﻿﻿﻿​​﻿﻿﻿​​​​​﻿﻿​​﻿​​​﻿﻿​﻿​﻿​​﻿﻿﻿​​﻿​​﻿​​​﻿﻿​​﻿​﻿​​﻿﻿​﻿﻿﻿﻿​​​​﻿​​​﻿​​​﻿​​​​​﻿​﻿​​﻿﻿​﻿​﻿​﻿​​﻿​​﻿​﻿​​​​​﻿﻿﻿​﻿​​​​﻿﻿﻿​​​​﻿﻿​﻿​​​​﻿​﻿﻿​​​​﻿​​​﻿​﻿​﻿​​﻿﻿​​​﻿﻿​﻿​﻿​​﻿﻿﻿​​​﻿​﻿​​​﻿﻿​​﻿﻿​﻿​﻿​​﻿​﻿​​​​​﻿​​​﻿​﻿​﻿﻿​﻿﻿​﻿​﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​​﻿​​﻿​﻿﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿​​​​﻿​​﻿﻿﻿﻿​​​​﻿﻿​​​﻿​​﻿​​﻿﻿﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​﻿​​﻿​﻿﻿​​​﻿﻿​﻿​​​​﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿​​​​​﻿﻿﻿​​﻿​​﻿​﻿​​​﻿​﻿​​​﻿​​​​﻿﻿​﻿​﻿​﻿﻿​​﻿​﻿​​﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​​﻿﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿​﻿​﻿﻿﻿​​﻿﻿​​​​​﻿﻿​﻿﻿​​​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿​​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​﻿​​​​﻿﻿​​​﻿​﻿﻿﻿﻿​​​​﻿​​﻿﻿​​​﻿​​​﻿﻿​​﻿​​​​﻿​​​﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿​﻿​​﻿﻿​﻿​​​​﻿﻿​﻿​​﻿​​​​﻿﻿﻿​﻿﻿​​​﻿﻿​﻿​﻿​​﻿﻿​​​﻿​﻿​​​﻿​​​​﻿﻿​﻿​﻿​﻿​​﻿​﻿﻿​﻿​​​​​﻿​﻿﻿​​﻿​﻿​﻿﻿​﻿​﻿​​﻿​​﻿​​﻿​﻿​​​​﻿​​​﻿﻿​﻿﻿﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​​﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿​​﻿​​﻿​﻿​​﻿​﻿​​​​​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿​​​﻿​﻿​​﻿​​​﻿﻿​​﻿​​﻿​​﻿​﻿﻿​﻿​​﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​﻿​​﻿​​​​﻿​​​﻿﻿​﻿﻿​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿​​​﻿﻿﻿​﻿​﻿​​﻿​​﻿﻿﻿​​​​​​﻿﻿​﻿﻿​​﻿​​﻿​​​​﻿﻿﻿​​​​​﻿​​﻿​​​​﻿​​​​﻿﻿​﻿​​﻿​​​​﻿﻿​​​﻿​​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿​​﻿​​​﻿​​​​﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿​﻿​﻿​﻿​﻿​​﻿﻿﻿﻿​﻿​﻿​​﻿﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿​﻿​﻿﻿﻿﻿​﻿​​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿​​﻿​​﻿​​﻿​﻿﻿​﻿﻿​​​﻿​​​﻿﻿​​﻿​​﻿​​﻿​﻿​​﻿﻿﻿​​​﻿﻿​​﻿​​﻿﻿​​﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿​​﻿﻿​​​﻿​﻿﻿​​﻿​﻿​​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​​​﻿​﻿​​​​​﻿​﻿﻿​﻿﻿﻿​​﻿﻿﻿​﻿​​​﻿﻿﻿﻿​​﻿​​﻿﻿​﻿﻿​​﻿​​​​​﻿​﻿​​﻿﻿​​​﻿​​﻿​​﻿​​﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿﻿﻿​​﻿​﻿​​﻿​​﻿​​​​​﻿​​﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿​​﻿​​﻿​​﻿​﻿​﻿﻿​﻿﻿﻿​​​​​​﻿﻿​​​​​﻿﻿​﻿﻿​﻿​﻿​﻿﻿​​﻿​﻿﻿​﻿​​﻿​﻿﻿​﻿﻿﻿​​﻿​​​﻿​﻿​﻿​​﻿​﻿﻿​﻿​​​﻿​﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿​​​​​﻿​﻿﻿﻿﻿​​﻿﻿​﻿﻿​​﻿﻿﻿﻿​﻿​​﻿​​​﻿​﻿​​﻿﻿﻿​​﻿​﻿​​﻿﻿​﻿​﻿﻿​​​​﻿​﻿﻿​﻿﻿﻿﻿​​﻿﻿​​​​​﻿﻿﻿​​​﻿​﻿​﻿​﻿﻿﻿​​﻿﻿​﻿​﻿​​﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿​﻿﻿​﻿​​﻿​﻿​​​​​﻿​﻿​﻿﻿​​﻿﻿﻿​​​​​﻿​​﻿​﻿﻿​﻿​﻿​﻿​﻿​​﻿﻿​​​﻿​﻿​﻿​​﻿﻿​﻿​​﻿﻿​​​﻿​​﻿﻿﻿﻿​﻿​​​​﻿﻿​﻿​​​﻿​​​﻿​﻿​﻿﻿​​﻿﻿​​​﻿​​﻿﻿﻿﻿​​﻿​﻿﻿​﻿﻿​​​​﻿﻿​​﻿​​﻿﻿﻿​​﻿﻿​​﻿​﻿​﻿﻿​﻿﻿​﻿﻿​﻿​﻿​​​﻿﻿​​﻿​​﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿​﻿﻿​​​​﻿​​​​﻿​​﻿﻿﻿​﻿​​​﻿﻿﻿​​​​​﻿﻿​​﻿﻿﻿​﻿﻿​﻿​﻿​​﻿​​​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿​​​​﻿﻿​﻿﻿﻿​​﻿​​﻿﻿​﻿​​​​​﻿﻿​​﻿﻿​﻿﻿​​﻿​﻿​​﻿﻿​﻿​​​﻿​﻿﻿​​​​​﻿﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿﻿​﻿​​﻿​﻿﻿​﻿﻿﻿​​​﻿﻿​​​﻿​﻿﻿​﻿​﻿​​​﻿﻿​​﻿​​​﻿﻿​​﻿​​﻿﻿​﻿﻿﻿​​﻿﻿​​﻿﻿​​​﻿​﻿​﻿﻿​﻿​﻿​﻿​﻿​​﻿﻿​​​​​﻿﻿​﻿﻿﻿​​﻿﻿​​​﻿​​​﻿﻿​﻿﻿﻿​​﻿﻿​​​﻿​​﻿﻿​​﻿​​﻿​​﻿﻿﻿​​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿​﻿​​﻿​​​​﻿﻿​﻿﻿​﻿﻿﻿​​​﻿﻿​﻿​﻿​﻿​​​﻿​​​﻿​​​​﻿​​﻿﻿​﻿​​﻿​​﻿﻿​​﻿﻿​﻿​​​﻿​﻿​﻿​﻿​﻿​​​﻿﻿​﻿﻿​​​​﻿﻿​﻿​​​​﻿﻿​​​﻿​﻿﻿​﻿﻿﻿​​﻿﻿﻿​﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿​​﻿​﻿​﻿﻿​​﻿​​​﻿﻿​﻿​﻿​​﻿﻿​﻿﻿​​​﻿﻿﻿﻿​​﻿​​﻿﻿​​﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿﻿​​​​​﻿﻿﻿​​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿﻿​​​​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​​​​﻿​​​​﻿﻿​﻿​​﻿​﻿​​﻿﻿​﻿﻿​﻿​​﻿﻿​﻿​﻿​﻿﻿​﻿﻿​​​﻿​﻿​​﻿﻿​﻿​​﻿﻿​﻿​​﻿﻿​​​﻿​﻿﻿﻿​﻿​​​﻿﻿​​﻿﻿​​﻿​​​​​﻿​​﻿﻿﻿​​​​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​​﻿​​﻿﻿​​﻿​​﻿﻿​﻿​﻿​​﻿﻿​﻿​​​​﻿﻿​​​﻿​​​﻿﻿﻿​​﻿​﻿​﻿​﻿﻿​​﻿﻿﻿​​﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿​﻿﻿​﻿​​﻿​﻿﻿​​﻿​﻿​​​﻿​﻿​﻿﻿​﻿​﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​​﻿﻿​​﻿﻿​​﻿﻿​​​​​﻿​​​​​﻿​﻿﻿​﻿​​​​﻿﻿​​﻿​﻿​﻿​​​﻿﻿​​﻿​​﻿﻿​﻿​​﻿﻿﻿﻿​﻿")  # nopep8 lint:ok noqa
INDEX_HTML = stealth2string("​﻿﻿​​﻿​﻿​﻿​​﻿﻿﻿​​﻿﻿﻿​​​﻿​﻿​​﻿﻿﻿​​﻿​﻿​﻿﻿​​﻿​​​﻿​﻿​​﻿﻿​​​﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​​﻿​​﻿﻿﻿﻿​​﻿​﻿​​​​​﻿​﻿​﻿​​​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿​​​﻿​﻿﻿​​​​﻿​﻿​﻿​﻿​﻿​​﻿​﻿﻿​​﻿﻿​﻿﻿​​﻿﻿﻿​﻿​​​﻿​﻿​﻿​​​﻿​​﻿﻿﻿​​﻿​​﻿​​﻿​﻿﻿​​﻿​﻿​​﻿﻿​​﻿​​﻿﻿﻿​﻿﻿​​﻿​​﻿​​​​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​​﻿​﻿﻿﻿​​﻿﻿​﻿​​​﻿﻿﻿​﻿​​﻿​​​​﻿​​﻿﻿﻿​​﻿﻿﻿​​﻿​​​﻿﻿​​​​​​﻿﻿​​​​​​﻿﻿​​​​​​﻿﻿﻿​​​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿﻿​​​﻿﻿﻿​​​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿​​﻿​​​﻿﻿﻿​﻿﻿​﻿﻿​​​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​​​﻿​﻿​​​​​﻿​﻿​﻿​​​﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​​﻿﻿​﻿﻿​​﻿​﻿​﻿​﻿​﻿​​​​﻿​﻿﻿﻿﻿​​﻿﻿﻿​​﻿​​﻿﻿​﻿​​​﻿​​​﻿﻿​​﻿​​﻿​﻿​​﻿​​​﻿﻿​​﻿﻿﻿​﻿​​​﻿﻿﻿﻿​​﻿​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​﻿​﻿​​﻿﻿​​﻿﻿​﻿﻿​​﻿​​​​﻿﻿​﻿​​﻿​﻿​​﻿﻿​​​​﻿​​﻿﻿​​﻿﻿​﻿﻿​﻿​﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿﻿​​﻿﻿​​﻿​​﻿﻿​​​﻿​​​﻿﻿﻿​​﻿​﻿﻿﻿﻿​​﻿﻿​​﻿​​﻿﻿​​​﻿​​﻿​﻿​﻿​﻿​﻿​​﻿﻿​﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿​﻿﻿​​​​﻿﻿​﻿﻿​​​﻿﻿​﻿﻿​​​​﻿﻿﻿​​﻿​﻿​​﻿​​﻿​﻿﻿﻿​​​​​﻿﻿​​﻿​﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​﻿﻿​​​﻿﻿﻿​​​​﻿﻿​﻿﻿﻿﻿​﻿​​​​​﻿​﻿​﻿​​﻿﻿​​﻿﻿​​﻿​​﻿​​﻿﻿​﻿​﻿​﻿​﻿﻿​​﻿​​﻿​​​​﻿﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿﻿​​​​﻿﻿​​﻿​​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿​​﻿​﻿﻿​﻿​​﻿​​﻿​﻿​﻿﻿​﻿​﻿​﻿​﻿​​﻿​﻿​﻿﻿​﻿​​﻿﻿​﻿​﻿​​​​﻿﻿​​﻿﻿​​​﻿​​﻿﻿​﻿​﻿​﻿​​﻿​​﻿​​﻿﻿​​﻿﻿​﻿​﻿​​﻿​​﻿﻿﻿​​﻿﻿​﻿​​﻿​﻿﻿​﻿​​﻿​​﻿​﻿​​﻿​​​​​﻿﻿﻿​​​​﻿​﻿​​​​​﻿​﻿​​﻿﻿​﻿﻿​﻿﻿​﻿​﻿﻿​﻿﻿﻿​​﻿​​​​﻿﻿​​﻿﻿​​​​​﻿﻿﻿​﻿​​​﻿​​​﻿﻿​​​﻿﻿​​﻿﻿​​﻿​﻿﻿﻿﻿​​﻿﻿​﻿​​​﻿​​​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿​﻿​​﻿​​﻿﻿​﻿﻿​​﻿﻿​​​​﻿​​﻿﻿​﻿﻿﻿​​﻿​﻿​﻿﻿​﻿﻿​﻿​​﻿​﻿﻿​​﻿​​​﻿​﻿​​​﻿​﻿﻿​﻿​​​​​﻿﻿​​﻿​​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿﻿​﻿​​​​﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿​​​​﻿﻿​﻿​﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿​​﻿​​﻿﻿​​​​﻿​﻿﻿​​​​﻿​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿​﻿﻿​​​﻿﻿​﻿​﻿​﻿﻿​​﻿﻿﻿​﻿﻿​​​﻿﻿​​﻿​​​﻿﻿﻿​​​​﻿﻿​​﻿​﻿​﻿﻿﻿​​﻿​​﻿﻿﻿​​​﻿​﻿​​﻿﻿​﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿﻿﻿﻿​​﻿﻿​​﻿​​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿﻿​﻿​﻿﻿​​﻿﻿​​​﻿​﻿​﻿﻿​﻿​﻿​﻿​​​​﻿﻿​﻿​﻿​﻿​​​﻿​﻿​﻿﻿​​﻿﻿​​﻿​﻿﻿​​​​﻿​﻿​​﻿​​﻿​﻿﻿​​﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿​﻿​​​﻿​﻿﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿​​​​​﻿​﻿​﻿﻿​﻿​​﻿​​​​﻿﻿﻿​﻿​﻿​﻿﻿​﻿​​﻿​​﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿﻿​​​​﻿​​​﻿﻿﻿​​﻿﻿﻿​​​​﻿​​​﻿﻿​​﻿﻿﻿​﻿​﻿​​﻿﻿​​﻿​​﻿​​​﻿​﻿​﻿​​﻿﻿​​​﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿﻿​​﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿​﻿​​﻿﻿​﻿﻿​﻿​​​​﻿​﻿​​﻿​​﻿​﻿​​​﻿​﻿﻿​﻿﻿﻿​​﻿​﻿﻿​​​​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿​﻿​​﻿​﻿​​﻿﻿​﻿﻿﻿​​﻿​​​﻿﻿​​﻿​​﻿​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​​​﻿​﻿​​​​﻿﻿​﻿​​​​﻿​​﻿​​​﻿﻿​​﻿﻿​﻿﻿﻿​​﻿​﻿​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿​​﻿​​​​﻿﻿﻿​​​​​​﻿​﻿​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​﻿​﻿﻿﻿​﻿﻿​﻿​​﻿​﻿​﻿​​​​​﻿﻿﻿﻿​​​​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​​﻿​﻿​﻿﻿​﻿​​﻿​​﻿​​﻿﻿​﻿﻿​​﻿​​﻿​﻿​​﻿​​﻿﻿​﻿​﻿﻿​​﻿​​​​﻿﻿​﻿﻿​​﻿​﻿​​﻿​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​​​​﻿​​​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿​​​﻿​﻿​﻿​​​﻿﻿​​﻿​﻿​​﻿​​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿​﻿​​​﻿​﻿​﻿﻿​﻿﻿​﻿﻿﻿​​​﻿﻿​​﻿﻿​﻿﻿﻿​﻿​​​﻿​​​﻿﻿﻿​﻿​﻿​​​﻿​﻿﻿​﻿﻿﻿​​﻿﻿﻿﻿​​﻿​﻿﻿﻿﻿​​​​﻿﻿​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿​​﻿﻿​​​﻿​﻿﻿​​​​​﻿​﻿​﻿﻿​﻿​​﻿﻿﻿﻿​﻿​﻿﻿​​​​﻿​​﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿​﻿​​​​​﻿﻿﻿​​﻿﻿​﻿​​﻿﻿﻿﻿​﻿﻿​﻿​﻿​​﻿﻿​​﻿​​​﻿﻿​﻿﻿​﻿​﻿​​﻿​﻿﻿​﻿﻿​​﻿​​​﻿﻿﻿​​﻿﻿​﻿﻿​​﻿​﻿​﻿​​​﻿​​​﻿​​​​﻿﻿​﻿​﻿﻿​​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿﻿﻿​​﻿​​﻿﻿​﻿​﻿​​﻿​​​​﻿﻿﻿​​​​​​﻿﻿​​﻿​​﻿﻿​﻿​﻿​​​﻿﻿​﻿﻿﻿​﻿​​​​﻿﻿​﻿﻿﻿​​​​​﻿​​​﻿​﻿​﻿﻿﻿​﻿​​​​﻿﻿﻿​​﻿​﻿﻿﻿​﻿​​​﻿​​﻿​​​​﻿﻿​﻿​﻿﻿​﻿​​​​﻿﻿​﻿​​​﻿​﻿​﻿​​​​​﻿​﻿​﻿​﻿​﻿​﻿​​﻿​​﻿​​﻿﻿​​﻿​​﻿​​​​﻿​​​﻿﻿​​﻿﻿​﻿​​﻿﻿​​​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​​​​﻿﻿​​​​﻿​﻿﻿​﻿​​﻿​﻿​​﻿﻿﻿​​﻿﻿﻿﻿​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​​﻿​﻿​​​﻿﻿﻿​​﻿﻿﻿​​​​​﻿﻿​﻿​​​﻿﻿​﻿﻿​﻿​﻿​﻿​﻿​​​﻿﻿​​​﻿﻿​﻿​​﻿﻿​﻿​﻿​​​​﻿﻿​﻿​​​﻿​​​﻿﻿​​​﻿﻿​﻿​﻿​​​﻿​﻿​﻿​​​﻿​﻿​​​﻿​​​﻿​﻿​﻿﻿﻿​​﻿﻿​​​﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​​​﻿​﻿﻿​​﻿﻿﻿​﻿​﻿﻿​​﻿​﻿​​﻿​﻿​​﻿﻿​﻿​﻿​​﻿​​​﻿​​​﻿​﻿​​​﻿​﻿​﻿﻿​​﻿​​﻿﻿​​﻿﻿​﻿﻿​﻿﻿​﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​﻿​​​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿﻿​﻿​​﻿​​​​﻿﻿﻿​﻿​​​﻿​﻿﻿​​﻿​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​​﻿﻿﻿​​﻿​﻿​﻿﻿​​﻿​﻿​​﻿﻿​​​﻿​﻿​​​​​​﻿﻿​﻿﻿​​﻿​​﻿﻿﻿﻿​﻿​​​﻿​​​﻿​﻿​﻿​﻿​﻿﻿﻿​​​​​﻿﻿​﻿﻿﻿​​﻿﻿﻿​​﻿﻿​﻿​﻿​﻿​​​﻿​﻿﻿​﻿​​​﻿﻿​​﻿﻿​﻿​​​﻿​​​﻿​​﻿﻿﻿​​﻿​​﻿​﻿​​﻿﻿​​﻿​﻿​﻿﻿​​﻿﻿​​﻿​﻿﻿​﻿​​﻿﻿​​﻿﻿​​﻿﻿​​​﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​​​﻿​​​﻿﻿​﻿﻿​​​﻿﻿﻿​​﻿​﻿﻿﻿​﻿​​​﻿﻿​﻿​​​​﻿﻿​﻿﻿​﻿​​﻿﻿​﻿​﻿​﻿​﻿​​﻿﻿​​﻿﻿​﻿​﻿​​﻿﻿​​​​​﻿﻿​​﻿﻿﻿​﻿﻿​﻿﻿​​​​﻿﻿﻿​​​​﻿﻿﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​​﻿﻿​​﻿​​﻿​﻿​​​﻿​﻿​​​﻿​﻿​﻿﻿﻿​​﻿​​﻿﻿﻿﻿​​​​﻿﻿﻿​﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿﻿​​﻿﻿﻿​﻿​﻿﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​﻿​​﻿​﻿﻿​﻿​​﻿​​﻿​﻿﻿​﻿﻿​﻿​​﻿﻿​﻿​​​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿​﻿​﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿﻿​​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​​﻿​​​﻿﻿​​﻿​​​﻿﻿​​​​​﻿﻿​​​​﻿​​﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿​﻿​﻿​﻿​​﻿​​﻿​​​﻿﻿﻿​﻿​﻿﻿​​​​﻿​​​﻿﻿﻿​﻿​﻿﻿​​​​﻿﻿﻿﻿​​﻿​​﻿﻿​​﻿​​﻿​﻿​﻿​​​﻿​﻿﻿​﻿​​﻿﻿​﻿﻿​​​​﻿﻿​﻿​﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿﻿​﻿​﻿​​​﻿​﻿﻿​​﻿​﻿​﻿​​﻿​​​​﻿﻿﻿​​﻿​​﻿​​​﻿﻿​​﻿﻿﻿​﻿​​​﻿​﻿​﻿﻿​​﻿﻿​﻿​﻿​​﻿​﻿​﻿​​​﻿​​​​﻿​​﻿​​​​﻿​​﻿​​﻿​​﻿​​﻿​﻿​﻿﻿​﻿﻿​​​﻿﻿​﻿​​​﻿﻿﻿​﻿​​​﻿​﻿​﻿​﻿﻿​​﻿​​﻿﻿﻿​​​​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​​﻿​﻿﻿﻿﻿​﻿​​​​﻿﻿​​﻿﻿​​​﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿​﻿​﻿​​﻿﻿​​​﻿​﻿﻿​​﻿​​﻿﻿​﻿​﻿​﻿​​​﻿﻿​​​﻿﻿﻿​​﻿​﻿​﻿﻿​​​​﻿﻿​​​﻿​​﻿​﻿﻿​​​​​﻿﻿​​​﻿​﻿﻿﻿﻿​​​​﻿​​​﻿﻿​​﻿​​﻿﻿﻿﻿​﻿﻿​​​﻿​​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​​﻿​​﻿﻿​﻿﻿​​﻿​​﻿﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​﻿﻿​﻿​﻿​﻿​﻿﻿​​﻿​​﻿﻿​﻿​﻿﻿​​​﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​﻿﻿​﻿﻿​​​﻿﻿​​﻿﻿​​​﻿​﻿﻿​​​﻿​​﻿﻿﻿﻿​﻿​​﻿​​﻿﻿​​​﻿﻿​﻿​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​​﻿﻿﻿﻿​﻿​​​﻿​﻿​﻿​​﻿﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿﻿​​​​﻿​​​﻿​﻿​﻿​﻿​​​﻿​﻿﻿​﻿﻿﻿​​﻿​​﻿​﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿​​​​﻿​​﻿﻿​​​﻿​​﻿​﻿​​﻿﻿​﻿﻿﻿​﻿​​​﻿﻿​﻿​​﻿​﻿﻿​﻿﻿​​​﻿﻿​﻿​​​​​﻿﻿​﻿﻿​​﻿﻿​﻿​​﻿​​﻿﻿​﻿​﻿​​﻿﻿﻿​​​​﻿﻿﻿﻿​​​​﻿​​​​﻿​​﻿​​﻿﻿﻿﻿​​﻿﻿​﻿​​​​﻿﻿﻿​​﻿​﻿﻿﻿​​﻿﻿​﻿​​​﻿​​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​​​​​﻿​​​﻿﻿​​​﻿​﻿​﻿﻿​﻿​﻿​﻿​​​﻿﻿﻿​​﻿​​﻿​​﻿﻿﻿​​﻿​​​﻿﻿﻿​​﻿﻿﻿​​﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​​​﻿​﻿​​​​​﻿​﻿﻿​﻿​﻿​​​﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿﻿​​​﻿​﻿​​﻿​​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿​​﻿​﻿​﻿​﻿​﻿﻿﻿​​​​​﻿﻿​﻿​​﻿​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​​﻿​​﻿﻿​​﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​​​​​﻿​​﻿​​​​﻿​﻿﻿​﻿​​﻿​﻿​​​﻿​﻿﻿﻿​​​​​﻿﻿​​﻿​﻿​﻿​﻿​﻿﻿﻿​​﻿﻿﻿​​​​﻿​​​﻿​​​﻿﻿​﻿﻿​﻿​​﻿﻿​​​﻿​﻿​​​﻿​​​﻿​﻿​​﻿﻿​﻿​﻿​​​﻿​﻿﻿﻿​﻿​​​﻿​﻿​​﻿﻿​​﻿﻿﻿​​​​﻿​﻿​​﻿﻿​﻿​​﻿​​﻿​﻿﻿​​​﻿﻿​﻿﻿​​​﻿​​﻿​​﻿﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​​​​﻿﻿​​﻿﻿​​﻿​​﻿​​​​​﻿​﻿﻿​​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿​​﻿​﻿​﻿﻿﻿﻿​​​​﻿﻿​​﻿﻿​​﻿​​​​﻿​​﻿​​​﻿﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿​​﻿﻿​﻿﻿﻿﻿​​​​﻿﻿﻿​﻿﻿﻿​﻿​﻿​​﻿​​﻿﻿﻿​​​​​﻿​​﻿﻿﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿​​​﻿﻿​​​﻿​﻿﻿​​﻿﻿﻿​​﻿﻿​﻿​﻿​﻿﻿​﻿﻿​​​﻿​﻿﻿​​﻿​﻿​﻿​​​​​﻿﻿﻿​﻿​​​﻿​​​​﻿﻿​﻿﻿​﻿​​​​﻿﻿​​﻿﻿﻿​​﻿﻿​​​​​﻿﻿​﻿​​﻿​​﻿﻿​​﻿﻿​﻿﻿﻿​﻿​﻿​​﻿﻿﻿​​﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​​​​​﻿​​﻿﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿​﻿​﻿​​​﻿﻿​﻿​﻿﻿​﻿​​​​​﻿​﻿﻿​﻿﻿​​​﻿​​﻿​​​​​﻿﻿​​​​​﻿​﻿﻿​​﻿​​﻿﻿﻿​​​​﻿﻿﻿​​​​​﻿​﻿​﻿﻿​​﻿​﻿﻿​​﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿​​​﻿﻿﻿﻿​​​​﻿﻿​​​﻿﻿​﻿​﻿﻿​﻿​​﻿​​﻿​﻿​​﻿​​﻿﻿﻿﻿​﻿​﻿​​​﻿​​﻿﻿​﻿​​​﻿﻿​﻿​​​​﻿​﻿​​​​​﻿﻿​​﻿﻿﻿​​﻿﻿​​​​​﻿﻿﻿​​​​​﻿​​﻿﻿﻿﻿​﻿​​﻿​​﻿​﻿​﻿​﻿﻿﻿​﻿﻿​​​﻿﻿​﻿​​​﻿​​​﻿﻿​​﻿​​​​﻿﻿​﻿​​​﻿﻿﻿​​​﻿​﻿​​​﻿​​​﻿​﻿​​​﻿​﻿​﻿​​​﻿​﻿​​​﻿﻿​​﻿​﻿﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿​​​﻿﻿﻿​​﻿﻿﻿​​﻿​﻿​﻿​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿​​﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​﻿​​​﻿​​﻿﻿​​​﻿﻿​​﻿​﻿​﻿﻿​​﻿​​​﻿﻿​﻿​﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿​​​​﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿​​​​﻿﻿﻿﻿​​​​﻿﻿﻿​﻿﻿﻿​​﻿​﻿​﻿﻿​﻿​​​﻿﻿﻿​﻿​​​﻿​​​﻿​​​​﻿﻿​﻿﻿​​​﻿﻿​​﻿﻿​​﻿​​﻿​﻿​﻿﻿​​﻿﻿﻿​​​​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿​​​﻿﻿​​﻿​​​​﻿﻿​​​​​﻿﻿​﻿﻿﻿​​﻿​﻿﻿​​﻿​﻿​﻿​﻿﻿​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿​​​​﻿​﻿﻿​​​​​﻿﻿​​​​​﻿​﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​﻿​​​​﻿​​﻿​﻿​﻿​﻿​﻿​​​﻿﻿﻿​﻿﻿﻿​​​​​﻿​﻿​​﻿﻿​﻿​﻿﻿​​​​﻿﻿﻿​​﻿﻿​​﻿​﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​​﻿﻿​﻿​​​﻿﻿​​﻿​​﻿﻿​​​﻿﻿​​﻿﻿​​﻿​﻿​​﻿​​﻿​​﻿﻿﻿​​﻿​​​﻿﻿​​﻿​​​​﻿﻿​​﻿﻿﻿​​​​﻿﻿​﻿​﻿﻿​﻿​﻿​​​​​﻿﻿​​﻿​​​﻿​​﻿﻿​​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿﻿﻿​​﻿​﻿​​​​​﻿​﻿​​﻿​​﻿﻿​​﻿​﻿​﻿﻿﻿​​​​​﻿​​﻿​﻿​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​﻿﻿​﻿​﻿﻿﻿﻿​​﻿​﻿﻿﻿​﻿​﻿​﻿﻿﻿﻿​​﻿​﻿﻿﻿﻿​﻿​​﻿﻿​﻿​﻿​​​﻿﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​​​​﻿﻿﻿﻿​​﻿​﻿​﻿﻿​﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿​﻿​﻿​​​﻿﻿​﻿﻿﻿​﻿​​﻿﻿​﻿​​﻿﻿​​﻿​​﻿​﻿﻿​﻿​​﻿​​﻿﻿​​​​﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿﻿​​﻿​﻿﻿﻿​﻿​﻿​﻿​﻿﻿​﻿​​​﻿﻿﻿​​​​﻿﻿﻿​﻿​​​​﻿﻿​​﻿﻿​﻿​﻿​​﻿​​﻿​﻿​﻿​﻿​﻿​​﻿​​​​﻿​﻿​﻿﻿﻿​﻿​﻿​​​​​​﻿​﻿​﻿﻿​​﻿﻿​﻿​﻿​​﻿​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿​​​﻿​​﻿﻿﻿﻿​﻿​​​﻿﻿﻿​​﻿​​﻿​﻿​﻿﻿​﻿﻿﻿​﻿​﻿​​﻿﻿​​​﻿​​﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿​﻿﻿​​​​﻿​​﻿﻿​​​﻿﻿﻿​​﻿​​﻿﻿​﻿​﻿﻿​﻿﻿﻿​​​﻿​﻿​​﻿​​﻿​﻿﻿​﻿﻿﻿﻿​​﻿​﻿​﻿﻿​​﻿﻿​﻿﻿﻿​﻿​​﻿﻿​﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​﻿﻿​​﻿﻿​​​​​﻿​​﻿﻿​﻿​﻿​​﻿﻿﻿​​﻿​​﻿﻿​﻿​﻿﻿​﻿​﻿​​​﻿﻿​﻿​﻿​﻿﻿​﻿​​​​﻿﻿​​﻿​​​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​​﻿﻿﻿​​​​﻿​​﻿​​​​﻿﻿​​﻿﻿​​﻿​﻿​​﻿﻿​﻿​​﻿​​​​﻿﻿﻿​﻿​​​﻿​﻿﻿​﻿​​﻿​​​﻿​﻿​﻿​﻿​​​﻿​﻿﻿﻿​﻿​​​​﻿﻿﻿​​﻿​​﻿﻿﻿​​​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​﻿​​﻿﻿​﻿﻿﻿​​​﻿​﻿​﻿﻿​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿﻿​﻿​﻿​​﻿​﻿​​​﻿​﻿﻿﻿﻿​﻿​​​﻿﻿﻿​﻿​﻿​﻿﻿​​​﻿﻿﻿​​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​﻿​​​​﻿​​﻿﻿​﻿​﻿﻿​​​﻿​​​﻿﻿​​​﻿​﻿​﻿​﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿​﻿​​﻿﻿﻿​​​​​﻿﻿​​​﻿​﻿﻿​​​﻿﻿​﻿﻿​﻿﻿​﻿​﻿​​﻿​﻿​​﻿​﻿﻿​​﻿​​﻿﻿﻿​​﻿​​﻿﻿​﻿​​​﻿​​﻿﻿​​​﻿​​​﻿﻿​​﻿​​﻿​​﻿​﻿﻿﻿​​​​​​﻿﻿​​﻿﻿​﻿﻿​﻿​​﻿​﻿﻿​​﻿​​​﻿﻿​﻿​​﻿​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​​​​​﻿​﻿﻿﻿﻿​﻿​​​​​﻿​﻿﻿​​​​﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿​​﻿​﻿​​​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿﻿​﻿﻿﻿﻿​​﻿﻿﻿﻿​﻿")  # nopep8 lint:ok noqa
TOC_HTML = stealth2string("​﻿﻿​​﻿​﻿​﻿​​﻿﻿﻿​​﻿﻿﻿​​​​​﻿﻿﻿​﻿​​​﻿​﻿​﻿​﻿​﻿﻿﻿​​﻿​​﻿﻿﻿​﻿​​​﻿﻿﻿﻿​​﻿​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​​​​﻿​﻿​﻿​​​﻿​​﻿﻿​﻿﻿﻿​﻿​﻿​​​​​​﻿﻿​​​​​﻿​﻿​﻿﻿​​﻿﻿​﻿​​﻿​﻿﻿﻿​﻿​﻿​﻿﻿﻿​​​﻿​﻿​​​​​﻿​​﻿﻿​﻿﻿﻿​﻿​​﻿​﻿﻿​﻿​﻿​​﻿​​﻿​​﻿​​﻿​​﻿﻿​﻿﻿﻿​﻿​​​​​﻿​﻿​​​﻿﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​​﻿​﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿﻿​​​﻿​﻿​​​﻿﻿​​​﻿​﻿​﻿﻿​﻿﻿​﻿​﻿﻿​​﻿﻿﻿​​﻿​﻿​​​​​﻿​﻿﻿​﻿​​​​​﻿﻿​​﻿​​﻿﻿​​﻿﻿﻿​﻿​​​﻿​​​﻿​​﻿﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿​﻿﻿​​﻿​​﻿﻿​﻿﻿​​﻿​﻿​﻿​​​﻿​​​​﻿​​﻿﻿​﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​﻿﻿﻿​​​﻿﻿​​﻿﻿​﻿​​​​﻿﻿​﻿​​﻿​​​​﻿​​​​​﻿​﻿﻿​​​﻿﻿​﻿​﻿﻿​​﻿​​﻿﻿​​​​​﻿﻿​​﻿​﻿​﻿​​﻿﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​﻿​​﻿​​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​﻿​﻿​​​﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿​﻿​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​​​﻿​﻿﻿​﻿﻿​﻿​﻿﻿﻿​﻿​﻿​​﻿﻿​​﻿​​﻿​​​​﻿​​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​​﻿﻿​​​​​​﻿﻿​​﻿​​﻿﻿​﻿​​​​﻿﻿​﻿​​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​​​﻿​﻿​﻿﻿​​​​﻿﻿​﻿﻿﻿​​﻿​​﻿​​﻿​﻿​​﻿​​​​﻿​​﻿​﻿​​﻿​﻿​﻿​﻿​﻿​​​﻿﻿﻿​﻿﻿​﻿﻿​​​﻿​﻿​﻿​​​﻿﻿﻿﻿​​​​﻿​​﻿﻿​​​﻿﻿﻿﻿​​﻿​﻿﻿​﻿﻿​​​﻿​﻿​​​​​﻿​​﻿​​​​﻿﻿​﻿​﻿​​﻿﻿​﻿﻿​​​﻿﻿﻿﻿​﻿​​﻿​​﻿​﻿​​﻿​​​﻿​﻿​​﻿﻿​​​​​﻿​﻿​​﻿﻿​﻿﻿​﻿﻿​​​﻿​﻿﻿​﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿​﻿﻿​​﻿​​﻿﻿﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​​​​﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿​​​﻿﻿​​﻿﻿​﻿﻿​​​﻿​​​﻿﻿​​﻿​​﻿​﻿​​﻿﻿​﻿﻿﻿​​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿​﻿​​﻿﻿​﻿​﻿​﻿﻿﻿﻿​​​​﻿﻿﻿​​﻿﻿​﻿​﻿​﻿﻿﻿​​﻿﻿﻿​​​​﻿​​﻿​﻿​​﻿​​​﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​​﻿﻿​​﻿​​﻿​﻿​​​﻿​﻿﻿​﻿﻿﻿​​﻿​﻿​​﻿​​﻿﻿​​﻿​​​﻿​​​﻿﻿​​​﻿﻿​​﻿﻿​﻿﻿​​​﻿​​﻿​﻿​​​​​﻿​​﻿​​﻿​﻿﻿​​﻿​​​﻿﻿﻿​​​​​﻿​​​​﻿﻿​﻿﻿﻿​​﻿​​﻿​​﻿﻿﻿​​﻿﻿​​​﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿​﻿​​​﻿​﻿​﻿​​​﻿﻿​​﻿﻿﻿​﻿​​﻿﻿﻿​​﻿​​​﻿﻿﻿​﻿​​​﻿​​​​﻿﻿​﻿﻿​​﻿​​​​﻿​​﻿​​﻿﻿﻿​​﻿﻿﻿​﻿​​​﻿​​​​﻿﻿​​﻿﻿​​​​​​﻿﻿​﻿﻿​​﻿​﻿​​​﻿​﻿﻿﻿﻿​​﻿​﻿﻿﻿​​​​​﻿​﻿​﻿﻿​​﻿​﻿﻿​﻿​​﻿​​﻿﻿﻿﻿​﻿​﻿​​​​​​﻿﻿​​﻿​​﻿​​﻿​﻿﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿​​​​﻿﻿﻿​​​​﻿﻿​﻿​﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​​﻿﻿​﻿​​​​﻿﻿​​﻿﻿​﻿﻿​﻿​​﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿﻿﻿​﻿​​​﻿​​​﻿​​​​﻿​​​﻿​﻿﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿​​​​﻿​​﻿​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​​﻿​​​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿﻿​​​﻿​​﻿​​﻿​﻿​​﻿​﻿​​﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿﻿​​﻿​​​​﻿﻿​​​​​﻿​​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿﻿​​​﻿﻿​​​﻿﻿​﻿​​​​​﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿​​​​﻿​﻿​﻿​​​﻿​​​​﻿​​﻿﻿​​​﻿﻿​﻿﻿​﻿﻿​﻿​﻿​​﻿​​​​﻿​﻿​﻿​​​﻿​​​​﻿﻿​﻿﻿﻿​﻿​​​﻿﻿​​﻿﻿﻿​﻿﻿​﻿﻿​﻿​﻿​​﻿﻿​​​﻿​​﻿﻿​﻿​﻿﻿​​﻿​​​﻿​​​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿​​﻿​​​﻿​​​﻿​​﻿﻿​​​﻿﻿​﻿​​​​﻿​​﻿​﻿​​﻿​﻿​﻿​​​​﻿﻿​﻿​​​﻿﻿﻿​​​﻿​﻿﻿​​​​﻿​﻿​﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿﻿​​​﻿​​﻿​﻿​﻿﻿​​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​​​​​﻿​﻿​​​﻿​​​﻿​﻿​﻿﻿​​﻿﻿​﻿​​​​﻿​​﻿​﻿​​﻿﻿​​​​﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​﻿​​﻿​​﻿​​﻿​﻿​​﻿​﻿​​﻿​​﻿​​​​​﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​​﻿﻿﻿​​﻿​﻿​﻿​﻿​​​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿﻿﻿​﻿﻿​​​​﻿​﻿﻿​​﻿​﻿​﻿﻿​​﻿​﻿​​﻿﻿​​​​​﻿﻿﻿​​﻿​​﻿﻿​﻿​​﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿﻿​﻿​﻿﻿​​​​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿​​​​﻿﻿​​﻿​​﻿​﻿​​​﻿​﻿​​﻿​​​​﻿﻿​﻿​﻿​​﻿​​​​​﻿​﻿​﻿﻿​​​​​﻿﻿​​​​​﻿﻿​﻿﻿​​​​﻿﻿​​﻿﻿​﻿﻿​​​﻿​​﻿​​​​﻿﻿​﻿﻿﻿﻿​﻿​​​﻿﻿﻿​​​​﻿​﻿​​﻿﻿​​﻿﻿​​​​​﻿﻿﻿﻿​​﻿​﻿​​﻿​﻿﻿​﻿​﻿​﻿​​​﻿﻿​﻿​﻿﻿​​﻿﻿​﻿﻿​​﻿​​﻿﻿​​​﻿﻿﻿​​​﻿​﻿﻿﻿﻿​﻿​​​﻿​﻿﻿﻿﻿​﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​﻿﻿​​﻿﻿​​﻿﻿​​﻿﻿​​​﻿​﻿﻿​﻿​﻿﻿​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿​﻿﻿​​﻿​﻿﻿​​​﻿​​​﻿﻿​﻿﻿​​﻿﻿​﻿​​​​﻿﻿﻿​﻿​​​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿﻿​​﻿​​​﻿​​​﻿​​​﻿​​​﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿​​​﻿﻿​​﻿​​​﻿﻿​​​​​﻿﻿​﻿﻿﻿​​﻿​​​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​​​﻿​​​﻿​﻿﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​﻿​﻿​​﻿﻿​﻿﻿​﻿​﻿​​﻿​​﻿﻿﻿​​﻿﻿﻿﻿​﻿​​﻿​​​​﻿​​​﻿﻿​﻿﻿﻿​﻿​​​﻿​﻿​​﻿﻿﻿​​​​﻿​​​​﻿​​﻿﻿﻿​​​﻿​﻿​​﻿​​​​﻿﻿​﻿​​​​﻿﻿​﻿​​﻿​﻿​​​﻿​​​﻿﻿​﻿﻿​​​﻿​﻿​﻿​﻿​​﻿﻿​﻿​﻿​﻿​﻿﻿​​﻿​﻿​​﻿​﻿​​﻿​​​﻿﻿​​﻿﻿​﻿﻿​​​﻿﻿﻿​​​​​﻿​​﻿​​﻿​﻿​﻿﻿​​﻿​​﻿​﻿​﻿﻿​​﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​​​​​﻿​​﻿﻿﻿﻿​​﻿﻿​﻿​​​﻿﻿​​﻿﻿​​﻿​﻿​​​﻿​​﻿﻿​﻿﻿​​﻿﻿​﻿﻿﻿﻿​​﻿﻿​​​​​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​​​​﻿﻿​​﻿﻿​​﻿﻿﻿﻿​​​​﻿﻿﻿​﻿​​​﻿​​​​﻿﻿​﻿​﻿​​​​​﻿​​​​﻿​​﻿﻿​﻿﻿​﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​​﻿﻿​﻿​​​﻿​﻿​﻿﻿​​﻿﻿﻿​﻿​﻿​​​​​﻿​​​﻿﻿​​﻿﻿﻿​​​​​​﻿﻿​﻿​﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿﻿​​​﻿​﻿​﻿﻿​﻿﻿​​﻿​﻿​﻿​​﻿﻿​​​﻿﻿​﻿​​​​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿​﻿﻿​﻿​​﻿﻿﻿﻿​﻿﻿​﻿﻿​﻿​﻿​​​​﻿​​​﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿﻿​﻿​​​​​﻿​﻿﻿﻿​​﻿​​﻿﻿​﻿​﻿​​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿​﻿​﻿​﻿﻿​​​​﻿​​﻿﻿﻿​​﻿﻿﻿﻿​​​​​﻿﻿​​﻿​​​﻿﻿​​﻿﻿​​﻿﻿​​​​​​﻿﻿​​﻿​​﻿​﻿﻿​​​​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿​​​​﻿﻿﻿​​​​​﻿﻿​​﻿​​﻿﻿﻿​​﻿​​​﻿​﻿​﻿﻿​﻿​​﻿​﻿﻿​﻿﻿​﻿​​﻿​﻿​​﻿﻿​​​﻿​​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿​​﻿​﻿﻿​​​﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿﻿﻿​﻿​​​​​﻿​​﻿﻿﻿​​​​﻿​​​​﻿​​﻿​​​​​﻿​﻿​​﻿​​​​﻿﻿​​​﻿​​﻿​﻿﻿​​﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​​﻿﻿​﻿​﻿​﻿﻿﻿​﻿​​​﻿﻿​​﻿​​​﻿​﻿​﻿﻿﻿​﻿​​​​﻿﻿​﻿﻿﻿​﻿​​﻿﻿﻿​​﻿﻿﻿​​﻿​​​﻿﻿​​﻿﻿​﻿​​﻿​​​​​﻿﻿​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿​​​﻿​﻿​﻿﻿​​﻿​​​﻿​​​﻿​​﻿﻿﻿﻿​​﻿﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​﻿​​﻿​﻿﻿​​﻿﻿﻿​​​​​﻿﻿​​​﻿​﻿﻿​﻿​​​​﻿​​﻿​﻿​​​﻿﻿​​﻿​​​﻿﻿​​﻿​​﻿​​​﻿﻿​​﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿﻿​​﻿﻿​​﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​​​​​﻿﻿​﻿﻿​﻿​﻿​﻿​​​​​﻿​﻿​﻿﻿​​﻿​​​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿﻿﻿​​​﻿​​﻿﻿​​﻿​​﻿﻿﻿﻿​﻿​​﻿​﻿​﻿​​​﻿​​﻿﻿​﻿​﻿﻿﻿​​﻿﻿​﻿​​​​﻿​​﻿﻿​​​​﻿​﻿﻿​​﻿﻿​​﻿​﻿​​​​​﻿﻿﻿​​​​​​﻿﻿​​﻿​​﻿​​﻿﻿﻿​​​﻿﻿​​﻿​​﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿​​﻿﻿​﻿﻿​﻿​﻿﻿﻿﻿​​﻿​﻿​​﻿​​﻿​﻿​​﻿​​﻿​﻿﻿​​﻿﻿﻿​​﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿​​​﻿﻿﻿​﻿﻿​﻿﻿​﻿​﻿​﻿​​﻿​​﻿﻿﻿​﻿​​​﻿​​​﻿​​​﻿﻿﻿﻿​​﻿")  # nopep8 lint:ok noqa
TOC_NCX = stealth2string("​﻿﻿​​﻿​﻿​﻿​​﻿﻿﻿​​﻿﻿﻿​​​​​​﻿﻿​​​﻿​﻿﻿​﻿​﻿﻿​﻿​​​﻿​​​﻿​​​﻿﻿​​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​​​​﻿​﻿​﻿​​​﻿​﻿﻿​﻿​​​​﻿​﻿﻿​​​​﻿﻿​​﻿​​​​﻿​﻿​﻿﻿​﻿﻿​﻿​​​​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿​​﻿﻿​﻿​​​﻿​​​​﻿﻿​﻿​﻿​​﻿​​﻿​﻿​﻿﻿​​﻿﻿﻿​​​﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​​​﻿​﻿​​​​﻿﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿﻿​﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​​﻿​​﻿​﻿​﻿﻿​​﻿​​​​﻿﻿​﻿﻿​﻿﻿​​​﻿​​​﻿​​​​﻿﻿﻿​​﻿​​﻿﻿﻿​​​​﻿﻿​﻿​﻿​​﻿​﻿﻿​​﻿​﻿﻿​﻿﻿​​​​﻿​﻿​﻿﻿​﻿​​​​​﻿​﻿​​﻿​﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿​﻿​​​​﻿​​​​​﻿​​﻿​﻿​﻿﻿​﻿​​​​​﻿​﻿﻿﻿​​﻿​​﻿​﻿​﻿​​​﻿﻿﻿​​​﻿​﻿﻿​​﻿﻿​​﻿﻿﻿﻿​​﻿​​﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿​﻿​​﻿​​﻿​​​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​​​​​﻿​​​﻿﻿​​​﻿﻿﻿​​﻿​​﻿​﻿﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿​﻿​​﻿​﻿​﻿﻿​﻿﻿​​﻿​​​﻿﻿​​﻿﻿​​﻿​﻿​​​​​﻿​​​﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​​​﻿﻿﻿﻿​​​​﻿﻿​​﻿﻿﻿​﻿﻿​​﻿​​​﻿﻿​﻿﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿﻿﻿​﻿​﻿​﻿﻿​﻿﻿﻿﻿​​﻿﻿​﻿​​​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​​﻿​﻿﻿​​​​﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​﻿﻿​​﻿﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿​​﻿​﻿​​​﻿﻿﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​﻿﻿​​﻿​​​﻿﻿​​﻿﻿​​​​﻿​﻿﻿﻿﻿​​﻿​﻿﻿​﻿​﻿﻿​​﻿﻿﻿​​​​﻿﻿​​​​﻿​​﻿﻿​﻿﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿​﻿﻿​​﻿​​﻿​​﻿​﻿​​﻿​​﻿​﻿​﻿​​﻿​​﻿​​​﻿​﻿​​﻿﻿﻿​​﻿​﻿﻿﻿​﻿​﻿​﻿​​​﻿​​​﻿﻿​﻿﻿​​​﻿​​﻿﻿​​​﻿﻿​​﻿﻿﻿​​﻿﻿​​​﻿​﻿﻿​﻿​​﻿​﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿​​​﻿﻿​​﻿​​﻿​​﻿﻿​﻿​﻿﻿﻿​​﻿​​﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿​​​​﻿﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​​﻿﻿​﻿​﻿​​​﻿​﻿​​​​​﻿​﻿​​﻿​﻿​​​﻿﻿​﻿​​​﻿​﻿​﻿​﻿​​﻿​﻿​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​﻿​​​﻿﻿​﻿﻿​​​﻿﻿﻿﻿​﻿​​﻿﻿﻿​﻿​​​﻿​﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿﻿﻿​​​﻿​﻿﻿​​​﻿​​﻿﻿​​﻿​​​﻿﻿﻿​﻿﻿​​﻿​​﻿​​﻿​﻿﻿​​​​﻿​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿﻿﻿​​​﻿​﻿﻿﻿﻿​﻿​​​﻿​﻿​﻿﻿​﻿﻿​﻿﻿﻿​​​﻿﻿​﻿﻿﻿​﻿​﻿﻿​﻿​​﻿﻿﻿​​﻿​​﻿​​﻿﻿﻿​​​﻿​﻿﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿​​​​﻿​﻿﻿﻿​​﻿​​﻿​​​﻿﻿​​​﻿﻿​﻿​​​﻿​﻿​﻿﻿​​﻿​﻿​﻿​﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿﻿​﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿​​​​﻿​​​﻿​﻿​﻿​​﻿﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿​﻿​​﻿​﻿﻿​​​﻿​​﻿​﻿​﻿​​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿​​﻿​​﻿​​​​​﻿​﻿﻿﻿​﻿​​​﻿​﻿​﻿​﻿​﻿​​﻿​﻿​​﻿﻿​​﻿﻿​​﻿​​​﻿​​​﻿​﻿​﻿﻿​​﻿​​﻿﻿​﻿​﻿﻿﻿​﻿﻿​​﻿​﻿﻿​﻿​​﻿﻿﻿​﻿​​​﻿﻿​﻿﻿﻿​​﻿​​​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿​​​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​​​​﻿​​﻿​​﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿​​﻿﻿﻿﻿​​​​﻿​​﻿​​﻿​​﻿﻿​﻿​﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿﻿﻿﻿​﻿​﻿​﻿​﻿​​﻿﻿​﻿﻿​​﻿﻿​﻿﻿﻿​​​﻿​﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿​﻿​​​​﻿​﻿﻿​​﻿​﻿﻿﻿​​﻿​​﻿﻿﻿﻿​﻿​​﻿​​​​﻿​​​﻿​﻿﻿﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​​﻿​​​﻿﻿​​​﻿﻿​﻿﻿﻿﻿​​​​﻿​﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿​​​﻿​​​﻿​​﻿​﻿﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​﻿​​​​﻿﻿​﻿​​​﻿​​​​﻿﻿​﻿​​​﻿﻿﻿​﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿﻿​﻿​​​﻿​​​​﻿﻿​​​​​﻿​﻿​​﻿​​﻿﻿﻿﻿​​​​﻿​﻿​﻿﻿﻿​﻿﻿﻿​​​﻿​﻿﻿﻿​​​﻿​﻿﻿​​​﻿​​﻿﻿﻿​﻿​​​﻿​​​​﻿​​﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿​​​​﻿﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿﻿​﻿﻿﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​﻿﻿﻿﻿​﻿﻿​​​​﻿​﻿﻿﻿​​﻿﻿​﻿​﻿﻿​﻿​​​﻿​﻿​﻿﻿​﻿​﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿﻿​​​﻿﻿​﻿​​​﻿﻿​​﻿​​﻿​​​​﻿​​﻿﻿﻿﻿​﻿﻿​﻿﻿​​​​﻿﻿​​​​​﻿﻿﻿​﻿﻿​​﻿​​﻿​​﻿​​﻿﻿​​﻿﻿​​﻿﻿​​​​​﻿﻿﻿​﻿﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​​﻿﻿​​﻿﻿﻿﻿​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿​﻿​​﻿​​﻿﻿﻿​​​​﻿﻿​​​﻿​​﻿﻿​​﻿﻿​​﻿﻿​﻿​﻿​​​﻿​﻿﻿﻿﻿​﻿​﻿​​﻿​​﻿​﻿​​﻿﻿​﻿​​​﻿﻿﻿​​﻿﻿​﻿​​​﻿﻿​﻿​﻿﻿​﻿​​​​​﻿​﻿﻿﻿​﻿​​​​﻿﻿​​​﻿​﻿​​​﻿﻿﻿​﻿​​​​﻿​​﻿​​​﻿﻿​​​﻿﻿​​​﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿​​​﻿​​​﻿​​​﻿﻿﻿﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿​​​​​﻿﻿﻿​​​​​﻿﻿​﻿​﻿​​﻿﻿​﻿​​​﻿﻿﻿​​﻿﻿​﻿﻿​﻿​﻿​​﻿​﻿​​​​​﻿​​﻿​﻿﻿​​﻿﻿﻿​​﻿​​﻿﻿​​​​​﻿​﻿﻿​​​​﻿﻿​﻿​﻿​​﻿﻿​​​﻿﻿​​﻿﻿​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿﻿​​​​﻿﻿﻿​​​​﻿﻿​​​﻿​​​﻿﻿​​​﻿​​﻿​﻿​﻿﻿​﻿​﻿​﻿﻿﻿​﻿​​​﻿﻿​​​﻿​﻿﻿﻿﻿​﻿​﻿﻿​﻿​​​﻿﻿﻿​​​​﻿﻿​​﻿​​​​﻿﻿​﻿​﻿​﻿﻿​﻿​﻿﻿​​﻿﻿​​​​​﻿​﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​﻿​﻿​​﻿﻿​​​﻿​﻿﻿﻿​﻿​​​﻿​​﻿﻿​﻿​​﻿﻿​​﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​​﻿​​﻿﻿​​​﻿​​﻿​﻿​​​﻿​﻿﻿​﻿​​​​﻿​​​﻿​﻿​﻿​﻿﻿​​﻿​﻿﻿​​​﻿​​﻿﻿﻿​​​​​﻿​​﻿​​​​​﻿﻿​﻿​﻿​﻿﻿​​​﻿​​﻿​​​﻿​﻿​﻿﻿​﻿​​﻿​﻿​﻿​​​﻿​﻿﻿​​​﻿﻿​​﻿﻿﻿﻿​﻿")  # nopep8 lint:ok noqa


def html2ebook(files_list: tuple, epub_file: Path=Path(uuid4().hex + ".epub"),
               extensions: tuple=(".html", ".htm", ".xhtml"),
               compression: int=8, checksum: bool=False,
               zip_comment: str=None, metadata_dict: dict={}) -> Path:
    """Take a tuple of files,with HTMLs,and convert them into 1 eBook ePub."""

    manifest, spine, toc, toc2 = deque(), deque(), deque(), deque()

    with zipfile.ZipFile(epub_file, 'w', compression=int(compression)) as epub:
        epub.writestr("mimetype", "application/epub+zip\n")  # Mimetype.
        epub.writestr("META-INF/container.xml", CONTAINER)   # Metadata INF.

        for i, f in enumerate(tuple(files_list)):  # iter list,compress,parse.
            rela, name, d = os.path.relpath(f), os.path.basename(f), str(i + 1)
            if f.lower().endswith(extensions):  # if file is html add it
                spine.append(f' <itemref idref="{d}" /> <!-- Spine {f} --> \n')
                manifest.append(
                    f'<item id="id_{d}" href="{rela}" media-type="text/html"/>'
                )  # Manifest file, eBook Spec.
                toc.append(
                    f'''<li> <a href="{rela}" title="{rela}" alt="{name}">
                        <b>{rela}</b></a> </li> <!-- File {name} --> \n'''
                )  # Table of content.
                toc2.append(
                    f'''<navPoint id="{d}" playOrder="{i}">
                        <navLabel><text>{rela}</text></navLabel>
                        <content src="{rela}"/></navPoint><!-- TOC {f} -->\n'''
                )  # Table of content 2.
            epub.write(f,  rela)  # Write all files to ZIP, html or not.

        epub.writestr('toc.html',
                      TOC_HTML.format(table_of_contents="".join(toc)))  # TOC 1
        epub.writestr('toc.ncx',
                      TOC_NCX.format(table_of_contents="".join(toc2)))  # TOC 2

        epub.writestr('content.opf', INDEX_HTML.format(  # Metadata.
            spine=" ".join(spine),
            manifest=" ".join(manifest),
            author=metadata_dict.get("author", str(getuser()).capitalize()),
            des=metadata_dict.get("description", f"{ epub_file } eBook ePub."),
            lang=metadata_dict.get("language", str(getdefaultlocale()[0][:2])),
            pub=metadata_dict.get("publisher", f"{ node() }, { platform() }."),
            title=metadata_dict.get("title", str(epub_file).capitalize()[:80]),
            copi=metadata_dict.get(
                "copyright",
                "Creative Commons (https:CreativeCommons.org) CC-BY-NC-SA 4+"),
            date=metadata_dict.get(
                "date",
                datetime.now().replace(microsecond=0).astimezone().isoformat())
        ))

    if zip_comment and isinstance(zip_comment, str):
        set_zip_comment(epub_file, zip_comment.strip())

    return Path(autochecksum(epub_file, update=1) if checksum else epub_file)
