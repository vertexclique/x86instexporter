# Intel x86/x86_64 instruction set exporter

This program exports instructions based on the set names received from Intel Intrinsics Guide webpage.
XML is downloaded from the page, it can be updated whenever a new set lands.
It exports the list as markdown format to track implementation in checklist format.

## Usage

```bash
$ python instexport.py <SETNAME>
```

Like:
```bash
$ python instexport.py AVX512BW
```

For any update you see, please open a PR.

## License
Unlicense