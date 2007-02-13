Summary:	Monitor for installed programs
Summary(pl.UTF-8):	Monitor instalacji programów
Name:		installwatch
Version:	0.6.3
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://asic-linux.com.mx/~izto/checkinstall/files/source/%{name}-%{version}.tgz
# Source0-md5:	5dd4c411432e8e88bfd64fb688a5fd6a
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-cflags.patch
URL:		http://asic-linux.com.mx/~izto/checkinstall/installwatch.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Installwatch is an extremely simple utility to keep track of created
and modified files during the installation of a new program.

%description -l pl.UTF-8
Installwatch jest bardzo prostym programem zapisującym informacje o
plikach tworzonych i modyfikowanych podczas instalacji nowego programu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	BINDIR=%{_bindir} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
