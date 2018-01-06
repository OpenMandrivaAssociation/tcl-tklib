%define oname	tklib

Summary:	Collection of utility modules for Tk
Name:		tcl-%{oname}
Version:	0.5
Release:	1
License:	BSD
Group:		Networking/WWW
URL:		https://core.tcl.tk/tklib/home
Source:	 	http://downloads.sourceforge.net/project/tcllib/%{oname}/%{version}/%{oname}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	tk
BuildRequires:	groff-for-man
BuildRequires:	tcl
BuildRequires:	tcl-tcllib

Requires:	tcl(abi) = 8.6
Requires:	tcl-tcllib
Requires:	tk

%description
Tklib is intended to be a collection of Tcl packages that provide utility
functions useful to a large collection of Tcl programmers.

%files
%dir %{tcl_sitelib}/tklib%{version}
%{tcl_sitelib}/tklib%{version}/*
%{_mandir}/mann/*
%doc README
%doc README-0.4.txt
%doc README-0.5.txt
%doc PACKAGES
%doc ChangeLog
%doc license.terms

#--------------------------------------------------------------------

%prep
%setup -q -n %oname-%version
%apply_patches

# fix spurious permissions
for d in diagrams khim plotchart swaplist widget
do
 chmod a-x modules/${d}/*.tcl
done
chmod a-x modules/khim/*.msg

%build
%configure \
	--libdir=%{tcl_sitelib}
	%{nil}
# There's nothing to build here
#% make

%install
%makeinstall_std

%check
%make check

