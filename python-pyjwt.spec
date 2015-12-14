%define name python-pyjwt
%define version 1.3.0
%define unmangled_version 1.3.0
%define release 1

Summary: Flask Migrate
Name: %{name}
Version: %{version}
Release: %{release}
Group: System/Authentication
Prefix: /usr
Provides: pyjwt
#Requires: 
Source0: %{name}-%{version}.tar.gz
License: MIT
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: x86_64
Vendor: José Padilla

%description
A Python implementation of JSON Web Token.

%prep
%setup -n %{name}-%{version} -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f INSTALLED_FILES
%files
/usr/lib/python2.7/site-packages/*
/usr/bin/jwt
%defattr(-,root,root)

