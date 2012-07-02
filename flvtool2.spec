%{!?ruby_sitelib: %global ruby_sitelib %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"] ')}

Summary: Manipulation tool for Macromedia Flash Video (FLV) files
Name: flvtool2
Version: 1.0.6
Release: 6%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://www.inlet-media.de/flvtool2
Source: http://rubyforge.org/frs/download.php/17497/flvtool2-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: ruby(abi) = 1.8
BuildRequires: ruby
BuildArch: noarch

%description
FLVTool2 is a manipulation tool for Macromedia Flash Video (FLV) files.
FLVTool2 can calculate a lot of meta data and insert a onMetaData tag. It can
cut FLV files and add cue Points (onCuePoint). A debug command lets you see
inside our FLV and the print command gives you meta data information in XML
or YAML format.


%prep
%setup -q


%build
ruby setup.rb config
ruby setup.rb setup


%install
%{__rm} -rf %{buildroot}
ruby setup.rb install --prefix=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE README examples/
%{_bindir}/flvtool2
%{ruby_sitelib}/flv.rb
%{ruby_sitelib}/flvtool2.rb
%{ruby_sitelib}/mixml.rb
%{ruby_sitelib}/miyaml.rb
%{ruby_sitelib}/flv/
%{ruby_sitelib}/flvtool2/


%changelog
* Mon Jul 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.6-6
- Rebuilt for rfbz#2370

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May  6 2009 Matthias Saou <http://freshrpms.net/> 1.0.6-4
- Add the mandatory "Requires: ruby(abi) = 1.8" line.
- Use the ruby_sitelib macro.
- Quiet setup.

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.0.6-3
- rebuild for new F11 features

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.0.6-2
- rebuild for RPM Fusion

* Wed Feb 14 2007 Matthias Saou <http://freshrpms.net/> 1.0.6-1
- Update to 1.0.6 (final).

* Wed Feb  7 2007 Matthias Saou <http://freshrpms.net/> 1.0.5-0.1.rc6
- Initial RPM release.

