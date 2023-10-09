import time

out_dir = 'out-shakespeare-char-4l8h-ft'
eval_interval = 250
eval_iters = 200
log_inerval = 10

wandb_log = False # feel free to turn on
wandb_project = 'ft7_5k-char'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'tt_7_5k'
init_from = 'resume' # this is the largest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = True

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 64
gradient_accumulation_steps = 1
max_iters = 7500
block_size = 256

# finetune at constant LR
learning_rate = 1e-3
lr_decay_iters = 7500

min_lr = 1e-4
beta2 = 0.99
