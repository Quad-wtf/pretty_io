try:
    try:
        from setuptools import setup, find_packages
    except ImportError:
        import os
        install = input("setuptools is not installed. Do you want to install it? (y/n) ")
        if install.lower() == 'y':
            print("Installing setuptools...")
            os.system("pip install setuptools")
            os.system("pip cache purge")
            os.system("cls" if os.name == "nt" else "clear")
        if install.lower() == 'n':
            print("Abort.")
            exit(1)
        if not install:
            print("Abort.")
            exit(1)


    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setup( # pyright: ignore[reportPossiblyUnboundVariable]
        name="pretty-io",
        version="1.0.1",
        author="Quad, Wtf",
        author_email="quad.business.inquirities@gmail.com",
        description="A Python module for pretty terminal input/output with ANSI styling",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/Quad-wtf/pretty-io",
        packages=find_packages(), # pyright: ignore[reportPossiblyUnboundVariable]
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: System :: Shells",
            "Topic :: Terminals",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
        ],
        python_requires=">=3.6",
        keywords="terminal, ansi, colors, styling, input, output, cli",
        project_urls={
            "Bug Reports": "https://github.com/Quad-wtf/pretty-io/issues",
            "Source": "https://github.com/Quad-wtf/pretty-io",
        },
    )

except Exception as e:
    import os
    import sys
    
    def pause():
        try:
            # Windows
            if os.name == 'nt':
                os.system('pause')
            # Linux / macOS
            else:
                input("Press Enter to continue...")
        except KeyboardInterrupt:
            sys.exit(0)

    print(e)
    pause()
