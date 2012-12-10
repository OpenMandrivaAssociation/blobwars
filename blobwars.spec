%define	name	blobwars
%define	oname	BlobWars
%define	version	1.19
%define	rel	1
%define	release	%mkrel %{rel}
%define	Summary	%{oname} Episode I : Metal Blob Solid 

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.parallelrealities.co.uk
Source0:	http://ovh.dl.sourceforge.net/project/blobwars/%{name}-%{version}.tar.gz
Patch0:		blobwars-1.19-link.patch
License:	GPLv2+
Group:		Games/Arcade
Summary:	%{Summary}
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_net-devel
BuildRequires:	zlib-devel
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Since their world was invaded by an alien race, the Blobs have
faced a lifetime of war. But now they have a chance to win
the war once and for all.

In Episode I : Metal Blob Solid, you take on the role of a
fearless Blob agent, Bob. Bob's mission is to infiltrate the
various enemy bases around the Blobs' homeworld and rescue as many
POWs as possible. But standing in his way are many vicious enemies,
other Blobs who have defected and the evil alien leader, Galdov.

%prep
%setup -q
%patch0 -p0
#patch0 -p1
#sed -i 's@-Werror@@' makefile

%build
CFLAGS="%optflags" LDFLAGS="%ldflags" %make DATADIR=%{_gamesdatadir}/%{name}/

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%{find_lang} %{name}

desktop-file-install --vendor="" \
  --remove-key="Encoding" \
  --remove-category="Application" \
  --add-category="ArcadeGame" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,games,755)
%doc %{_docdir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/*
%defattr(755,root,games,755)
%{_gamesbindir}/%{name}


%changelog
* Wed May 18 2011 Funda Wang <fwang@mandriva.org> 1.19-1mdv2011.0
+ Revision: 676024
- new version 1.19

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.16-2mdv2011.0
+ Revision: 610077
- rebuild

  + Funda Wang <fwang@mandriva.org>
    - update BR

* Tue Feb 23 2010 Funda Wang <fwang@mandriva.org> 1.16-1mdv2010.1
+ Revision: 509985
- BR SDL_net
- new version 1.16

* Mon Jul 27 2009 Frederik Himpe <fhimpe@mandriva.org> 1.14-1mdv2010.0
+ Revision: 401035
- Update to new version 1.14
- Remove patches integrated upstream
- Replace no -Werror patch by sed hack
- Ensure it uses Mandriva %%optflags

* Fri May 15 2009 Samuel Verschelde <stormi@mandriva.org> 1.11-1mdv2010.0
+ Revision: 376185
- fix build (add patch from gentoo)
- fix licence

  + Emmanuel Andry <eandry@mandriva.org>
    - fix URL
    - New version 1.11
    - fix spanish translation with P1 and P2

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri May 02 2008 Funda Wang <fwang@mandriva.org> 1.08-1mdv2009.0
+ Revision: 200019
- New version 1.08

* Tue Mar 18 2008 Emmanuel Andry <eandry@mandriva.org> 1.07-3mdv2008.1
+ Revision: 188674
- don't remove ArcadeGame XDG category

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.07-2mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 16 2007 Funda Wang <fwang@mandriva.org> 1.07-2mdv2008.0
+ Revision: 88481
- more standard game category
- fix bug#31533 (updated es translatiion)

* Fri Jun 15 2007 Funda Wang <fwang@mandriva.org> 1.07-1mdv2008.0
+ Revision: 39871
- New buildrequires
  add locales files
- patch is needed to install correctly
- use makeinstall_std
- Patch not needed, too
- SOURCE2 not needed
  remove old menu
- No more source1
- clean patch
- New version
- Import blobwars



* Sat Aug 18 2006 Emmanuel Andry <eandry@mandriva.org> 1.05-2mdv2007.0
- xdg menu
- drop patch0
- add patch1 from debian to fix gcc4.1 compilation

* Wed Aug 10 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.05-1mdk
- 1.05 (1.04 game data)
- regenerate P0
- %%mkrel

* Sat Apr 09 2005 Emmanuel Andry <eandry@free.fr> 1.03-1mdk
- 1.03

* Tue Jan 18 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.02-1mdk
- 1.02

* Mon Jan 10 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.01-1mdk
- 1.01

* Sat Dec 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.99-1mdk
- 0.99
- regenerate P0

* Thu Dec 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.98-1mdk
- 0.98

* Tue Nov 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.97-1mdk
- 0.97
- added music
- fix path to docs (updated P0)

* Wed Oct 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.96-1mdk
- 0.96
- regenerate P0

* Mon Oct 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.94-1mdk
- 0.94
- update P0

* Wed Sep 01 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9-2mdk
- rebuild for new menu (fixes #11015)

* Wed Aug 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9-1mdk
- 0.9

* Tue Jun 15 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.52-2mdk
- rebuild

* Sat May 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.52-1mdk
- 0.52
- regenerate P0

* Fri May 28 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5-2mdk
- rebuild against new zzlip

* Wed Feb 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5-1mdk
- 0.5
- fix buildrequires
- regenerate P0

* Mon Nov 17 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.4-1mdk
- 0.4

* Tue Oct 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3-1mdk
- 0.3
- regenerated P0 and adjusted spec for changes in 0.3
- this release actually works!

* Sat Sep 20 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2-1mdk
- 0.2

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.2-1mdk
- new release
- regenerate P0

* Sat Aug 02 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1-1mdk
- initial mdk release
