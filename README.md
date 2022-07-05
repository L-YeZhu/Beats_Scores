# Beats_Scores
A simple tool for calculating musical beats cover and hit scores in terms of rhythm correspondence.

## Required packges
```
- librosa
- soundfile
```

## Usage
Reference music and synthesized music of wav format in their repective folders, run ```python beats_scores.py``` to calculate. Metric details can be found in the [D2M-GAN paper (ECCV 2022)](https://arxiv.org/abs/2204.00604).

## Citation
Please consider citing our paper if you find it useful.
```
@inproceedings{yezhu2022quantizedgan,
  title={Quantized GAN for Complex Music Generation from Dance Videos},
  author={Zhu, Ye and Olszewski, Kyle and Wu, Yu and Achlioptas, Panos and Chai, Menglei and Yan, Yan and Tulyakov, Sergey},
  booktitle={The European Conference on Computer Vision (ECCV)},
  year={2022}
}
```