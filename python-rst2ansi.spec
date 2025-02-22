Name:		python-rst2ansi
Version:	0.1.5
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/rst2ansi/rst2ansi-%{version}.tar.gz
Summary:	A rst converter to ansi-decorated console output
URL:		https://pypi.org/project/rst2ansi/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
A rst converter to ansi-decorated console output

%files
%{_bindir}/rst2ansi
%{py_sitedir}/rst2ansi
%{py_sitedir}/rst2ansi-*.*-info
