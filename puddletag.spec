Summary:	A tag editor for Linux similar to Mp3tag
Name:		puddletag
Version:	1.0.3
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/puddletag/%{name}-%{version}.tar.gz
# Source0-md5:	7105fde17fa83dc7121341a7ce095be6
URL:		http://puddletag.sourceforge.net
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	python-PyQt-QtSvg
Requires:	python-configobj
Requires:	python-devel-tools
Requires:	python-musicbrainz2
Requires:	python-mutagen
Requires:	python-pyparsing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
puddletag is a tag editor for Linux loosely based on the Windows
program Mp3tag. Basically it uses a table layout so that all the tags
you want to edit by hand are visible and easily editable. However,
puddletag excels at automating repetitive task like extracting tag
information from filenames, renaming files based on their tags by
using patterns.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO THANKS
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitescriptdir}/puddlestuff
%dir %{py_sitescriptdir}/puddlestuff/audioinfo
%dir %{py_sitescriptdir}/puddlestuff/libraries
%dir %{py_sitescriptdir}/puddlestuff/mainwin
%dir %{py_sitescriptdir}/puddlestuff/tagsources
%dir %{py_sitescriptdir}/puddlestuff/tagsources/mp3tag
%dir %{py_sitescriptdir}/puddlestuff/plugins
%dir %{py_sitescriptdir}/puddlestuff/masstag
%{py_sitescriptdir}/puddlestuff/*.py[co]
%{py_sitescriptdir}/puddlestuff/audioinfo/*.py[co]
%{py_sitescriptdir}/puddlestuff/libraries/*.py[co]
%{py_sitescriptdir}/puddlestuff/mainwin/*.py[co]
%{py_sitescriptdir}/puddlestuff/masstag/*.py[co]
%{py_sitescriptdir}/puddlestuff/plugins/*.py[co]
%{py_sitescriptdir}/puddlestuff/tagsources/*.py[co]
%{py_sitescriptdir}/puddlestuff/tagsources/mp3tag/*.py[co]
%{_desktopdir}/puddletag.desktop
%{_pixmapsdir}/puddletag.png
%{_mandir}/man1/puddletag.1*

