%define oname   tklib
Name:           tcl-%{oname}
Version:        0.4.1
Release:        %mkrel 7
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


