#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-httpclient
Version  : 3.1
Release  : 4
URL      : https://repo1.maven.org/maven2/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.jar
Source0  : https://repo1.maven.org/maven2/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.jar
Source1  : https://repo.maven.apache.org/maven2/commons-httpclient/commons-httpclient/3.0.1/commons-httpclient-3.0.1.jar
Source2  : https://repo.maven.apache.org/maven2/commons-httpclient/commons-httpclient/3.0.1/commons-httpclient-3.0.1.pom
Source3  : https://repo1.maven.org/maven2/commons-httpclient/commons-httpclient/3.0/commons-httpclient-3.0.pom
Source4  : https://repo1.maven.org/maven2/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-httpclient-data = %{version}-%{release}
Requires: mvn-commons-httpclient-license = %{version}-%{release}

%description
Jakarta HttpClient
===========================
Welcome to the HttpClient component of the Jakarta HttpComponents project.

%package data
Summary: data components for the mvn-commons-httpclient package.
Group: Data

%description data
data components for the mvn-commons-httpclient package.


%package license
Summary: license components for the mvn-commons-httpclient package.
Group: Default

%description license
license components for the mvn-commons-httpclient package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-commons-httpclient
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-commons-httpclient/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.0.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.0.1/commons-httpclient-3.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.0.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.0.1/commons-httpclient-3.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.0/commons-httpclient-3.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.0.1/commons-httpclient-3.0.1.jar
/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.0.1/commons-httpclient-3.0.1.pom
/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.0/commons-httpclient-3.0.pom
/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.jar
/usr/share/java/.m2/repository/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-commons-httpclient/LICENSE.txt
