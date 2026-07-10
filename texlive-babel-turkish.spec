%global tl_name babel-turkish
%global tl_revision 51560

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Babel support for Turkish documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/turkish
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-turkish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-turkish.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-turkish.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support, within babel, of the Turkish language.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-turkish
%dir %{_datadir}/texmf-dist/source/generic/babel-turkish
%dir %{_datadir}/texmf-dist/tex/generic/babel-turkish
%doc %{_datadir}/texmf-dist/doc/generic/babel-turkish/README.md
%doc %{_datadir}/texmf-dist/doc/generic/babel-turkish/turkish.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-turkish/turkish.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-turkish/turkish.ins
%{_datadir}/texmf-dist/tex/generic/babel-turkish/turkish.ldf
