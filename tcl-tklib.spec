%define oname	tklib

Summary:	Collection of utility modules for Tk
Name:		tcl-%{oname}
Version:	0.7
Release:	1
License:	BSD
Group:		Networking/WWW
URL:		https://core.tcl.tk/tklib/home
#Source:	http://downloads.sourceforge.net/project/tcllib/%{oname}/%{version}/%{oname}-%{version}.tar.bz2
Source0:	https://core.tcl-lang.org/tklib/attachdownload/%{oname}-%{version}.tar.bz2?page=Downloads&file=%{oname}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	tk
BuildRequires:	groff-for-man
BuildRequires:	tcl-devel
BuildRequires:	tcl-tcllib

Requires:	tcl(abi) = 8.6
Requires:	tcl-tcllib
Requires:	tk

%description
Tklib is intended to be a collection of Tcl packages that provide utility
functions useful to a large collection of Tcl programmers.

%files
%_bindir/bitmap-editor
%_bindir/diagram-viewer
%dir %{tcl_sitelib}/tklib%{version}
%{tcl_sitelib}/tklib%{version}/*
%{_mandir}/mann/*
%doc README README.developer
%doc ChangeLog
%doc license.terms

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n %oname-%version

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
%make_install

%check
%make check

