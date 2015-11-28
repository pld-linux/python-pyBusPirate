#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_with	python3		# Python 3.x module
#
%define	module	pyBusPirate
#
Summary:	Library for interacting with the Bus Pirate
Name:		python-pyBusPirate
Version:	r597
Release:	2
License:	GPL
Group:		Development/Languages/Python
Source0:	https://the-bus-pirate.googlecode.com/files/pyBusPirateLite-%{version}.zip
# Source0-md5:	0fa40ef236f1f195bad9ac4291b9efac
URL:		https://code.google.com/p/the-bus-pirate/
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	python
Requires:	python-serial
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for interacting with the Bus Pirate.

%package -n	python3-%{module}
Summary:	Library for interacting with the Bus Pirate
Version:	r597
Release:	2
Group:		Libraries/Python
Requires:	python3
Requires:	python3-serial

%description -n python3-%{module}
Library for interacting with the Bus Pirate.

%prep
%setup -q -n pyBusPirateLite

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
cp -a pyBusPirateLite $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}
cp -a pyBusPirateLite $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc *.py
%{py_sitescriptdir}/%{module}Lite
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc *.py
%{py3_sitescriptdir}/%{module}Lite
%endif
