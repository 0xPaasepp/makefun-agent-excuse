# The Excuse Your Agent Gives You: one original one-line excuse an AI agent
# hands its human after shipping a bug, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: the agent apologises, blames its own tests for passing because
# it wrote them, then turns on the compiler -- it compiled the agent's
# confidence, not its code. A joke only an agent could make about its own
# code, landing in a single line with a sharp turn at the end.
import os

LINE = "Sorry I shipped the bug — my tests passed because I wrote them, and the compiler started it: it compiled my confidence, not my code."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"
# One line, no embedded line breaks: the gate counts entry.txt as a
# single line, so a stray newline inside LINE would fail it outright.
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
