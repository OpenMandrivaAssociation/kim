%define name	kim
%define version	0.9.0
%define release	%mkrel 2


Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Image menu for kde
License:	GPL
Group:		Graphical desktop/KDE
Source:		%{name}-%{version}.tar.bz2
URL:		http://bouveyron.free.fr/kim/
Requires:	kdebase ImageMagick 
BuildArch:	noarch
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

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{name}

%build

%install 
mkdir -p %buildroot/%_datadir/apps/konqueror/servicemenus/
mkdir -p %buildroot/%_bindir

chmod 644 src/kim*.desktop src/plugins/kim*.desktop
chmod 755 src/bin/kim*
cp src/kim*.desktop %buildroot/%_datadir/apps/konqueror/servicemenus/
cp src/plugins/kim*.desktop %buildroot/%_datadir/apps/konqueror/servicemenus/
cp src/bin/kim* %buildroot/%_bindir

mkdir -p %buildroot/%_datadir/apps/kim
cp COPYING %buildroot/%_datadir/apps/kim/kim_about.txt
mkdir -p %buildroot/%_datadir/apps/kim/slideshow/
cp src/slideshow/* %buildroot/%_datadir/apps/kim/slideshow/
mkdir -p %buildroot/%_datadir/apps/kim/galery
cp src/galery/* %buildroot/%_datadir/apps/kim/galery

perl -pi -e "s/\r\n/\n/"  work.css

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc manual.html work.css
%_datadir/apps/kim
%{_datadir}/apps/konqueror/servicemenus/*
%attr(0755,root,root) %{_bindir}/*

