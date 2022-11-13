Name:		texlive-incgraph
Version:	60810
Release:	1
Summary:	Sophisticated graphics inclusion in a PDF document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/incgraph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/incgraph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/incgraph.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides tools for including graphics at the full
size of the output medium, or for creating "pages" whose size
is that of the graphic they contain. A principal use case is
documents that require inclusion of (potentially many) scans or
photographs. Bookmarking is especially supported. The tool box
has basic macros and a 'convenience' user interface that wraps
\includegraphics.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/incgraph
%doc %{_texmfdistdir}/doc/latex/incgraph

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
