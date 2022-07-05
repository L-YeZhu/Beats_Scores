import glob, os, sys
import soundfile as sf
import librosa
from librosa.core import load
import numpy as np
import argparse


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--ref_path", default='./ref_samples')
	parser.add_argument("--syn_path", default='./syn_samples')
	args = parser.parse_args()
	return args



def beat_detect(x, sr=22050):
	onsets = librosa.onset.onset_detect(x, sr=sr, wait=1, delta=0.2, pre_avg=1, post_avg=1, post_max=1, units='time')
	n = np.ceil( len(x) / sr)
	beats = [0] * int(n)
	for time in onsets:
		beats[int(np.trunc(time))] = 1
	return beats

def beat_scores(gt, syn):
	assert len(gt) == len(syn)
	total_beats = sum(gt)
	cover_beats = sum(syn)
	hit_beats = 0
	for i in range(len(gt)):
		if gt[i] == 1 and gt[i] == syn[i]:
			hit_beats += 1
	return cover_beats/total_beats, hit_beats/total_beats


if __name__ == '__main__':
	args = parse_args()
	ref_path = args.ref_path
	syn_path = args.syn_path
	ref_music = sorted(glob.glob(ref_path+'/*'))
	syn_music = sorted(glob.glob(syn_path+'/*'))
	total_score_cover = 0
	total_score_hit = 0
	for i, c in enumerate(ref_music):
		ref, _ = load(ref_music[i])
		syn, _ = load(syn_music[i])
		gt_beats = beat_detect(ref)
		syn_beats = beat_detect(syn)
		score_cover, score_hit = beat_scores(gt_beats, syn_beats)
		total_score_cover += score_cover
		total_score_hit += score_hit
	total_score_cover /= len(ref_music)
	total_score_hit /= len(ref_music)
	print("Total beats-cover and beats-hit:", total_score_cover, total_score_hit)

