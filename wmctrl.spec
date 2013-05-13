%define	name	wmctrl
%define	version	1.07
%define release 	6

Name:		%name
Version:	%version 
Release:	%release
License:	GPLv2+
Group:		System/X11
Url:		http://sweb.cz/tripie/utils/wmctrl/
Source:		%name-%version.tar.bz2
Patch0:         http://ftp.de.debian.org/debian/pool/main/w/wmctrl/wmctrl_1.07-6.diff.gz
Patch1:         wmctrl-sticky-workspace.patch
Summary:	Command line tool to interact with an EWMH/NetWM compatible X Window Manager
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)

%description
Wmctrl provides command line access to almost all the features defined
in the EWMH specification. Using it, it's possible to, for example,
obtain information about the window manager, get a detailed list of
desktops and managed windows, switch and resize desktops, change number
of desktops, make windows full-screen, always-above or sticky, and
activate, close, move, resize, maximize and minimize them.

The command line access makes it easy to automate these tasks and
execute them from any application that is able to run a command in
response to some event.

Please note that wmctrl only works with window managers which implement
this specification.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%_bindir/*
%_mandir/man1/wmctrl.1.*


%changelog
* Mon Jun  4 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1.0.7-5
- apply fedora patches

* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.07-4mdv2011.0
+ Revision: 634785
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.07-3mdv2010.0
+ Revision: 434778
- rebuild

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 1.07-2mdv2009.0
+ Revision: 269708
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 04 2008 Pascal Terjan <pterjan@mandriva.org> 1.07-1mdv2009.0
+ Revision: 214993
- import wmctrl


