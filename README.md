[![Build Status](https://travis-ci.org/uilianries/conan-bison.svg?branch=release/3.0.4)](https://travis-ci.org/uilianries/conan-bison)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-red.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![Download](https://api.bintray.com/packages/uilianries/conan/bison%3Aconan/images/download.svg) ](https://bintray.com/uilianries/conan/bison%3Aconan/_latestVersion)
[![Conan.io](https://img.shields.io/badge/conan.io-bison%2F3.0.4-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/bison/3.0.4/uilianries/stable)

# conan-bison

![Conan Bison](conan-bison.png)

**Bison** is a general-purpose parser generator that converts an annotated context-free grammar into a deterministic LR or generalized LR (GLR) parser employing LALR(1) parser tables

[Conan.io](https://conan.io) package for [Bison](https://www.gnu.org/software/bison/) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/uilianries/conan/bison%3Auilianries).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload bison/3.0.4@uilianries/stable --all

## Reuse the packages

### Basic setup

    $ conan install bison/3.0.4@uilianries/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    bison/3.0.4@uilianries/stable

    [options]
    bison:enable_yacc=True # False

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

### Constraints

Bison is **NOT** supported on Windows. If you are looking for it, see [here](https://sourceforge.net/projects/winflexbison/).

### License
[GPL-3.0](LICENSE)
