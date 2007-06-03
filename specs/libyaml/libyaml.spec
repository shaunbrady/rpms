# $Id$
# Authority: dries
# Upstream: Kirill <xi$gamma,dn,ua>

Summary: Implementation of a YAML 1.1 parser and emitter
Name: libyaml
Version: 0.0.1
Release: 1
License: MIT/X Consortium
Group: Development/Libraries
URL: http://pyyaml.org/wiki/LibYAML

Source: http://pyyaml.org/download/libyaml/yaml-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
LibYAML is a C library implementation of a YAML 1.1 parser and emitter. 
It includes a Python language binding.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n yaml-%{version}

%build
%configure --disable-static
%{__make} %{?_smp_mflags} AM_CFLAGS=""

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_libdir}/libyaml-0.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/yaml.h
%{_libdir}/libyaml.so
%exclude %{_libdir}/*.la

%changelog
* Mon May 28 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.1-1
- Initial package.
