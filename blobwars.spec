%define	name	blobwars
%define	oname	BlobWars
%define	version	1.19
%define	release	2
%define	Summary	%{oname} Episode I : Metal Blob Solid 

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.parallelrealities.co.uk
Source0:	http://ovh.dl.sourceforge.net/project/blobwars/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
Patch0:		blobwars-1.19-link.patch

License:	GPLv2+
Group:		Games/Arcade
Summary:	%{Summary}
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(zlib)



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

%build
CFLAGS="%optflags" LDFLAGS="%ldflags" %make DATADIR=%{_gamesdatadir}/%{name}/

%install
%makeinstall_std

%find_lang %{name}

desktop-file-install --vendor="" \
  --remove-key="Encoding" \
  --remove-category="Application" \
  --add-category="ArcadeGame" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


%files -f %{name}.lang
%defattr(644,root,games,755)
%doc %{_docdir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/*
%defattr(755,root,games,755)
%{_gamesbindir}/%{name}

