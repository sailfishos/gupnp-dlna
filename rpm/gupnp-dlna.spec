Name:          gupnp-dlna
Version:       0.10.2
Release:       2%{?dist}
Summary:       A collection of helpers for building UPnP AV applications

Group:         System Environment/Libraries
License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       %{name}-%{version}.tar.gz

BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel >= 1.36
BuildRequires: gssdp-devel
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: gupnp-devel
BuildRequires: gupnp-av-devel
BuildRequires: libxml2-devel
BuildRequires: vala-devel
BuildRequires: vala-tools

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-dlna is a collection of helpers for building DLNA (Digital 
Living Network Alliance) compliant applications using GUPnP.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Contains libraries and header files for developing applications that 
use %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%autogen --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README TODO
%{_bindir}/gupnp-dlna*
%{_libdir}/lib*.so.*
%{_libdir}/gupnp-dlna/libgstreamer.so
%{_libdir}/girepository-1.0/GUPnPDLNA-2.0.typelib
%{_libdir}/girepository-1.0/GUPnPDLNAGst-2.0.typelib
%{_datadir}/%{name}-2.0/

%files devel
%{_libdir}/lib*.so
%{_libdir}/gupnp-dlna/libgstreamer.so
%{_libdir}/pkgconfig/%{name}-2.0.pc
%{_libdir}/pkgconfig/%{name}-gst-2.0.pc
%{_libdir}/pkgconfig/%{name}-metadata-2.0.pc
%{_datadir}/gir-1.0/GUPnPDLNA-2.0.gir
%{_datadir}/gir-1.0/GUPnPDLNAGst-2.0.gir
%{_includedir}/%{name}-2.0/
%{_datadir}/vala/vapi/gupnp-dlna-2.0.deps
%{_datadir}/vala/vapi/gupnp-dlna-2.0.vapi
%{_datadir}/vala/vapi/gupnp-dlna-gst-2.0.deps
%{_datadir}/vala/vapi/gupnp-dlna-gst-2.0.vapi
