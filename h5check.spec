Summary:	h5check: the HDF5 Format Checker
Summary(pl.UTF-8):	h5check - narzędzie do sprawdzania formatu plików HDF5
Name:		h5check
Version:	2.0.1
Release:	1
Group:		Applications/File
License:	BSD-like, changed sources must be marked
Source0:	http://www.hdfgroup.org/ftp/HDF5/tools/h5check/src/%{name}-%{version}.tar.gz
# Source0-md5:	0fd33d2058af2e081737b5993f6887e8
URL:		http://www.hdfgroup.org/products/hdf5_tools/h5check.html
BuildRequires:	hdf5-devel
BuildRequires:	szip-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HDF5 Format Checker, h5check, is a validation tool for verifying
that an HDF5 file is encoded according to the HDF File Format
Specification. Its purpose is to ensure data model integrity and
long-term compatibility between evolving versions of the HDF5 library.

%description -l pl.UTF-8
h5check (HDF5 Format Checker) to narzędzie do kontroli poprawności,
sprawdzające czy plik HDF5 jest zakodowany zgodnie ze specyfikacją
formatu HDF. Celem jest zapewnienie integralności modelu danych i
długoterminowa kompatybilność między ewolującymi wersjami biblioteki
HDF5.

%prep
%setup -q

%build
%configure

%{__make} \
	HDF5_USE_SHLIB=yes

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING doc/{HISTORY,RELEASE}.txt doc/h5check.pdf
%attr(755,root,root) %{_bindir}/h5check
