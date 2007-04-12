%define module  Class-Generate
%define name    perl-%{module}
%define version 1.07
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Generate Perl class hierarchies
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}
chmod 644 Changes README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*


