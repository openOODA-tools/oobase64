Name:           oobase64
Version:        0.1.0
Release:        1%{?dist}
Summary:        SIMD-accelerated RFC 4648 Base64 data encoder and decoder with URL-safe variants.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobase64
Source0:        oobase64-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobase64 is a sovereign, capability-bounded BASE64 ENCODER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobase64
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobase64-uninstall

%files
/usr/bin/oobase64
/usr/bin/oobase64-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
