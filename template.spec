%global         debug_package   %{nil}
%global         lowercase_name  [lowercase_name]

Name:           [name]
Epoch:          1
Version:        [version]
Release:        [release]
Summary:        It's time to ditch Skype and TeamSpeak

License:        Custom
URL:            https://discordapp.com/
Source0:        [url]#/%{name}-%{version}.tar.gz

BuildArch:      x86_64
Requires:       alsa-lib
Requires:       GConf2
Requires:       glibc
Requires:       libappindicator
Requires:       libnotify
Requires:       libstdc++
Requires:       libXScrnSaver
Requires:       libXtst
Requires:       nspr
Requires:       nss
AutoReqProv:    no

%description
All-in-one voice and text chat for gamers that's free, secure, and works on both your desktop and phone.
Stop paying for TeamSpeak servers and hassling with Skype.
Simplify your life.


%prep
%autosetup -n %{name}


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/{%{lowercase_name},applications,pixmaps}
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}
cp -R $RPM_BUILD_DIR/%{name}/* $RPM_BUILD_ROOT/%{_datadir}/%{lowercase_name}
cp $RPM_BUILD_DIR/%{name}/*.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{lowercase_name}.png
cp $RPM_BUILD_DIR/%{name}/*.desktop $RPM_BUILD_ROOT/%{_datadir}/applications
rm $RPM_BUILD_ROOT/%{_datadir}/%{lowercase_name}/postinst.sh
ln -s %{_datadir}/%{lowercase_name}/%{name} $RPM_BUILD_ROOT/%{_bindir}


%files
%{_bindir}/%{name}
%{_datadir}/%{lowercase_name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
