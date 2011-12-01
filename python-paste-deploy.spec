%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

Name:           python-paste-deploy
Version:        1.3.3
Release:        2.1%{?dist}
Summary:        Load, configure, and compose WSGI applications and servers
Group:          System Environment/Libraries
License:        MIT
URL:            http://pythonpaste.org/deploy
Source0:        http://cheeseshop.python.org/packages/source/P/PasteDeploy/PasteDeploy-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires: python-devel
%if 0%{?fedora} >= 8 || 0%{?rhel} >= 6
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-setuptools
%endif
Requires:       python-paste

%description
This tool provides code to load WSGI applications and servers from
URIs; these URIs can refer to Python Eggs for INI-style configuration
files.  PasteScript provides commands to serve applications based on
this configuration file.

%prep
%setup -q -n PasteDeploy-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --single-version-externally-managed \
                             --skip-build -O1 --root=%{buildroot}

echo '%defattr (0644,root,root,0755)' > pyfiles
find %{buildroot}%{python_sitelib}/paste/deploy -type d | \
        sed 's:%{buildroot}\(.*\):%dir \1:' >> pyfiles
find %{buildroot}%{python_sitelib}/paste/deploy -not -type d | \
        sed 's:%{buildroot}\(.*\):\1:' >> pyfiles

%clean
rm -rf %{buildroot}


%files -f pyfiles
%defattr(-,root,root,-)
%doc docs/*
%{python_sitelib}/PasteDeploy-%{version}-py%{pyver}*



%changelog
* Fri Nov 13 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.3.3-2.1
- Fix conditional for RHEL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.2-2
- Rebuild for Python 2.6

* Sat Jun 14 2008 Luke Macken <lmacken@redhat.com> - 1.3.2-3
- Update to PasteDeploy 1.3.2

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 1.3.1-2
- Update for python-setuptools changes in rawhide

* Sun Jul  8 2007 Luke Macken <lmacken@redhat.com> - 1.3.1-1
- 1.3.1

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> - 1.1-1
- 1.1

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> - 1.0-2
- Add python-devel to BuildRequires
- 1.0

* Sun Sep 17 2006 Luke Macken <lmacken@redhat.com> - 0.9.6-1
- 0.9.6

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> - 0.5-4
- Rebuild for FC6

* Mon Aug 21 2006 Luke Macken <lmacken@redhat.com> - 0.5-3
- Include .pyo files instead of ghosting them.

* Mon Jul 24 2006 Luke Macken <lmacken@redhat.com> - 0.5-2
- Fix docs inclusion
- Rename package to python-paste-deploy
- Fix inconsistent use of buildroots

* Mon Jul 10 2006 Luke Macken <lmacken@redhat.com> - 0.5-1
- Initial package
