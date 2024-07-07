import numpy as np
import torch

class EarlyStopping:
    def __init__(self, patience=300, delta=0, save_path='checkpoint.pth', verbose=False):
        """
        Parameters:
        - patience (int): How long to wait after the last time validation loss improved.
        - delta (float): Minimum change in the monitored quantity to qualify as an improvement.
        - save_path (str): Path to save the model if early stopping is triggered.
        - verbose (bool): If True, prints a message for each validation loss improvement.
        """
        self.patience = patience
        self.delta = delta
        self.save_path = save_path
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.Inf
        self.epoch_logs = []

    def __call__(self, val_loss, model):
        """
        Call method to check whether to apply early stopping.

        Parameters:
        - val_loss (float): The current validation loss.
        - model (torch.nn.Module): The model being trained.
        """
        score = -val_loss

        if self.best_score is None:
            self.best_score = score
            self._save_model(val_loss, model)
        elif score < self.best_score + self.delta:
            self.counter += 1
            if self.verbose:
                print(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self._save_model(val_loss, model)
            self.counter = 0

        self._log_epoch(val_loss)

    def _save_model(self, val_loss, model):
        """
        Save the model when validation loss decreases.

        Parameters:
        - val_loss (float): The current validation loss.
        - model (torch.nn.Module): The model being trained.
        """
        torch.save(model.state_dict(), self.save_path)
        if self.verbose:
            print(f'Validation loss increased ({self.val_loss_min:.6f} --> {val_loss:.6f}). Saving model ...')
        self.val_loss_min = val_loss

    def _log_epoch(self, val_loss):
        """
        Log the validation loss for the epoch.

        Parameters:
        - val_loss (float): The current validation loss.
        """
        self.epoch_logs.append(val_loss)
        if self.verbose:
            print(f'Validation loss: {val_loss:.6f}')
