Summary:	GOB, The GTK+ Object Builder
Summary(pl):	GOB, Budowniczy obiekt�w GTK+
Name:		gob
Version:	1.0.2
Release:	1
License:	GPL
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	http://ftp.5z.com/pub/gob/%{name}-%{version}.tar.gz
URL:		http://www.5z.com/jirka/gob.html
BuildRequires:	glib-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOB is a simple preprocessor for making GTK+ objects. It makes objects
from a single file which has inline C code so that you don't have to
edit the generated files. Syntax is somewhat inspired by java and
yacc.

%description -l pl
GOB jest prostym preprocesorem s�u��cym do tworzenia obiekt�w GTK+.
Tworzy on obiekty z pojedynczego pliku posiadaj�cego wbudowany kod C,
dlatego nie musi si� edytowa� wygenerowanych plik�w. Sk�adnia jest do
pewnego stopnia inspirowana Jav� i Yaccem.

%prep
%setup -q
%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4dir=%{_aclocaldir}

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}
gzip -9nf README AUTHORS NEWS TODO ChangeLog \
	$RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_aclocaldir}/*
%{_prefix}/src/examples/%{name}-%{version}
