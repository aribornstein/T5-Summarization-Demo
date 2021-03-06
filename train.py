
# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import torch
from argparse import ArgumentParser
from flash import Trainer
from flash.core.data.utils import download_data
from flash.text import SummarizationData, SummarizationTask


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--seed', type=int, default=1234)
    parser.add_argument('--backbone', type=str, default="google/mt5-small")
    parser.add_argument('--download', type=bool, default=True)
    parser.add_argument('--train_file', type=str,
                        default="data/xsum/train.csv")
    parser.add_argument('--valid_file', type=str,
                        default="data/xsum/valid.csv")
    parser.add_argument('--test_file', type=str, default="data/xsum/test.csv")
    parser.add_argument('--max_epochs', type=int, default=1)
    parser.add_argument('--learning_rate', type=float, default=1e-3)
    parser.add_argument('--gpus', type=int, default=None)
    args = parser.parse_args()

    # 1. Download the data
    if args.download:
        download_data("https://pl-flash-data.s3.amazonaws.com/xsum.zip", "data/")


    # 2. Load the data
    datamodule = SummarizationData.from_csv(
        "input",
        "target",
        train_file=args.train_file,
        val_file=args.valid_file,
        test_file=args.test_file,
    )

    # 3. Build the model
    model = SummarizationTask(backbone=args.backbone,
                              learning_rate=args.learning_rate)

    # 4. Create the trainer. Run once on data
    trainer = Trainer(gpus=args.gpus,
                            max_epochs=args.max_epochs, 
                            fast_dev_run=True)

    # 5. Fine-tune the model
    trainer.finetune(model, datamodule=datamodule)

    # 6. Save it!
    trainer.save_checkpoint("summarization_model_xsum.pt")
