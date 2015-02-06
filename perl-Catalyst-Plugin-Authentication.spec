%define upstream_name    Catalyst-Plugin-Authentication
%define upstream_version 0.10023

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Infrastructure plugin for the Catalyst authentication framework
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Catalyst/Catalyst-Plugin-Authentication-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.10
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::MockObject)
BuildArch:	noarch

%description
The authentication plugin provides generic user support. It is the basis for
both authentication (checking the user is who they claim to be), and
authorization (allowing the user to do what the system authorises them to do).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

## Temporarily disabled waiting for upstream fix (sak)
%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1:0.100.160-2mdv2011.0
+ Revision: 680728
- mass rebuild

* Sun Jan 24 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.100.160-1mdv2011.0
+ Revision: 495429
- update to 0.10016

* Mon Sep 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.100.150-1mdv2010.0
+ Revision: 432799
- update to 0.10015

* Mon Aug 31 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.100.140-1mdv2010.0
+ Revision: 422883
- update to 0.10014

* Thu Jul 23 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.100.130-1mdv2010.0
+ Revision: 398890
- adding missing buildrequires:
- adding missing buildrequires:
- bumping epoch to force new version scheme
- update to 0.10013
- using %%perl_convert_version

* Tue Feb 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.100092-1mdv2009.1
+ Revision: 337001
- update to new version 0.100092

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10008-1mdv2009.1
+ Revision: 299372
- update to new version 0.10008

* Thu Jul 31 2008 Olivier Thauvin <nanardon@mandriva.org> 0.10006-1mdv2009.0
+ Revision: 258136
- 0.10006

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.09-5mdv2009.0
+ Revision: 255551
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.09-3mdv2008.1
+ Revision: 136676
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-3mdv2008.0
+ Revision: 85980
- rebuild


* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-06 18:46:36 (53536)
- Added BuildRequires: perl(Test::Exception)

* Sat Aug 05 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-05 23:49:46 (53373)
- import perl-Catalyst-Plugin-Authentication-0.09-1mdv2007.0

* Thu Aug 03 2006 Scott Karns <scottk@mandriva.org> 0.09-1mdv2007.0
- Version 0.09
- Reenabled %%check

* Wed May 03 2006 Scott Karns <scottk@mandriva.org> 0.07-3mdk
- Temporarily disabled %%check waiting for upstream fix
- Updated BuildRequires
- Updated package file ownership

* Thu Apr 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-2mdk
- Add BuildRequires

* Mon Mar 20 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-1mdk
- New release 0.07

* Tue Jan 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.05-1mdk
- 0.05

* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-2mdk
- Add BuildRequires

* Fri Dec 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.04-1mdk
- Initial MDV RPM



