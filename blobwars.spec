%define	oname	BlobWars

Name:		blobwars
Version:	2.00
Release:	1
URL:		http://www.parallelrealities.co.uk
Source0:	https://github.com/perpendicular-dimensions/blobwars/archive/master/%{oname}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
Patch0:		blobwars-compile.patch

License:	GPLv2+
Group:		Games/Arcade
Summary:	BlobWars Episode I : Metal Blob Solid
BuildRequires:	desktop-file-utils
BuildRequires:	meson ninja
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_net)
BuildRequires:	pkgconfig(SDL2_ttf)
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
%autosetup -p1 -n blobwars-master
%meson

%build
%meson_build

%install
%meson_install
rm %{buildroot}%{_datadir}/applications/*.ico

%files
%defattr(644,root,games,755)
%doc %{_docdir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/*
%defattr(755,root,games,755)
%{_gamesbindir}/%{name}

