#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Password
Summary:	Data::Password - Perl extension for assesing password quality
Summary(pl):	Data::Password - rozszerzenie Perla zapewniaj�ce odpowiedni� jako�� hase�
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

%description -l pl
Ten modu� sprawdza potencjalne has�a pod k�tem mo�liwo�ci ich
z�amania. Sprawdza czy has�o ma odpowiedni� d�ugo��, czy posiada
odpowiedni� ilo�� grup znak�w, czy nie zawiera tych samych znak�w
powtarzaj�cych si� rosn�co lub malej�co albo znak�w umiejscowionych
blisko siebie na klawiaturze. Spr�buje tak�e przeszuka� s�ownik
ispella pod k�tem istnienia ca�ych s��w. Polityka modu�u mo�e by�
modyfikowana za pomoc� odpowiednich zmiennych.

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
