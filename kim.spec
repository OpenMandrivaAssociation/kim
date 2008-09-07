%define name	kim
%define version	0.9.5
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Image menu for kde
License:	GPL
Group:		Graphical desktop/KDE
Source:		%{name}-%{version}.tar.gz
URL:		http://bouveyron.free.fr/kim/
Requires:	kdebase-progs 
Requires:       ImageMagick 
BuildArch:	noarch
BuildRequires:	kde3-macros
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
%_kde3_datadir/apps/kim
%{_kde3_datadir}/apps/konqueror/servicemenus/*
%attr(0755,root,root) %{_kde3_bindir}/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build

%install 
rm -fr %buildroot
mkdir -p %buildroot/%_kde3_datadir/apps/konqueror/servicemenus/
mkdir -p %buildroot/%_kde3_bindir

chmod 644 src/kim*.desktop
chmod 755 src/bin/kim*
cp src/kim*.desktop %buildroot/%_kde3_datadir/apps/konqueror/servicemenus/
cp src/bin/kim* %buildroot/%_kde3_bindir

mkdir -p %buildroot/%_kde3_datadir/apps/kim
cp COPYING %buildroot/%_kde3_datadir/apps/kim/kim_about.txt
mkdir -p %buildroot/%_kde3_datadir/apps/kim/slideshow/
cp src/slideshow/* %buildroot/%_kde3_datadir/apps/kim/slideshow/
mkdir -p %buildroot/%_kde3_datadir/apps/kim/galery
cp src/galery/* %buildroot/%_kde3_datadir/apps/kim/galery

perl -pi -e "s/\r\n/\n/"  work.css

%clean
rm -rf $RPM_BUILD_ROOT
