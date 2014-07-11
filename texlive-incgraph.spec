# revision 28868
# category Package
# catalog-ctan /macros/latex/contrib/incgraph
# catalog-date 2013-01-17 11:27:48 +0100
# catalog-license lppl1.3
# catalog-version 1.11
Name:		texlive-incgraph
Version:	1.11
Release:	7
Summary:	Sophisticated graphics inclusion in a PDF document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/incgraph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/incgraph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/incgraph.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/incgraph/incgraph.sty
%doc %{_texmfdistdir}/doc/latex/incgraph/CHANGES
%doc %{_texmfdistdir}/doc/latex/incgraph/README
%doc %{_texmfdistdir}/doc/latex/incgraph/exaimage-0001.png
%doc %{_texmfdistdir}/doc/latex/incgraph/exaimage-0037.png
%doc %{_texmfdistdir}/doc/latex/incgraph/exaimage-0123.png
%doc %{_texmfdistdir}/doc/latex/incgraph/example.jpg
%doc %{_texmfdistdir}/doc/latex/incgraph/incgraph-example-a.pdf
%doc %{_texmfdistdir}/doc/latex/incgraph/incgraph-example-a.tex
%doc %{_texmfdistdir}/doc/latex/incgraph/incgraph-example-b.pdf
%doc %{_texmfdistdir}/doc/latex/incgraph/incgraph-example-b.tex
%doc %{_texmfdistdir}/doc/latex/incgraph/incgraph-example-c.pdf
%doc %{_texmfdistdir}/doc/latex/incgraph/incgraph-example-c.tex
%doc %{_texmfdistdir}/doc/latex/incgraph/incgraph.pdf
%doc %{_texmfdistdir}/doc/latex/incgraph/incgraph.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
