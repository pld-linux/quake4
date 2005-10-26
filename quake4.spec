Summary:	Quake4 for Linux
Name:		quake4
Version:	1.0.2147.12
Release:	0.1
License:	?
Group:		Applications/Games
Source0:	%{name}-linux-%{version}.x86.run
# Source0-md5:	96ac1b993dafe5d255a7ee85d07187db
URL:		http://zerowing.idsoftware.com/linux/quake4/
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quake 4 for Linux.

%description -l pl
Quake 4 dla linuksa.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
