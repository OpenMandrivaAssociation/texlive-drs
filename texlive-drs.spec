# revision 19232
# category Package
# catalog-ctan /macros/latex/contrib/drs
# catalog-date 2010-07-03 21:56:37 +0200
# catalog-license lppl1.3
# catalog-version 1.1b
Name:		texlive-drs
Version:	1.1b
Release:	3
Summary:	Typeset Discourse Representation Structures (DRS)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/drs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drs.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package draws Discourse Representation Structures (DRSs).
It can draw embedded DRSs, if-then conditions and
quantificational "duplex conditions" (with a properly scaled
connecting diamond). Formatting parameters allow the user to
control the appearance and placement of DRSs, and of DRS
variables and conditions. The package is based on DRS macros in
the covington package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/drs/drs.sty
%doc %{_texmfdistdir}/doc/latex/drs/README
%doc %{_texmfdistdir}/doc/latex/drs/drsdoc.pdf
%doc %{_texmfdistdir}/doc/latex/drs/drsdoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1b-2
+ Revision: 751094
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1b-1
+ Revision: 718264
- texlive-drs
- texlive-drs
- texlive-drs
- texlive-drs

