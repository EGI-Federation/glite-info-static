# glite-info-static

This application is an information provider that generates information in LDIF
format from combining an LDIF template with configuration values.

BDII documentation is available at
[gridinfo documentation site](https://gridinfo-documentation.readthedocs.io/).

## Installing from packages

### On RHEL-based systems

On RHEL-based systems, it's possible to install packages from [EGI UMD
packages](https://go.egi.eu/umd). The packages are build from this repository,
and tested to work with other components part of the Unified Middleware
Distribution.

## Building packages

A Makefile allowing to build source tarball and packages is provided.

### Building a RPM

The required build dependencies are:

- rpm-build
- make
- rsync
- python
- python-setuptools

```shell
# Checkout tag to be packaged
$ git clone https://github.com/EGI-Foundation/glite-info-static.git
$ cd glite-info-static
$ git checkout X.X.X
# Building in a container
$ docker run --rm -v $(pwd):/source -it quay.io/centos/centos:7
[root@8a9d60c61f42 /]# cd /source
[root@8a9d60c61f42 /]# yum install -y rpm-build yum-utils
[root@8a9d60c61f42 /]# yum-builddep -y glite-info-static.spec
[root@8a9d60c61f42 /]# make rpm
```

The RPM will be available into the `build/RPMS` directory.

## Installing from source

This procedure is not recommended for production deployment, please consider
using packages.

* Build dependencies: None
* Runtime dependencies: openldap, python

Get the source by cloning this repository and do a `make install`.

## Usage

Edit the corresponding `.cfg` file for your module and fill in the parameters
needed. Invoke `glite-info-static` without arguments for help if needed.
The resulting LDIF files will be created in the `output/` directory.

## Core Structure

* glite-info-static: The main script to invoke
* README.md: This file

## Module Structure

  [name].1.cfg                  Config file to be filled out by the sysadmin
  [name]/
    [name].glue.ifc             Interface to comply with GLUE standard
    [name].wlcg.ifg             Interface to comply with WLCG standard
    [name].glue1.tpl            Template to create an LDIF for GLUE 1.3
    [name].glue2.tpl            Template to create an LDIF for GLUE 2.0

## TODO

None. :)

Do you have more suggestions?
Open an [issue](https://github.com/EGI-Federation/glite-info-static/issues/new)!

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in
    - [CHANGELOG](CHANGELOG)
    - [glite-info-static.spec](glite-info-static.spec)
- Once the PR has been merged tag and release a new version in GitHub
  - Packages will be built using GitHub Actions and attached to the release page

## History

This work started under the EGEE project, and was hosted and maintained for a
long time by CERN. This is now hosted here on GitHub, maintained by the BDII
community with support of members of the EGI Federation.
