# T5-Summarization-Demo
T5 Flash Summarization Demo, with option for training on custom data.


Summarization is the task of summarizing text from a larger document/article into a short sentence/description. For example, taking a web article and describing the topic in a short sentence. This task is a subset of Sequence to Sequence tasks, which requires the model to generate a variable length sequence given an input sequence. In our case the article would be our input sequence, and the short description/sentence would be the output sequence from the model.



[![Grid](https://img.shields.io/badge/rid_AI-run-78FF96.svg?labelColor=black&logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEgMTR2MjBhMTQgMTQgMCAwMDE0IDE0aDlWMzYuOEgxMi42VjExaDIyLjV2N2gxMS4yVjE0QTE0IDE0IDAgMDAzMi40IDBIMTVBMTQgMTQgMCAwMDEgMTR6IiBmaWxsPSIjZmZmIi8+PHBhdGggZD0iTTM1LjIgNDhoMTEuMlYyNS41SDIzLjl2MTEuM2gxMS4zVjQ4eiIgZmlsbD0iI2ZmZiIvPjwvc3ZnPg==)](https://platform.grid.ai/#/runs?script=https://github.com/aribornstein/T5-Summarization-Demo/blob/05d348b4/train.py&cloud=grid&use_spot&instance=g4dn.xlarge&accelerators=1&disk_size=200&framework=lightning&script_args=--grid_name%20silent-iguana-136%20%5C%0A--grid_strategy%20grid_search%20%5C%0A--grid_disk_size%20200%20%5C%0A--grid_max_nodes%2010%20%5C%0A--grid_instance_type%20g4dn.xlarge%20%5C%0A--use_spot%20true%20%5C%0A--grid_framework%20lightning%20%5C%0A--grid_credential%20cc-vnpnm%20%5C%0A--grid_gpus%201%20%5C%0Atrain.py%20--gpus%201%20--max_epochs%203)
