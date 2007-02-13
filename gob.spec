Summary:	GOB, The GTK+ Object Builder
Summary(pl.UTF-8):	GOB - budowniczy obiektów GTK+
Name:		gob
Version:	1.0.12
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.5z.com/pub/gob/%{name}-%{version}.tar.gz
# Source0-md5:	573706a03ff6696ee5b6ab3fbbd17d67
Patch0:		%{name}-am15.patch
Patch1:		%{name}-am18.patch
URL:		http://www.5z.com/jirka/gob.html
BuildRequires:	autoconf >= 2.2
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	glib-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOB is a simple preprocessor for making GTK+ objects. It makes objects
from a single file which has inline C code so that you don't have to
edit the generated files. Syntax is somewhat inspired by Java and
yacc.

%description -l pl.UTF-8
GOB jest prostym preprocesorem służącym do tworzenia obiektów GTK+.
Tworzy on obiekty z pojedynczego pliku zawierającego wbudowany kod C,
dzięki czemu nie trzeba modyfikować wygenerowanych plików. Składnia
jest do pewnego stopnia inspirowana Javą i yaccem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4dir=%{_aclocaldir}

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_aclocaldir}/*
%{_examplesdir}/%{name}-%{version}
