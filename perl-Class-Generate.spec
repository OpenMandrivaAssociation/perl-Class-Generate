%define upstream_name    Class-Generate
%define upstream_version 1.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Generate Perl class hierarchies
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/Class-Generate-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRequires: perl(Module::Build)
BuildArch:      noarch

%description
The Class::Generate package exports functions that take as arguments a class
specification and create from these specifications a Perl 5 class. The
specification language allows many object-oriented constructs: typed members,
inheritance, private members, required members, default values, object methods,
class methods, class variables, and more.

CPAN contains similar packages. Why another? Because object-oriented
programming, especially in a dynamic language like Perl, is a complicated
endeavor. I wanted a package that would work very hard to catch the errors you
(well, I anyway) commonly make. I wanted a package that could help me enforce
the contract of object-oriented programming. I also wanted it to get out of my
way when I asked.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes README

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files 
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.0-1mdv2011.0
+ Revision: 659887
- update to new version 1.11

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 403012
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.10-3mdv2009.0
+ Revision: 241186
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2008.0
+ Revision: 63923
- update to new version 1.10

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2008.0
+ Revision: 46522
- update to new version 1.09

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.08-1mdv2008.0
+ Revision: 19794
- 1.08


* Wed Jan 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2007.0
+ Revision: 109947
- new version
- Import perl-Class-Generate

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-5mdv2007.0
- Rebuild

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-4mdk
- spec cleanup
- %%mkrel
- better URL
- rpmbuilupdate aware
- fix doc files perms

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.06-3mdk
- fix buildrequires in a backward compatible way

* Sun Aug 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.06-2mdk 
- fix directory ownership (distlint)

* Wed Mar 03 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.06-1mdk
- first mdk release


