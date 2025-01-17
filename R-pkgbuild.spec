#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-pkgbuild
Version  : 1.4.6
Release  : 61
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/pkgbuild_1.4.6.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/pkgbuild_1.4.6.tar.gz
Summary  : Find Tools Needed to Build R Packages
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-callr
Requires: R-cli
Requires: R-desc
Requires: R-processx
BuildRequires : R-R6
BuildRequires : R-callr
BuildRequires : R-cli
BuildRequires : R-desc
BuildRequires : R-processx
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
compilers needed to build R packages on various platforms and ensures
    the PATH is configured appropriately so R can use them.

%prep
%setup -q -n pkgbuild
pushd ..
cp -a pkgbuild buildavx2
popd
pushd ..
cp -a pkgbuild buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737132008

%install
export SOURCE_DATE_EPOCH=1737132008
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pkgbuild/DESCRIPTION
/usr/lib64/R/library/pkgbuild/INDEX
/usr/lib64/R/library/pkgbuild/LICENSE
/usr/lib64/R/library/pkgbuild/Meta/Rd.rds
/usr/lib64/R/library/pkgbuild/Meta/features.rds
/usr/lib64/R/library/pkgbuild/Meta/hsearch.rds
/usr/lib64/R/library/pkgbuild/Meta/links.rds
/usr/lib64/R/library/pkgbuild/Meta/nsInfo.rds
/usr/lib64/R/library/pkgbuild/Meta/package.rds
/usr/lib64/R/library/pkgbuild/NAMESPACE
/usr/lib64/R/library/pkgbuild/NEWS.md
/usr/lib64/R/library/pkgbuild/R/pkgbuild
/usr/lib64/R/library/pkgbuild/R/pkgbuild.rdb
/usr/lib64/R/library/pkgbuild/R/pkgbuild.rdx
/usr/lib64/R/library/pkgbuild/help/AnIndex
/usr/lib64/R/library/pkgbuild/help/aliases.rds
/usr/lib64/R/library/pkgbuild/help/paths.rds
/usr/lib64/R/library/pkgbuild/help/pkgbuild.rdb
/usr/lib64/R/library/pkgbuild/help/pkgbuild.rdx
/usr/lib64/R/library/pkgbuild/html/00Index.html
/usr/lib64/R/library/pkgbuild/html/R.css
/usr/lib64/R/library/pkgbuild/tests/build-tools.R
/usr/lib64/R/library/pkgbuild/tests/testthat.R
/usr/lib64/R/library/pkgbuild/tests/testthat/_snaps/build.md
/usr/lib64/R/library/pkgbuild/tests/testthat/_snaps/compiler.md
/usr/lib64/R/library/pkgbuild/tests/testthat/_snaps/exclude.md
/usr/lib64/R/library/pkgbuild/tests/testthat/_snaps/style.md
/usr/lib64/R/library/pkgbuild/tests/testthat/_snaps/utils.md
/usr/lib64/R/library/pkgbuild/tests/testthat/fixtures/testDummy_0.1.tar.gz
/usr/lib64/R/library/pkgbuild/tests/testthat/fixtures/testWithSrc_0.1.tar.gz
/usr/lib64/R/library/pkgbuild/tests/testthat/fixtures/xxx.gz
/usr/lib64/R/library/pkgbuild/tests/testthat/fixtures/xxx.tar.gz
/usr/lib64/R/library/pkgbuild/tests/testthat/fixtures/xxx.zip
/usr/lib64/R/library/pkgbuild/tests/testthat/test-archives.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-build-process.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-build.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-build_tools.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-c-registration.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-compile_dll.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-compiler-flags.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-compiler.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-exclude.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-find-package-root.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-rtools.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-style.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-utils.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-withr.R
/usr/lib64/R/library/pkgbuild/tests/testthat/testDummy/DESCRIPTION
/usr/lib64/R/library/pkgbuild/tests/testthat/testDummy/NAMESPACE
/usr/lib64/R/library/pkgbuild/tests/testthat/testDummy/R/a.R
/usr/lib64/R/library/pkgbuild/tests/testthat/testDummy/R/b.R
/usr/lib64/R/library/pkgbuild/tests/testthat/testInstDoc/DESCRIPTION
/usr/lib64/R/library/pkgbuild/tests/testthat/testInstDoc/NAMESPACE
/usr/lib64/R/library/pkgbuild/tests/testthat/testInstDoc/R/a.R
/usr/lib64/R/library/pkgbuild/tests/testthat/testInstDoc/R/b.R
/usr/lib64/R/library/pkgbuild/tests/testthat/testInstDoc/inst/doc/keep.me
/usr/lib64/R/library/pkgbuild/tests/testthat/testInstDoc/vignettes/test.Rmd
/usr/lib64/R/library/pkgbuild/tests/testthat/testWithSrc/DESCRIPTION
/usr/lib64/R/library/pkgbuild/tests/testthat/testWithSrc/NAMESPACE
/usr/lib64/R/library/pkgbuild/tests/testthat/testWithSrc/R/a.R
/usr/lib64/R/library/pkgbuild/tests/testthat/testWithSrc/R/b.R
/usr/lib64/R/library/pkgbuild/tests/testthat/testWithSrc/src/add1.c
