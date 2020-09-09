#!/bin/bash

VERSION=$1

if [ ! $(echo $VERSION | egrep "^[0-9\.]+$") ]; then
	echo "Specify a vaild version number as argument"
	exit 1
fi

TARBALL=../tarballs/sessioninstaller-$VERSION.tar

if [ -e $TARBALL.gz ]; then
	echo "Tarball already exists!"
	exit 1
fi

bzr export --format tar $TARBALL
bzr log --gnu-changelog -n0 > ChangeLog
tar -rvf $TARBALL ChangeLog
gzip $TARBALL
gpg --armor --sign --detach-sig $TARBALL.gz
