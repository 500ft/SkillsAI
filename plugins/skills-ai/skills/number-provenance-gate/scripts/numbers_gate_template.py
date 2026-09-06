#!/usr/bin/env python3
"""Template for a document-vs-artifact numbers gate. Copy into <repo>/tests/, then:

  1. implement expected_values() -> {label: float} by COMPUTING from the committed artifact
  2. list DOCS (paths of every document that quotes those numbers)
  3. run:  python -m unittest test_numbers          (gate)
           python test_numbers.py --negative-control (perturbs one expected value; gate must FAIL)

Historical-marker lines are exempt from the superseded-value check, so "vs the prior 129.76 g"
is allowed while "nominal mass 129.76 g" is not once 129.76 is superseded.
"""
import re, sys, unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]      # adjust if the test lives deeper
DOCS = [                                        # every document that quotes the numbers
    # "README.md", "docs/results.md",
]
SUPERSEDED = [                                  # values that were once current and no longer are
    # 129.76, 149.5, 155.0,
]
TOL = 0.006                                     # half a unit in the last printed decimal
UNIT = r"(?:g\b|gf\b|mm\b|Hz\b|%|\|)"           # what follows a number for it to count
HISTORICAL = re.compile(r"\b(prior|previous(ly)?|was|were|formerly|superseded|corrected|used to|earlier|before the|old)\b", re.I)

def expected_values() -> dict:
    """COMPUTE from the committed artifact. Never type constants here."""
    raise NotImplementedError("compute expected values from the committed source, e.g. run budget.py or read the CSV")

def numbers_in(text: str, skip_historical: bool) -> set:
    found = set()
    for line in text.splitlines():
        if skip_historical and HISTORICAL.search(line):
            continue
        for m in re.finditer(rf"(?<![\w.])(\d+(?:\.\d+)?)\s*{UNIT}", line):
            found.add(float(m.group(1)))
    return found

class NumbersGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exp = expected_values()

    def _read(self, rel): return (REPO / rel).read_text(encoding="utf-8")

    def test_each_document_states_every_current_value(self):
        for rel in DOCS:
            present = numbers_in(self._read(rel), skip_historical=False)
            for label, v in self.exp.items():
                self.assertTrue(any(abs(v - p) < TOL for p in present),
                                f"{rel} does not state {label} = {v:g}")

    def test_no_document_asserts_a_superseded_value(self):
        for rel in DOCS:
            present = numbers_in(self._read(rel), skip_historical=True)
            for s in SUPERSEDED:
                self.assertFalse(any(abs(s - p) < TOL for p in present),
                                 f"{rel} still asserts superseded value {s:g} as current")

if __name__ == "__main__":
    if "--negative-control" in sys.argv:
        sys.argv.remove("--negative-control")
        _orig = expected_values
        def expected_values():                   # perturb one value; the gate must now FAIL
            d = _orig(); k = next(iter(d)); d[k] = d[k] * 1.1 + 1.0; return d
        globals()["expected_values"] = expected_values
        r = unittest.main(exit=False).result
        ok = not r.wasSuccessful()
        print("NEGATIVE CONTROL", "PASS (gate failed as required)" if ok else "FAIL (gate is vacuous)")
        sys.exit(0 if ok else 1)
    unittest.main()
