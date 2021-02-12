import sys
import xml.etree.ElementTree as ET

ENTRY = "* [ ] [`{0}`](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text={0}&expand=100)"


def main(group_name):
    root = ET.parse("x86-intel.xml").getroot()
    insts = [i for i in root.findall("intrinsic")]
    requestedintrins = []
    for i in insts:
        d = i.find("CPUID")
        if d is None:
            continue
        if d.text == group_name:
            requestedintrins.append(i)

    for intr in requestedintrins:
        n = intr.attrib["name"]
        if n is None:
            continue
        x = ENTRY.format(n)
        print(x)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        group_name = sys.argv[1]
        main(group_name)
    else:
        print("You need to give instruction set name to export it's data.")
        print("ex: python instexport.py AVX512BW")
