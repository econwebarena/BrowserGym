# EconWebArena × BrowserGym

This package integrates the [EconWebArena](https://econwebarena.github.io/) benchmark with the [BrowserGym](https://github.com/ServiceNow/BrowserGym) environment, enabling the evaluation of web agents on economic tasks grounded in real-world websites.

## 🔧 Setup

You can install the package either from PyPI or from source:

### Option 1: Install from PyPI (coming soon)

```bash
pip install browsergym-econwebarena
```

### Option 2: Install from source

```bash
git clone https://github.com/econwebarena/BrowserGym.git
cd BrowserGym
git checkout econ-web-arena
make install
```

## 🚀 Running a Demo

To run inference on a sample task, use the following command:

```bash
python demo_agent/run_demo.py --model_name gpt-4.1 --task_name econwebarena.1 --use_axtree True --use_screenshot True
```

This runs a demo agent using GPT-4.1 on the `econwebarena.1` task with both DOM accessibility tree and screenshot modalities enabled.

## 📚 More Information

* For details about BrowserGym: [BrowserGym GitHub](https://github.com/ServiceNow/BrowserGym)
* For information on the EconWebArena benchmark: [EconWebArena Webpage](https://econwebarena.github.io/)

## 📖 Citation

If you find this benchmark useful in your research, please consider citing the following work:

```bibtex
@article{liu2025econwebarena,
  title={EconWebArena: Benchmarking Autonomous Agents on Economic Tasks in Realistic Web Environments},
  author={Liu, Zefang and Quan, Yinzhu},
  journal={arXiv preprint arXiv:2506.08136},
  year={2025}
}
```
