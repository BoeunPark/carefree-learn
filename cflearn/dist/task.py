import os

from ..bases import *


class Task:
    def __init__(self,
                 idx: int,
                 model: str,
                 identifier: str,
                 temp_folder: str):
        self.idx = idx
        self.model = model
        self.identifier = identifier
        self.temp_folder = temp_folder

    @property
    def saving_folder(self) -> str:
        folder = os.path.join(self.temp_folder, self.identifier, str(self.idx))
        os.makedirs(folder, exist_ok=True)
        return folder

    def fit(self,
            make: callable,
            save: callable,
            x: data_type,
            y: data_type = None,
            x_cv: data_type = None,
            y_cv: data_type = None,
            cuda: int = 0,
            **kwargs) -> "Task":
        kwargs["logging_path"] = os.path.join(self.saving_folder, "trainer.log")
        m = make(self.model, cuda=cuda, **kwargs)
        m.fit(x, y, x_cv, y_cv)
        save(m, saving_folder=self.saving_folder)
        return self


__all__ = ["Task"]