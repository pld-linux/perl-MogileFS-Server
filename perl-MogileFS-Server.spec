#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	mogilefs
%define	pnam	server
Summary:	none
#Summary(pl.UTF-8):	
Name:		perl-MogileFS-Server
Version:	2.17
Release:	1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/mogilefs/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	96814eb32b258557a1beea73d2ff4647
URL:		http://search.cpan.org/dist/mogilefs-server/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Gearman-Client-Async
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MogileFS server. 

# unfinished, could be run with some effort but things need to be checked

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES doc TODO
%dir %{perl_vendorlib}/MogileFS
%{perl_vendorlib}/MogileFS/*.pm
%dir %{perl_vendorlib}/MogileFS/Connection
%{perl_vendorlib}/MogileFS/Connection/*.pm
%dir %{perl_vendorlib}/MogileFS/Store
%{perl_vendorlib}/MogileFS/Store/*.pm
%dir %{perl_vendorlib}/MogileFS/Worker
%{perl_vendorlib}/MogileFS/Worker/*.pm
%dir %{perl_vendorlib}/MogileFS/RebalancePolicy
%{perl_vendorlib}/MogileFS/RebalancePolicy/*.pm
%dir %{perl_vendorlib}/MogileFS/ReplicationPolicy
%{perl_vendorlib}/MogileFS/ReplicationPolicy/*.pm
%dir %{perl_vendorlib}/Mogstored
%{perl_vendorlib}/Mogstored/*.pm
%dir %{perl_vendorlib}/Mogstored/ChildProcess
%{perl_vendorlib}/Mogstored/ChildProcess/*.pm
%dir %{perl_vendorlib}/Mogstored/HTTPServer
%{perl_vendorlib}/Mogstored/HTTPServer/*.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/mogstored
%attr(755,root,root) %{_bindir}/mogilefsd
%attr(755,root,root) %{_bindir}/mogdbsetup
%attr(755,root,root) %{_bindir}/mogautomount
