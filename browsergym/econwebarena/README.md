# EconWebArena × BrowserGym

This package provides an integration of the [EconWebArena](https://econwebarena.github.io/) benchmark with [BrowserGym](https://github.com/ServiceNow/BrowserGym).

## Setup

- Install the package:

  ```bash
  pip install browsergym-econwebarena
  ```

- Run inference on a sample task:

  ```bash
  python demo_agent/run_demo.py --model_name gpt-4.1 --task_name econwebarena.1 --use_axtree True --use_screenshot True
  ```
