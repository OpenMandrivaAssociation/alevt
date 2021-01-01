Summary:	Teletext decoder and browser for bttv and DVB
Name:		alevt
Version:	1.8.0
Release:	1
License:	GPL
Group:		Video
Source0:	https://gitlab.com/alevt/alevt/-/archive/v%{version}/alevt-v%{version}.tar.bz2
Source10:	alevt-big.png
Source11:	alevt-mini.png
Source12:	alevt.png
Patch0:		%name-1.6.0-time.h.patch
Patch1:		alevt-1.6.1-vbi-fix.patch
URL:		https://gitlab.com/alevt/alevt
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libpng) >= 1.0.8
BuildRequires:	pkgconfig(zlib)

%description
AleVT is a teletext/videotext decoder and browser for the bttv and DVB
drivers. It features multiple windows, a page cache, regexp searching,
built-in manual, and more. There's also a program to get the time from
teletext and one to capture teletext pages from scripts.

%prep
%autosetup -p1 -n %{name}-v%{version}
sed -i 's£-L/usr/X11R6/lib£-L/usr/X11R6/%{_lib}£' Makefile
sed -i '7i#include <zlib.h>' exp-gfx.c

%build
make OPT="$RPM_OPT_FLAGS"

%install
install -d $RPM_BUILD_ROOT{%_bindir,%_mandir/man1,%_liconsdir,%_miconsdir}

install alevt alevt-date alevt-cap $RPM_BUILD_ROOT%_bindir
install {alevt-cap.1,alevt-date.1,alevt.1x} $RPM_BUILD_ROOT%_mandir/man1

# Mandriva menu entry

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Alevt
Comment=Teletext/Videotext decoder and browser
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;Video;TV;
EOF

install %SOURCE10 $RPM_BUILD_ROOT%_liconsdir/%name.png
install %SOURCE11 $RPM_BUILD_ROOT%_miconsdir/%name.png
install %SOURCE12 $RPM_BUILD_ROOT%_iconsdir/%name.png 

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif


%files
%doc CHANGELOG COPYRIGHT
%attr(755,root,root) %_bindir/*
%_mandir/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
