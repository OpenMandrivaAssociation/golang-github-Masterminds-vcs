# http://github.com/Masterminds/vcs
%global goipath         github.com/Masterminds/vcs
%global gcommit          3084677c2c188840777bff30054f2b553729d329

Version:        1.11.1

%gometa -i

Name:           golang-github-Masterminds-vcs
Release:        3%{?dist}
Summary:        VCS Repo management through a common interface in Go
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE.txt'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: bzr

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE.txt
%doc CHANGELOG.md README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.11.1-2
- Upload glide files

* Sun Mar 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.11.1-1
- Update to 1.11.1

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.8.0-0.6.20160629gitfbe9fb6
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.5.gitfbe9fb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.4.gitfbe9fb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.3.gitfbe9fb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-0.2.gitfbe9fb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gitfbe9fb6
- First package for Fedora
  resolves: #1373612
