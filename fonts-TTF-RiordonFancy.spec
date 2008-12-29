Summary:	RiordonFancy TrueType font
Summary(pl.UTF-8):	Czcionka TrueType RiordonFancy
Name:		fonts-TTF-RiordonFancy
Version:	2
Release:	2
License:	SIL Open Font License
Group:		Fonts
Source0:	http://openfontlibrary.org/people/tthurman/tthurman_-_Riordon_Fancy.ttf
# Source0-md5:	38940c142b4468f1728dfddcdcebdf69
URL:		http://openfontlibrary.org/media/files/tthurman/354
Requires(post,postun):	fontpostinst
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

install %{SOURCE0} $RPM_BUILD_ROOT%{ttffontsdir}/RiordonFancy.ttf

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/*.ttf
