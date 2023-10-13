#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-selinux
Version  : 0.3.0
Release  : 14
URL      : https://files.pythonhosted.org/packages/25/07/51acd62e1e15e1172d46f7e32faf138725b147f8c08dbf2d512159d7a310/selinux-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/25/07/51acd62e1e15e1172d46f7e32faf138725b147f8c08dbf2d512159d7a310/selinux-0.3.0.tar.gz
Summary  : shim selinux module
Group    : Development/Tools
License  : MIT
Requires: pypi-selinux-license = %{version}-%{release}
Requires: pypi-selinux-python = %{version}-%{release}
Requires: pypi-selinux-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(distro)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
:target: https://github.com/python/black
:alt: Python Black Code Style

%package license
Summary: license components for the pypi-selinux package.
Group: Default

%description license
license components for the pypi-selinux package.


%package python
Summary: python components for the pypi-selinux package.
Group: Default
Requires: pypi-selinux-python3 = %{version}-%{release}

%description python
python components for the pypi-selinux package.


%package python3
Summary: python3 components for the pypi-selinux package.
Group: Default
Requires: python3-core
Provides: pypi(selinux)
Requires: pypi(distro)

%description python3
python3 components for the pypi-selinux package.


%prep
%setup -q -n selinux-0.3.0
cd %{_builddir}/selinux-0.3.0
pushd ..
cp -a selinux-0.3.0 buildavx2
cp -a selinux-0.3.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672083351
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-selinux
cp %{_builddir}/selinux-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-selinux/357c3fcfb0d2ce5d76d67ef977706eb8147f9fc2
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-selinux/357c3fcfb0d2ce5d76d67ef977706eb8147f9fc2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
