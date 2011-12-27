Summary:	LV2 Event extension - port-based real-time generic event interface
Summary(pl.UTF-8):	Rozszerzenie LV2 Event - ogólny interfejs zdarzeń czasu rzeczywistego oparty na porcie
Name:		lv2-event
Version:	1.4
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	95f1a04518e592220d06a3665e152d73
URL:		http://lv2plug.in/ns/ext/event/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
Requires:	lv2core >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 Event extension defines a generic time-stamped event port type,
which can be used to create plugins that read and write real-time
events, such as MIDI, OSC, or any other type of event payload. The
type(s) of event supported by a port is defined in the data file for a
plugin.

%description -l pl.UTF-8
Rozszerzenie LV2 Event definiuje ogólny typ portu zdarzeń ze
znacznikami czasu; typ ten może być wykorzystany do tworzenia wtyczek
czytających i zapisujących zdarzenia czasu rzeczywistego, takie jak
MIDI, OSC lub dowolny inny typ zdarzeń. Typy zdarzeń obsługiwanych
przez port są definiowane w pliku danych dla wtyczki.

%package devel
Summary:	Header file for LV2 Event extension
Summary(pl.UTF-8):	Plik nagłówkowy rozszerzenia LV2 Event
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core-devel >= 6.0

%description devel
Header file for LV2 Event extension.

%description devel -l pl.UTF-8
Plik nagłówkowy rozszerzenia LV2 Event.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%dir %{_libdir}/lv2/event.lv2
%{_libdir}/lv2/event.lv2/event.ttl
%{_libdir}/lv2/event.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
%{_libdir}/lv2/event.lv2/event.h
%{_libdir}/lv2/event.lv2/event-helpers.h
%{_includedir}/lv2/lv2plug.in/ns/ext/event
%{_pkgconfigdir}/lv2-lv2plug.in-ns-ext-event.pc
