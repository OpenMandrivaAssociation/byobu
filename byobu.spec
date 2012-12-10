%define name	byobu
%define version 5.16
%define release 1

Summary: 	Profiles for the GNU screen manager
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://launchpad.net/byobu/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
License: 	GPLv3+
Group:		Terminals
Url:		https://launchpad.net/byobu
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

%files 
%defattr(-,root,root)
%doc README COPYING 
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


%changelog
* Tue Mar 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 5.16-1
+ Revision: 784650
- version update 5.16

* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 5.15-1
+ Revision: 780981
- version update 5.15

* Wed Feb 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 5.10-1
+ Revision: 774375
- version update 5.10

* Sat Jan 21 2012 Alexander Khrukin <akhrukin@mandriva.org> 5.5-1
+ Revision: 764834
- version update 5.5

* Wed Jan 18 2012 Alexander Khrukin <akhrukin@mandriva.org> 5.4-1
+ Revision: 762094
- version update 5.4

* Thu Jan 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 5.2-1
+ Revision: 760337
- version update 5.2

* Tue Dec 27 2011 Alexander Khrukin <akhrukin@mandriva.org> 5.0-1
+ Revision: 745524
- version update 5.0

* Fri Dec 23 2011 Alexander Khrukin <akhrukin@mandriva.org> 4.55-1
+ Revision: 744821
- version update 4.55

* Sun Dec 11 2011 Alexander Khrukin <akhrukin@mandriva.org> 4.54-1
+ Revision: 740305
- version update 4.54

* Wed Oct 05 2011 Lev Givon <lev@mandriva.org> 4.37-1
+ Revision: 703185
- Update to 4.37.

* Mon Aug 08 2011 Lev Givon <lev@mandriva.org> 4.25-1
+ Revision: 693655
- Update to 4.25.

* Tue May 17 2011 Lev Givon <lev@mandriva.org> 4.1-1
+ Revision: 675927
- Update to 4.1.

* Tue Sep 07 2010 Lev Givon <lev@mandriva.org> 3.4-1mdv2011.0
+ Revision: 576668
- Update to 3.4.

* Mon Aug 16 2010 Lev Givon <lev@mandriva.org> 3.1-1mdv2011.0
+ Revision: 570548
- Update to 3.1.

* Sun Jul 11 2010 Lev Givon <lev@mandriva.org> 2.80-1mdv2011.0
+ Revision: 551166
- Update to 2.80.
- Update to 2.76.
- Update to 2.74.

* Thu Apr 01 2010 Lev Givon <lev@mandriva.org> 2.67-1mdv2010.1
+ Revision: 530557
- Update to 2.67.

* Mon Mar 15 2010 Lev Givon <lev@mandriva.org> 2.64-1mdv2010.1
+ Revision: 519113
- Update to 2.64.

* Tue Dec 15 2009 Lev Givon <lev@mandriva.org> 2.40-1mdv2010.1
+ Revision: 478768
- Update to 2.40.

* Wed Oct 14 2009 Frederic Crozat <fcrozat@mandriva.com> 2.38-2mdv2010.0
+ Revision: 457257
- use find_lang macro
- fix missing common keybinding files
- clean up specfile

* Tue Oct 13 2009 Frederic Crozat <fcrozat@mandriva.com> 2.38-1mdv2010.0
+ Revision: 457112
- Release 2.38

  + Lev Givon <lev@mandriva.org>
    - Update to 2.37.

* Mon Aug 31 2009 Lev Givon <lev@mandriva.org> 2.29-1mdv2010.0
+ Revision: 423027
- Update to 2.29.

* Thu Aug 13 2009 Lev Givon <lev@mandriva.org> 2.25-1mdv2010.0
+ Revision: 416056
- Update to 2.25.

* Thu Jul 23 2009 Lev Givon <lev@mandriva.org> 2.23-1mdv2010.0
+ Revision: 399051
- Update to 2.23.

* Mon Jul 13 2009 Lev Givon <lev@mandriva.org> 2.20-1mdv2010.0
+ Revision: 395521
- Update to 2.20.

* Tue Jun 23 2009 Lev Givon <lev@mandriva.org> 2.15-1mdv2010.0
+ Revision: 388678
- Update to 2.15.

* Wed Jun 03 2009 Lev Givon <lev@mandriva.org> 2.8-1mdv2010.0
+ Revision: 382533
- imported package byobu

