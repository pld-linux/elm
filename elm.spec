Summary:	The elm mail user agent.
Name:		elm
Version:	2.5.0
Release:	0.3pre8
Copyright:	distributable
Group:		Applications/Mail
Url:		http://www.myxa.com/elm.html
Source0:	ftp://dsinc.myxa.com/pub/elm/elm2.5.0pre8.tar.gz
Source1:	elm.wmconfig
Patch0:		elm-2.5.0pre8-config.patch.gz
Patch1:		elm-2.5.0pre8-compat21.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Elm is a popular terminal mode email user agent. Elm includes all
standard mailhandling features, including MIME support via metamail.

Elm is still used by some people, but is no longer in development. If
you've used Elm before and you're devoted to it, you should install the
elm package.  If you would like to use metamail's MIME support, you'll
also need to install the metamail package.

%prep
%setup -q -n elm2.5.0pre8
%patch0 -p1
%patch1 -p1

%build
mkdir -p bin
make	# XXX This make to rerun Makefile.SH everywhere ...
make	# XXX ... and this make to buils.
strip bin/* || :

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/elm,%{_mandir}/man1}

make	DESTBIN=$RPM_BUILD_ROOT%{_bindir} \
	BIN=$RPM_BUILD_ROOT%{_bindir} \
	DESTLIB=$RPM_BUILD_ROOT%{_datadir}/elm \
	LIB=$RPM_BUILD_ROOT%{_datadir}/elm \
	MAN=$RPM_BUILD_ROOT%{_mandir}/man1 \
	install

( cd $RPM_BUILD_ROOT
  install -d ./etc/X11/wmconfig
  install -m 644 $RPM_SOURCE_DIR/elm.wmconfig ./etc/X11/wmconfig/elm
)

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(missingok) /etc/X11/wmconfig/elm
%attr(755,root,root) %{_bindir}/elm
%attr(755,root,root) %{_bindir}/answer
%attr(755,root,root) %{_bindir}/checkalias
%attr(755,root,root) %{_bindir}/elmalias
%attr(755,root,root) %{_bindir}/fastmail
%attr(755,root,root) %{_bindir}/frm
%attr(755,root,root) %{_bindir}/listalias
%attr(755,root,root) %{_bindir}/messages
%attr(755,root,root) %{_bindir}/newalias
%attr(755,root,root) %{_bindir}/newmail
%attr(755,root,root) %{_bindir}/printmail
%attr(755,root,root) %{_bindir}/readmsg
%attr(755,root,root) %{_bindir}/wnewmail
%attr(755,root,root) %{_bindir}/nfrm
%{_datadir}/elm
%{_mandir}/man1/answer.1.gz
%{_mandir}/man1/checkalias.1.gz
%{_mandir}/man1/elm.1.gz
%{_mandir}/man1/elmalias.1.gz
%{_mandir}/man1/fastmail.1.gz
%{_mandir}/man1/frm.1.gz
%{_mandir}/man1/listalias.1.gz
%{_mandir}/man1/messages.1.gz
%{_mandir}/man1/newalias.1.gz
%{_mandir}/man1/newmail.1.gz
%{_mandir}/man1/printmail.1.gz
%{_mandir}/man1/readmsg.1.gz
%{_mandir}/man1/wnewmail.1.gz
