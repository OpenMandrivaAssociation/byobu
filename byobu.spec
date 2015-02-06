%define name	byobu
%define version 5.43
%define release 2
Summary: 	Profiles for the GNU screen manager
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://launchpad.net/byobu/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
License: 	GPLv3+
Group:		Terminals
URL:		https://launchpad.net/byobu
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
%setup -q

%build
%configure2_5x

%install
%makeinstall_std
chmod -x %{buildroot}%{_datadir}/applications/%{name}.desktop



%post
ln -s /usr/share/byobu/pixmaps/byobu.svg /usr/share/pixmaps/byobu.svg

%postun
rm -rf /usr/share/pixmaps/byobu.svg

%files 
%defattr(-,root,root)
%doc README COPYING ChangeLog
%doc usr/share/doc/%{name}/help.screen.txt
%doc usr/share/doc/%{name}/help.tmux.txt
%dir %{_datadir}/%{name}
%dir %{_prefix}/lib/%{name}
%{_bindir}/%{name}*
%{_sysconfdir}/%{name}/
%{_sysconfdir}/profile.d/Z97-%{name}.sh
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}*.1.*
%{_prefix}/lib/%{name}/*

