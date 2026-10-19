from render_sdk import Workflows

app = Workflows()


def burn(n: int) -> int:
  # Busy work so each run uses measurable CPU time.
  return sum(i * i for i in range(n))


# No plan: the task registers on the default plan (Flex, usage-based).
@app.task
def flex_task(n: int) -> int:
  return burn(n)


# Flat-rate plan: billed per instance-hour.
@app.task(plan="2c-4g")
def flat_task(n: int) -> int:
  return burn(n)


if __name__ == "__main__":
  app.start()
