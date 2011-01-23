%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Validate_IS
Summary:	%{_pearname} - Validation class for Iceland
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Islandii
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d971c005841f965ecc0cf6c2f1f42ffc
URL:		http://pear.php.net/package/Validate_IS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-ctype
Requires:	php-pear
Obsoletes:	php-pear-Validate_IS-tests
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
