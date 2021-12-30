#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pkgbuild
Version  : 1.3.1
Release  : 41
URL      : https://cran.r-project.org/src/contrib/pkgbuild_1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pkgbuild_1.3.1.tar.gz
Summary  : Find Tools Needed to Build R Packages
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-callr
Requires: R-cli
Requires: R-crayon
Requires: R-desc
Requires: R-prettyunits
Requires: R-rprojroot
Requires: R-withr
BuildRequires : R-R6
BuildRequires : R-callr
BuildRequires : R-cli
BuildRequires : R-crayon
BuildRequires : R-desc
BuildRequires : R-prettyunits
BuildRequires : R-rprojroot
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
needed to build R packages on various platforms and ensures the PATH is
  configured appropriately so R can use them.

%prep
%setup -q -c -n pkgbuild
cd %{_builddir}/pkgbuild

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640017357

%install
export SOURCE_DATE_EPOCH=1640017357
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgbuild
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgbuild
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgbuild
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pkgbuild || :


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
/usr/lib64/R/library/pkgbuild/tests/testthat/fixtures/testDummy_0.1.tar.gz
/usr/lib64/R/library/pkgbuild/tests/testthat/fixtures/testWithSrc_0.1.tar.gz
/usr/lib64/R/library/pkgbuild/tests/testthat/fixtures/xxx.gz
/usr/lib64/R/library/pkgbuild/tests/testthat/fixtures/xxx.tar.gz
/usr/lib64/R/library/pkgbuild/tests/testthat/fixtures/xxx.zip
/usr/lib64/R/library/pkgbuild/tests/testthat/test-archives.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-build-process.r
/usr/lib64/R/library/pkgbuild/tests/testthat/test-build.r
/usr/lib64/R/library/pkgbuild/tests/testthat/test-build_tools.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-c-registration.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-compile_dll.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-compiler.R
/usr/lib64/R/library/pkgbuild/tests/testthat/test-rtools.r
/usr/lib64/R/library/pkgbuild/tests/testthat/testDummy/DESCRIPTION
/usr/lib64/R/library/pkgbuild/tests/testthat/testDummy/NAMESPACE
/usr/lib64/R/library/pkgbuild/tests/testthat/testDummy/R/a.r
/usr/lib64/R/library/pkgbuild/tests/testthat/testDummy/R/b.r
/usr/lib64/R/library/pkgbuild/tests/testthat/testWithSrc/DESCRIPTION
/usr/lib64/R/library/pkgbuild/tests/testthat/testWithSrc/NAMESPACE
/usr/lib64/R/library/pkgbuild/tests/testthat/testWithSrc/R/a.r
/usr/lib64/R/library/pkgbuild/tests/testthat/testWithSrc/R/b.r
/usr/lib64/R/library/pkgbuild/tests/testthat/testWithSrc/src/add1.c
