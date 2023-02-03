# TODO: PLDify init scripts
#
# Conditional build:
%bcond_with	gnome1	# Hoover GUI client (GTK+ 1.x + GNOME 1.x ZVT based)
%bcond_without	gtk1	# FLIM and Hoover GUI clients (GTK+ 1.x based)
#
%if %{without gtk1}
%undefine	with_gnome1
%endif
Summary:	System for monitoring and management of a cluster of nodes
Summary(pl.UTF-8):	System do monitorowania i zarządzania klastrem węzłów
Name:		vacm
Version:	2.0.5a
Release:	9
License:	LGPL v2.1+ (library), GPL v2+ (the rest)
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/vacm/%{name}-%{version}.tar.gz
# Source0-md5:	8c68f51bded2a6c268e899013d6420f3
Patch0:		%{name}-build.patch
Patch1:		%{name}-sh.patch
Patch2:		%{name}-link.patch
Patch3:		dvips.patch
Patch4:		openssl.patch
Patch5:		%{name}-gettext.patch
Patch6:		glibc.patch
URL:		http://vacm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-utils
BuildRequires:	gettext-tools
%{?with_gtk1:BuildRequires:	gtk+-devel >= 1.2.6}
# libzvt component
%{?with_gnome1:BuildRequires:	gnome-libs-devel}
%{?with_gnome1:BuildRequires:	imlib-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	openjade
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	readline-devel
BuildRequires:	texlive-dvips
BuildRequires:	texlive-jadetex
BuildRequires:	texlive-latex-marvosym
BuildRequires:	texlive-latex-ams
BuildRequires:	texlive-latex-extend
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VACM (Pronounced VaKuum) is a client/server system allowing monitoring
and management of a cluster of nodes equipped with Intel(TM)'s
Intelligent Platform Management Interface (IPMI). Management
capabilities include device power control, nvram system event log
download, hardware reset, and remote BIOS console. Monitoring
capabilities include power system monitoring, chassis intrusion
monitoring, fan status monitoring, and O/S watchdog monitoring. Since
the IPMI is implemented in hardware running on separate
microcontrollers, monitoring a node does *not* impact on the monitored
node's performance. Furthermore, VACM allows monitoring and management
of a node from a remote station (via TCP/IP).

%description -l pl.UTF-8
VACM (wymawiane jak VaKuum) to system klient-serwer umożliwiający
monitorowanie i zarządzanie klastrem węzłów wyposażonych w interfejs
Intel(TM) IPMI (Intelligent Platform Management Interface). Możliwości
zarządzania obejmują sterowanie zasilaniem urządzenia, pobieranie logu
systemowego z pamięci nvram, sprzętowy reset oraz zdalną konsolę
BIOS-u. Możliwości monitorowania obejmują monitorowanie zasilania
systemu, monitorowanie otwarcia obudowy, monitorowanie stanu
wentylatorów oraz monitorowanie watchdoga systemu operacyjnego. Jako
że IMPI jest zaimplementowane w sprzęcie działającym na osobnych
mikrokontrolerach, monitorowanie węzła nie ma wpływu na wydajność
monitorowanego węzła. Co więcej, VACM pozwala na monitorowanie i
zarządzanie węzła ze zdalnej maszyny (poprzez TCP/IP).

%package libs
Summary:	VACM libraries
Summary(pl.UTF-8):	Biblioteki VACM
Group:		Libraries

%description libs
VACM libraries.

%description libs -l pl.UTF
Biblioteki VACM.

%package devel
Summary:	Header files for VACM libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek VACM
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for VACM libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek VACM.

%package static
Summary:	Static VACM libraries
Summary(pl.UTF-8):	Statyczne biblioteki VACM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static VACM libraries.

%description static -l pl.UTF-8
Statyczne biblioteki VACM.

%package node
Summary:	VACM client node
Summary(pl.UTF-8):	Węzeł kliencki VACM
Group:		Applications/System
Requires:	%{name}-libs = %{version}-%{release}

%description node
Package to be installed on VACM client nodes. It contains daemons for
use with various VACM modules for additional monitoring functionality.

%description node -l pl.UTF-8
Pakiet do zainstalowania na węzłach klienckich VACM. Zawiera demony
przeznaczone do użycia z różnymi modułami VACM, dostarczającymi
dodatkowe funkcje monitorowania.

%package flim
Summary:	Flim GUI for VACM
Summary(pl.UTF-8):	Graficzny interfejs Flim do VACM-a
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-sercon = %{version}-%{release}
Requires:	xterm
Requires:	gtk+ >= 1.2.6

%description flim
Flim is a Graphical User Interface (GUI) for VACM which provides
easy interaction with the nexxus through several plugin modules.

%description flim -l pl.UTF-8
Flim to graficzny interfejs użytkownika (GUI) do VACM-a, zapewniający
łatwą interakcję z nexxusem poprzez kilka modułów wtyczek.

%package hoover
Summary:	Hoover GUI for VACM
Summary(pl.UTF-8):	Graficzny interfejs Hoover do VACM-a
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}

%description hoover
Hoover is a Graphical User Interface (GUI) for VACM.

%description hoover -l pl.UTF-8
Hoover to graficzny interfejs użytkownika (GUI) do VACM-a.

%package sercon
Summary:	Serial Console Terminal program
Summary(pl.UTF-8):	Program terminala do konsoli szeregowej
Group:		Applications/System
Requires:	%{name}-libs = %{version}-%{release}

%description sercon
Command-line serial console terminal program to remotely access
consoles of nodes on a VACM cluster.

%description sercon -l pl.UTF-8
Działający z linii poleceń program terminala do konsoli szeregowej
służący do zdalnego dostępu do konsol węzłów w klastrze VACM.

%package vash
Summary:	VACM command line client
Summary(pl.UTF-8):	Klient linii poleceń do VACM-a
Group:		Applications/System
Requires:	%{name}-libs = %{version}-%{release}

%description vash
VACM command line client for scripting and low level command-line
access.

%description vash -l pl.UTF-8
Klient linii poleceń do wykonywania skryptów oraz niskopoziomowego
dostępu.

%package doc
Summary:	VACM documentation
Summary(pl.UTF-8):	Dokumentacja do VACM-a
Group:		Documentation

%description doc
VACM documentation.

%description doc -l pl.UTF-8
Dokumentacja do VACM-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%{__sed} -i -e 's///g' nexxus/nexxus_modules/emp/include/iana_list.h

%build
cp -f /usr/share/gettext/config.rpath .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd clients/flim
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../..
%configure \
	--enable-pam \
	--enable-ssl \
	--enable-static \
	%{!?with_gtk1:--without-flim} \
	%{!?with_gnome1:--without-hoover}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/rc.d/init.d,/etc/logrotate.d,/etc/sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=$RPM_BUILD_ROOT%{_docdir}/vacm-doc-%{version}

install $RPM_BUILD_ROOT%{_libdir}/vacm/exports/* $RPM_BUILD_ROOT%{_sbindir}
install packaging/RedHat/vacm.init $RPM_BUILD_ROOT/etc/rc.d/init.d/vacm
install packaging/RedHat/node.init $RPM_BUILD_ROOT/etc/rc.d/init.d/vacm-node
install packaging/RedHat/vacm-logrotate $RPM_BUILD_ROOT/etc/logrotate.d/vacm
install packaging/RedHat/vacm.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/vacm

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libloose.la

%{?with_gtk1:%find_lang flim}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add vacm
%service vacm restart

%preun
if [ "$1" = "0" ]; then
	%service -q vacm stop
	/sbin/chkconfig --del vacm
fi

%post node
/sbin/chkconfig --add vacm-node
%service vacm-node restart

%preun node
if [ "$1" = "0" ]; then
	%service -q vacm-node stop
	/sbin/chkconfig --del vacm-node
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	hoover -p /sbin/ldconfig
%postun	hoover -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README_FIRST
%attr(755,root,root) %{_bindir}/nexxus
%attr(755,root,root) %{_bindir}/nuptime
%dir %{_libdir}/vacm
%dir %{_libdir}/vacm/exports
%attr(755,root,root) %{_libdir}/vacm/exports/vacm_*
%dir %{_libdir}/vacm/modules
%attr(755,root,root) %{_libdir}/vacm/modules/*.loose
%{_libdir}/vacm/sercon.otp
%attr(754,root,root) /etc/rc.d/init.d/vacm
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vacm
%config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/vacm
# FIXME: /etc
%config(noreplace) %verify(not md5 mtime size) %{_libdir}/vacm/vacm_configuration

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libloose-%{version}.so
%attr(755,root,root) %{_libdir}/libvacmclient-%{version}.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libloose.so
%attr(755,root,root) %{_libdir}/libvacmclient.so
%{_libdir}/libvacmclient.la
%{_includedir}/libloose.h
%{_includedir}/vacmclient_api.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libloose.a
%{_libdir}/libvacmclient.a

%files node
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/vacm_sys_stat_proxy
%attr(755,root,root) %{_sbindir}/vacm_sys_statd
%attr(755,root,root) %{_sbindir}/vacm_user_admd
%attr(754,root,root) /etc/rc.d/init.d/vacm-node

%if %{with gtk1}
%files flim -f flim.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flim
%dir %{_libdir}/flim
%attr(755,root,root) %{_libdir}/flim/*.p
%{_datadir}/flim
%endif

%if %{with gnome1}
%files hoover
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hoover
%attr(755,root,root) %{_libdir}/libgessie-%{version}.so
%{_mandir}/man8/hoover.8*
%endif

%files sercon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sercon_terminal

%files vash
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vash

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}
