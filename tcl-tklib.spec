%define oname   tklib
Name:           tcl-%{oname}
Version:        0.4.1
Release:        8
Summary:        Collection of utility modules for Tk
License:        BSD
Group:          Networking/WWW
Source:         http://ovh.dl.sourceforge.net/sourceforge/tcllib/%oname-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-root
URL:            http://www.tcl.tk/software/tcllib/

BuildRequires:  tk
BuildRequires:  groff-for-man
BuildRequires:  tcl-tcllib
BuildRequires:  tcl

Obsoletes:      tk-tklib

%description
Tklib is like Tcllib, a collection of many small packages providing 
utilities, except that packages here are expected to depend on Tk. 
Tklib specializes in utilities for GUI programming.

%files
%defattr(-,root,root,0755)
%dir %{_libdir}/tklib0.4
%{_libdir}/tklib0.4/*
%{_mandir}/mann/*
#--------------------------------------------------------------------

%prep
%setup -q -n %oname-%version
%build

%configure

%make 


%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.1-7mdv2010.0
+ Revision: 434311
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.1-6mdv2009.0
+ Revision: 261431
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.1-5mdv2009.0
+ Revision: 254193
- rebuild
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix spacing at top of description

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.4.1-2mdv2008.1
+ Revision: 140918
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.1-2mdv2007.0
+ Revision: 99108
- Fix BuildRequires
- Import tcl-tklib

