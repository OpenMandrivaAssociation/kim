%define name	kim
%define oname	kim4
%define version	0.9.8
%define release	1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Image menu for kde
License:	GPL
Group:		Graphical desktop/KDE
Source0:	http://www.librepc.com/dl/kim/%{oname}-%{version}.tar.gz
URL:		http://bouveyron.free.fr/kim/

BuildRequires:	cmake(ECM)

Requires:	plasma-workspace
Requires:	imagemagick
Requires:	xwd
Requires:	xwininfo
Requires:	tesseract
Requires:	unpaper
Requires:	kdialog

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
%setup -q -n %{oname}-%{version}
%build

%install 
mkdir -p %{buildroot}%{_kf5_bindir}
mkdir -p %{buildroot}%{_kf5_services}
mkdir -p %{buildroot}%{_kf5_appsdir}/%{name}/slideshow
mkdir -p %{buildroot}%{_kf5_appsdir}/%{name}/gallery

install -m 644 src/kim*.desktop %{buildroot}%{_kf5_services}/
install -m 755 src/bin/kim* %{buildroot}%{_kf5_bindir}/

install -m 644 src/slideshow/* %{buildroot}%{_kf5_appsdir}/%{name}/slideshow/
install -m 644 src/gallery/* %{buildroot}%{_kf5_appsdir}/%{name}/gallery/

perl -pi -e "s/\r\n/\n/"  manual/work.css

# translations files for kim4
pushd language/locale
for locale in de fr;
do
	mkdir -p %{buildroot}%{_datadir}/locale/$locale/LC_MESSAGES
	install -m 644 $locale/%{oname}.mo \
	"%{buildroot}%{_datadir}/locale/$locale/LC_MESSAGES/"
done
popd

%find_lang %{oname}

%files -f %{oname}.lang
%doc AUTHORS ChangeLog README manual
%{_kf5_bindir}/kim*
%{_kf5_services}/kim*.desktop
%{_kf5_appsdir}/%{name}/


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

