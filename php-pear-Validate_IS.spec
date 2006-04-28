%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	IS
%define		_status		alpha
%define		_pearname	Validate_IS

Summary:	%{_pearname} - Validation class for Iceland
Summary(pl):	%{_pearname} - Klasa sprawdzaj±ca poprawno¶æ dla Islandii
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	04afd1ffbb48496fd62ff30e9ed93e31
URL:		http://pear.php.net/package/Validate_IS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for IS (Iceland) such as:
- SSN
- Postal Code
- Telephone

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet do sprawdzania poprawno¶ci dla Islandii danych takich jak:
- numer ubezpieczenia spo³ecznego (SSN)
- kod pocztowy
- numer telefonu

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
%dir %{php_pear_dir}/data/Validate_IS
%{php_pear_dir}/data/Validate_IS/IS_postcodes.txt

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_IS
