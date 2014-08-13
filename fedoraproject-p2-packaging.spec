%global commit   e86ba2af811bc2ee058c43bb7e6a82565be26086
%global shorttag %(cut -c 1-7 <<<"%{commit}")

Name:           fedoraproject-p2
Version:        0.0.1
Release:        0.1.git%{shorttag}%{?dist}
Summary:        XXX
License:        EPL
URL:            XXX
Source0:        https://github.com/rgrunber/%{name}/archive/%{commit}.tar.gz#/%{name}-%{version}-%{shorttag}.tar.gz
# XXX Add EPL license text
BuildArch:      noarch

BuildRequires:  xmvn-p2

%description
XXX

%prep
%setup -q -n %{name}-%{commit}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Wed Aug 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.1-0.1.gitee86ba2a
- Initial packaging
