Name: glite-info-static
Version: 0.2.0
Release: 2%{?dist}
Summary: Core component for the static information framework
Group: System/Monitoring
License: ASL 2.0
URL: https://github.com/EGI-Federation/glite-info-static
Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildRequires: rsync
BuildRequires: make
BuildRequires: python3-rpm-macros
Requires: openldap-servers
Requires: python3

%description
This application is an information provider that generates information
in LDIF format from combining an LDIF template with configuration values.

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(0755,root,root) /usr/sbin/glite-info-static
%doc %{_docdir}/%{name}-%{version}/README.md
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license /usr/share/licenses/%{name}-%{version}/COPYRIGHT
%license /usr/share/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* Wed Apr 24 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 0.2.0-2
- Added Source URL information
* Thu Apr 8 2010 Laurence Field <laurence.field@cern.ch> - 0.2.0-1
- Refactored
* Mon Feb 15 2010 Laurence Field <laurence.field@cern.ch> - 0.1.0-1
- First release
