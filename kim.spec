%define name	kim
%define oname	kim4
%define version	0.9.5
%define release	8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Image menu for kde
License:	GPL
Group:		Graphical desktop/KDE
Source0:	%{oname}-%{version}.tar.gz
Patch0:		kim4-0.9.5-fix-icons-compressandresize-desktop-file.patch
Patch1:		kim4-0.9.5-fix-icons-converandrotate-desktop-file.patch
Patch2:		kim4-0.9.5-fix-icons-pulication-desktop-file.patch
URL:		http://bouveyron.free.fr/kim/
Requires:	kdebase4-runtime
Requires:       imagemagick 
BuildArch:	noarch
BuildRequires:	kde4-macros
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This is an image Kde servicemenu which allows to:
- compress images,
- resize images,
- convert images,
- rotate images,
- rename images,
- resize and send by mail images,
- and more other actions !
This servicemenu use ImageMagick.

%files
%defattr(-,root,root)
%{_kde_datadir}/apps/kim
%{_kde_datadir}/kde4/services/*
%attr(0755,root,root) %{_kde_bindir}/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%build

%install 
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_kde_datadir}/kde4/services/
mkdir -p %{buildroot}/%{_kde_bindir}

chmod 644 src/kim*.desktop
chmod 755 src/bin/kim*
cp src/kim*.desktop %{buildroot}%{_kde_datadir}/kde4/services/
cp src/bin/kim* %{buildroot}/%{_kde_bindir}

mkdir -p %{buildroot}/%{_kde_datadir}/apps/kim
cp COPYING %{buildroot}/%{_kde_datadir}/apps/kim/kim_about.txt
mkdir -p %{buildroot}/%{_kde_datadir}/apps/kim/slideshow/
cp src/slideshow/* %{buildroot}/%{_kde_datadir}/apps/kim/slideshow/
mkdir -p %{buildroot}/%{_kde_datadir}/apps/kim/gallery
cp src/gallery/* %{buildroot}/%{_kde_datadir}/apps/kim/gallery

perl -pi -e "s/\r\n/\n/"  work.css

%clean
rm -rf %{buildroot}


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.5-7mdv2011.0
+ Revision: 612608
- the mass rebuild of 2010.1 packages

* Tue Jan 12 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.5-6mdv2010.1
+ Revision: 490295
- add patches to fix service menu icons (bug #56302)
- clean spec file

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.5-5mdv2010.0
+ Revision: 388910
- Fix copy/paste error
- Make actions available on dolphin and konqueror

* Sat Mar 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.5-4mdv2009.1
+ Revision: 350794
- Update to kde4 version

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Sep 07 2008 Funda Wang <fwang@mandriva.org> 0.9.5-4mdv2009.0
+ Revision: 282254
- switch to /opt

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.9.5-3mdv2009.0
+ Revision: 247763
- rebuild

* Sat Mar 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.5-1mdv2008.1
+ Revision: 177041
- New version 0.9.5

* Sat Mar 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.4-2mdv2008.1
+ Revision: 177040
- Fix Requires

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.4-1mdv2008.0
+ Revision: 54478
- New version 0.9.4


* Sun Jul 02 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.9.0-2mdv2007.0
- Rebuild for new extension

* Sat Apr 15 2006 Couriousous <couriousous@mandriva.org> 0.9.0-1mdk
- 0.9.0

* Sat Oct 01 2005 Couriousous <couriousous@mandriva.org> 0.8.1-1mdk
- 0.8.1

* Mon May 30 2005 Sebastien Savarin <plouf@mandriva.org> 0.8-1mdk
- New release 0.8
- Use %%{1}mdv2007.0

* Sat Feb 05 2005 Couriousous <couriousous@mandrake.org> 0.7-2mdk
- Fix requires

* Sat Feb 05 2005 Couriousous <couriousous@mandrake.org> 0.7-1mdk
- From: Sebastien Savarin <plouf@zarb.org> :
	- first release

