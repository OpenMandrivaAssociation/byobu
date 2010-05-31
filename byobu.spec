%define name	byobu
%define version 2.76
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
%setup -q

%install
%__rm -rf %{buildroot}

mkdir -p %{buildroot}
cp -ar etc %{buildroot}
cp -ar usr %{buildroot}
rm -rf %{buildroot}/usr/share/doc

for po in po/*.po
do
    lang=${po#po/}
    lang=${lang%.po}
    mkdir -p ${RPM_BUILD_ROOT}/usr/share/locale/${lang}/LC_MESSAGES/
    msgfmt ${po} -o ${RPM_BUILD_ROOT}/usr/share/locale/${lang}/LC_MESSAGES/%{name}.mo
done

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README COPYING 
%doc usr/share/doc/%{name}/help.txt
%dir %{_datadir}/%{name}
%dir %{_prefix}/lib/%{name}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*
%{_bindir}/%{name}*
%{_bindir}/motd+shell
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_mandir}/man1/%{name}*.1.*
%{_mandir}/man1/motd+shell.1.*
%{_prefix}/lib/%{name}/*
