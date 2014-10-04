%define _files_listed_twice_terminate_build 0
%define build_mrb 0

%define name	byobu
%define version 5.86
%define release 2
Summary: 	Profiles for the GNU screen manager
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPLv3+
Group:		Terminals
URL:		http://byobu.co/index.html
Source0: 	http://byobu.co/download/%{name}_%{version}.orig.tar.gz
BuildArch:	noarch
BuildRequires:	gettext
BuildRequires:	desktop-file-utils

# Do not drop TTY req. Sflo
%if %{build_mrb}
# lauched as byobu-screen
Requires:	screen >= 4.2.1
%else
Requires:	screen >= 4.0.3
%endif

Requires:	python >= 2.7
Requires:	newt
Requires:	gettext
#From X xterm-256color .Sflo
Requires:	ncurses-extraterms
# lauched as byobu, tmux also needed in X .Sflo
Requires:	tmux >= 1.9

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
# lang
for po in po/*.po
do
    lang=${po#po/}
    lang=${lang%.po}
    mkdir -p %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/
    msgfmt ${po} -o %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/%{name}.mo
done
# desktop
desktop-file-install usr/share/applications/%{name}.desktop --dir %{buildroot}%{_datadir}/applications
# icons in DE
mkdir -p %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/byobu/pixmaps/byobu.svg %{buildroot}%{_datadir}/pixmaps/byobu.svg

%find_lang %{name}


%files -f %{name}.lang
%doc README COPYING ChangeLog 
%doc /usr/share/doc/%{name}/help.screen.txt
%doc /usr/share/doc/%{name}/help.tmux.txt
%dir %{_datadir}/%{name}
%dir %{_prefix}/lib/%{name}
%{_bindir}/%{name}*
%{_bindir}/col1
%{_bindir}/wifi-status
%{_bindir}/ctail
%config(noreplace) %{_sysconfdir}/%{name}/backend
%config(noreplace) %{_sysconfdir}/%{name}/socketdir
%config(noreplace) %{_sysconfdir}/profile.d/Z97-%{name}.sh
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}*.1.*
%{_mandir}/man1/col1.1.xz
%{_mandir}/man1/ctail.1.xz
%{_mandir}/man1/wifi-status.1.xz
%{_prefix}/lib/%{name}/*
%{_datadir}/pixmaps/byobu.svg