%global _empty_manifest_terminate_build 0
Name:		python-tinyrpc
Version:	1.1.5
Release:	1
Summary:	A small, modular, transport and protocol neutral RPC library that, among other things, supports JSON-RPC and zmq.
License:	MIT
URL:		http://github.com/mbr/tinyrpc
Source0:	https://files.pythonhosted.org/packages/4c/d6/f0429f1af12e9c263135779514f9e4ed7f38253574c427726f517d45f049/tinyrpc-1.1.5.tar.gz
BuildArch:	noarch


%description


%package -n python3-tinyrpc
Summary:	A small, modular, transport and protocol neutral RPC library that, among other things, supports JSON-RPC and zmq.
Provides:	python-tinyrpc
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-tinyrpc


%package help
Summary:	Development documents and examples for tinyrpc
Provides:	python3-tinyrpc-doc
%description help


%prep
%autosetup -n tinyrpc-1.1.5

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-tinyrpc -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Jul 15 2022 hkgy <kaguyahatu@outlook.com> - 1.1.5-1
- Update package to 1.1.5

* Tue Nov 24 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
