%define major	2
%define libname	%mklibname %{name} %major

Summary:	X On Screen Display
Name:		xosd
Version:	2.2.14
Release:	14
Source0:	http://www.ignavus.net/%{name}-%{version}.tar.bz2
Source1:	http://ldots.org/xosd-guide/xosd-doc-0.01.tar.bz2
Patch0:		xosd-2.2.14-fix-underquoted-calls.patch
License:	GPL
Group:		System/Libraries
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
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
%patch0 -p1 -b .underquoted

%build
%configure2_5x
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*/General/*.la

%files tools
%doc COPYING
%{_bindir}/osd_cat
%{_mandir}/man1/osd_cat.1*
%{_datadir}/%{name}/*png

%files -n %{libname}
%doc COPYING
%{_libdir}/libxosd.so.*

%files -n %{libname}-devel
%doc COPYING ChangeLog README AUTHORS xosd-doc-0.01/html
%{_bindir}/xosd-config
%{_mandir}/man1/xosd-config.1*
%{_libdir}/libxosd.so
%{_includedir}/*.h
%{_datadir}/aclocal/libxosd.m4
%{_mandir}/man3/*

