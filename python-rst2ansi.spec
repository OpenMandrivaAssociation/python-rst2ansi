Name:		python-rst2ansi
Version:	0.1.5
Release:	5
Source0:	https://files.pythonhosted.org/packages/source/r/rst2ansi/rst2ansi-%{version}.tar.gz
Summary:	A rst converter to ansi-decorated console output
URL:		https://pypi.org/project/rst2ansi/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%patchlist
https://github.com/Snaipe/python-rst2ansi/commit/1b1b963804bcc87a7187d07c3943585d9385ea92.patch
https://github.com/Snaipe/python-rst2ansi/commit/c6f390b45be689a5760060c990e3fe10f502e671.patch
https://github.com/Snaipe/python-rst2ansi/commit/81758ed43336833a77deb2a7c751abf362ff8761.patch
https://github.com/Snaipe/python-rst2ansi/commit/3728e16f8b8b1dc338e5df90ba2c4a93ee054b3f.patch

%description
A rst converter to ansi-decorated console output

%files
%{_bindir}/rst2ansi
%{py_sitedir}/rst2ansi
%{py_sitedir}/rst2ansi-*.*-info
