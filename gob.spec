Summary:	GOB, The GTK+ Object Builder
Name:		gob
Version:	0.92.3
Release:	1
License:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source0:	http://ftp.5z.com/pub/gob/%{name}-%{version}.tar.gz
Url:		http://www.5z.com/jirka/gob.html
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GOB is a simple preprocessor for making GTK+ objects. It makes objects
from a single file which has inline C code so that you don't have to edit
the generated files.  Syntax is somewhat inspired by java and yacc.

%prep
%setup -q
%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{varsion}

make DESTDIR=$RPM_BUILD_ROOT install

install examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{varsion}
gzip -9nf README AUTHORS NEWS TODO ChangeLog \
	$RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*
/usr/src/examples/%{name}-%{varsion}
