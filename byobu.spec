%define name	byobu
%define version 2.40
%define release %mkrel 1

Summary: 	Profiles for the GNU screen manager
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://launchpad.net/byobu/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
License: 	GPLv3+
Group:		Terminals
Url:		https://launchpad.net/byobu
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

%install
%__rm -rf %{buildroot}

make -f debian/rules install-po

%__install -m 755 -d %{buildroot}/usr/lib/byobu/
%__install -m 755 -d %{buildroot}%{_sysconfdir}/byobu/
%__install -m 755 -d %{buildroot}%{_datadir}/applications/
%__install -m 755 -d %{buildroot}%{_datadir}/locale/
%__install -m 755 -d %{buildroot}%{_datadir}/byobu/{profiles,keybindings,windows}
%__install -m 755 -d %{buildroot}%{_bindir}/
%__install -m 755 -d %{buildroot}%{_mandir}/man1/

%__install -m 755 bin/* %{buildroot}/usr/lib/byobu/
for d in `find po/locale/ -maxdepth 1 -mindepth 1`; do 
    %__install -D -m 755 $d/LC_MESSAGES/byobu.mo %{buildroot}%{_datadir}/locale/`basename $d`/LC_MESSAGES/byobu.mo ;
done

%__install -m 644 profiles/* %{buildroot}%{_datadir}/byobu/profiles/
%__install -m 644 keybindings/* %{buildroot}%{_datadir}/byobu/keybindings/
%__install -m 644 windows/* %{buildroot}%{_datadir}/byobu/windows/
ln -sf f-keys ${RPM_BUILD_ROOT}/usr/share/byobu/keybindings/common

%__install -m 644 desktop/byobu.desktop %{buildroot}%{_datadir}/applications/
%__install -m 644 desktop/byobu.svg %{buildroot}%{_datadir}/byobu/

%__install -m 644 statusrc %{buildroot}%{_sysconfdir}/byobu/

%__install -m 755 byobu %{buildroot}%{_bindir}/
%__install -m 755 byobu-config %{buildroot}%{_bindir}/
%__install -m 755 byobu-export %{buildroot}%{_bindir}/
%__install -m 755 byobu-status %{buildroot}%{_bindir}/
%__install -m 755 byobu-status-detail %{buildroot}%{_bindir}/
%__install -m 755 byobu-janitor %{buildroot}%{_bindir}/
%__install -m 755 byobu-select-profile %{buildroot}%{_bindir}/
%__install -m 755 byobu-launcher-install %{buildroot}%{_datadir}/byobu/
%__install -m 755 byobu-launcher-uninstall %{buildroot}%{_datadir}/byobu/
%__install -m 755 byobu-reconnect-sockets %{buildroot}%{_datadir}/byobu/
%__install -m 755 motd+shell %{buildroot}%{_bindir}/
%__install -m 755 byobu-launcher %{buildroot}%{_bindir}/

%__install -m 644 *.1 %{buildroot}%{_mandir}/man1/

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING doc/help.txt
%{_bindir}/*
%{_sysconfdir}/byobu/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
/usr/lib/%{name}
%{_mandir}/man1/*

