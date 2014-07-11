# revision 33284
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/turkish
# catalog-date 2014-03-25 07:43:48 +0100
# catalog-license lppl1.3
# catalog-version 1.3b
Name:		texlive-babel-turkish
Version:	1.30b
Release:	2
Summary:	Babel support for Turkish documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/turkish
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-turkish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-turkish.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-turkish.source.tar.xz
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
%{_texmfdistdir}/tex/generic/babel-turkish/turkish.ldf
%doc %{_texmfdistdir}/doc/generic/babel-turkish/README
%doc %{_texmfdistdir}/doc/generic/babel-turkish/turkish.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-turkish/turkish.dtx
%doc %{_texmfdistdir}/source/generic/babel-turkish/turkish.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
