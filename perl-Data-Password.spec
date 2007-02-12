#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Password
Summary:	Data::Password - Perl extension for assesing password quality
Summary(pl.UTF-8):   Data::Password - rozszerzenie Perla zapewniające odpowiednią jakość haseł
Name:		perl-%{pdir}-%{pnam}
Version:	1.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0fa2f19f5e4dbf3366396214a30ff634
URL:		http://search.cpan.org/dist/Data-Password/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules checks potential passwords for crackability. It checks
that the password is in the appropriate length, that it has enough
character groups, that it does not contain the same chars repeatedly
or ascending or descending characters, or charcters close to each
other in the keyboard. It will also attempt to search the ispell word
file for existance of whole words. The module's policies can be
modified by changing its variables.

%description -l pl.UTF-8
Ten moduł sprawdza potencjalne hasła pod kątem możliwości ich
złamania. Sprawdza czy hasło ma odpowiednią długość, czy posiada
odpowiednią ilość grup znaków, czy nie zawiera tych samych znaków
powtarzających się rosnąco lub malejąco albo znaków umiejscowionych
blisko siebie na klawiaturze. Spróbuje także przeszukać słownik
ispella pod kątem istnienia całych słów. Polityka modułu może być
modyfikowana za pomocą odpowiednich zmiennych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/*.pm
%{_mandir}/man3/*
