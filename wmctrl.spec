%define	name	wmctrl
%define	version	1.07
%define	release	%mkrel 5

Name:		%name
Version:	%version 
Release:	%release
License:	GPLv2+
Group:		System/X11
Url:		http://sweb.cz/tripie/utils/wmctrl/
Source:		%name-%version.tar.bz2
Summary:	Command line tool to interact with an EWMH/NetWM compatible X Window Manager
BuildRequires:	glib2-devel
BuildRequires:	libx11-devel
BuildRequires:	libxmu-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Patch0:		0001-Fix-desktop-id-parsing.patch

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
