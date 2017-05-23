# TODO: port to audacious >= 3.6
Summary:	Audacious plugin that uses XMP library to play music modules
Summary(pl.UTF-8):	Wtyczka dla Audaciousa odtwarzająca moduły dźwiękowe z użyciem XMP
Name:		audacious-input-xmp
Version:	4
%define	snap	20131126
%define	gitref	ff914873bbf8bcdd552c78accfdb456c1cd76d5c
Release:	0.%{snap}.1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	https://github.com/cmatsuoka/xmp-plugin-audacious/archive/%{gitref}/xmp-plugin-audacious-%{snap}.tar.gz
# Source0-md5:	934832356d7afbf6f93772fe55520ffe
URL:		https://github.com/cmatsuoka/xmp-plugin-audacious
BuildRequires:	audacious-devel >= 3
BuildRequires:	audacious-devel < 3.6
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libxmp-devel >= 4
BuildRequires:	pkgconfig
Requires:	audacious >= 3
Requires:	libxmp >= 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audacious plugin that uses XMP library to play music modules.

%description -l pl.UTF-8
Wtyczka dla Audaciousa odtwarzająca moduły dźwiękowe z użyciem
biblioteki XMP.

%prep
%setup -q -n xmp-plugin-audacious-%{gitref}

%build
%{__cc} %{rpmcflags} %{rpmcppflags} $(pkg-config --cflags audacious glib-2.0 libxmp) -fPIC -DVERSION='"%{version}"' -o audacious3.o -c audacious3.c
%{__cc} %{rpmldflags} %{rpmcflags} -shared -o xmp-audacious3.so audacious3.o $(pkg-config --libs audacious glib-2.0 libxmp)

%install
rm -rf $RPM_BUILD_ROOT

install -D xmp-audacious3.so $RPM_BUILD_ROOT%{_libdir}/audacious/Input/xmp-audacious3.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/xmp-audacious3.so
