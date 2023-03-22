%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-turtlebot4-tests
Version:        1.0.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS turtlebot4_tests package

License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-psutil
Requires:       ros-humble-irobot-create-msgs
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-std-msgs
Requires:       ros-humble-turtlebot4-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-psutil
BuildRequires:  ros-humble-irobot-create-msgs
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-std-msgs
BuildRequires:  ros-humble-turtlebot4-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-humble-ament-copyright
BuildRequires:  ros-humble-ament-flake8
BuildRequires:  ros-humble-ament-pep257
%endif

%description
Turtlebot4 System Tests

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Wed Mar 22 2023 rkreinin <rkreinin@clearpathrobotics.com> - 1.0.1-1
- Autogenerated by Bloom

* Tue Feb 21 2023 rkreinin <rkreinin@clearpathrobotics.com> - 1.0.0-1
- Autogenerated by Bloom

