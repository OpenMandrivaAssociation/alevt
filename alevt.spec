Summary:	Teletext decoder and browser for bttv and DVB
Name:		alevt
Version:	1.6.1
Release:	%mkrel 7
License:	GPL
Group:		Video
Source0:	http://www.goron.de/~froese/%name/%name-%version.tar.bz2
Source10:	alevt-big.png
Source11:	alevt-mini.png
Source12:	alevt.png
Patch0:		%name-1.6.0-time.h.patch
Patch1:		alevt-1.6.1-vbi-fix.patch
Patch2:		alevt-1.6.1-koi8.patch
Patch3:		alevt-1.6.1-xio.patch
Patch4:		alevt-1.6.1-dvb.patch
URL:		http://www.goron.de/~froese/
BuildRequires:	X11-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	zlib-devel
BuildRoot:	%_tmppath/%name-%version-root-%(id -u -n)

%description
AleVT is a teletext/videotext decoder and browser for the bttv and DVB
drivers. It features multiple windows, a page cache, regexp searching,
built-in manual, and more. There's also a program to get the time from
teletext and one to capture teletext pages from scripts.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p0 -b .xio
%patch4 -p1
sed -i 's£-L/usr/X11R6/lib£-L/usr/X11R6/%{_lib}£' Makefile

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%_bindir,%_mandir/man1}

install alevt alevt-date alevt-cap $RPM_BUILD_ROOT%_bindir
install {alevt-cap.1,alevt-date.1,alevt.1x} $RPM_BUILD_ROOT%_mandir/man1

# Mandriva menu entry
mkdir -p $RPM_BUILD_ROOT/{%_liconsdir,%_miconsdir,%_menudir}
cat << EOF >$RPM_BUILD_ROOT%_menudir/%name
?package(%name): command="%name" icon="%name.png" \
needs="x11" title="Alevt" \
longtitle="Teletext/Videotext decoder and browser" section="Multimedia/Video" \
xdg="true"
EOF

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


%clean
rm -rf $RPM_BUILD_ROOT


%post
%update_menus

%postun
%clean_menus


%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYRIGHT README
%attr(755,root,root) %_bindir/*
%_mandir/man1/*
%_menudir/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png


