VERSION=1.3.0
clean:
	rm -f PyJWT-${VERSION}.tar.gz
	rm -fr RHBUILD
	rm -fr PyJWT-${VERSION}
centos:
	make clean
	wget https://pypi.python.org/packages/source/P/PyJWT/PyJWT-${VERSION}.tar.gz
	mkdir -p RHBUILD/BUILD
	mkdir -p RHBUILD/RPMS
	mkdir -p RHBUILD/SOURCES
	tar -zxf PyJWT-${VERSION}.tar.gz
	mv PyJWT-${VERSION} RHBUILD/SOURCES/python-pyjwt-${VERSION}
	(cd RHBUILD/SOURCES; tar -zcf python-pyjwt-${VERSION}.tar.gz python-pyjwt-${VERSION})
	rpmbuild --define "_topdir $(CURDIR)/RHBUILD" -ba python-pyjwt.spec
	
