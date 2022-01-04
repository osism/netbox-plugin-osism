from setuptools import setup

setup(
    name='netbox_plugin_osism',
    version='0.0.1',
    description='NetBox Plugin OSISM',
    long_description='Netbox Plugin OSISM',
    url='https://github.com/osism/netbox-plugin-osism',
    download_url='https://github.com/osism/netbox-plugin-osism',
    author='OSISM GmbH',
    author_email='info@osism.tech',
    maintainer='OSISM GmbH',
    maintainer_email='info@osism.tech',
    install_requires=[],
    packages=['netbox_plugin_osism'],
    package_data={
        'netbox_plugin_osism':
            ['templates/netbox_plugin_osism/*.html']
    },
    include_package_data=True,
    zip_safe=False,
    platforms=['Any'],
    keywords=['netbox', 'netbox-plugin'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],
)
