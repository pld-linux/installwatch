Summary:	Monitor for installed programs
Summary(pl):	Monitoruj instalacje progamów
Name:		installwatch
Version:	0.5.6
Release:	1
Group:		Applications/System
License:	GPL
Source0:	http://mayams.net/~izto/%{name}-%{version}.tgz
Patch0:		%{name}-DESTDIR.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Installwatch is an extremely simple utility to keep track of created
and modified files during the installation of a new program.

%description -l pl
Installwatch jest bardzo prostym programem zapisuj±cym pliki tworzone
i modyfikowane podczas instalacji nowego programu.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf BUGS CHANGELOG README TODO contrib/README.inst2rpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}
%attr(755,root,root) %{_libdir}
%doc *.gz contrib/*.gz
