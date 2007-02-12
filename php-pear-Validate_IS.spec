%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	IS
%define		_status		alpha
%define		_pearname	Validate_IS

Summary:	%{_pearname} - Validation class for Iceland
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Islandii
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	eb28115c77c0459f05560cd13959a562
URL:		http://pear.php.net/package/Validate_IS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for IS (Iceland) such as:
- SSN
- Postal Code
- Address
- Telephone

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Islandii danych takich jak:
- numer ubezpieczenia społecznego (SSN)
- kod pocztowy
- adres
- numer telefonu

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/IS.php
%{php_pear_dir}/data/Validate_IS

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_IS
