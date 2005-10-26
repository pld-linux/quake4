# TODO
# - dedicated package
# - .desktop and icon
# - separate -common, create language packs (us, german available)?
# - put some decent license
# - punkbuster? (pb/ subdir)?
Summary:	Quake4 for Linux
Name:		quake4
Version:	1.0.2147.12
Release:	0.1
License:	?
Group:		Applications/Games
Source0:	%{name}-linux-%{version}.x86.run
# NoSource0-md5:	96ac1b993dafe5d255a7ee85d07187db
NoSource:	0
URL:		http://zerowing.idsoftware.com/linux/quake4/
Requires:	OpenGL
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		_noautoprov		libgcc_s.so.1 libstdc++.so.5
%define		_noautoreqdep	libgcc_s.so.1 libstdc++.so.5
%define		_gamelibdir		%{_libdir}/games/quake4
%define		_gamedatadir	%{_datadir}/games/quake4

%description
Quake 4 for Linux.

%description -l pl
Quake 4 dla linuksa.

%prep
%setup -qcT
sh %{SOURCE0} --tar xf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_gamelibdir},%{_gamedatadir}/q4base} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_bindir}}

install bin/Linux/x86/{libgcc_s.so.1,libstdc++.so.5} $RPM_BUILD_ROOT%{_gamelibdir}
install bin/Linux/x86/{q4ded,quake4}.x86 $RPM_BUILD_ROOT%{_gamelibdir}
cp -a q4base/* $RPM_BUILD_ROOT%{_gamedatadir}/q4base
cp -a us/q4base/* $RPM_BUILD_ROOT%{_gamedatadir}/q4base
ln -s %{_gamedatadir}/q4base $RPM_BUILD_ROOT%{_gamelibdir}/q4base

cat << 'EOF' > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
cd %{_gamelibdir}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
exec ./quake4.x86 "$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc License.txt README Docs/ENG/readme.txt
%attr(755,root,root) %{_bindir}/%{name}

%dir %{_gamelibdir}
%attr(755,root,root) %{_gamelibdir}/quake4.x86
%attr(755,root,root) %{_gamelibdir}/libgcc_s.so.1
%attr(755,root,root) %{_gamelibdir}/libstdc++.so.5
%{_gamelibdir}/q4base

%dir %{_gamedatadir}
%dir %{_gamedatadir}/q4base
%{_gamedatadir}/q4base/*
