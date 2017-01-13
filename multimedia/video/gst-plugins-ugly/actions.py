#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")

    # sidplay is in contrib.
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --disable-sidplay \
                         --with-package-name=\"PisiLinux gstreamer-plugins-ugly package\" \
                         --with-package-origin=\"http://www.pisilinux.org/eng\"")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

# causes sandbox violations
#def check():
#    # causes sandbox violation
#    autotools.make("-C tests/check check")

def install():
    autotools.install()

    pisitools.dodoc("README", "COPYING", "AUTHORS", "NEWS")
