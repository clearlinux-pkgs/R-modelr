#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-modelr
Version  : 0.1.4
Release  : 25
URL      : https://cran.r-project.org/src/contrib/modelr_0.1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/modelr_0.1.4.tar.gz
Summary  : Modelling Functions that Work with the Pipe
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : R-backports
BuildRequires : R-broom
BuildRequires : R-cli
BuildRequires : R-dplyr
BuildRequires : R-generics
BuildRequires : R-glue
BuildRequires : R-lme4
BuildRequires : R-rstanarm
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : R-tidyselect
BuildRequires : buildreq-R

%description
# modelr <img src="man/figures/logo.png" align="right" />
<!-- badges: start -->

%prep
%setup -q -c -n modelr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556476805

%install
export SOURCE_DATE_EPOCH=1556476805
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library modelr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library modelr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library modelr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc modelr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/modelr/DESCRIPTION
/usr/lib64/R/library/modelr/INDEX
/usr/lib64/R/library/modelr/Meta/Rd.rds
/usr/lib64/R/library/modelr/Meta/data.rds
/usr/lib64/R/library/modelr/Meta/features.rds
/usr/lib64/R/library/modelr/Meta/hsearch.rds
/usr/lib64/R/library/modelr/Meta/links.rds
/usr/lib64/R/library/modelr/Meta/nsInfo.rds
/usr/lib64/R/library/modelr/Meta/package.rds
/usr/lib64/R/library/modelr/NAMESPACE
/usr/lib64/R/library/modelr/NEWS.md
/usr/lib64/R/library/modelr/R/modelr
/usr/lib64/R/library/modelr/R/modelr.rdb
/usr/lib64/R/library/modelr/R/modelr.rdx
/usr/lib64/R/library/modelr/data/Rdata.rdb
/usr/lib64/R/library/modelr/data/Rdata.rds
/usr/lib64/R/library/modelr/data/Rdata.rdx
/usr/lib64/R/library/modelr/help/AnIndex
/usr/lib64/R/library/modelr/help/aliases.rds
/usr/lib64/R/library/modelr/help/figures/logo.png
/usr/lib64/R/library/modelr/help/modelr.rdb
/usr/lib64/R/library/modelr/help/modelr.rdx
/usr/lib64/R/library/modelr/help/paths.rds
/usr/lib64/R/library/modelr/html/00Index.html
/usr/lib64/R/library/modelr/html/R.css
/usr/lib64/R/library/modelr/tests/testthat.R
/usr/lib64/R/library/modelr/tests/testthat/test-cross-validate.R
/usr/lib64/R/library/modelr/tests/testthat/test-data-grid.R
/usr/lib64/R/library/modelr/tests/testthat/test-formulas.R
/usr/lib64/R/library/modelr/tests/testthat/test-geom-ref-line.R
/usr/lib64/R/library/modelr/tests/testthat/test-model-matrix.R
/usr/lib64/R/library/modelr/tests/testthat/test-na-warn.R
/usr/lib64/R/library/modelr/tests/testthat/test-predictions.R
/usr/lib64/R/library/modelr/tests/testthat/test-resample-partition.R
/usr/lib64/R/library/modelr/tests/testthat/test-resampling.R
/usr/lib64/R/library/modelr/tests/testthat/test-residuals.R
/usr/lib64/R/library/modelr/tests/testthat/test-response_var.R
/usr/lib64/R/library/modelr/tests/testthat/test-seq-range.R
/usr/lib64/R/library/modelr/tests/testthat/test-typical.R
