%define major	2
%define libname	%mklibname %{name} %major

Summary:	X On Screen Display
Name:		xosd
Version:	2.2.14
Release:	14
Source0:	http://www.ignavus.net/%{name}-%{version}.tar.bz2
Source1:	http://ldots.org/xosd-guide/xosd-doc-0.01.tar.bz2
Patch0:		xosd-2.2.14-fix-underquoted-calls.patch
Patch1:		xosd-drop-gtk+.patch
License:	GPL
Group:		System/Libraries
#BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xinerama)
URL:		http://www.ignavus.net/software.html

%description
This package contains an xmms plugin to display various things whenever they 
change (volume, track, paused/shuffle/repeat,...) in a TV set's on screen 
display fashion.

%package	tools
Group:		Graphics
Summary:	Example applications of the xosd library
Provides:	osd_cat
Obsoletes:	osd_cat

%description	tools
This package contains sample applications for the xosd library that
can be used to display information in a TV set's on screen display
fashion.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for displaying information in an OSD

%description -n	%{libname}
This package contains the shared library of xosd, it is requires by programs 
that display it's output in a TV set's on screen display fashion.

%package -n	%{libname}-devel
Group:		Development/C
Summary:	Header files for developing programs using libxosd
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
This package contains the header files you need to develop programs based on 
libxosd that display it's output in a TV set's on screen display fashion.

%prep
%setup -q -a 1
%autopatch -p1

%build
%configure2_5x
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*/General/*.la

%files tools
%defattr(-,root,root)
%doc COPYING
%{_bindir}/osd_cat
%{_mandir}/man1/osd_cat.1*
%{_datadir}/%{name}/*png

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libxosd.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING ChangeLog README AUTHORS xosd-doc-0.01/html
%{_bindir}/xosd-config
%{_mandir}/man1/xosd-config.1*
%{_libdir}/libxosd.so
%{_includedir}/*.h
%{_datadir}/aclocal/libxosd.m4
%{_mandir}/man3/*

%changelog
* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 2.2.14-12mdv2010.0
+ Revision: 446260
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 2.2.14-11mdv2009.0
+ Revision: 262655
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.2.14-10mdv2009.0
+ Revision: 257643
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Thierry Vignaud <tv@mandriva.org> 2.2.14-8mdv2008.1
+ Revision: 140757
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.2.14-7mdv2008.1
+ Revision: 136618
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jan 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.14-7mdv2007.0
+ Revision: 113198
- unpack patch

* Tue Oct 10 2006 Götz Waschk <waschk@mandriva.org> 2.2.14-6mdv2007.1
- disable audacious

* Fri Jul 14 2006 Götz Waschk <waschk@mandriva.org> 2.2.14-5mdv2007.0
- patch for audacious

* Tue Jan 31 2006 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 2.2.14-4mdk
- fix underquoted calls (P0)
- utf-8!

* Fri Dec 02 2005 Götz Waschk <waschk@mandriva.org> 2.2.14-3mdk
- replace bmp by audacious

* Sun Apr 17 2005 Giuseppe GhibÃ² <ghibo@mandriva.com> 2.2.14-2mdk
- %%multiarch.

* Thu Nov 18 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.2.14-1mdk
- drop merged patches
- new version

* Wed Nov 10 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.2.13-2mdk
- add debian patches

* Tue Nov 09 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.2.13-1mdk
- add beep-media-player plugin
- new version

* Wed Sep 15 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.2.12-1mdk
- new version

* Sat Sep 04 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.2.11-1mdk
- new version

* Sat Aug 28 2004 Erwan Velu <erwan@mandrakesoft.com> 2.2.10-1mdk
- 2.2.10
- Removing Patch0 (merged upstream)

* Fri Aug 27 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.2.9-2mdk
- apply line width patch from debian

* Tue Aug 24 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.2.9-1mdk
- fix permissions
- new version

* Tue Jul 06 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.2.8-1mdk
- reenable libtoolize
- new version

* Thu Feb 12 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.2.7-4mdk
- move the xmms plugin to the xmms-xosd package
- move the xosd-config man page to the devel package
- move osd_cat to the tools package

* Thu Feb 12 2004 Michael Scherer <misc@mandrake.org> 2.2.7-3mdk
- split package, and rename it.

