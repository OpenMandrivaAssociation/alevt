Summary:		Teletext decoder and browser for bttv and DVB
Name:		alevt
Version:		1.6.1
Release:		11
License:		GPL
Group:		Video
Source0:		http://www.goron.de/~froese/%name/%name-%version.tar.bz2
Source10:	alevt-big.png
Source11:	alevt-mini.png
Source12:	alevt.png
Patch0:		%name-1.6.0-time.h.patch
Patch1:		alevt-1.6.1-vbi-fix.patch
Patch2:		alevt-1.6.1-koi8.patch
Patch3:		alevt-1.6.1-xio.patch
Patch4:		alevt-1.6.1-dvb.patch
URL:		http://www.goron.de/~froese/
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libpng) >= 1.0.8
BuildRequires:	pkgconfig(zlib)


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
%doc CHANGELOG COPYRIGHT README
%attr(755,root,root) %_bindir/*
%_mandir/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-11mdv2011.0
+ Revision: 609964
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 1.6.1-10mdv2010.1
+ Revision: 508054
- fix BR
- rediff dvb patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.6.1-7mdv2008.1
+ Revision: 135819
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - s/Mandrake/Mandriva/


* Fri Dec 22 2006 Anssi Hannula <anssi@mandriva.org> 1.6.1-7mdv2007.0
+ Revision: 101532
- patch4: add dvb support
- Import alevt

* Tue Sep 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.6.1-6mdv2007.0
- XDG

* Thu Jun 29 2006 Lenny Cartier <lenny@mandriva.com> 1.6.1-5mdv2007.0
- rebuild

* Mon Jul 25 2005 Pascal Terjan <pterjan@mandriva.org> 1.6.1-4mdk
- Fix build (P3)
- Fix lib64

