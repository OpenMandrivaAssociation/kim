%define name	kim
%define oname    kim4
%define version	0.9.5
%define release	%mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Image menu for kde
License:	GPL
Group:		Graphical desktop/KDE
Source:		%{oname}-%{version}.tar.gz
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
%_kde_datadir/apps/kim
%buildroot/%_kde_datadir/kde4/services/*
%attr(0755,root,root) %{_kde_bindir}/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}

%build

%install 
rm -fr %buildroot
mkdir -p %buildroot/%_kde_datadir/kde4/services/
mkdir -p %buildroot/%_kde_bindir

chmod 644 src/kim*.desktop
chmod 755 src/bin/kim*
cp src/kim*.desktop %buildroot/%_kde_datadir/kde4/services/
cp src/bin/kim* %buildroot/%_kde_bindir

mkdir -p %buildroot/%_kde_datadir/apps/kim
cp COPYING %buildroot/%_kde_datadir/apps/kim/kim_about.txt
mkdir -p %buildroot/%_kde_datadir/apps/kim/slideshow/
cp src/slideshow/* %buildroot/%_kde_datadir/apps/kim/slideshow/
mkdir -p %buildroot/%_kde_datadir/apps/kim/gallery
cp src/gallery/* %buildroot/%_kde_datadir/apps/kim/gallery

perl -pi -e "s/\r\n/\n/"  work.css

%clean
rm -rf $RPM_BUILD_ROOT
