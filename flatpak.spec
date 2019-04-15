#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flatpak
Version  : 1.0.7
Release  : 47
URL      : https://github.com/flatpak/flatpak/releases/download/1.0.7/flatpak-1.0.7.tar.xz
Source0  : https://github.com/flatpak/flatpak/releases/download/1.0.7/flatpak-1.0.7.tar.xz
Source1  : flatpak-init.service
Source2  : flatpak.tmpfiles
Summary  : Linux application sandboxing and distribution framework (formerly xdg-app)
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: flatpak-autostart = %{version}-%{release}
Requires: flatpak-bin = %{version}-%{release}
Requires: flatpak-config = %{version}-%{release}
Requires: flatpak-data = %{version}-%{release}
Requires: flatpak-lib = %{version}-%{release}
Requires: flatpak-libexec = %{version}-%{release}
Requires: flatpak-license = %{version}-%{release}
Requires: flatpak-locales = %{version}-%{release}
Requires: flatpak-services = %{version}-%{release}
Requires: glib-networking
Requires: gnupg
Requires: gsettings-desktop-schemas
Requires: xdg-desktop-portal
BuildRequires : bison
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : gpgme
BuildRequires : gpgme-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libarchive-dev
BuildRequires : libassuan-dev
BuildRequires : libcap-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(appstream-glib)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libgsystem)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(ostree-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xdg-desktop-portal)
BuildRequires : sed
BuildRequires : valgrind
BuildRequires : xdg-desktop-portal
BuildRequires : xmlto
Patch1: 0001-Add-var-cache-to-XDG_DATA_DIRS-var.patch
Patch2: 0002-add-cleanup-helpers.patch
Patch3: CVE-2019-10063.patch

%description
<p align="center">
<img src="https://github.com/flatpak/flatpak/blob/master/flatpak.png?raw=true" alt="Flatpak icon"/>
</p>

%package autostart
Summary: autostart components for the flatpak package.
Group: Default

%description autostart
autostart components for the flatpak package.


%package bin
Summary: bin components for the flatpak package.
Group: Binaries
Requires: flatpak-data = %{version}-%{release}
Requires: flatpak-libexec = %{version}-%{release}
Requires: flatpak-config = %{version}-%{release}
Requires: flatpak-license = %{version}-%{release}
Requires: flatpak-services = %{version}-%{release}

%description bin
bin components for the flatpak package.


%package config
Summary: config components for the flatpak package.
Group: Default

%description config
config components for the flatpak package.


%package data
Summary: data components for the flatpak package.
Group: Data

%description data
data components for the flatpak package.


%package dev
Summary: dev components for the flatpak package.
Group: Development
Requires: flatpak-lib = %{version}-%{release}
Requires: flatpak-bin = %{version}-%{release}
Requires: flatpak-data = %{version}-%{release}
Provides: flatpak-devel = %{version}-%{release}
Requires: flatpak = %{version}-%{release}

%description dev
dev components for the flatpak package.


%package lib
Summary: lib components for the flatpak package.
Group: Libraries
Requires: flatpak-data = %{version}-%{release}
Requires: flatpak-libexec = %{version}-%{release}
Requires: flatpak-license = %{version}-%{release}

%description lib
lib components for the flatpak package.


%package libexec
Summary: libexec components for the flatpak package.
Group: Default
Requires: flatpak-config = %{version}-%{release}
Requires: flatpak-license = %{version}-%{release}

%description libexec
libexec components for the flatpak package.


%package license
Summary: license components for the flatpak package.
Group: Default

%description license
license components for the flatpak package.


%package locales
Summary: locales components for the flatpak package.
Group: Default

%description locales
locales components for the flatpak package.


%package services
Summary: services components for the flatpak package.
Group: Systemd services

%description services
services components for the flatpak package.


%prep
%setup -q -n flatpak-1.0.7
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555297250
export CFLAGS="$CFLAGS -fcf-protection=full -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fcf-protection=full -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fcf-protection=full -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fcf-protection=full -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --disable-documentation --with-profile-dir=/usr/share/defaults/etc/profile.d
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check ||:

%install
export SOURCE_DATE_EPOCH=1555297250
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flatpak
cp COPYING %{buildroot}/usr/share/package-licenses/flatpak/COPYING
cp libglnx/COPYING %{buildroot}/usr/share/package-licenses/flatpak/libglnx_COPYING
%make_install
%find_lang flatpak
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/flatpak-init.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/flatpak.conf
## install_append content
mkdir -p %{buildroot}/usr/share/dbus-1/system.d/
mv system-helper/org.freedesktop.Flatpak.SystemHelper.conf %{buildroot}/usr/share/dbus-1/system.d/
mkdir -p %{buildroot}/usr/lib/systemd/system/graphical.target.wants
ln -sf ../flatpak-init.service %{buildroot}/usr/lib/systemd/system/graphical.target.wants/flatpak-init.service
cp flatpak-cleanup.service %{buildroot}/usr/lib/systemd/system/flatpak-cleanup.service
mkdir -p %{buildroot}/usr/libexec
cp clr-flatpak-cleanup %{buildroot}/usr/libexec/clr-flatpak-cleanup
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/graphical.target.wants/flatpak-init.service

%files bin
%defattr(-,root,root,-)
/usr/bin/flatpak
/usr/bin/flatpak-bisect
/usr/bin/flatpak-coredumpctl

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/flatpak.conf

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Flatpak-1.0.typelib
/usr/share/bash-completion/completions/flatpak
/usr/share/dbus-1/interfaces/org.freedesktop.Flatpak.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Flatpak.xml
/usr/share/dbus-1/services/org.freedesktop.Flatpak.service
/usr/share/dbus-1/services/org.freedesktop.portal.Flatpak.service
/usr/share/dbus-1/system-services/org.freedesktop.Flatpak.SystemHelper.service
/usr/share/dbus-1/system.d/org.freedesktop.Flatpak.SystemHelper.conf
/usr/share/defaults/etc/profile.d/flatpak.sh
/usr/share/flatpak/triggers/desktop-database.trigger
/usr/share/flatpak/triggers/gtk-icon-cache.trigger
/usr/share/flatpak/triggers/mime-database.trigger
/usr/share/gdm/env.d/flatpak.env
/usr/share/gir-1.0/*.gir
/usr/share/polkit-1/actions/org.freedesktop.Flatpak.policy
/usr/share/polkit-1/rules.d/org.freedesktop.Flatpak.rules
/usr/share/zsh/site-functions/_flatpak

%files dev
%defattr(-,root,root,-)
/usr/include/flatpak/flatpak-bundle-ref.h
/usr/include/flatpak/flatpak-enum-types.h
/usr/include/flatpak/flatpak-error.h
/usr/include/flatpak/flatpak-installation.h
/usr/include/flatpak/flatpak-installed-ref.h
/usr/include/flatpak/flatpak-portal-error.h
/usr/include/flatpak/flatpak-ref.h
/usr/include/flatpak/flatpak-related-ref.h
/usr/include/flatpak/flatpak-remote-ref.h
/usr/include/flatpak/flatpak-remote.h
/usr/include/flatpak/flatpak-transaction.h
/usr/include/flatpak/flatpak-version-macros.h
/usr/include/flatpak/flatpak.h
/usr/lib64/libflatpak.so
/usr/lib64/pkgconfig/flatpak.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libflatpak.so.0
/usr/lib64/libflatpak.so.0.10007.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/clr-flatpak-cleanup
/usr/libexec/flatpak-bwrap
/usr/libexec/flatpak-dbus-proxy
/usr/libexec/flatpak-portal
/usr/libexec/flatpak-session-helper
/usr/libexec/flatpak-system-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flatpak/COPYING
/usr/share/package-licenses/flatpak/libglnx_COPYING

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/graphical.target.wants/flatpak-init.service
/usr/lib/systemd/system/flatpak-cleanup.service
/usr/lib/systemd/system/flatpak-init.service
/usr/lib/systemd/system/flatpak-system-helper.service
/usr/lib/systemd/user/dbus.service.d/flatpak.conf
/usr/lib/systemd/user/flatpak-portal.service
/usr/lib/systemd/user/flatpak-session-helper.service

%files locales -f flatpak.lang
%defattr(-,root,root,-)

