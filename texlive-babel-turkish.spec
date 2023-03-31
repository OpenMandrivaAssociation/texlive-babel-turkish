Name:		texlive-babel-turkish
Version:	51560
Release:	2
Summary:	Babel support for Turkish documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/turkish
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-turkish.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-turkish.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-turkish.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support, within babel, of the Turkish
language.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-turkish
%doc %{_texmfdistdir}/doc/generic/babel-turkish
#- source
%doc %{_texmfdistdir}/source/generic/babel-turkish

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
