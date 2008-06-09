%define	name	xosd
%define	version	2.2.14
%define release	%mkrel 8
%define major	2
%define libname	%mklibname %{name} %major

Summary:	X On Screen Display, displays XMMS status information
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.ignavus.net/%{name}-%{version}.tar.bz2
Source1:	http://ldots.org/xosd-guide/xosd-doc-0.01.tar.bz2
Patch0:		xosd-2.2.14-fix-underquoted-calls.patch
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	xmms-devel
Buildrequires:	gdk-pixbuf-devel
%if %mdkversion >= 1020
BuildRequires:	multiarch-utils >= 1.0.3
%endif
URL:		http://www.ignavus.net/software.html

%description
This package contains an xmms plugin to display various things whenever they 
change (volume, track, paused/shuffle/repeat,...) in a TV set's on screen 
display fashion.

%package -n	xmms-xosd
Group:		Sound
Summary:	X On Screen Display, displays XMMS status information
Requires:	xmms
Provides:	xosd
Obsoletes:	xosd

%description -n	xmms-xosd
This package contains an xmms plugin to display various things whenever they 
change (volume, track, paused/shuffle/repeat,...) in a TV set's on screen 
display fashion.

%if 0
%package -n	audacious-xosd
Group:		Sound
Summary:	X On Screen Display, displays Audacious status information
Requires:	audacious
Buildrequires:	libaudacious-devel
Provides:	beep-media-player-xosd
Obsoletes:	beep-media-player-xosd

%description -n	audacious-xosd
This package contains an Audacious plugin to display various things
whenever they change (volume, track, paused/shuffle/repeat,...)  in a
TV set's on screen display fashion.
%endif

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
%patch0 -p1 -b .underquoted

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*/General/*.la
%if %mdkversion >= 1020
%multiarch_binaries %{buildroot}%{_bindir}/xosd-config
%endif

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n xmms-xosd
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xmms/General/libxmms_osd.so*
%{_datadir}/xosd/

%if 0
%files -n audacious-xosd
%defattr(-,root,root)
%doc COPYING
%{_libdir}/audacious/General/libbmp_osd.so*
%{_datadir}/xosd/
%endif

%files tools
%defattr(-,root,root)
%doc COPYING
%{_bindir}/osd_cat
%{_mandir}/man1/osd_cat.1*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libxosd.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING ChangeLog README AUTHORS xosd-doc-0.01/html
%if %mdkversion >= 1020
%multiarch %{multiarch_bindir}/xosd-config
%endif
%{_bindir}/xosd-config
%{_mandir}/man1/xosd-config.1*
%{_libdir}/libxosd.so
%{_libdir}/libxosd.la
%{_includedir}/*.h
%{_datadir}/aclocal/libxosd.m4
%{_mandir}/man3/*


