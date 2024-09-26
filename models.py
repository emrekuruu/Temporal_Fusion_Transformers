import torch
import torch.nn as nn
import torch.nn.functional as F

class TemporalFusionTransformer(nn.Module):
    def __init__(self, num_categorical_variables, num_regular_variables, num_qts, num_heads, 
                 dropout, output_size, input_size, num_encoder_steps, num_decoder_steps):
        "Pass"

    