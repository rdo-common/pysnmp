%global sum An SNMP engine written in Python

Name:           pysnmp
Version:        4.3.1
Release:        1%{?dist}
Summary:        %{sum}

License:        BSD
URL:            http://pysnmp.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-setuptools

Requires:       net-snmp
Requires:       python-pyasn1

%description
This is a Python implementation of SNMP v.1/v.2c engine. It's
general functionality is to assemble/disassemble SNMP messages
from/into given SNMP Object IDs along with associated values.
PySNMP also provides a few transport methods specific to TCP/IP
networking.

%package -n python2-%{name}
Summary:        %{sum}
Requires:       python2-pyasn1
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
This is a Python implementation of SNMP v.1/v.2c engine. It's
general functionality is to assemble/disassemble SNMP messages
from/into given SNMP Object IDs along with associated values.
PySNMP also provides a few transport methods specific to TCP/IP
networking.

%package -n python3-%{name}
Summary:        %{sum}
Requires:       python3-pyasn1
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This is a Python implementation of SNMP v.1/v.2c engine. It's
general functionality is to assemble/disassemble SNMP messages
from/into given SNMP Object IDs along with associated values.
PySNMP also provides a few transport methods specific to TCP/IP
networking.

%prep
%autosetup -n %{name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{name}
%doc CHANGES README THANKS TODO examples/ docs/
%license LICENSE
%{_bindir}/*%{name}*
%{python2_sitelib}/%{name}/
%{python2_sitelib}/%{name}*.egg-info

%files -n python3-%{name}
%doc CHANGES README THANKS TODO examples/ docs/
%license LICENSE
%{_bindir}/*%{name}*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info

%changelog
* Thu Jan 28 2016 Fabian Affolter <mail@fabian-affolter.ch> - 4.3.1-1
- Add py3 support (rhbz#1282245)
- Updated to new upstream version 4.3.1 (rhbz#1145004)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 18 2013 Fabian Affolter <mail@fabian-affolter.ch> - 4.2.5-1
- Updated to new upstream version 4.2.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Fabian Affolter <mail@fabian-affolter.ch> - 4.2.4-1
- Updated to new upstream version 4.2.4

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 4.2.3-1
- Updated to new upstream version 4.2.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-1.rc1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-1.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 4.2.2-1.rc1
- Updated to new upstream version 4.2.2rc1
- Updated BR (#727395)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.14-2.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.14-1.a
- Updated to new upstream version 4.1.14.a

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 4.1.12-2.a
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Dec 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.12-1.a
- Updated to new upstream version 4.1.12.a

* Tue Sep 29 2009 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.11-1.a
- Removed shebang and permission fixing
- Added new doc files
- Added scripts to files section
- Updated to new upstream version 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 28 2008 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.9-2
- Changed license to BSD (#478603)
- Removed duplicated content, removed examples subpackage

* Tue Jan 01 2008 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.9-1
- Initial spec for Fedora
