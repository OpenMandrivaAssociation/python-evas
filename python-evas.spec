#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/BINDINGS/python/python-evas python-evas; \
#cd python-evas; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf python-evas-$PKG_VERSION.tar.xz python-evas/ --exclude .svn --exclude .*ignore

%define svnrev  72422

Summary:	Evas bindings for Python 
Name:		python-evas
Version:	0.7.3
Release:	0.%{svnrev}.1
Group:		Graphical desktop/Enlightenment
License:	GPLv2
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.%{svnrev}.tar.xz

BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-cython
%py_requires -d

%description
Python support files for Evas

%package devel
Summary:	Development files for %{name}
Group:		Development/Python

%description devel
Development files for the Python wrapper for the Evas libraries.

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc README
%{py_platsitedir}/evas/*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/python*/evas/*
%{_datadir}/%{name}/*

