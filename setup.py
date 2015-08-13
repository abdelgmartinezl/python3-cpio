from distutils.core import setup
import cpioarchive

setup(name='python3-cpio',
  version=cpioarchive.version(),
  author="Ignacio Vazquez-Abrams",
  author_email="ivazquez@ivazquez.net",
  maintainer="Abdel Gadiel Martinez Lassonde",
  maintainer_email="abdel.g.martinez.l@gmail.com",
  url="https://github.com/ampotty/python3-cpio",
  description="Access to cpio archives",
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Environment :: Console',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: System :: Archiving'
  ],
  py_modules=['cpioarchive'],
  )
