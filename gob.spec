Summary:	GOB, The GTK+ Object Builder
Name:		gob
Version:	0.92.3
Release:	1
License:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
Url:		http://www.5z.com/jirka/linux.html#gob
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GOB is a simple preprocessor for making GTK+ objects.  It makes objects
from a single file which has inline C code so that you don't have to edit
the generated files.  Syntax is somewhat inspired by java and yacc.

%prep
%setup -q
%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README AUTHORS COPYING NEWS TODO ChangeLog \
    $RPM_BUILD_ROOT%{_mandir}/*/* examples/*

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(644,root,root,755)
%doc {README,AUTHORS,COPYING,NEWS,TODO,ChangeLog}.gz
%doc examples
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.gz
%{_datadir}/aclocal/*
