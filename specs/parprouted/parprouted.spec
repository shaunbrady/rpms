# $Id$
# Authority: dag
# Upstream: Vladimir Ivaschenko <vi$maks,net>

Summary: Proxy ARP IP bridging daemon
Name: parprouted
Version: 0.63
Release: 1.2
License: GPL
Group: Applications/Internet
URL: http://www.hazard.maks.net/

Source: http://www.hazard.maks.net/parprouted/parprouted-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
parprouted is a daemon for transparent IP (Layer 3) proxy ARP bridging.
Unlike standard bridging, proxy ARP bridging allows to bridge Ethernet
networks behind wireless nodes. Normal L2 bridging does not work between
wireless nodes because wireless does not know about MAC addresses used
in the wired Ethernet networks. Also this daemon is useful for making
transparent firewalls.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 parprouted %{buildroot}%{_bindir}/parprouted
%{__install} -Dp -m0644 parprouted.8 %{buildroot}%{_mandir}/man8/parprouted.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README
%doc %{_mandir}/man8/parprouted.8*
%{_bindir}/parprouted

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.63-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 27 2005 Dag Wieers <dag@wieers.com> - 0.63-1
- Initial package. (using DAR)
