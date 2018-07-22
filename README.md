# conan-winflexbison
A [Conan](https://conan.io) package recipe for the [winflexbison](https://github.com/lexxmark/winflexbison). Requires Visual Studio 2013 or superior.

Example files inside `test_package` folder are taken from [meyerd/flex-bison-example](https://github.com/meyerd/flex-bison-example).

Usage:
```bash
$ conan remote add jgsogo-conan-packages https://api.bintray.com/conan/jgsogo/conan-packages
$ conan install winflexbison/2.5.14@jgsogo/stable
```

Build status:

<table>
    <thead>
        <tr>
            <th></th>
            <th>Windows</th>
        </tr>
    </thead>
    <tr>
        <td>master</td>
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-winflexbison"><img src="https://ci.appveyor.com/api/projects/status/sbu2sohg582h8252/branch/master" alt="Build status master-windows"/></a></td>
    </tr>
    <tr>
        <td>stable/2.5.14</td>
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-winflexbison"><img src="https://ci.appveyor.com/api/projects/status/sbu2sohg582h8252/branch/stable/2.5.14" alt="Build status master-windows"/></a></td>
    </tr>
</table>


