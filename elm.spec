Summary:	The elm mail user agent
Summary(de.UTF-8):	ELM-Mail-User-Agent
Summary(es.UTF-8):	Agente de mail ELM
Summary(fr.UTF-8):	Agent courrier ELM
Summary(pl.UTF-8):	Program pocztowy elm
Summary(pt_BR.UTF-8):	Agente de mail ELM
Summary(ru.UTF-8):	Почтовая программа elm
Summary(tr.UTF-8):	e-posta okuma yazılımı
Summary(uk.UTF-8):	поштова програма elm
Name:		elm
Version:	2.5.7
Release:	4
License:	distributable
Group:		Applications/Mail
Source0:	ftp://ftp.virginia.edu/pub/elm/%{name}%{version}.tar.gz
# Source0-md5:	47bb6d6af6dceda4108076507baa99ba
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	b8891e4d62117163025e594e6608f747
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-config.patch.gz
Patch1:		%{name}-y2k.patch
Patch2:		%{name}-security.patch
Patch3:		%{name}-no-static-libcrypt.patch
Patch4:		%{name}-makefile-fix.patch
Patch5:		%{name}-tempnam.patch
URL:		http://www.instinct.org/elm/
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

%description -l de.UTF-8
ELM ist eines der beliebtesten Terminalmodus-Mailhandling-Programme.
Es ist ausgesprochen leistungsfähig, leicht zu bedienen und gut
unterstützt. Es stellt alle Mail-Handlingfunktionen bereit, die man
sich nur wünscht, einschließlich MIME-Support (über Metamail).

%description -l es.UTF-8
ELM es un popular lector de mail en modo terminal. Es potente, fácil
de usar y de conseguir ayuda. Posee todas las características que se
podría esperar, incluso soporte a MINE (vía metamail).

%description -l fr.UTF-8
ELM est l'un des programmes de gestion du courrier en mode texte les
plus populaires. Il est puissant, facile à utiliser et a apprendre. Il
a toutes les possibilités de gestion du courrier que vous attendez, y
compris la gestion MIME (via metamail).

%description -l pl.UTF-8
Elm jest popularnym programem pocztowym dla terminali tekstowych.
Obsługuje wszystkie standardy pocztowe z MIME włącznie (żeby z niego
skorzystać musisz zainstalować także pakiet metamail).

%description -l pt_BR.UTF-8
ELM é um popular leitor de mail em modo terminal. É poderoso, fácil de
usar e fácil de conseguir ajuda. Possui todas as características que
você poderia esperar, inclusive suporte a MINE (via metamail).

%description -l ru.UTF-8
Elm - это популярная терминальная почтовая программа. Elm включает все
стандартные возможности работы с почтой, включая поддержку MIME через
metamail.

Elm по-прежнему используется некоторыми его любителями, хотя развитие
его прекратилось.

%description -l tr.UTF-8
ELM, en yaygın kullanılan, metin ekran tabanlı e-posta yazılımlarından
biridir. Kullanıcıya mektuplarını okuyabilmesi için basit bir ortam
sağlar.

%description -l uk.UTF-8
Elm - це популярна термінальна поштова програма. Elm містить усі
стандартні можливості роботи з поштою, включаючи підтримку MIME через
metamail.

Elm все ще використовується деякими його шанувальниками, хоча розвиток
його припинено.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0
#%patch5 -p1

%build
mkdir -p bin
sh ./Makefile.SH
sh ./doc/Makefile.SH
%{__make} \
	OPTIMIZE="%{rpmcflags} -DI_STDARG" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/elm,%{_mandir}/{man1,pl/man1}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTBIN=$RPM_BUILD_ROOT%{_bindir} \
	BIN=$RPM_BUILD_ROOT%{_bindir} \
	DESTLIB=$RPM_BUILD_ROOT%{_datadir}/elm \
	LIB=$RPM_BUILD_ROOT%{_datadir}/elm \
	MAN=$RPM_BUILD_ROOT%{_mandir}/man1

echo .so frm.1 > $RPM_BUILD_ROOT%{_mandir}/man1/nfrm.1

ln -sf newmail	$RPM_BUILD_ROOT%{_bindir}/wnewmail
ln -sf frm 	$RPM_BUILD_ROOT%{_bindir}/nfrm

# mmencode is provided by metamail package
rm -f $RPM_BUILD_ROOT%{_bindir}/mmencode
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/mmencode.1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Overview README

%attr(755,root,root) %{_bindir}/*
%{_datadir}/elm
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(fi) %{_mandir}/fi/man1/*

%{_desktopdir}/elm.desktop
%{_pixmapsdir}/*
