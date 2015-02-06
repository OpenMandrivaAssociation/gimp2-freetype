%define req_gimp_version 2.0.0

%define pkgname gimp-freetype

Summary:	A GIMP font renderer based on the freetype library
Name:		gimp2-freetype
Version:	0.6
Release:	8
License:	GPL
Group:		Graphics
URL:		http://freetype.gimp.org/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		%{pkgname}-%{version}.tar.bz2

BuildRequires:	gimp-devel >= %{req_gimp_version}
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
export LDFLAGS="-lm"
%configure2_5x
%make

%install
%makeinstall_std

%define gettext_package gimp20-freetype
%{find_lang} %{gettext_package}

%files -f %{gettext_package}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/gimp/*/plug-ins/*
%{_datadir}/gimp-freetype



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-6mdv2011.0
+ Revision: 618946
- the mass rebuild of 2010.0 packages

* Mon Sep 07 2009 Thierry Vignaud <tv@mandriva.org> 0.6-5mdv2010.0
+ Revision: 432306
- BR s/gimp2-devel/gimp-devel/
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6-4mdv2009.0
+ Revision: 246153
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.6-2mdv2008.1
+ Revision: 125711
- kill re-definition of %%buildroot on Pixel's request
- import gimp2-freetype


* Mon Feb 13 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.6-2mdk
- fix build on x86_64

* Wed Jul 28 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6-1mdk
- new release

* Thu Mar 25 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5-3mdk
- new release

* Fri Feb  6 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-2mdk
- fix buildrequires

* Thu Feb  5 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-1mdk
- new version

* Fri Dec  5 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4-0.20031205.1mdk
- rename to gimp1.3-devel to make the Gimp developers happy
- new snapshot


* Tue Aug 19 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4-0.20030810.2mdk
- new gimp

* Sun Aug 10 2003 Abel Cheung <maddog@linux.org.hk> 0.4-0.20030810.1mdk
- First Mandrake spec
- CVS 2003-08-10
