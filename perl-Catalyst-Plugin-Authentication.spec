%define realname Catalyst-Plugin-Authentication
%define name	perl-%{realname}
%define	modprefix Catalyst

%define version	0.09
%define release	%mkrel 3

Summary:	Infrastructure plugin for the Catalyst authentication framework
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.10
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Test::Exception)
Requires:	perl >= 5.8.1
BuildArch:	noarch

%description
The authentication plugin provides generic user support. It is the basis for
both authentication (checking the user is who they claim to be), and
authorization (allowing the user to do what the system authorises them to do).

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

## Temporarily disabled waiting for upstream fix (sak)
%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}



