Summary:	The elm mail user agent
Summary(pl):	Program pocztowy elm
Name:		elm
Version:	2.5.1
Release:	4
Copyright:	distributable
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source0:	ftp://ftp.virginia.edu/pub/elm/%{name}%{version}.tar.gz
Source1:	elm.desktop
Patch0:		elm-config.patch.gz
Patch1:		elm-temp-mbox.patch
URL:		http://www.myxa.com/elm.html
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	glibc-static
Requires:	metamail
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_applnkdir	/usr/X11R6/share/applnk

%description
Elm is a popular terminal mode email user agent. Elm includes all
standard mailhandling features, including MIME support via metamail.

Elm is still used by some people, but is no longer in development. If
you've used Elm before and you're devoted to it, you should install the
elm package.  If you would like to use metamail's MIME support, you'll
also need to install the metamail package.

%description -l pl
Elm jest popularnym programem pocztowym dla terminali tekstowych. Obs³uguje
wszystkie standardy pocztowe z MIME w³±cznie (¿eby z niego skorzystaæ musisz
zainstalowaæ tak¿e pakiet metamail).

Elm jest wci±¿ powszechnnie u¿ywany, ale nie jest ju¿ rozwijany.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1

%build
mkdir -p bin
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/elm,%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/Networking/Mail

make	DESTBIN=$RPM_BUILD_ROOT%{_bindir} \
	BIN=$RPM_BUILD_ROOT%{_bindir} \
	DESTLIB=$RPM_BUILD_ROOT%{_datadir}/elm \
	LIB=$RPM_BUILD_ROOT%{_datadir}/elm \
	MAN=$RPM_BUILD_ROOT%{_mandir}/man1 \
	install

echo .so frm.1 > $RPM_BUILD_ROOT%{_mandir}/man1/nfrm.1

ln -sf newmail	$RPM_BUILD_ROOT%{_bindir}/wnewmail 
ln -sf frm 	$RPM_BUILD_ROOT%{_bindir}/nfrm

# mmencode is provided by metamail package
rm -f $RPM_BUILD_ROOT%{_bindir}/mmencode
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/mmencode.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Networking/Mail

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	Changes Overview README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,Overview,README,BUGS}.gz

%attr(755,root,root) %{_bindir}/*
%{_datadir}/elm
%{_mandir}/man1/*

%{_applnkdir}/Networking/Mail/elm.desktop
