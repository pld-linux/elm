Summary:	The elm mail user agent
Summary(de):	ELM-Mail-User-Agent
Summary(fr):	Agent courrier ELM
Summary(pl):	Program pocztowy elm
Summary(tr):	e-posta okuma yazýlýmý
Name:		elm
Version:	2.5.3
Release:	2
Copyright:	distributable
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source0:	ftp://ftp.virginia.edu/pub/elm/%{name}%{version}.tar.gz
Source1:	elm.desktop
Patch0:		elm-config.patch.gz
Patch1:		elm-temp-mbox.patch
Patch2:		elm-y2k.patch
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

%description -l de
ELM ist eines der beliebtesten Terminalmodus-Mailhandling-Programme.  Es ist
ausgesprochen leistungsfähig, leicht zu bedienen und gut unterstützt.  Es
stellt alle Mail-Handlingfunktionen bereit, die man sich nur wünscht,
einschließlich MIME-Support (über Metamail).

%description -l fr
ELM est l'un des programmes de gestion du courrier en mode texte les plus
populaires. Il est puissant, facile à utiliser et a apprendre. Il a toutes
les possibilités de gestion du courrier que vous attendez, y compris la
gestion MIME (via metamail).

%description -l pl
Elm jest popularnym programem pocztowym dla terminali tekstowych. Obs³uguje
wszystkie standardy pocztowe z MIME w³±cznie (¿eby z niego skorzystaæ musisz
zainstalowaæ tak¿e pakiet metamail).

%description -l tr
ELM, en yaygýn kullanýlan, metin ekran tabanlý e-posta yazýlýmlarýndan
biridir. Kullanýcýya mektuplarýný okuyabilmesi için basit bir ortam saðlar.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
