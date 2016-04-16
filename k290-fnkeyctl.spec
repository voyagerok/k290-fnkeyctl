Name:           k290-fnkeyctl
Version:        1.1
Release:        1%{?dist}
Summary:        Configures the behaviour of the F-keys on the Logitech K290

License:        MIT
URL:            https://github.com/milgner/k290-fnkeyctl
Source0:        https://github.com/milgner/k290-fnkeyctl/archive/v1.1.tar.gz

BuildRequires:  libusbx-devel

%description
Configures the behaviour of the F-keys on the Logitech K290

%prep
%setup -q

%build
./build.sh

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/sbin/
mkdir -p %{buildroot}/etc/udev/rules.d/

install -m 755 k290_fnkeyctl %{buildroot}/usr/sbin/
install -m 644 99-k290-config.rules %{buildroot}/etc/udev/rules.d/

%files
/usr/sbin/k290_fnkeyctl
/etc/udev/rules.d/99-k290-config.rules

%changelog
* Thu Nov  5 2015 Mariusz Smykuła
- Initial rpm version
