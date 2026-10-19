import time

from render_sdk import Workflows

app = Workflows()


def burn(seconds: float) -> int:
  # Keep one core busy for the given number of seconds.
  deadline = time.monotonic() + seconds
  loops = 0
  while time.monotonic() < deadline:
    loops += 1
  return loops


# No plan: the task registers on the default plan (Flex, usage-based).
# Flex charges for CPU-seconds and memory GB-seconds, so this task also holds
# memory while it runs.
@app.task
def flex_task(seconds: float, memory_gib: float = 0) -> int:
  # Fill with a non-zero byte so every page is resident, not lazily zeroed.
  held = bytearray(b"\x01") * int(memory_gib * (1 << 30))
  loops = burn(seconds)
  del held
  return loops


# Flat-rate plan: billed per instance-hour of wall-clock time.
@app.task(plan="2c-4g")
def flat_task(seconds: float) -> int:
  return burn(seconds)


if __name__ == "__main__":
  app.start()
