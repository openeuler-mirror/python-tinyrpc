%global _empty_manifest_terminate_build 0
Name:		python-tinyrpc
Version:	0.9.1
Release:	1
Summary:	A small, modular, transport and protocol neutral RPC library that, among other things, supports JSON-RPC and zmq.
License:	MIT
URL:		http://github.com/mbr/tinyrpc
Source0:	https://files.pythonhosted.org/packages/90/c7/d91dc2eeb8d6ce15c23062f57255d78be8df4a803d8d4ba52c52c1c2fde9/tinyrpc-0.9.1.tar.gz
BuildArch:	noarch
%description
A small, modular, transport and protocol neutral RPC library that, among other things, supports JSON-RPC and zmq.


%package -n python2-tinyrpc
Summary:	A small, modular, transport and protocol neutral RPC library that, among other things, supports JSON-RPC and zmq.
Provides:	python-tinyrpc
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:  python2-pip
%description -n python2-tinyrpc
A small, modular, transport and protocol neutral RPC library that, among other things, supports JSON-RPC and zmq.


%package help
Summary:	Development documents and examples for tinyrpc
Provides:	python2-tinyrpc-doc
%description help
A small, modular, transport and protocol neutral RPC library that, among other things, supports JSON-RPC and zmq.


%prep
%autosetup -n tinyrpc-0.9.1

%build
%py2_build

%install
%py2_install
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

%files -n python2-tinyrpc -f filelist.lst
%dir %{python2_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Apr 29 2021 openstack-sig <openstack@openeuler.org>
- Package Spec generated
