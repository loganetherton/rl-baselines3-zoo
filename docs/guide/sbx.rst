.. _sbx:

==========================
Stable Baselines Jax (SBX)
==========================

`Stable Baselines Jax (SBX) <https://github.com/araffin/sbx>`_ is a proof of concept version of Stable-Baselines3 in Jax.

It provides a minimal number of features compared to SB3 but can be much faster (up to 20x times!): https://twitter.com/araffin2/status/1590714558628253698


It is also compatible with the RL Zoo.
For that you will need to create two files.

``train_sbx.py``:

.. code-block:: python

  import mle_zoo3
  import mle_zoo3.train
  from mle_zoo3.train import train
  from sbx import DQN, PPO, SAC, TQC, DroQ


  mle_zoo3.ALGOS["tqc"] = TQC
  mle_zoo3.ALGOS["droq"] = DroQ
  mle_zoo3.ALGOS["sac"] = SAC
  mle_zoo3.ALGOS["ppo"] = PPO
  mle_zoo3.ALGOS["dqn"] = DQN
  mle_zoo3.train.ALGOS = mle_zoo3.ALGOS
  mle_zoo3.exp_manager.ALGOS = mle_zoo3.ALGOS

  if __name__ == "__main__":
      train()

Then you can call ``python train_sbx.py --algo sac --env Pendulum-v1`` and use the RL Zoo CLI.


``enjoy_sbx.py``:

.. code-block:: python

  import mle_zoo3
  import mle_zoo3.enjoy
  from mle_zoo3.enjoy import enjoy
  from sbx import DQN, PPO, SAC, TQC, DroQ


  mle_zoo3.ALGOS["tqc"] = TQC
  mle_zoo3.ALGOS["droq"] = DroQ
  mle_zoo3.ALGOS["sac"] = SAC
  mle_zoo3.ALGOS["ppo"] = PPO
  mle_zoo3.ALGOS["dqn"] = DQN
  mle_zoo3.enjoy.ALGOS = mle_zoo3.ALGOS
  mle_zoo3.exp_manager.ALGOS = mle_zoo3.ALGOS

  if __name__ == "__main__":
      enjoy()
