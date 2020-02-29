#!/bin/bash
set -e


apt update
apt upgrade -y
apt install -y lsb-release
export DEBIAN_FRONTEND=noninteractive
echo "mysql-apt-config mysql-apt-config/select-server select mysql-8.0" | debconf-set-selections
MYSQL_DEB_NAME=mysql-apt-config_0.8.13-1_all.deb
wget http://dev.mysql.com/get/${MYSQL_DEB_NAME}
dpkg -i ${MYSQL_DEB_NAME}
apt update
apt install -y mysql-client libmysqlclient-dev libssl-dev binutils libproj-dev gdal-bin

LIBGEOS_VERSION=3.6.0
wget http://download.osgeo.org/geos/geos-${LIBGEOS_VERSION}.tar.bz2
tar xjf geos-${LIBGEOS_VERSION}.tar.bz2
cd geos-${LIBGEOS_VERSION}
./configure
make
make install

pip install -U pip pipenv
