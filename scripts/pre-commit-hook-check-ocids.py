#!/usr/bin/env python

import sys
import re
import click

@click.command()
@click.argument("filenames", nargs=-1)
def main(filenames) -> int:
  retcode = 0
  for filename in filenames:
    with open(filename, "rb") as inputfile:
      for i, line in enumerate(inputfile):
        if (
                re.search(
                  rb"ocid[123]\.[a-z1-9A-Z]*\.oc\d\.[a-z1-9A-Z]*\.[a-z1-9A-Z]+",
                  line,
                )
                is not None
        ):
          print(
            f"OCID found in {filename}:{i + 1}",
          )
          retcode = 1

  sys.exit(retcode)

if __name__ == "__main__":
  main()