%define upstream_name    Catalyst-Plugin-Authentication
%define upstream_version 0.10013

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Infrastructure plugin for the Catalyst authentication framework
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.10
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl >= 5.8.1

%description
The authentication plugin provides generic user support. It is the basis for
both authentication (checking the user is who they claim to be), and
authorization (allowing the user to do what the system authorises them to do).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*

%clean
rm -rf %{buildroot}



