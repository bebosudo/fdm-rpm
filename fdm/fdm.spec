Name:           fdm
Summary:        A program to fetch, manipulate and deliver email
Version:        2.0
Release:        1%{?dist}
URL:            https://github.com/nicm/%{name}
License:        ISC
Source0:        https://github.com/nicm/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

# No explicit runtime require on libtdb, let rpm find the correct match for it.

BuildRequires:  zlib-devel, libtdb-devel, openssl-devel
BuildRequires:  gcc, make

%description
fdm is a program to fetch mail and deliver it in various ways depending on a
user-supplied rule-set. Mail may be fetched from stdin, IMAP or POP3 servers,
or from local maildirs, and filtered based on whether it matches a regexp, its
size or age, or the output of a shell command. It can be rewritten by an
external process, dropped, left on the server or delivered into maildirs,
mboxes, to a file or pipe, or any combination.

fdm is designed to be lightweight but powerful, with a compact but clear
configuration syntax. It is primarily designed for single-user uses but may
also be configured to deliver mail in a multi-user setup. In this case, it uses
privilege separation to minimize the amount of code running as the root user.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}
mv MANUAL %{buildroot}%{_docdir}/%{name}

%files
%{_bindir}/%{name}
%{_mandir}/man*/%{name}.*
%doc %{_docdir}/%{name}

%changelog
* Sun Nov 03 2019 Alberto Chiusole <bebo.sudo@gmail.com> - 2.0-1
- Initial packaging of fdm
