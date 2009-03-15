Summary:	RiordonFancy TrueType font
Summary(pl.UTF-8):	Czcionka TrueType RiordonFancy
Name:		fonts-TTF-RiordonFancy
Version:	4
Release:	1
License:	SIL Open Font License
Group:		Fonts
Source0:	http://openfontlibrary.org/people/tthurman/tthurman_-_Riordon_Fancy.zip
# Source0-md5:	b60772543ccb9bb95d4a6199f0054ef1
URL:		http://openfontlibrary.org/media/files/tthurman/354
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
RiordonFancy is a font designed one paper by the ten year old Riordon
Turner. It contains the whole ASCII set, Polish, Czech, Spanish and
Portuguese diacritics and an interrobang.

%description -l pl.UTF-8
RiordonFancy jest czcionką zaprojektowaną na papierze przez
dziesięcioletnią Riordon Turner. Zawiera kompletny zestaw znaków
ASCII, polskie, czeskie, hiszpańskie i portugalskie znaki diakrytyczne
oraz interrobang.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install RiordonFancy.ttf $RPM_BUILD_ROOT%{ttffontsdir}/RiordonFancy.ttf

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc fontlog.txt readme.txt
%{ttffontsdir}/*.ttf
