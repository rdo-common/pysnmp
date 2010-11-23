Name:           pysnmp
Version:        4.1.14
Release:        1.a%{?dist}
Summary:        SNMP engine written in Python

Group:          Development/Libraries
License:        BSD
URL:            http://pysnmp.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}a.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

Requires:       net-snmp

%description
This is a Python implementation of SNMP v.1/v.2c engine. It's
general functionality is to assemble/disassemble SNMP messages
from/into given SNMP Object IDs along with associated values.
PySNMP also provides a few transport methods specific to TCP/IP
networking.


%prep
%setup -q -n %{name}-%{version}a


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README THANKS TODO examples/ docs/
%{_bindir}/*%{name}*
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}*.egg-info


%changelog
* Tue Nov 23 2010 Fabian Affolter <fabian@bernewireless.net> - 4.1.14-1.a
- Updated to new upstream version 4.1.14.a

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 4.1.12-2.a
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Dec 18 2009 Fabian Affolter <fabian@bernewireless.net> - 4.1.12-1.a
- Updated to new upstream version 4.1.12.a

* Tue Sep 29 2009 Fabian Affolter <fabian@bernewireless.net> - 4.1.11-1.a
- Removed shebang and permission fixing
- Added new doc files
- Added scripts to files section
- Updated to new upstream version 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2008 Fabian Affolter <fabian@bernewireless.net> - 2.0.9-2
- Changed license to BSD (#478603)
- Removed duplicated content, removed examples subpackage

* Thu Jan 01 2008 Fabian Affolter <fabian@bernewireless.net> - 2.0.9-1
- Initial spec for Fedora
