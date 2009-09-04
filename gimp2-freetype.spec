%define version 0.6
%define release %mkrel 5
%define req_gimp_version 2.0.0

%define pkgname gimp-freetype

Summary:	A GIMP font renderer based on the freetype library
Name:		gimp2-freetype
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphics
URL:		http://freetype.gimp.org/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		%{pkgname}-%{version}.tar.bz2

BuildRequires:	gimp2-devel >= %{req_gimp_version}
BuildRequires:	freetype2-devel
#gw for the broken intltool scripts:
BuildRequires: perl-XML-Parser
Provides:	gimp1_3-freetype = %version
Obsoletes:	gimp1_3-freetype
Requires:	gimp2_0 >= %{req_gimp_version}

%description
The goal of gimp-freetype project is to get superb font support into
The GIMP. As a first step, a plug-in for GIMP based on the freetype2
library is developed. Later it might become a tool or a pluggable
module.

%prep
%setup -q -n %pkgname-%version

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%define gettext_package gimp20-freetype
%{find_lang} %{gettext_package}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{gettext_package}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/gimp/*/plug-ins/*
%{_datadir}/gimp-freetype

