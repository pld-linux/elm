Summary:	The elm mail user agent
Summary(de):	ELM-Mail-User-Agent
Summary(es):	Agente de mail ELM
Summary(fr):	Agent courrier ELM
Summary(pl):	Program pocztowy elm
Summary(pt_BR):	Agente de mail ELM
Summary(tr):	e-posta okuma yazýlýmý
Name:		elm
Version:	2.5.6
Release:	1
License:	Distributable
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0:	ftp://ftp.virginia.edu/pub/elm/%{name}%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-config.patch.gz
Patch1:		%{name}-y2k.patch
Patch2:		%{name}-security.patch
Patch3:		%{name}-no-static-libcrypt.patch
Patch4:		%{name}-makefile-fix.patch
Patch5:		%{name}-tempnam.patch
URL:		http://www.myxa.com/elm.html
BuildRequires:	ncurses-devel >= 5.0
Requires:	metamail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elm is a popular terminal mode email user agent. Elm includes all
standard mailhandling features, including MIME support via metamail.

Elm is still used by some people, but is no longer in development. If
you've used Elm before and you're devoted to it, you should install
the elm package. If you would like to use metamail's MIME support,
you'll also need to install the metamail package.

%description -l de
ELM ist eines der beliebtesten Terminalmodus-Mailhandling-Programme.
Es ist ausgesprochen leistungsfähig, leicht zu bedienen und gut
unterstützt. Es stellt alle Mail-Handlingfunktionen bereit, die man
sich nur wünscht, einschließlich MIME-Support (über Metamail).

%description -l es
ELM es un popular lector de mail en modo terminal. Es potente, fácil
de usar y de conseguir ayuda. Posee todas las características que se
podría esperar, incluso soporte a MINE (vía metamail).

%description -l fr
ELM est l'un des programmes de gestion du courrier en mode texte les
plus populaires. Il est puissant, facile à utiliser et a apprendre. Il
a toutes les possibilités de gestion du courrier que vous attendez, y
compris la gestion MIME (via metamail).

%description -l pl
Elm jest popularnym programem pocztowym dla terminali tekstowych.
Obs³uguje wszystkie standardy pocztowe z MIME w³±cznie (¿eby z niego
skorzystaæ musisz zainstalowaæ tak¿e pakiet metamail).

%description -l pt_BR
ELM é um popular leitor de mail em modo terminal. É poderoso, fácil de
usar e fácil de conseguir ajuda. Possui todas as características que
você poderia esperar, inclusive suporte a MINE (via metamail).

%description -l tr
ELM, en yaygýn kullanýlan, metin ekran tabanlý e-posta yazýlýmlarýndan
biridir. Kullanýcýya mektuplarýný okuyabilmesi için basit bir ortam
saðlar.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0
%patch5 -p1

%build
mkdir -p bin
%{__make} OPTIMIZE="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/elm,%{_mandir}/{man1,pl/man1}} \
	$RPM_BUILD_ROOT%{_applnkdir}/Network/Mail

%{__make} DESTBIN=$RPM_BUILD_ROOT%{_bindir} \
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

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf Changes Overview README # BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,Overview,README}.gz

%attr(755,root,root) %{_bindir}/*
%{_datadir}/elm
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(fi) %{_mandir}/fi/man1/*

%{_applnkdir}/Network/Mail/elm.desktop
