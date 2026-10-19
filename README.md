# fgu-workflow-plans-test

A Render Workflows test service with one task on each kind of plan:

- `flex_task` has no plan, so it registers on the default plan (Flex, usage-based).
- `flat_task` uses the `2c-4g` flat-rate plan.

Build command: `pip install -r requirements.txt`
Run command: `python main.py`
