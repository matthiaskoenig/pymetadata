# COMBINE archives

A [COMBINE archive](https://combinearchive.org/) (OMEX, *Open Modeling EXchange format*) bundles everything belonging to a modeling study into a single ZIP file: models, simulation experiments, data, figures and documentation. What makes it more than a ZIP file is the `manifest.xml` at its root, which lists every file together with the format it is in:

```xml
<omexManifest xmlns="http://identifiers.org/combine.specifications/omex-manifest">
  <content location="." format="http://identifiers.org/combine.specifications/omex"/>
  <content location="./manifest.xml" format="http://identifiers.org/combine.specifications/omex-manifest"/>
  <content location="./model.xml" format="http://identifiers.org/combine.specifications/sbml" master="false"/>
</omexManifest>
```

Formats are identifiers.org URIs rather than file extensions, so a consumer knows that `./model.xml` is SBML without having to guess from the suffix. The `master` attribute marks the entry a tool should open first.

`pymetadata` maps this onto three classes:

| class | purpose |
| --- | --- |
| `Omex` | the archive itself; reading, writing and the files it contains |
| `Manifest` | the list of entries, i.e., the `manifest.xml` |
| `ManifestEntry` | a single file with its `location`, `format` and `master` flag |

## Reading an archive

An archive is read from a path, from a directory or directly from a URL:

```python
from pathlib import Path
from pymetadata.omex import Omex

omex = Omex.from_omex(Path("archive.omex"))
print(omex)
```

```python
omex = Omex.from_url(
    "https://github.com/matthiaskoenig/canagliflozin-model/releases/download/0.7.0/canagliflozin_model.omex"
)
```

Reading extracts the archive into a temporary directory, so the content can be inspected without unpacking it by hand. `Omex.get_path(location)` returns the path of a single entry, which is what you pass on to a model reader:

```python
model_path = omex.get_path("./model.xml")
```

Encrypted archives can be opened by passing the password; writing encrypted archives is not supported:

```python
omex = Omex.from_omex(Path("archive.omex"), password=b"secret")
```

To check whether a file is a COMBINE archive at all, use `Omex.is_omex(path)`.

## Working with the manifest

The manifest behaves like a mapping keyed by location:

```python
print(len(omex.manifest))  # number of entries
print("./model.xml" in omex.manifest)
entry = omex.manifest["./model.xml"]
print(entry.format, entry.master)
```

Locations are normalized to relative paths starting with `./`. An entry given as `model/model1.xml` is stored as `./model/model1.xml`, so lookups are predictable.

Entries can be selected by format, which avoids matching format URIs by hand:

```python
for entry in omex.entries_by_format("sbml"):
    print(entry.location)
```

`entries_by_format` understands `sbml`, `sedml` and `sbgn` across all their level and version variants; `ManifestEntry.is_sbml()`, `is_sedml()` and `is_sbgn()` answer the same question for a single entry.

## Creating an archive

An archive can be assembled entry by entry. Every file needs a `ManifestEntry` describing where it goes and what it is:

```python
from pathlib import Path
from pymetadata.omex import EntryFormat, ManifestEntry, Omex

omex = Omex()
omex.add_entry(
    entry_path=Path("model.xml"),
    entry=ManifestEntry(
        location="./model.xml", format=EntryFormat.SBML_L3V2, master=True
    ),
)
omex.add_entry(
    entry_path=Path("README.md"),
    entry=ManifestEntry(location="./README.md", format=EntryFormat.MARKDOWN),
)
omex.to_omex(Path("archive.omex"))
```

Files are copied when they are added, so later changes to the source file do not affect the archive. Adding a second entry for an existing location replaces the first one and logs a warning.

For a directory that already has the intended layout, `from_directory` creates the archive in one step and guesses the format of every file from its suffix:

```python
omex = Omex.from_directory(Path("./study"))
omex.to_omex(Path("study.omex"))
```

If the directory contains a `manifest.xml`, the entries listed there are reused and only files missing from it are guessed. SED-ML files added this way get `master=True`, since they are the entry point of a simulation study.

## Formats

`EntryFormat` is an enum of the format URIs, covering the COMBINE specifications (SBML down to the level/version, SED-ML, CellML, SBGN, BioPAX, OMEX metadata, FROG results) and a large list of media types for everything else. Two helpers translate between suffixes and URIs:

```python
from pathlib import Path
from pymetadata.omex import Omex

Omex.guess_format(Path("model.xml"))  # from the file suffix and content
Omex.lookup_format("sbml")  # from a format key
```

`guess_format` looks at the start of `.xml` files to tell SBML, SED-ML, CellML and COPASI apart, so an `.xml` file is not classified as plain XML when it is in fact a model. For every other file the suffix decides.

## Cleaning up

Reading an archive extracts it into a temporary directory. Using the archive as a context manager removes that directory when the block is left, which matters when many archives are processed in one run:

```python
with Omex.from_omex(Path("archive.omex")) as omex:
    model_path = omex.get_path("./model.xml")
    ...
```

## Writing back out

```python
omex.to_omex(Path("archive.omex"))  # write a COMBINE archive
omex.to_directory(Path("./unpacked"))  # extract, including the manifest.xml
```

`to_directory` writes the `manifest.xml` next to the files, so the result is a valid input for `Omex.from_directory` again.

## Examples

Runnable examples are in [`examples/omex`](https://github.com/matthiaskoenig/pymetadata/tree/develop/examples/omex) of the repository:

```bash
python examples/omex/omex.py           # read, extract, create, write
python examples/omex/omex_from_url.py  # read an archive from a url
```

The full API, generated from the docstrings, is in the [API reference](api/omex.md).

## References

The COMBINE archive and the OMEX format are described in:

> Bergmann FT, Adams R, Moodie S, Cooper J, Glont M, Golebiewski M, Hucka M, Laibe C, Miller AK, Nickerson DP, Olivier BG, Rodriguez N, Sauro HM, Scharm M, Soiland-Reyes S, Waltemath D, Yvon F, Le Novère N. **COMBINE archive and OMEX format: one file to share all information to reproduce a modeling project.** *BMC Bioinformatics.* 2014 Dec 14;15(1):369. doi: [10.1186/s12859-014-0369-z](https://doi.org/10.1186/s12859-014-0369-z), PMID: [25494900](https://pubmed.ncbi.nlm.nih.gov/25494900/)

> Bergmann FT, Rodriguez N, Le Novère N. **COMBINE Archive Specification Version 1.** *J Integr Bioinform.* 2015 Sep 4;12(2):261. doi: [10.2390/biecoll-jib-2015-261](https://doi.org/10.2390/biecoll-jib-2015-261), PMID: [26528559](https://pubmed.ncbi.nlm.nih.gov/26528559/)

Further resources:

- [COMBINE archive](https://combinearchive.org/) — specifications and tooling
- [COMBINE](https://co.mbine.org/) — the standards this archive format ties together
- [identifiers.org combine.specifications](https://registry.identifiers.org/registry/combine.specifications) — the format URIs used in the manifest
