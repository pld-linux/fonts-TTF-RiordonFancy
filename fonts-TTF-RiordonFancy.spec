Summary:	RiordonFancy TrueType font
Summary(pl.UTF-8):	Czcionka TrueType RiordonFancy
Name:		fonts-TTF-RiordonFancy
Version:	2
Release:	1
License:	Creative Commons cc-by-nc
Group:		Fonts
URL:		http://blogs.gnome.org/tthurman/2008/12/27/riordonfancy-version-2/
Requires(post,postun):	fontpostinst
Source0:	http://dorothy.thurman.org.uk/~tthurman/RiordonFancy/RiordonFancy.ttf
# Source0-md5:	9d7cb93b5678b36f447bb04f2babd5ae
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
RiordonFancy is a font designed one paper by the ten year old Riordon
Turner. It contains the whole ASCII set and an interrobang.

%description -l pl.UTF-8
RiordonFancy jest czcionką zaprojektowaną na papierze przez
dziesięcioletnią Riordon Turner. Zawiera kompletny zestaw znaków ASCII
oraz interrobang.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install %{SOURCE0} $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/*.ttf
