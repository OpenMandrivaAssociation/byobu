%define name	byobu
%define version 2.20
%define release %mkrel 1

Summary: 	Profiles for the GNU screen manager
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://launchpad.net/byobu/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
License: 	GPLv3+
Group:		Terminals
Url:		https://launchpad.net/screen-profiles
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	gettext
Requires:	screen, python >= 2.5, newt, gettext

%description
byobu includes a set of profiles for the GNU screen window
manager. These profiles are quite useful on server machines which are
not running a graphical desktop. The 'screen' command provides a
number of advanced features are not necessarily exposed in the default
profile. These profiles provide features such as status bars, clocks,
notifiers (reboot-required, updates-available), etc. The
profile-switcher allows users to quickly switch their .screenrc to any
of the available profiles.

%prep
%setup -q -n %{name}_%{version}.orig

%build
make -f debian/rules install-po
make -f debian/rules build
rm -f profiles/{generate,profile.skel}

%install
%__rm -rf %{buildroot}

install -m 755 -d %{buildroot}/usr/lib/byobu/
install -m 755 -d %{buildroot}%{_datadir}/locale/
install -m 755 -d %{buildroot}%{_datadir}/byobu/{profiles,keybindings,windows}
install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_mandir}/man1/

install -m 755 bin/* %{buildroot}/usr/lib/byobu/
for d in `find po/locale/ -maxdepth 1 -mindepth 1`; do 
    install -D -m 755 $d/LC_MESSAGES/byobu.mo %{buildroot}%{_datadir}/locale/`basename $d`/LC_MESSAGES/byobu.mo ;
done

install -m 644 profiles/* %{buildroot}%{_datadir}/byobu/profiles/
install -m 644 keybindings/* %{buildroot}%{_datadir}/byobu/keybindings/
install -m 644 windows/* %{buildroot}%{_datadir}/byobu/windows/

install -m 755 byobu %{buildroot}%{_bindir}/
install -m 755 byobu-config %{buildroot}%{_bindir}/
install -m 755 byobu-export %{buildroot}%{_bindir}/
install -m 755 byobu-status %{buildroot}%{_bindir}/
install -m 755 byobu-status-detail %{buildroot}%{_bindir}/
install -m 755 byobu-janitor %{buildroot}%{_bindir}/
install -m 755 byobu-select-profile %{buildroot}%{_bindir}/
install -m 755 byobu-launcher-install %{buildroot}%{_datadir}/byobu/
install -m 755 byobu-launcher-uninstall %{buildroot}%{_datadir}/byobu/
install -m 755 motd+shell %{buildroot}%{_bindir}/
install -m 755 byobu-launcher %{buildroot}%{_bindir}/

install -m 644 *.1 %{buildroot}%{_mandir}/man1/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING doc/help.txt
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/locale/*
/usr/lib/%{name}/*
%{_mandir}/man1/*

