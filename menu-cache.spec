%define major 3
%define libname %mklibname %{name}
%define devname %mklibname -d %{name}
%define oldlibname %mklibname %{name} 3

# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		83d90343ba7ed345f8c2f0e9d5b71e2fc88d1d6e
	%global commitdate	20240821
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	A library to speed up freedesktop.org application menus
Name:		menu-cache
Version:	1.1.0
#Source0:	https://github.com/lxde/menu-cache/archive/%{version}.tar.gz
Source0:	https://github.com/lxde/%{name}/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
Release:	7
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://github.com/lxde/menu-cache
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(libfm-extra)

%description
Libmenu-cache is a library creating and utilizing caches to speed up
freedesktop.org application menus.
It can be used as a replacement of libgnome-menu of gnome-menus.

Advantages:
1. Faster loading of menus.
2. Ease of use. (API is very similar to that of libgnome-menu)
3. Lightweight runtime library. (Parsing of the menu definition files
   are done by menu-cache-gen when the menus are really changed.)
4. Less unnecessary and complicated file monitoring.
5. Greatly reduced disk I/O.

%files
%{_libexecdir}/menu-cache*

#----------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		Graphical desktop/Other
Requires:	%{name} >= %{version}-%{release}
Obsoletes:	%oldlibname < %{EVRD}

%description -n %{libname}
This package contains shared library for %{name}.

%files -n %{libname}
%{_libdir}/libmenu-cache.so.%{major}*

#----------------------------------------------------------------------

%package -n %{devname}
Summary:	Contains development files for %{name}
Group:		Graphical desktop/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains development files for %{name}.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

