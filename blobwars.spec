%define	name	blobwars
%define	oname	BlobWars
%define	version	1.07
%define	rel	2
%define	release	%mkrel %{rel}
%define	Summary	%{oname} Episode I : Metal Blob Solid 

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.parallelrealities.co.uk/blobWars.php
Source0:	%{name}-%{version}-1.tar.bz2
Patch1:		blobwars-1.07-makefile.patch
Patch2:		blobwars-1.07-es-translation.patch
License:	GPL-like
Group:		Games/Arcade
Summary:	%{Summary}
BuildRequires:	SDL_mixer-devel SDL_image-devel SDL_ttf-devel zziplib-devel
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
%patch1 -p1
%patch2 -p0

%build
%make OPTFLAGS="$RPM_OPT_FLAGS" DATADIR=%{_gamesdatadir}/%{name}/

%install
%{__rm} -rf $RPM_BUILD_ROOT
#%{__install} -m755 %{name} -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
#%{makeinstall_std} DATADIR=$RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/
%{makeinstall_std}
#%{__rm} -rf $RPM_BUILD_ROOT%{_bindir}/%{name}

%{find_lang} %{name}

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%post
%update_menus

%postun
%clean_menus

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,games,755)
%doc %{_docdir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/*
%defattr(755,root,games,755)
%{_gamesbindir}/%{name}
