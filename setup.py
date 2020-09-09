#!/usr/bin/env python

import DistUtilsExtra.auto

DistUtilsExtra.auto.setup(name="sessioninstaller",
      description="APT based installer using PackageKit session DBus API",
      homepage="http://launchpad.net/sessioninstaller",
      author="Sebastian Heinlein",
      packages=["sessioninstaller", "sessioninstaller.backends"],
      scripts=["session-installer", "gst-install"],
      data_files=[("share/dbus-1/services",
                   ["data/sessioninstaller.service"]),
                  ("share/man/man1",
                   ["doc/session-installer.1", "doc/gst-install.1"])],
      license = "GNU GPL",
      platforms = "posix")
