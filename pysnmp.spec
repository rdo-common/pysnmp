%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pysnmp
Version:        2.0.9
Release:        4%{?dist}
Summary:        SNMP engine written in Python

Group:          Development/Libraries
License:        BSD
URL:            http://pysnmp.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python
BuildRequires:  python-setuptools-devel

Requires:       net-snmp

%description
This is a Python implementation of SNMP v.1/v.2c engine. It's
general functionality is to assemble/disassemble SNMP messages
from/into given SNMP Object IDs along with associated values.
PySNMP also provides a few transport methods specific to TCP/IP
networking.


%prep
%setup -q
#Remove exec permission from example files
chmod -x examples/*.py
#Change shebang
sed -i -e '1d;2i#!/usr/bin/python' examples/*.py

%build
python ./setup.py build


%install
rm -rf %{buildroot}
python ./setup.py install -O1 --skip-build --root=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README examples/ html/
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}*.egg-info


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2008 Fabian Affolter <fabian@bernewireless.net> - 2.0.9-2
- Changed license to BSD (#478603)
- Removed duplicated content, removed examples subpackage

* Thu Jan 01 2008 Fabian Affolter <fabian@bernewireless.net> - 2.0.9-1
- Initial spec for Fedora
